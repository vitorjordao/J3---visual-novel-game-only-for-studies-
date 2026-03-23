# Estrutura de pastas para o projeto J3
# Este arquivo documenta a organização de assets do jogo

## Pastas Principais:

### /game/
├── script.rpy                    # Script principal do jogo
├── options.rpy                   # Configurações do jogo
├── gui.rpy                       # Configuração da interface
├── screens.rpy                   # Telas personalizadas
├── 
├── characters/                   # Personagens e sprites
│   ├── j3/                       # J3-001 protagonista
│   │   ├── j3_neutral.png        # Sprite neutro
│   │   ├── j3_confused.png       # Sprite confuso
│   │   ├── j3_determined.png     # Sprite determinado
│   │   └── j3_hologram.png       # Efeito holográfico
│   ├── maya/                     # Maya - aliada humana
│   ├── elias/                    # Elias - entregador
│   ├── unit7/                    # Unit-7 - sintético militar
│   └── elena/                    # Dra. Elena - cientista
│
├── backgrounds/                  # Cenários e backgrounds
│   ├── day1/                     # Dia 1 - A Avenida
│   │   ├── avenue_rain.png       # Avenida com chuva
│   │   ├── avenue_night.png      # Avenida noturna
│   │   └── alley_dark.png        # Beco escuro
│   ├── day2/                     # Dia 2 - O Fliperama
│   │   ├── arcade_inside.png     # Interior do fliperama
│   │   └── arcade_neon.png       # Fliperama externo
│   ├── day3/                     # Dia 3 - O Beco
│   ├── day4/                     # Dia 4 - O Refúgio
│   ├── day5/                     # Dia 5 - O Cerco
│   ├── day6/                     # Dia 6 - A Revelação
│   └── day7/                     # Dia 7 - O Final
│
├── gui/                          # Interface e elementos gráficos
│   ├── buttons/                  # Botões personalizados
│   ├── textbox/                  # Caixas de diálogo
│   ├── menus/                    # Menus do jogo
│   └── hud/                      # Heads-up display do J3
│
├── audio/                        # Áudio do jogo
│   ├── music/                    # Músicas temáticas
│   │   ├── main_theme.mp3        # Tema principal
│   │   ├── cyberpunk_ambient.mp3 # Ambiente cyberpunk
│   │   └── tension_theme.mp3     # Tema de tensão
│   ├── sfx/                      # Efeitos sonoros
│   │   ├── system_boot.wav       # Som de inicialização
│   │   ├── choice_select.wav     # Som de escolha
│   │   └── notification.wav      # Notificação do sistema
│   └── voice/                    # Dublagens (futuro)
│
├── fonts/                        # Fontes personalizadas
│   ├── cyberpunk.ttf             # Fonte principal cyberpunk
│   ├── system_font.ttf           # Fonte do sistema J3
│   └── dialogue_font.ttf         # Fonte para diálogos
│
├── scripts/                      # Scripts organizados por dia
│   ├── day1.rpy                  # Dia 1 - A Avenida
│   ├── day2.rpy                  # Dia 2 - O Fliperama
│   ├── day3.rpy                  # Dia 3 - O Beco
│   ├── day4.rpy                  # Dia 4 - O Refúgio
│   ├── day5.rpy                  # Dia 5 - O Cerco
│   ├── day6.rpy                  # Dia 6 - A Revelação
│   └── day7.rpy                  # Dia 7 - O Final
│
└── transitions/                  # Efeitos de transição
    ├── glitch.rpy                # Efeito glitch cyberpunk
    ├── hologram.rpy              # Transição holográfica
    └── system_boot.rpy          # Animação de boot

## Organização de Desenvolvimento:

### Fase 1: Configuração Básica
- Estrutura de pastas
- Configuração de cores e fontes
- Sistema de personagens
- Variáveis globais

### Fase 2: Assets Visuais
- Backgrounds principais
- Sprites básicos dos personagens
- Interface personalizada

### Fase 3: Conteúdo
- Scripts dos diálogos
- Sistema de escolhas
- Música e efeitos sonoros

### Fase 4: Polimento
- Transições e animações
- Efeitos especiais
- Testes e correções
