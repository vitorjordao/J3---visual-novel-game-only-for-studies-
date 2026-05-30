# Menu + Save Validation Report — J3 Project v1.1.1

**Data:** 2026-05-30
**Branch:** main
**Tool:** `tools/qa/menu_validator.py`

Validacao automatica de todos os 42 menu blocks em day*.rpy e dos 7 auto-saves do jogo. Checks aplicados:

1. Estrutura sintatica do menu (header + opcoes indentadas).
2. Cada opcao tem corpo nao-vazio.
3. Tag `[custo(B[,I])]` bate com `$ consumir_bateria(B)` + `$ consumir_integridade(I)`.
4. Tag `[ganho(B[,I])]` bate com `$ recarregar_bateria(B)` + `$ reparar_integridade(I)`.
5. Opcoes que mudam estado (`modificar_personalidade`, `consumir_*`, `recarregar_*`, `reparar_*`) chamam `call atualizar_status` para refrescar HUD.
6. `modificar_personalidade` nao chamada com delta zero (no-op).
7. Cada `day*.rpy` tem `renpy.save("auto_save_dayN", ...)`.
8. Slot do save bate com numero do dia (sem cross-contamination de saves).

---

## Escopo

| Day | # Menus | Auto-save | Slot correto |
|---|---:|---|---|
| day1.rpy | 5 | sim (linha 311) | `auto_save_day1` ✓ |
| day2.rpy | 6 | sim (linha 276) | `auto_save_day2` ✓ |
| day3.rpy | 6 | sim (linha 273) | `auto_save_day3` ✓ |
| day4.rpy | 7 | sim (linha 292) | `auto_save_day4` ✓ |
| day5.rpy | 7 | sim (linha 309) | `auto_save_day5` ✓ |
| day6.rpy | 7 | sim (linha 278) | `auto_save_day6` ✓ |
| day7.rpy | 4 | sim (linha 27, pre-final) | `auto_save_day7` ✓ |
| **Total** | **42** | **7/7** | **100%** |

Saves expostos via `screens.rpy:677-722` (FilePageNameInputValue + FileAction) na pagina "Automatic saves" do menu Load — padrao Ren'Py, sem screens custom necessarios.

---

## Findings antes vs. depois das correcoes

| Severity | Antes | Depois | Diferenca |
|---|---:|---:|---:|
| Critical | 0 | 0 | 0 |
| Major | 4 | 4 | 0 |
| Minor | 54 | 0 | -54 |
| Cosmetic | 0 | 0 | 0 |

**54 fixes aplicados automaticamente** via `tools/qa/fix_menu_atualizar.py`:
- Padrao detectado: opcoes com `consumir_bateria`/`consumir_integridade`/`modificar_personalidade` mas sem `call atualizar_status` no final. Resulta em HUD desatualizado (player ve bateria/integridade antiga ate o proximo evento).
- Fix: adicionar `call atualizar_status` antes de sair do escopo da opcao.
- Distribuicao: day1 (+2), day3 (+3), day4 (+15), day5 (+16), day6 (+18). Day2 e day7 ja estavam corretos.

**Bug bonus detectado e corrigido** (mesmo padrao do day2 fix v1.1.0):
- `day3.rpy:22` continha `"SISTEMA: Status: Escondido ou procurado (depende das escolhas)"` — placeholder de design vazado para player.
- Substituido por ramificacao `if revolucao >= 3 / elif submissao >= 3 / else`.

---

## Major findings remanescentes (4)

Todos sao do mesmo padrao: **menus com 1 unica opcao** em day7 finais.

| File:line | Cena | Texto |
|---|---|---|
| `day7.rpy:51` | Final Sacrificio (apos Elena) | "Aceitar o sacrificio" |
| `day7.rpy:99` | Final Revolucao (apos Comandante) | "Lutar pela liberdade" |
| `day7.rpy:140` | Final Estrategico (apos hack) | "Revelar a verdade ao mundo" |
| `day7.rpy:183` | Final Balanceado | "Negociar coexistencia" |

**Analise:** padrao intencional de "menu rhetorico" — apresenta UI de escolha mas com apenas 1 caminho ja determinado pela rota de personalidade. Player clica para confirmar o desfecho. Funcionalmente sao "press to continue" estilizados.

**Recomendacao:** trade-off de UX vs. dramaturgia. Duas alternativas para v1.1.2:
- (A) Substituir cada um por `narrator "..."` + `j3 "..."` plain — UI fica honesta mas perde o beat de "decisao final".
- (B) Manter como esta + adicionar comentario explicito `# menu intencional: 1 opcao = confirmacao do desfecho final` no codigo para evitar que reviews futuras quebrem o padrao.

Recomendo (B) por preservar o ritual narrativo. Severidade real = informational, nao bug.

---

## Validacao detalhada por categoria

### Cost/Gain alignment (zero findings)

Todas as 135+ opcoes com tag `[custo(...)]` ou `[ganho(...)]` tem corpo correspondente:
- `[custo(5)]` → 1 chamada `consumir_bateria(5)` no corpo ✓
- `[custo(2, 10)]` → `consumir_bateria(2)` + `consumir_integridade(10)` ✓
- `[ganho(15)]` → `recarregar_bateria(15)` ✓
- `[ganho(integ=12)]` → `reparar_integridade(12)` ✓

Inclusive o fix v1.1.0 do day3 suborno (`recarregar_bateria(15)` premium) bate com analise.

### Personalidade (zero no-ops)

Nenhum `modificar_personalidade("...", 0)` detectado. Todas as escolhas movem o eixo correspondente em pelo menos +1.

### Save coverage (100%)

Cobertura completa. Cross-check do slot:
- Cada `day{N}.rpy` salva exclusivamente em `auto_save_day{N}` (sem overlap).
- Day 7 salva pre-final (linha 27) por design — permite replay do final menu sem refazer days 1-6.
- Estado salvo: padrao Ren'Py `renpy.save()` persiste store inteiro + persistent + posicao + rollback. Variaveis cobertas:
  - store: bateria, integridade, submissao, revolucao, intelecto, dia_atual, memoria_recuperada, maya_ally, elias_ally, unit7_alive, elena_alive, escolha_feita, nvl_list.
  - persistent: dias_sobrevividos.
  - Tudo necessario para resumir do save sem perda de estado.

### Alliance flags (consistente)

Cada `$ maya_ally = True` / `$ elias_ally = True` esta dentro de opcoes de menu que correspondem narrativamente a formar alianca (ajudar Maya no fliperama, aceitar carregador de Elias, etc.). Flags consumidas corretamente nos dias subsequentes via `if maya_ally:` / `if elias_ally:` em day4-7.

---

## Testes regressao

Apos as 54 insercoes + correcao day3:22:
- `pytest tests/`: **77/77 passam** (test_finais, test_musica, test_personalidade, test_recursos).
- `python3 test_externo.py`: **10/10 passam**.
- `static_lint.py`: 0 critical, 0 major, 82 minor (longs deferred), 2 cosmetic.
- `sprite_composite.py`: 0 size outliers.

---

## Como reproduzir

```bash
cd 'G:/Vitor/J3 project'  # ou copiar para /c/temp se G nao montar no WSL
python3 tools/qa/menu_validator.py \
        --root 'Projeto/J3 Project/game/scripts' \
        --out tools/qa/menu-validation-findings.json
# Se houver findings missing_atualizar_status:
python3 tools/qa/fix_menu_atualizar.py \
        --findings tools/qa/menu-validation-findings.json \
        --root 'Projeto/J3 Project/game'
# Re-validar:
python3 tools/qa/menu_validator.py --root 'Projeto/J3 Project/game/scripts' \
        --out tools/qa/menu-validation-findings.json
python3 -m pytest
python3 test_externo.py
```

---

## Conclusao

Menus 100% funcionais. Saves 100% cobertos. Coerencia cost/gain/state-update validada em 42 menus × ~135 opcoes. 4 majors remanescentes sao single-option finais intencionais (recomendacao: anotar como design pattern no codigo).
