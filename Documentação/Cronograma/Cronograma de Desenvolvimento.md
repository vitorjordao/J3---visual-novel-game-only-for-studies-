# Cronograma de Desenvolvimento - J3 Projeto (Dev Solo)

**Data de Início:** 21 de Março de 2026
**Data de Lançamento (build final):** 30 de Maio de 2026
**Duração efetiva:** ~10 semanas (previsto 3 meses, antecipado em 3 semanas)

## Fases do Projeto (Equipe: 1 Pessoa)

### Fase 1: Documentação e Design (21/03 - 03/04/2026)

| Período | Tarefas | Status |
| :--- | :--- | :--- |
| 07/03 - 08/03 | Organizar estrutura de arquivos e pastas | Concluído |
| 14/03 - 15/03 | Criar roteiro em arquivos individuais por dia | Concluído |
| 21/03 - 22/03 | Configurar ambiente Ren'Py e projeto base | Concluído |
| 28/03 - 03/04 | Criar GDD completo e revisar roteiro | Concluído |

### Fase 2: Programação e Arte (04/04 - 24/04/2026)

| Período | Tarefas | Status |
| :--- | :--- | :--- |
| 04/04 - 12/04 | Arte conceitual + sprites placeholder v0.5 (5 principais) | Concluído |
| 13/04 - 18/04 | Terminar programação dos 7 dias + finais + mecânicas | Concluído |
| 18/04 - 24/04 | Regerar elenco completo via IA (v1.0, 25 sprites + 22 backgrounds) | Concluído |

### Fase 3: Balanceamento, Playtest e Polimento (24/04 - 30/05/2026)

| Período | Tarefas | Status |
| :--- | :--- | :--- |
| 24/04 - 03/05 | Build v1.0 + correções de balanceamento + integração de arte | Concluído |
| 04/05 - 24/05 | Playtest interno + correções v1.1 (4 bugs + trilha sonora via Suno) | Concluído |
| 25/05 - 30/05 | Validações finais v1.1.1/v1.2.0 + síntese de sfx + build final | Concluído |

## Linha do Tempo de Releases

| Versão | Data | Marco |
| :--- | :--- | :--- |
| v0.1 | Mar/2026 | Setup Ren'Py, personagens, primeiros diálogos Dias 1-3, sistema J3 rascunhado |
| v0.2 | Mar/2026 | Mecânicas de sobrevivência (bateria/integridade), HUD, finais críticos 0A/0B/0C |
| v0.3 | Mar/2026 | Roteiros dos 7 dias completos, finais 1-4 por personalidade dominante |
| v0.4 | Abr/2026 | Menu de debug, testes de mecânicas e fluxos completos, bugs iniciais corrigidos |
| v0.5 | Abr/2026 | Arte inicial — 5 sprites principais + 1 background, gerados via Nano Banana |
| v1.0 | 03/04/2026 | Arte completa (25 sprites + 22 backgrounds via Nano Banana 2), balanceamento corrigido, primeira release MINC |
| v1.1 | 24/05/2026 | Ciclo de playtest: 4 bugs corrigidos (Dia 3 suborno, Dia 4 placeholder, Dia 7 auto-save, normalização de sprites). Trilha sonora (5 faixas Suno) com aleatorização persistente |
| v1.1.1 | 30/05/2026 | Segunda passada de validações: synth_army upscale + zorder, protester recenter, day3 placeholder ramificado, 54x atualizar_status, 10 sfx sintetizados localmente em Python |
| v1.2.0 | 30/05/2026 | **Build final.** Fix patrol_drone Dia 1 (crop pixel-absoluto obsoleto cortava drone após regeneração). Roteiro completo consolidado em docx único para entrega |

## Distribuição

Build v1.2.0 em `Projeto/J3ConscienciaArtificial-1.2.0-dists/`:

| Arquivo | Tamanho | Plataforma |
| :--- | :--- | :--- |
| `*-win.zip` | 66 MB | Windows |
| `*-mac.zip` | 73 MB | macOS |
| `*-linux.tar.bz2` | 59 MB | Linux |
| `*-pc.zip` | 78 MB | Windows + Linux combinado |
| `*-market.zip` | 104 MB | Tudo + Mac (itch.io / marketplaces) |

## Recursos Auxiliares

- **GDD completo:** `Documentação/GDD - J3 Projeto.md` (+ docx)
- **Roteiro completo:** `Documentação/Roteiro - J3 Completo.md` (+ docx, 1581 linhas, 7 dias)
- **Repositório:** https://github.com/vitorjordao/J3---visual-novel-game-only-for-studies-
- **Branch:** `main`
