# J3 - A Consciência Artificial

## Sobre o Projeto

**J3 - A Consciência Artificial** é um visual novel cyberpunk desenvolvido em Ren'Py que explora identidade, preconceito e livre-arbítrio. O jogador controla **J3-001**, uma unidade robótica experimental que desperta sem memória em uma cidade hostil. Cada escolha molda sua personalidade e define um entre múltiplos finais possíveis.

- **Gênero:** Visual Novel / Narrativa Interativa
- **Engine:** Ren'Py 8.x
- **Versão atual:** 1.0
- **Idioma:** Português Brasileiro
- **Duração estimada:** 35-70 minutos por run
- **Classificação:** +16

## Estrutura do Projeto

```
J3 Project/
├── game/
│   ├── script.rpy                # Entrada principal
│   ├── options.rpy               # Configurações do jogo
│   ├── gui.rpy                   # Interface gráfica
│   ├── screens.rpy               # Telas customizadas
│   ├── sistema_j3.rpy            # Sistema de personalidade/HUD
│   ├── finais_alternativos.rpy   # Ramificações de final
│   ├── images.rpy                # Declaração de imagens
│   │
│   ├── scripts/                  # Scripts por dia
│   │   ├── day1.rpy              # Dia 1 - A Avenida
│   │   ├── day2.rpy              # Dia 2 - O Fliperama
│   │   ├── day3.rpy              # Dia 3 - O Beco
│   │   ├── day4.rpy              # Dia 4 - O Refúgio
│   │   ├── day5.rpy              # Dia 5 - O Cerco
│   │   ├── day6.rpy              # Dia 6 - A Revelação
│   │   ├── day7.rpy              # Dia 7 - O Final
│   │   └── functions.rpy         # Funções auxiliares
│   │
│   ├── characters/               # Sprites dos personagens
│   ├── backgrounds/              # Cenários (day1..day7)
│   ├── audio/                    # music / sfx / voice
│   ├── gui/                      # Elementos de UI + fontes
│   ├── transitions/              # Transições visuais
│   ├── test_mecanicas.rpy        # Testes de mecânica
│   └── test_fluxos_completos.rpy # Testes de fluxo integral
│
└── README.md
```

Documentação e roteiro ficam em `Documentação/` e `Roteiro/` na raiz do repositório.

## Sistema de Jogo

### Personalidade (3 eixos, 0-10)
- **Submissão** — obediência e sacrifício
- **Revolução** — rebelião e confronto
- **Intelecto** — estratégia e manipulação

### Sobrevivência
- **Bateria (0-100%)** — consumida por ações; 0% = Final 0A (desligamento)
- **Integridade (0-100%)** — só cai em conflito físico; 0% = Final 0B (colapso)
- **Bateria ≤10% + Integridade ≤20%** = Final 0C (captura)

### Memória
Fragmentos e flashbacks recuperados em eventos específicos ao longo dos 7 dias.

### HUD J3
Interface em tempo real mostrando bateria, integridade, personalidade, memória recuperada e dia atual. Toggle via `show/hide screen j3_hud`.

## Estrutura Narrativa

7 dias, 3 atos:
- **Ato 1 (Dias 1-3):** Despertar, conflito, preconceito estrutural
- **Ato 2 (Dias 4-5):** Consequências e cerco
- **Ato 3 (Dias 6-7):** Revelação e escolha final

**Finais:** 4 finais principais por personalidade dominante + 3 game overs (0A/0B/0C).

## Tema Visual

**Cyberpunk 2D pixel art 16/32-bit com pegada heroica.** Referências: Snatcher, Policenauts, Shadowrun SNES, VA-11 HALL-A, capas de JRPG clássico, grafite urbano brasileiro.

- Paleta restrita: azul escuro, roxo, verde/laranja neon, magenta para elementos sintéticos
- Enquadramento frontal heroico, silhueta legível
- Dithering e cores chapadas, sem gradiente suave
- HUD com borda CRT/arcade, scanlines, fonte pixelada

## Status

- [x] Scripts Dias 1-7 implementados
- [x] Sistema de personalidade + HUD funcional
- [x] Sistema de bateria/integridade
- [x] Finais alternativos implementados
- [x] Testes de mecânica e fluxo
- [x] Sprites dos personagens principais
- [x] Interface cyberpunk completa
- [x] **Build 1.0 gerado** (Windows / Mac / Linux / Market)

## Como Executar

### Jogar build pronto
Baixar release do Itch.io ou repositório (Windows/Mac/Linux).

### Rodar do código-fonte
1. Instalar **Ren'Py SDK 8.x**
2. Abrir projeto em `Projeto/J3 Project/`
3. `Launch Project` (F5)

## Builds

Distribuíveis gerados em `Projeto/J3ConscienciaArtificial-1.0-dists/` (não versionados no Git por tamanho — publicados como release/anexo):
- `J3ConscienciaArtificial-1.0-pc.zip` (Windows/Linux universal)
- `J3ConscienciaArtificial-1.0-win.zip` (Windows)
- `J3ConscienciaArtificial-1.0-mac.zip` (macOS)
- `J3ConscienciaArtificial-1.0-linux.tar.bz2` (Linux)
- `J3ConscienciaArtificial-1.0-market.zip` (Itch.io)

## Desenvolvimento

- **Arte:** Krita / GIMP (pixel art)
- **Áudio:** Audacity
- **Código:** VS Code + Ren'Py
- **Versionamento:** Git / GitHub
- **Distribuição:** Itch.io

### Padrões de código
- Use `escolha_j3()` para escolhas que afetam personalidade
- Use `call mensagem_sistema()` para mensagens do sistema
- Sistema de personalidade em `sistema_j3.rpy`
- HUD em `screens.rpy` (screen `j3_hud`)

## Contato

**Desenvolvedor:** Vitor Jordão
**Projeto:** J3 - A Consciência Artificial
**Motor:** Ren'Py 8.x

---

*"O que nos torna humanos não é nossa origem, mas nossas escolhas."*
