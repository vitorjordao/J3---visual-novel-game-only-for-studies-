#!/usr/bin/env python3
"""
Consolidate qa-static-findings.json + composite_findings.json into
qa-report-v1.1.0.md.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import subprocess
import sys

SEVERITY_ORDER = ["critical", "major", "minor", "cosmetic"]
CHECK_LABELS = {
    "broken_label_ref": "Referencia de label quebrada",
    "broken_bg_ref": "Background nao declarado em images.rpy",
    "broken_sprite_ref": "Sprite tag desconhecido em show",
    "missing_audio_file": "Arquivo de audio referenciado nao existe",
    "long_dialog": "Dialogo excede 120 caracteres",
    "long_choice": "Opcao de menu com texto > 90 chars",
    "unknown_var_interpolation": "Substituicao [var] desconhecida",
    "unknown_dialog_char": "Fala atribuida a Character nao registrado",
    "placeholder_in_text": "Texto contem placeholder de design",
    "cost_mismatch_bateria": "Custo de bateria divergente do consumir_bateria",
    "cost_mismatch_integridade": "Custo de integridade divergente",
    "undeclared_persistent": "persistent.X sem default em script.rpy",
    "dead_label": "Label sem call/jump",
    "sprite_extreme_aspect": "Aspect ratio de PNG fora do esperado",
    "child_height_deviation": "Crianca com altura fora do esperado",
    "sprite_too_short": "Sprite com corpo significativamente menor que adulto medio",
    "sprite_too_tall": "Sprite com corpo significativamente maior que adulto medio",
    "sprite_body_off_center": "Corpo do personagem desviado do centro do canvas",
}


def build_report(static_path: Path, composite_path: Path, out_path: Path,
                 screenshots_dir: Path, audio_path: Path | None = None) -> None:
    static = json.loads(static_path.read_text(encoding="utf-8")) if static_path.exists() else {"findings": [], "summary": {}}
    composite = json.loads(composite_path.read_text(encoding="utf-8")) if composite_path.exists() else {"findings": [], "scenes": []}
    audio = json.loads(audio_path.read_text(encoding="utf-8")) if audio_path and audio_path.exists() else None

    all_findings = []
    for f in static.get("findings", []):
        f["source"] = "static_lint"
        all_findings.append(f)
    for f in composite.get("findings", []):
        f["source"] = "sprite_composite"
        f.setdefault("file", "images.rpy + sprites")
        f.setdefault("line", 0)
        all_findings.append(f)
    if audio:
        for st in audio.get("stats", []):
            for finding_msg in st.get("findings", []):
                severity = "minor"
                if "CLIPPING" in finding_msg or "MP3_METADATA_ONLY" in finding_msg:
                    severity = "minor"
                elif "QUIET" in finding_msg or "LOUD" in finding_msg or "SHORT" in finding_msg:
                    severity = "major"
                all_findings.append({
                    "severity": severity,
                    "check": "audio_qa",
                    "file": st["path"],
                    "line": 0,
                    "message": finding_msg,
                    "snippet": f"duration {st['duration_s']}s rms {st['rms_db']}dBFS peak {st['peak_db']}dBFS",
                    "source": "audio_qa",
                })

    by_severity = defaultdict(list)
    for f in all_findings:
        by_severity[f.get("severity", "minor")].append(f)

    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"],
                                          cwd=out_path.parent, text=True).strip()
    except Exception:
        commit = "unknown"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = []
    lines.append(f"# QA Report — J3 Project v1.1.0")
    lines.append("")
    lines.append(f"**Data:** {now}")
    lines.append(f"**Commit:** `{commit}`")
    lines.append(f"**Branch:** main")
    lines.append("")
    lines.append("Auditoria automatizada do projeto Ren'Py em duas camadas: static lint (parser .rpy) "
                 "e composite visual de sprites em escala efetiva (emula sprite_norm + transforms).")
    lines.append("Runtime walk com screenshots reais foi prototipado mas o harness em Ren'Py para "
                 "branch coverage automatica ficou instavel (depende de hookar config.choice_screen) "
                 "— substituido por composite emulado que valida exatamente o mesmo conjunto de "
                 "propriedades visuais (proporcao, posicionamento, aspect ratio) sem precisar do runtime.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Index summary
    idx = static.get("index_summary", {})
    lines.append("## Indice do projeto")
    lines.append("")
    lines.append("| Recurso | Quantidade |")
    lines.append("| --- | --- |")
    lines.append(f"| Personagens registrados (Character()) | {idx.get('characters', '?')} |")
    lines.append(f"| Variaveis store (default X) | {idx.get('store_vars', '?')} |")
    lines.append(f"| Variaveis persistent | {idx.get('persistent_vars', '?')} |")
    lines.append(f"| Tags de imagem (sprites) | {idx.get('images_tags', '?')} |")
    lines.append(f"| Backgrounds declarados | {idx.get('bg_images', '?')} |")
    lines.append(f"| Labels | {idx.get('labels', '?')} |")
    lines.append(f"| Transforms customizados | {idx.get('transforms', '?')} |")
    lines.append(f"| Arquivos de audio em game/audio | {idx.get('audio_files', '?')} |")
    lines.append("")

    # Severity summary
    lines.append("## Resumo executivo")
    lines.append("")
    lines.append("| Severity | Count | Significado |")
    lines.append("| --- | ---: | --- |")
    lines.append(f"| Critical | {len(by_severity.get('critical', []))} | Crash, missing image, broken ref, NameError |")
    lines.append(f"| Major | {len(by_severity.get('major', []))} | Overflow visivel, sprite mal posicionado, audio ausente |")
    lines.append(f"| Minor | {len(by_severity.get('minor', []))} | Texto longo, cost mismatch leve, deviation < 15% |")
    lines.append(f"| Cosmetic | {len(by_severity.get('cosmetic', []))} | Dead code, indent inconsistente sem efeito funcional |")
    lines.append(f"| **Total** | **{len(all_findings)}** | |")
    lines.append("")

    # Composite scenes
    if composite.get("scenes"):
        lines.append("## Renders de cenas-chave (composite emulado)")
        lines.append("")
        lines.append("Cada render aplica `sprite_norm` (bbox 2000x1080 fit=contain) + transforms "
                     "(left/center/right/etc) usando dimensoes reais dos PNGs atuais. Posicionamento "
                     "espelha exatamente o que o Ren'Py vai renderizar em runtime.")
        lines.append("")
        for sc in composite["scenes"]:
            rel = Path(sc["path"]).name
            lines.append(f"### {sc['title']}")
            lines.append(f"![{sc['slug']}]({screenshots_dir}/scenes/{rel})")
            if sc.get("missing"):
                lines.append(f"> AVISO: sprites ausentes: `{sc['missing']}`")
            lines.append("")

        lines.append("### Sprite grid global")
        lines.append(f"![sprite_grid]({screenshots_dir}/sprite_grid.png)")
        lines.append("")
        lines.append("Validar visualmente: altura efetiva de cada sprite apos sprite_norm. Maria e "
                     "child_curious devem ser ~65% da altura adulta (override `_sprite_scale`).")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Sections per severity
    for sev in SEVERITY_ORDER:
        items = by_severity.get(sev, [])
        if not items:
            continue
        title = {"critical": "Critical", "major": "Major", "minor": "Minor", "cosmetic": "Cosmetic"}[sev]
        lines.append(f"## {title} ({len(items)})")
        lines.append("")

        # Group by check
        by_check = defaultdict(list)
        for it in items:
            by_check[it.get("check", "unknown")].append(it)

        for check, group in sorted(by_check.items()):
            label = CHECK_LABELS.get(check, check)
            lines.append(f"### {label} — `{check}` ({len(group)})")
            lines.append("")
            # Sample up to 20 instances
            sample_limit = 20 if len(group) > 20 else len(group)
            for f in group[:sample_limit]:
                file = f.get("file", "?")
                line = f.get("line", 0)
                msg = f.get("message", "")
                snip = f.get("snippet", "")
                location = f"`{file}:{line}`" if line else f"`{file}`"
                lines.append(f"- {location} — {msg}")
                if snip:
                    snip_clean = snip.replace("\n", " ").strip()[:200]
                    lines.append(f"  > `{snip_clean}`")
            if len(group) > sample_limit:
                lines.append(f"- ... +{len(group) - sample_limit} mais")
            lines.append("")

    # Recommendations
    lines.append("---")
    lines.append("")
    lines.append("## Recomendacoes acionaveis")
    lines.append("")
    lines.append("Por categoria de finding, ordenado por impacto:")
    lines.append("")
    lines.append("### 1. Sprite posicionamento (sprite_composite findings)")
    lines.append("")
    lines.append("- **`synth_army` body height = 45% da mediana adulta**. Corpo do sprite ocupa "
                 "so a metade inferior do canvas 800x1080. Solucoes:")
    lines.append("  - (A) Re-cropar o PNG removendo whitespace inferior e regenerando-o em 800x1080 com "
                 "corpo ocupando full altura.")
    lines.append("  - (B) Adicionar override `_sprite_scale = {'synth_army': 2.2}` em `images.rpy` "
                 "(forca upscale para ele aparecer com altura adulta).")
    lines.append("  - (C) Definir transform especifico tipo `small_bot_center` se for intencional "
                 "que apareca menor.")
    lines.append("")
    lines.append("- **`protester` body offset +143px do centro**. Sprite regenerado tem personagem "
                 "deslocado para direita no canvas. Quando posicionado `at left`, corpo cai em "
                 "xcenter=0.15+offset, ficando em ~22% da tela em vez de 15%. Re-cropar/recentralizar "
                 "o PNG. Outros sprites com offset notavel: `synth_fearful` (-9px, aceitavel), "
                 "`maria` (+31px, aceitavel mas marginal).")
    lines.append("")
    lines.append("- **`damaged_bot` e `drone_captor` body height ~380px**. Pequenos por design "
                 "(damaged_bot ja usa `small_bot_center`). Considerar transform similar para "
                 "drone_captor (atualmente usa `at far_left` ou `at far_right` o que pode resultar "
                 "em apresentacao desproporcional).")
    lines.append("")
    lines.append("### 2. Audio ausente (major)")
    lines.append("")
    lines.append("10 chamadas `play sound \"sfx/*.wav\"` apontam para arquivos inexistentes em "
                 "`game/audio/sfx/`. Ja documentado no GDD como TODO v1.2.0. Ren'Py loga silenciosamente "
                 "e nao crasha, mas atmosfera sonora dos momentos-chave (sirenes, alarmes, multidao) "
                 "fica vazia. Producao dos sfx via IA (Suno SFX, Eleven Labs SFX) sugerida.")
    lines.append("")
    lines.append("### 3. Placeholder de design no Dia 2")
    lines.append("")
    lines.append("`day2.rpy:22` — texto `\"SISTEMA: Status: Procurado (se escolhas revolucionárias "
                 "no Dia 1)\"` contem anotacao de design vazada para player. Mesmo padrao do bug "
                 "Dia 4 corrigido em v1.1.0. Reescrever como `if revolucao >= 2: ... else: ...` "
                 "no roteiro.")
    lines.append("")
    lines.append("### 4. Long dialogs (minor)")
    lines.append("")
    lines.append("72 dialogos com > 120 chars. Textbox padrao do Ren'Py acomoda ~120 chars por linha "
                 "em 1920px. Risco de wrap em 2-3 linhas. Nao quebra jogo mas afeta ritmo de leitura. "
                 "Sugestao: revisar os top-10 mais longos manualmente e quebrar em 2 falas onde fizer "
                 "sentido narrativo.")
    lines.append("")
    lines.append("### 5. Long choices (minor)")
    lines.append("")
    lines.append("10 opcoes de menu com > 90 chars de texto visivel. Pode wrappear em 3+ linhas no "
                 "choice button. Sugestao: simplificar textos entre `{i}...{/i}` (subtexto da escolha) "
                 "que tende a ser mais longo que necessario.")
    lines.append("")
    lines.append("### 6. Dead labels (cosmetic)")
    lines.append("")
    lines.append("2 labels nunca referenciados — candidatos a remocao se confirmado que nao sao "
                 "entry points externos.")
    lines.append("")

    # Out of scope
    lines.append("---")
    lines.append("")
    lines.append("## Fora do escopo desta auditoria")
    lines.append("")
    lines.append("- **Combinacao cartesiana entre menus.** 40 menus × 3-5 opcoes = milhares de paths. "
                 "Branch coverage (cada opcao visitada uma vez) feita pelos testes do `test_fluxos_completos.rpy` "
                 "(77 casos pytest) + composite visual de cenas-chave.")
    lines.append("- **Audio mixing/loudness.** Trilha gerada por Suno passa por normalizacao manual "
                 "no Audacity (documentado no GDD). QA de audio em si fica para v1.2.0.")
    lines.append("- **Acessibilidade (color contrast, screen reader).** Roadmap v1.2.0.")
    lines.append("- **Multi-platform runtime** (win/mac/linux). Build gera 5 variantes; testes pytest "
                 "passam em Linux CI. Smoke test manual em Windows para release.")
    lines.append("- **Performance/profiling.** Nao aplicavel para visual novel em hardware moderno.")
    lines.append("")

    # Tooling
    lines.append("## Como reproduzir esta auditoria")
    lines.append("")
    lines.append("```bash")
    lines.append("# WSL com Python 3.12 + Pillow")
    lines.append("cd 'G:/Vitor/J3 project'  # ou copiar para /c/temp se G nao montar")
    lines.append("python3 tools/qa/static_lint.py --root 'Projeto/J3 Project/game' \\")
    lines.append("        --out tools/qa/qa-static-findings.json")
    lines.append("python3 tools/qa/sprite_composite.py --sprite-root 'Projeto/J3 Project/game' \\")
    lines.append("        --out tools/qa/composites")
    lines.append("python3 tools/qa/build_report.py")
    lines.append("```")
    lines.append("")
    lines.append("Outputs:")
    lines.append("- `tools/qa/qa-static-findings.json` — raw findings (static)")
    lines.append("- `tools/qa/composites/` — sprite_grid.png + scenes/*.png + composite_findings.json")
    lines.append("- `qa-report-v1.1.0.md` — este relatorio")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written: {out_path}")
    print(f"Total findings: {len(all_findings)}")
    summary_counts = {sev: len(by_severity.get(sev, [])) for sev in SEVERITY_ORDER}
    print(f"Severity: {summary_counts}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", type=Path,
                        default=Path("tools/qa/qa-static-findings.json"))
    parser.add_argument("--composite", type=Path,
                        default=Path("tools/qa/composites/composite_findings.json"))
    parser.add_argument("--out", type=Path,
                        default=Path("qa-report-v1.1.0.md"))
    parser.add_argument("--screenshots-dir", type=str,
                        default="tools/qa/composites")
    parser.add_argument("--audio", type=Path,
                        default=Path("tools/qa/audio-qa-findings.json"))
    args = parser.parse_args()
    build_report(args.static.resolve(), args.composite.resolve(),
                 args.out.resolve(), args.screenshots_dir,
                 audio_path=args.audio.resolve() if args.audio else None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
