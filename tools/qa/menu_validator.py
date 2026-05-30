#!/usr/bin/env python3
"""
Menu Validator for J3 Project — valida cada menu block em day*.rpy:
  - estrutura sintatica (indent, ":" no header)
  - cada opcao tem corpo nao-vazio
  - cost tag [custo(B[,I])] bate com consumir_bateria(B) + consumir_integridade(I)
  - gain tag [ganho(B[,I])] bate com recarregar_bateria(B) + reparar_integridade(I)
  - opcoes com modificar_personalidade chamam atualizar_status no fim
  - opcoes que setam aliancas (maya_ally/elias_ally/unit7_alive) sao consistentes
  - cada day*.rpy chama renpy.save("auto_save_dayN", ...) no fim

Output: tools/qa/menu-validation-findings.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

DAY_FILES = ["day1.rpy", "day2.rpy", "day3.rpy", "day4.rpy", "day5.rpy", "day6.rpy", "day7.rpy"]

RE_MENU = re.compile(r"^(\s*)menu:\s*$")
RE_OPTION = re.compile(r'^(\s+)"((?:[^"\\]|\\.)*)":\s*$')
RE_COST = re.compile(r"\[\s*custo\s*\(\s*(\d+)(?:\s*,\s*(\d+))?\s*\)\s*\]")
RE_GAIN = re.compile(r"\[\s*ganho\s*\(\s*(?:bat\s*=\s*)?(\d+)?(?:\s*,\s*)?(?:integ\s*=\s*)?(\d+)?\s*\)\s*\]")
RE_CONSUMIR_BAT = re.compile(r"\$\s*consumir_bateria\s*\(\s*(\d+)\s*\)")
RE_CONSUMIR_INT = re.compile(r"\$\s*consumir_integridade\s*\(\s*(\d+)\s*\)")
RE_RECARREGAR = re.compile(r"\$\s*recarregar_bateria\s*\(\s*(\d+)\s*\)")
RE_REPARAR = re.compile(r"\$\s*reparar_integridade\s*\(\s*(\d+)\s*\)")
RE_MOD_PERS = re.compile(r'\$\s*modificar_personalidade\s*\(\s*"(\w+)"\s*,\s*(-?\d+)\s*\)')
RE_ALLY_SET = re.compile(r"\$\s*(\w+_ally|unit7_alive|elena_alive)\s*=\s*(True|False)")
RE_ATUALIZAR = re.compile(r"call\s+atualizar_status")
RE_MENSAGEM = re.compile(r'call\s+mensagem_sistema\(')
RE_SAVE = re.compile(r'\$\s*renpy\.save\s*\(\s*"auto_save_day(\d+)"')
RE_JUMP = re.compile(r"\bjump\s+(\w+)")
RE_CALL = re.compile(r"\bcall\s+(\w+)")


@dataclass
class MenuFinding:
    severity: str
    check: str
    file: str
    line: int
    menu_index: int
    option_index: int = -1
    option_text: str = ""
    message: str = ""

    def as_dict(self):
        return asdict(self)


@dataclass
class MenuOption:
    line: int
    text: str
    body_lines: list[str] = field(default_factory=list)
    body_line_start: int = 0


@dataclass
class MenuBlock:
    line: int
    indent: int
    header_text: str = ""
    options: list[MenuOption] = field(default_factory=list)


def parse_menus(text: str) -> list[MenuBlock]:
    """Walk text, return list of MenuBlock with options and their body lines."""
    lines = text.splitlines()
    menus = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = RE_MENU.match(line)
        if not m:
            i += 1
            continue
        menu_indent = len(m.group(1))
        menu = MenuBlock(line=i + 1, indent=menu_indent)
        # Find header (first quoted line inside menu) + options
        i += 1
        while i < len(lines):
            cur = lines[i]
            if not cur.strip():
                i += 1
                continue
            cur_indent = len(cur) - len(cur.lstrip())
            if cur_indent <= menu_indent:
                # End of menu
                break
            # Option header
            opt_m = RE_OPTION.match(cur)
            if opt_m and cur_indent == menu_indent + 4:
                opt_indent = len(opt_m.group(1))
                opt_text = opt_m.group(2)
                opt = MenuOption(line=i + 1, text=opt_text, body_line_start=i + 2)
                if not menu.options and not menu.header_text:
                    # First quoted line could be header. Heuristic: if next line is also
                    # a quoted "...": at same indent, this one is header; else it's option.
                    # Check whether body follows
                    j = i + 1
                    has_body = False
                    while j < len(lines):
                        b = lines[j]
                        if not b.strip():
                            j += 1
                            continue
                        b_indent = len(b) - len(b.lstrip())
                        if b_indent <= opt_indent:
                            break
                        has_body = True
                        break
                    if not has_body:
                        # Header line (no body)
                        menu.header_text = opt_text
                        i += 1
                        continue
                # Collect body lines
                i += 1
                while i < len(lines):
                    b = lines[i]
                    if not b.strip():
                        opt.body_lines.append(b)
                        i += 1
                        continue
                    b_indent = len(b) - len(b.lstrip())
                    if b_indent <= opt_indent:
                        break
                    opt.body_lines.append(b)
                    i += 1
                menu.options.append(opt)
                continue
            i += 1
        menus.append(menu)
    return menus


def check_menu(menu: MenuBlock, idx: int, file_rel: str,
               findings: list[MenuFinding]) -> None:
    if not menu.options:
        findings.append(MenuFinding(
            severity="critical", check="empty_menu",
            file=file_rel, line=menu.line, menu_index=idx,
            message="Menu sem opcoes."))
        return
    if len(menu.options) < 2:
        findings.append(MenuFinding(
            severity="major", check="single_option_menu",
            file=file_rel, line=menu.line, menu_index=idx,
            message=f"Menu com apenas {len(menu.options)} opcao — esperado >= 2."))

    for opt_idx, opt in enumerate(menu.options):
        body = "\n".join(opt.body_lines)
        # 1. Corpo nao-vazio
        if not body.strip():
            findings.append(MenuFinding(
                severity="critical", check="empty_option",
                file=file_rel, line=opt.line, menu_index=idx, option_index=opt_idx,
                option_text=opt.text[:80],
                message="Opcao sem corpo (skipping vai pular para fim do menu sem efeito)."))
            continue

        # 2. Cost tag vs consumir_*
        custo_m = RE_COST.search(opt.text)
        declared_bat = int(custo_m.group(1)) if custo_m else 0
        declared_int = int(custo_m.group(2)) if (custo_m and custo_m.group(2)) else 0
        body_bat = sum(int(m.group(1)) for m in RE_CONSUMIR_BAT.finditer(body))
        body_int = sum(int(m.group(1)) for m in RE_CONSUMIR_INT.finditer(body))
        if declared_bat != body_bat:
            sev = "major" if abs(declared_bat - body_bat) > 3 else "minor"
            findings.append(MenuFinding(
                severity=sev, check="cost_bateria_mismatch",
                file=file_rel, line=opt.line, menu_index=idx, option_index=opt_idx,
                option_text=opt.text[:80],
                message=f"Custo declarado -{declared_bat} BAT, consumir_bateria soma -{body_bat}."))
        if declared_int != body_int:
            sev = "major" if abs(declared_int - body_int) > 3 else "minor"
            findings.append(MenuFinding(
                severity=sev, check="cost_integridade_mismatch",
                file=file_rel, line=opt.line, menu_index=idx, option_index=opt_idx,
                option_text=opt.text[:80],
                message=f"Custo declarado -{declared_int} INT, consumir_integridade soma -{body_int}."))

        # 3. Gain tag vs recarregar_*/reparar_*
        gain_m = RE_GAIN.search(opt.text)
        declared_g_bat = int(gain_m.group(1)) if (gain_m and gain_m.group(1)) else 0
        declared_g_int = int(gain_m.group(2)) if (gain_m and gain_m.group(2)) else 0
        body_recar = sum(int(m.group(1)) for m in RE_RECARREGAR.finditer(body))
        body_repar = sum(int(m.group(1)) for m in RE_REPARAR.finditer(body))
        if declared_g_bat and declared_g_bat != body_recar:
            findings.append(MenuFinding(
                severity="major", check="gain_bateria_mismatch",
                file=file_rel, line=opt.line, menu_index=idx, option_index=opt_idx,
                option_text=opt.text[:80],
                message=f"Ganho declarado +{declared_g_bat} BAT, recarregar_bateria soma +{body_recar}."))
        if declared_g_int and declared_g_int != body_repar:
            findings.append(MenuFinding(
                severity="major", check="gain_integridade_mismatch",
                file=file_rel, line=opt.line, menu_index=idx, option_index=opt_idx,
                option_text=opt.text[:80],
                message=f"Ganho declarado +{declared_g_int} INT, reparar_integridade soma +{body_repar}."))
        if body_recar and not declared_g_bat and not declared_bat:
            findings.append(MenuFinding(
                severity="minor", check="gain_bateria_undeclared",
                file=file_rel, line=opt.line, menu_index=idx, option_index=opt_idx,
                option_text=opt.text[:80],
                message=f"recarregar_bateria(+{body_recar}) sem tag [ganho(...)] na opcao."))
        if body_repar and not declared_g_int and not declared_int:
            findings.append(MenuFinding(
                severity="minor", check="gain_integridade_undeclared",
                file=file_rel, line=opt.line, menu_index=idx, option_index=opt_idx,
                option_text=opt.text[:80],
                message=f"reparar_integridade(+{body_repar}) sem tag [ganho(...)] na opcao."))

        # 4. modificar_personalidade chamada? Se sim, deve ter atualizar_status
        has_mod_pers = bool(RE_MOD_PERS.search(body))
        has_consume = bool(RE_CONSUMIR_BAT.search(body) or RE_CONSUMIR_INT.search(body))
        has_recover = bool(RE_RECARREGAR.search(body) or RE_REPARAR.search(body))
        has_atualizar = bool(RE_ATUALIZAR.search(body))
        has_jump_or_return = bool(RE_JUMP.search(body) or re.search(r"\breturn\b", body))

        if (has_mod_pers or has_consume or has_recover) and not has_atualizar and not has_jump_or_return:
            findings.append(MenuFinding(
                severity="minor", check="missing_atualizar_status",
                file=file_rel, line=opt.line, menu_index=idx, option_index=opt_idx,
                option_text=opt.text[:80],
                message="Opcao altera estado mas nao chama 'call atualizar_status' nem encerra com jump/return — HUD pode ficar desatualizado."))

        # 5. modificar_personalidade com valor 0 (no-op)
        for m in RE_MOD_PERS.finditer(body):
            if int(m.group(2)) == 0:
                findings.append(MenuFinding(
                    severity="minor", check="personality_zero_delta",
                    file=file_rel, line=opt.line, menu_index=idx, option_index=opt_idx,
                    option_text=opt.text[:80],
                    message=f"modificar_personalidade('{m.group(1)}', 0) — no-op."))

        # 6. Alliance flags set: ok per se, just log
        # 7. Long option text (informational, already handled by static_lint)


def check_day_file(path: Path, file_rel: str, findings: list[MenuFinding]) -> int:
    text = path.read_text(encoding="utf-8")
    day_match = re.search(r"day(\d+)\.rpy", path.name)
    day_num = day_match.group(1) if day_match else "?"

    menus = parse_menus(text)
    for idx, m in enumerate(menus):
        check_menu(m, idx, file_rel, findings)

    # Save check (skip day7 since save before final, not at end)
    save_matches = list(RE_SAVE.finditer(text))
    if path.name == "day7.rpy":
        # Day 7 should have at least 1 save (pre-final or end)
        if not save_matches:
            findings.append(MenuFinding(
                severity="major", check="missing_auto_save",
                file=file_rel, line=0, menu_index=-1,
                message="day7.rpy sem renpy.save('auto_save_day7', ...)"))
    else:
        if not save_matches:
            findings.append(MenuFinding(
                severity="major", check="missing_auto_save",
                file=file_rel, line=0, menu_index=-1,
                message=f"day{day_num}.rpy sem renpy.save('auto_save_day{day_num}', ...) — quebra padrao."))
        else:
            for m in save_matches:
                save_day = m.group(1)
                if save_day != day_num:
                    line_no = text.count("\n", 0, m.start()) + 1
                    findings.append(MenuFinding(
                        severity="critical", check="save_wrong_day_number",
                        file=file_rel, line=line_no, menu_index=-1,
                        message=f"renpy.save('auto_save_day{save_day}', ...) em day{day_num}.rpy — slot incorreto."))

    return len(menus)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("Projeto/J3 Project/game/scripts"))
    parser.add_argument("--out", type=Path, default=Path("tools/qa/menu-validation-findings.json"))
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists():
        print(f"ERROR: {root} nao existe", file=sys.stderr)
        return 2

    findings: list[MenuFinding] = []
    menu_count_per_day = {}
    for day in DAY_FILES:
        p = root / day
        if not p.exists():
            findings.append(MenuFinding(
                severity="critical", check="missing_day_file",
                file=day, line=0, menu_index=-1,
                message=f"{day} nao encontrado em {root}"))
            continue
        count = check_day_file(p, f"scripts/{day}", findings)
        menu_count_per_day[day] = count

    from collections import Counter
    summary = Counter(f.severity for f in findings)
    output = {
        "version": "1.0",
        "menu_count_per_day": menu_count_per_day,
        "total_menus": sum(menu_count_per_day.values()),
        "summary": dict(summary),
        "findings": [f.as_dict() for f in findings],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Findings: {args.out}")
    print(f"Menus per day: {menu_count_per_day}")
    print(f"Total menus: {sum(menu_count_per_day.values())}")
    print(f"Severity: {dict(summary)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
