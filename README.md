# J3 - A Consciência Artificial

**Visual novel cyberpunk em Ren'Py.** Robô sem memória descobre sua identidade através de escolhas que moldam sua alma em mundo cyberpunk preconceituoso.

- **Gênero:** Visual Novel / Narrativa Interativa
- **Engine:** Ren'Py 8.x
- **Versão:** 1.0
- **Idioma:** Português Brasileiro
- **Duração:** 35-70 min por run
- **Classificação:** +16
- **Desenvolvedor:** Vitor Jordão

---

## 📂 Mapa do Repositório

```
J3 project/
├── README.md                          ← este arquivo (índice geral)
├── AGENT_KNOWLEDGE_BASE.md            ← base de conhecimento para agentes IA
│
├── Documentação/                      ← GDD, cronograma, guias
│   ├── GDD - J3 Projeto.md
│   ├── GDD - J3 Projeto.docx
│   ├── RESUMO_ENTREGA_GDD.md
│   ├── Resumo MINC - J3 Projeto.md
│   ├── Cronograma/
│   │   └── Cronograma de Desenvolvimento.md
│   └── Guia de Implementação/
│       └── Guia Ren'Py.md
│
├── Roteiro/                           ← roteiro narrativo
│   ├── J3 - Roteiro.md
│   └── Dias/                          ← roteiro dia a dia
│       ├── Dia 1 - A Avenida.md
│       ├── Dia 2 - O Fliperama.md
│       ├── Dia 3 - O Beco.md
│       ├── Dia 4 - O Refúgio.md
│       ├── Dia 5 - O Cerco.md
│       ├── Dia 6 - A Revelação.md
│       └── Dia 7 - O Final.md
│
├── Projeto/
│   ├── J3 Project/                    ← projeto Ren'Py (código-fonte)
│   │   ├── README.md                  ← detalhes técnicos do projeto
│   │   └── game/                      ← scripts, assets, sistema J3
│   │
│   └── J3ConscienciaArtificial-1.0-dists/  ← builds (gitignored — ver Releases)
│
├── minc-manual-game-e-cultura.md      ← manual MinC (referência edital)
├── minc-manual-game-e-cultura.pdf
│
├── diagrama_j3_ascii.md               ← diagrama de árvores de decisão (ASCII)
├── diagrama_j3_visual.html            ← diagrama interativo
├── diagrama_arvores_j3.py             ← gerador dos diagramas
│
├── convert_gdd_to_docx.py             ← utilitário md→docx do GDD
├── convert_to_docx.py                 ← utilitário md→docx genérico
└── test_externo.py                    ← testes externos
```

---

## 📖 Documentação

### Principal
- **[GDD - Game Design Document](Documentação/GDD%20-%20J3%20Projeto.md)** — documento completo de design (narrativa, mecânicas, arte, som, personagens)
- **[Resumo da Entrega MinC](Documentação/RESUMO_ENTREGA_GDD.md)** — consolidado para entrega
- **[Resumo MinC](Documentação/Resumo%20MINC%20-%20J3%20Projeto.md)** — pitch/overview do edital

### Planejamento e Implementação
- **[Cronograma de Desenvolvimento](Documentação/Cronograma/Cronograma%20de%20Desenvolvimento.md)**
- **[Guia Ren'Py](Documentação/Guia%20de%20Implementação/Guia%20Ren'Py.md)** — referência técnica Ren'Py

### Referência Externa
- **[Manual MinC - Games e Cultura](minc-manual-game-e-cultura.md)** ([PDF](minc-manual-game-e-cultura.pdf))

---

## 🎬 Roteiro

### Visão Geral
- **[Roteiro Principal](Roteiro/J3%20-%20Roteiro.md)**

### Por Dia
| Dia | Título | Link |
|-----|--------|------|
| 1 | A Avenida | [📄](Roteiro/Dias/Dia%201%20-%20A%20Avenida.md) |
| 2 | O Fliperama | [📄](Roteiro/Dias/Dia%202%20-%20O%20Fliperama.md) |
| 3 | O Beco | [📄](Roteiro/Dias/Dia%203%20-%20O%20Beco.md) |
| 4 | O Refúgio | [📄](Roteiro/Dias/Dia%204%20-%20O%20Refúgio.md) |
| 5 | O Cerco | [📄](Roteiro/Dias/Dia%205%20-%20O%20Cerco.md) |
| 6 | A Revelação | [📄](Roteiro/Dias/Dia%206%20-%20A%20Revelação.md) |
| 7 | O Final | [📄](Roteiro/Dias/Dia%207%20-%20O%20Final.md) |

---

## 💻 Código-fonte

- **[Projeto Ren'Py (J3 Project)](Projeto/J3%20Project/)** — código principal
- **[README técnico do projeto](Projeto/J3%20Project/README.md)** — estrutura de pastas, sistema J3, como rodar

### Arquivos-chave do game
| Arquivo | Função |
|---------|--------|
| [script.rpy](Projeto/J3%20Project/game/script.rpy) | Entrada principal |
| [options.rpy](Projeto/J3%20Project/game/options.rpy) | Configurações |
| [gui.rpy](Projeto/J3%20Project/game/gui.rpy) | Interface gráfica |
| [screens.rpy](Projeto/J3%20Project/game/screens.rpy) | Telas customizadas + HUD |
| [sistema_j3.rpy](Projeto/J3%20Project/game/sistema_j3.rpy) | Personalidade + sobrevivência |
| [finais_alternativos.rpy](Projeto/J3%20Project/game/finais_alternativos.rpy) | Ramificações de final |
| [scripts/day1-day7.rpy](Projeto/J3%20Project/game/scripts/) | Scripts por dia |
| [scripts/functions.rpy](Projeto/J3%20Project/game/scripts/functions.rpy) | Funções auxiliares |

---

## 🗺️ Diagramas

- **[Árvore de Decisão - ASCII](diagrama_j3_ascii.md)** — visualização textual
- **[Diagrama Visual Interativo](diagrama_j3_visual.html)** — abrir no navegador
- **[Gerador de Diagramas](diagrama_arvores_j3.py)** — script Python

---

## 🎮 Sistema de Jogo

### Personalidade (3 eixos, 0-10)
- **Submissão** — obediência e sacrifício
- **Revolução** — rebelião e confronto
- **Intelecto** — estratégia e manipulação

### Sobrevivência
- **Bateria (0-100%)** — ações consomem; 0% = Final 0A (desligamento)
- **Integridade (0-100%)** — só cai em conflito físico; 0% = Final 0B (colapso)
- **Bateria ≤10% + Integridade ≤20%** = Final 0C (captura)

### Narrativa
- 7 dias em 3 atos
- 4 finais principais por personalidade dominante
- 3 game overs (0A/0B/0C)

---

## 🚀 Como Executar

### Jogar build pronto
Baixar em **[Releases](../../releases)** do GitHub ou Itch.io.

### Rodar do código-fonte
1. Instalar **[Ren'Py SDK 8.x](https://www.renpy.org/latest.html)**
2. Abrir `Projeto/J3 Project/` no Ren'Py Launcher
3. `Launch Project` (F5)

### Build de distribuição
Via Ren'Py Launcher → `Build Distributions`. Saídas em `Projeto/J3ConscienciaArtificial-1.0-dists/`:
- `*-pc.zip` — Windows/Linux universal
- `*-win.zip` — Windows
- `*-mac.zip` — macOS
- `*-linux.tar.bz2` — Linux
- `*-market.zip` — Itch.io

> ⚠️ **Builds não são versionados no Git** (arquivos >100MB estouram limite GitHub). Publicação via GitHub Releases / Itch.io.

---

## 🛠️ Ferramentas de Desenvolvimento

| Área | Ferramenta |
|------|------------|
| Arte | Krita, GIMP (pixel art) |
| Áudio | Audacity |
| Código | VS Code, Ren'Py Launcher |
| Versionamento | Git, GitHub |
| Distribuição | Itch.io, GitHub Releases |

---

## 🎨 Direção Visual

Cyberpunk 2D pixel art 16/32-bit com pegada heroica. Referências: Snatcher, Policenauts, Shadowrun SNES, VA-11 HALL-A, capas de JRPG clássico, grafite urbano brasileiro. Ver [GDD seção 4](Documentação/GDD%20-%20J3%20Projeto.md) para detalhes.

---

## 📋 Status

- [x] Scripts Dias 1-7 implementados
- [x] Sistema de personalidade + HUD
- [x] Sistema bateria/integridade
- [x] Finais alternativos
- [x] Testes de mecânica e fluxo
- [x] Sprites personagens principais
- [x] Build 1.0 gerado (Win/Mac/Linux/Market)
- [ ] Release publicada no GitHub/Itch.io

---

## 👤 Contato

**Vitor Jordão** — [vitorpeviano@gmail.com](mailto:vitorpeviano@gmail.com)

Repositório: **[J3 - Visual Novel (Studies)](https://github.com/vitorjordao/J3---visual-novel-game-only-for-studies-)**

---

*"O que nos torna humanos não é nossa origem, mas nossas escolhas."*
