#!/usr/bin/env python3
"""
Static QA Suite for J3 Project (Ren'Py 8.2.3).

Reads all .rpy files under Projeto/J3 Project/game/ and runs 10 checks
without needing the Ren'Py runtime. Produces qa-static-findings.json.

Usage:
    python3 tools/qa/static_lint.py [--root PATH] [--out PATH]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable

DEFAULT_ROOT = Path("Projeto/J3 Project/game")
DEFAULT_OUT = Path("tools/qa/qa-static-findings.json")

LONG_TEXT_THRESHOLD = 120
LONG_CHOICE_THRESHOLD = 90


@dataclass
class Finding:
    severity: str  # critical | major | minor | cosmetic
    check: str
    file: str
    line: int
    message: str
    snippet: str = ""

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class ProjectIndex:
    characters: set[str] = field(default_factory=set)
    store_vars: set[str] = field(default_factory=set)
    persistent_vars: set[str] = field(default_factory=set)
    images: set[str] = field(default_factory=set)
    bg_images: set[str] = field(default_factory=set)
    labels: set[str] = field(default_factory=set)
    label_refs: list[tuple[str, str, int]] = field(default_factory=list)
    image_refs: list[tuple[str, str, int, str]] = field(default_factory=list)
    transforms: set[str] = field(default_factory=set)
    audio_files: set[str] = field(default_factory=set)
    label_lines: dict[str, tuple[str, int]] = field(default_factory=dict)


# Regexes precompiled
RE_DEFINE_CHAR = re.compile(r"^\s*define\s+(\w+)\s*=\s*(?:ADV)?(?:Character|Char)\s*\(", re.MULTILINE)
RE_DEFAULT_VAR = re.compile(r"^\s*default\s+(?:persistent\.)?(\w+)\s*=", re.MULTILINE)
RE_DEFAULT_PERSISTENT = re.compile(r"^\s*default\s+persistent\.(\w+)\s*=", re.MULTILINE)
RE_IMAGE_BG = re.compile(r"^\s*image\s+bg\s+(\w+)\s*=", re.MULTILINE)
RE_LABEL = re.compile(r"^\s*label\s+(\w+)\s*(?:\([^)]*\))?\s*:", re.MULTILINE)
RE_CALL_JUMP = re.compile(r"^\s*(?:call|jump)\s+(\w+)\b", re.MULTILINE)
RE_SHOW = re.compile(r"^\s*show\s+(\w+(?:\s+\w+)?)(?:\s+at\s+\w+)?", re.MULTILINE)
RE_SCENE = re.compile(r"^\s*scene\s+bg\s+(\w+)", re.MULTILINE)
RE_TRANSFORM = re.compile(r"^\s*transform\s+(\w+):", re.MULTILINE)
RE_PLAY_SOUND = re.compile(r"""play\s+(?:sound|music)\s+["']([^"']+)["']""")
RE_VAR_INTERPOLATION = re.compile(r"\[([^\]\s]+)(?:\s*[!:][^\]]*)?\]")
RE_CONSUMIR_BAT = re.compile(r"\$\s*consumir_bateria\s*\(\s*(\d+)\s*\)")
RE_CONSUMIR_INT = re.compile(r"\$\s*consumir_integridade\s*\(\s*(\d+)\s*\)")
RE_CUSTO_TAG = re.compile(r"\[\s*custo\s*\(\s*(\d+)(?:\s*,\s*(\d+))?\s*\)\s*\]")
RE_DIALOG = re.compile(r'^\s*(\w+)\s+(_p\(|")', re.MULTILINE)


def iter_rpy(root: Path) -> Iterable[Path]:
    skip_dirs = {"_backups", "cache", "lib", "tl"}
    for p in root.rglob("*.rpy"):
        if any(part in skip_dirs for part in p.parts):
            continue
        if p.name.startswith("test_") or "qa_harness" in p.name:
            continue
        yield p


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def relpath(p: Path, root: Path) -> str:
    try:
        return str(p.relative_to(root.parent))
    except ValueError:
        return str(p)


def index_project(root: Path, char_map_path: Path) -> ProjectIndex:
    idx = ProjectIndex()
    # Built-in chars + special tokens
    idx.characters.update({"narrator", "centered", "nvl"})
    idx.store_vars.update({
        "_music_random_enabled", "_music_last_track", "nvl_list",
        "music_tracks", "qa_mode", "qa_pending_options",
    })

    # Parse all .rpy
    for p in iter_rpy(root):
        text = read_text(p)
        idx.characters.update(RE_DEFINE_CHAR.findall(text))
        for m in RE_DEFAULT_VAR.finditer(text):
            idx.store_vars.add(m.group(1))
        for m in RE_DEFAULT_PERSISTENT.finditer(text):
            idx.persistent_vars.add(m.group(1))
            idx.store_vars.add(m.group(1))
        idx.bg_images.update(RE_IMAGE_BG.findall(text))
        for m in RE_LABEL.finditer(text):
            name = m.group(1)
            idx.labels.add(name)
            line_no = text.count("\n", 0, m.start()) + 1
            idx.label_lines[name] = (str(p), line_no)
        idx.transforms.update(RE_TRANSFORM.findall(text))

    # Parse _char_map tags from images.rpy
    if char_map_path.exists():
        text = read_text(char_map_path)
        # Tags are dict keys in _char_map
        for m in re.finditer(r'"(\w+)":\s+\("characters/', text):
            idx.images.add(m.group(1))
        # Plus attribute variants
        for tag_m in re.finditer(r'"(\w+)":\s+\("characters/[^"]+",\s*\[([^\]]*)\]', text):
            tag = tag_m.group(1)
            attrs_text = tag_m.group(2)
            attrs = re.findall(r'"(\w+)"', attrs_text)
            for a in attrs:
                idx.images.add(f"{tag} {a}")

    # Audio files in audio/music
    audio_root = root / "audio"
    if audio_root.exists():
        for sound in audio_root.rglob("*"):
            if sound.is_file():
                rel = sound.relative_to(root).as_posix()
                idx.audio_files.add(rel)

    return idx


def check_long_text(text: str, file_rel: str, findings: list[Finding]) -> None:
    for line_no, line in enumerate(text.splitlines(), 1):
        # Dialogue line: <char> "..."
        m = re.match(r'^\s*\w+\s+"([^"]*)"', line)
        if m:
            dialog = m.group(1)
            if len(dialog) > LONG_TEXT_THRESHOLD:
                findings.append(Finding(
                    severity="minor",
                    check="long_dialog",
                    file=file_rel,
                    line=line_no,
                    message=f"Dialog {len(dialog)} chars (>{LONG_TEXT_THRESHOLD}), possivel overflow textbox.",
                    snippet=dialog[:80] + ("..." if len(dialog) > 80 else ""),
                ))
        # Menu choice line: indented "..." :
        m_choice = re.match(r'^\s+"([^"]+)":\s*$', line)
        if m_choice:
            choice = m_choice.group(1)
            # Remove [custo(..)] and {markup} for length count
            clean = re.sub(r"\[[^\]]+\]|\{[^}]+\}", "", choice).strip()
            if len(clean) > LONG_CHOICE_THRESHOLD:
                findings.append(Finding(
                    severity="minor",
                    check="long_choice",
                    file=file_rel,
                    line=line_no,
                    message=f"Choice option {len(clean)} chars de texto visivel (>{LONG_CHOICE_THRESHOLD}), pode wrap em 3+ linhas.",
                    snippet=clean[:80] + ("..." if len(clean) > 80 else ""),
                ))


def check_var_interpolation(text: str, file_rel: str, idx: ProjectIndex, findings: list[Finding]) -> None:
    """Find [var] inside strings and validate var is known."""
    KNOWN_NAMESPACES = {"persistent", "config", "preferences", "store", "renpy"}
    # Functions/labels known to be callable in Ren'Py interpolation contexts.
    KNOWN_FUNCS = {"custo", "ganho", "get_personalidade_dominante",
                   "get_final_type", "verificar_final_critico",
                   "format", "int", "str", "len",
                   "get_status_bateria", "get_status_integridade",
                   "get_status_geral"}
    # Add any def funcname found in init python blocks.
    for m in re.finditer(r"^\s+def\s+(\w+)\s*\(", text, re.MULTILINE):
        KNOWN_FUNCS.add(m.group(1))
    for line_no, line in enumerate(text.splitlines(), 1):
        # Skip inside screen blocks — they use Ren'Py screen DSL.
        # Lightweight: if line starts with screen-widget keyword, skip.
        stripped = line.lstrip()
        if any(stripped.startswith(w + " ") for w in
               ("text ", "background ", "frame ", "label ", "key ", "imagebutton ",
                "textbutton ", "image ", "button ", "bar ", "vbar ")):
            continue
        for str_m in re.finditer(r'"((?:[^"\\]|\\.)*)"', line):
            s = str_m.group(1)
            # Ren'Py escapes: [[ -> literal [. Mask out so regex doesn't capture.
            s = s.replace("[[", "\x00\x00")
            for vm in RE_VAR_INTERPOLATION.finditer(s):
                token = vm.group(1)
                # Function call in interpolation: skip if function name is known
                if "(" in token:
                    fn = token.split("(")[0].split(".")[-1]
                    if fn in KNOWN_FUNCS or fn in idx.store_vars or fn in idx.characters:
                        continue
                    # Unknown function — flag
                    findings.append(Finding(
                        severity="major",
                        check="unknown_var_interpolation",
                        file=file_rel,
                        line=line_no,
                        message=f"Chamada de funcao '[{token}]' nao reconhecida.",
                        snippet=line.strip()[:120],
                    ))
                    continue
                # Attribute access: validate namespace
                if "." in token:
                    head = token.split(".")[0]
                    if head in KNOWN_NAMESPACES or head in idx.store_vars:
                        continue
                # Single-letter all-caps markup (escapes done by user)
                if len(token) <= 2 and token.isupper():
                    continue
                if token in idx.store_vars or token in idx.characters:
                    continue
                findings.append(Finding(
                    severity="major",
                    check="unknown_var_interpolation",
                    file=file_rel,
                    line=line_no,
                    message=f"Substituicao '[{token}]' refere identificador desconhecido em runtime.",
                    snippet=line.strip()[:120],
                ))


def check_reference_integrity(text: str, file_rel: str, idx: ProjectIndex, findings: list[Finding]) -> None:
    # call/jump
    for m in RE_CALL_JUMP.finditer(text):
        target = m.group(1)
        line_no = text.count("\n", 0, m.start()) + 1
        # Skip dynamic / known runtime labels
        if target in {"mensagem_sistema", "atualizar_status", "iniciar_musica_aleatoria",
                      "parar_musica_aleatoria"}:
            if target not in idx.labels:
                # mensagem_sistema is a label defined in sistema_j3.rpy
                pass
        if target not in idx.labels:
            findings.append(Finding(
                severity="critical",
                check="broken_label_ref",
                file=file_rel,
                line=line_no,
                message=f"call/jump para label inexistente '{target}'.",
                snippet=text.splitlines()[line_no - 1].strip(),
            ))
    # scene bg
    for m in RE_SCENE.finditer(text):
        bg = m.group(1)
        line_no = text.count("\n", 0, m.start()) + 1
        if bg not in idx.bg_images:
            findings.append(Finding(
                severity="critical",
                check="broken_bg_ref",
                file=file_rel,
                line=line_no,
                message=f"scene bg '{bg}' nao declarada em images.rpy.",
                snippet=text.splitlines()[line_no - 1].strip(),
            ))
    # show <char> [attr]
    for m in RE_SHOW.finditer(text):
        token = m.group(1).strip()
        line_no = text.count("\n", 0, m.start()) + 1
        # show screen X is different (handled below)
        if token.startswith("screen "):
            continue
        # Multi-word: "char attr" — validate combined or base
        parts = token.split()
        base = parts[0]
        if base not in {t.split()[0] for t in idx.images}:
            # Maybe scene bg X was matched accidentally
            if base == "bg":
                continue
            findings.append(Finding(
                severity="critical",
                check="broken_sprite_ref",
                file=file_rel,
                line=line_no,
                message=f"show '{token}' refere sprite tag desconhecido '{base}'.",
                snippet=text.splitlines()[line_no - 1].strip(),
            ))


def check_audio_refs(text: str, file_rel: str, idx: ProjectIndex, findings: list[Finding]) -> None:
    for m in RE_PLAY_SOUND.finditer(text):
        ref = m.group(1)
        line_no = text.count("\n", 0, m.start()) + 1
        if ref not in idx.audio_files:
            findings.append(Finding(
                severity="major",
                check="missing_audio_file",
                file=file_rel,
                line=line_no,
                message=f"play sound '{ref}' aponta para arquivo inexistente em game/.",
                snippet=text.splitlines()[line_no - 1].strip(),
            ))


def check_choice_costs(text: str, file_rel: str, findings: list[Finding]) -> None:
    """For each menu option with [custo(B[,I])] tag, validate consumir_* calls match."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect choice header with custo tag
        m = re.match(r'^(\s+)"(\[custo\([^)]+\)\][^"]*)":\s*$', line)
        if not m:
            i += 1
            continue
        indent = len(m.group(1))
        choice_text = m.group(2)
        custo_m = RE_CUSTO_TAG.search(choice_text)
        if not custo_m:
            i += 1
            continue
        declared_bat = int(custo_m.group(1))
        declared_int = int(custo_m.group(2)) if custo_m.group(2) else 0
        # Scan body of option (indented deeper than choice header)
        j = i + 1
        body_bat = 0
        body_int = 0
        while j < len(lines):
            body_line = lines[j]
            if not body_line.strip():
                j += 1
                continue
            body_indent = len(body_line) - len(body_line.lstrip())
            if body_indent <= indent:
                break
            for bm in RE_CONSUMIR_BAT.finditer(body_line):
                body_bat += int(bm.group(1))
            for im in RE_CONSUMIR_INT.finditer(body_line):
                body_int += int(im.group(1))
            j += 1
        # Report mismatches
        if declared_bat != body_bat:
            severity = "major" if abs(declared_bat - body_bat) > 5 else "minor"
            findings.append(Finding(
                severity=severity,
                check="cost_mismatch_bateria",
                file=file_rel,
                line=i + 1,
                message=f"Custo declarado -{declared_bat} BAT mas consumir_bateria soma -{body_bat}.",
                snippet=choice_text[:120],
            ))
        if declared_int != body_int:
            severity = "major" if abs(declared_int - body_int) > 5 else "minor"
            findings.append(Finding(
                severity=severity,
                check="cost_mismatch_integridade",
                file=file_rel,
                line=i + 1,
                message=f"Custo declarado -{declared_int} INT mas consumir_integridade soma -{body_int}.",
                snippet=choice_text[:120],
            ))
        i = j


def check_dialog_chars(text: str, file_rel: str, idx: ProjectIndex, findings: list[Finding]) -> None:
    """Validate every dialog line has a known character. Skip lines inside screen blocks."""
    keywords = {
        "menu", "label", "scene", "show", "hide", "if", "elif", "else",
        "with", "return", "jump", "call", "play", "stop", "pause", "queue",
        "init", "default", "define", "image", "transform", "screen",
        "window", "nvl", "narrator", "python",
    }
    # Screen widget keywords — these appear inside `screen X:` blocks.
    screen_widgets = {
        "text", "background", "frame", "hbox", "vbox", "fixed", "viewport",
        "side", "grid", "imagebutton", "textbutton", "button", "image",
        "bar", "vbar", "input", "key", "mousearea", "drag", "label",
        "use", "add", "style", "spacing", "xalign", "yalign", "xpos", "ypos",
        "color", "size", "font", "tag", "id", "modal", "zorder", "thumb",
        "child", "alpha", "value", "action", "hovered", "unhovered",
        "selected", "sensitive", "tooltip", "alt", "screen", "vpgrid",
    }
    # Track if we're inside a `screen X:` block by indentation
    in_screen = False
    screen_indent = -1
    for line_no, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        cur_indent = len(line) - len(stripped)
        if in_screen and stripped and cur_indent <= screen_indent:
            in_screen = False
        if re.match(r'^\s*screen\s+\w+', line):
            in_screen = True
            screen_indent = cur_indent
            continue
        if in_screen:
            continue
        m = re.match(r'^\s*(\w+)\s+"', line)
        if not m:
            continue
        token = m.group(1)
        if token in keywords or token in screen_widgets:
            continue
        if token in idx.characters:
            continue
        findings.append(Finding(
            severity="major",
            check="unknown_dialog_char",
            file=file_rel,
            line=line_no,
            message=f"Fala atribuida a identificador nao registrado como Character: '{token}'.",
            snippet=line.strip()[:120],
        ))


def check_dead_labels(idx: ProjectIndex, root: Path, findings: list[Finding]) -> None:
    """Find labels never referenced."""
    refs: set[str] = set()
    for p in iter_rpy(root):
        text = read_text(p)
        for m in RE_CALL_JUMP.finditer(text):
            refs.add(m.group(1))
    excluded_suffixes = ("_start", "_common", "_accepted", "_refused", "_joined",
                         "_observed", "_recarga_accepted", "_recarga_refused",
                         "_recharge_accepted", "_recharge_refused", "_repair_accepted",
                         "_repair_refused")
    excluded_exact = {"start", "credits", "iniciar_musica_aleatoria",
                      "parar_musica_aleatoria", "mensagem_sistema",
                      "atualizar_status", "after_load", "main_menu",
                      "run_tests", "run_comprehensive_tests", "verificar_final_critico"}
    for label in sorted(idx.labels):
        if label in refs:
            continue
        if label in excluded_exact:
            continue
        if any(label.endswith(s) for s in excluded_suffixes):
            continue
        # Finals always reachable via jump from finals_alternativos or day7
        if label.startswith("final_"):
            continue
        if label.startswith("day"):
            continue
        file_rel, line_no = idx.label_lines.get(label, ("?", 0))
        findings.append(Finding(
            severity="cosmetic",
            check="dead_label",
            file=file_rel,
            line=line_no,
            message=f"Label '{label}' definido mas nunca referenciado.",
            snippet="",
        ))


def check_placeholders(text: str, file_rel: str, findings: list[Finding]) -> None:
    """Find common placeholder/TODO patterns in strings."""
    # Stricter: placeholder patterns that look like design notes leaked to player.
    # "(se " in lowercase is a reflexive pronoun ("se aproxima") — NOT a placeholder.
    # Real placeholders use lowercase "se a ajudou" / "se escolheu" / "se +X" style.
    patterns = [
        (r"\[TODO\]", "critical"),
        (r"\bFIXME\b", "critical"),
        (r"\bXXX\b", "major"),
        (r"\bTBD\b", "major"),
        (r"\(se (?:a |o |escolh|n[aã]o |jogador|player)", "major"),
        (r"\(caso (?:o |a |jogador|player|n[aã]o |escolh)", "major"),
        (r"\bPLACEHOLDER\b", "critical"),
        (r"\[NOTA\]|\[NOTE\]|\[DESIGN\]", "critical"),
    ]
    for line_no, line in enumerate(text.splitlines(), 1):
        # Only look inside quoted strings
        for str_m in re.finditer(r'"((?:[^"\\]|\\.)*)"', line):
            s = str_m.group(1)
            for pattern, sev in patterns:
                if re.search(pattern, s, re.IGNORECASE):
                    findings.append(Finding(
                        severity=sev,
                        check="placeholder_in_text",
                        file=file_rel,
                        line=line_no,
                        message=f"String contem padrao placeholder '{pattern}'.",
                        snippet=s[:120],
                    ))
                    break


def check_persistent_refs(text: str, file_rel: str, idx: ProjectIndex, findings: list[Finding]) -> None:
    for line_no, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\bpersistent\.(\w+)", line):
            var = m.group(1)
            if var not in idx.persistent_vars:
                findings.append(Finding(
                    severity="major",
                    check="undeclared_persistent",
                    file=file_rel,
                    line=line_no,
                    message=f"persistent.{var} usado mas nao tem default em script.rpy.",
                    snippet=line.strip()[:120],
                ))


def integrate_png_audit(root: Path, project_root: Path, findings: list[Finding]) -> None:
    """If audit_png_size.ps1 output available, integrate. Otherwise re-check via Python."""
    import struct
    char_dir = root / "characters"
    if not char_dir.exists():
        return
    aspects = {}
    for png in char_dir.rglob("*.png"):
        if "_backups" in png.parts:
            continue
        try:
            with open(png, "rb") as fh:
                head = fh.read(24)
            if head[:8] != b"\x89PNG\r\n\x1a\n":
                continue
            w, h = struct.unpack(">II", head[16:24])
            ar = w / h if h else 0
            aspects[png.name] = (w, h, ar)
        except Exception:
            continue
    # Flag character PNGs with extreme aspect (>2.5 = ultra-wide, <0.4 = ultra-tall)
    for name, (w, h, ar) in aspects.items():
        if ar > 2.5 or ar < 0.4:
            rel = (char_dir / name).relative_to(project_root.parent).as_posix()
            findings.append(Finding(
                severity="minor",
                check="sprite_extreme_aspect",
                file=rel,
                line=0,
                message=f"Sprite {w}x{h} (aspect {ar:.2f}). Pode demandar override em _sprite_scale ou _sprite_no_norm.",
                snippet="",
            ))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    root: Path = args.root.resolve()
    if not root.exists():
        print(f"ERROR: root {root} nao existe", file=sys.stderr)
        return 2

    char_map_path = root / "images.rpy"
    idx = index_project(root, char_map_path)

    findings: list[Finding] = []

    # screens.rpy uses Ren'Py screen language with its own DSL — skip dialog/var checks.
    # gui.rpy/options.rpy similar (config files).
    SCRIPT_ONLY = {"day1.rpy", "day2.rpy", "day3.rpy", "day4.rpy", "day5.rpy",
                   "day6.rpy", "day7.rpy", "script.rpy", "finais_alternativos.rpy",
                   "sistema_j3.rpy", "functions.rpy", "musica.rpy"}

    for p in iter_rpy(root):
        text = read_text(p)
        file_rel = relpath(p, root)
        is_script = p.name in SCRIPT_ONLY
        check_reference_integrity(text, file_rel, idx, findings)
        if is_script:
            check_long_text(text, file_rel, findings)
            check_var_interpolation(text, file_rel, idx, findings)
            check_audio_refs(text, file_rel, idx, findings)
            check_choice_costs(text, file_rel, findings)
            check_dialog_chars(text, file_rel, idx, findings)
            check_placeholders(text, file_rel, findings)
            check_persistent_refs(text, file_rel, idx, findings)

    check_dead_labels(idx, root, findings)
    integrate_png_audit(root, root.parent.parent, findings)

    # Summary counts
    counts = {"critical": 0, "major": 0, "minor": 0, "cosmetic": 0}
    for f in findings:
        counts[f.severity] = counts.get(f.severity, 0) + 1

    output = {
        "version": "1.0",
        "root": str(root),
        "summary": counts,
        "index_summary": {
            "characters": len(idx.characters),
            "store_vars": len(idx.store_vars),
            "persistent_vars": len(idx.persistent_vars),
            "images_tags": len(idx.images),
            "bg_images": len(idx.bg_images),
            "labels": len(idx.labels),
            "transforms": len(idx.transforms),
            "audio_files": len(idx.audio_files),
        },
        "findings": [f.as_dict() for f in findings],
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Findings written: {args.out}")
    print(f"Counts: {counts}")
    print(f"Index: {output['index_summary']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
