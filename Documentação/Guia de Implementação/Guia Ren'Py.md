# Guia de Implementação em Ren'Py - J3 Projeto

## Estrutura de Arquivos Recomendada

```
/game/
  script.rpy           # Arquivo principal de inicialização
  /days/
    day1.rpy          # Dia 1: A Avenida
    day2.rpy          # Dia 2: O Fliperama  
    day3.rpy          # Dia 3: O Beco
    day4.rpy          # Dia 4: O Refúgio
    day5.rpy          # Dia 5: O Cerco
    day6.rpy          # Dia 6: A Revelação
    day7.rpy          # Dia 7: O Final
  /characters/
    j3.rpy            # Definições do protagonista
    maya.rpy          # Definições da aliada
    elias.rpy         # Definições do aliado
    unit7.rpy         # Definições do líder
    elena.rpy         # Definições da cientista
  /system/
    choices.rpy       # Sistema de escolhas
    stats.rpy         # Sistema de estatísticas
    endings.rpy       # Lógica dos finais
    ui.rpy            # Interface personalizada
  /assets/
    /images/
      backgrounds/
      characters/
      ui/
    /audio/
      music/
      sfx/
      voice/
```

## Sistema de Escolhas e Estatísticas

### Variáveis Globais

```python
# Sistema de pontos de personalidade
default submission_points = 0
default revolution_points = 0  
default intellect_points = 0

# Status dos personagens
default maya_status = "neutral"  # neutral, ally, enemy
default elias_status = "neutral"  # neutral, ally, enemy
default unit7_status = "neutral"  # neutral, ally, enemy

# Status de J3
default j3_battery = 87
default j3_integrity = 100
default j3_memory_corrupted = True
```

### Função de Escolha

```python
# Função para registrar escolhas
label make_choice(choice_type):
    if choice_type == "submission":
        $ submission_points += 1
        $ j3_status = "submissive"
    elif choice_type == "revolution":
        $ revolution_points += 1
        $ j3_status = "revolutionary"
    elif choice_type == "intellect":
        $ intellect_points += 1
        $ j3_status = "strategic"
    
    # Atualiza status dos personagens conforme necessário
    update_character_relationships()
    return
```

### Sistema de Diálogos com Escolhas

```python
# Exemplo de implementação de cena com escolhas
label day1_scene2:
    scene bg_avenue_rain
    show j3 neutral at center
    
    "Um grupo de manifestantes se aproxima."
    
    menu:
        "Manifestante: 'Olha só... mais uma dessas bonecas de lata!'"
        
        "[ESCOLHA 1 - Submissa]":
            jump choice_submissive_1
            
        "[ESCOLHA 2 - Neutra]":
            jump choice_neutral_1
            
        "[ESCOLHA 3 - Revolucionária]":
            jump choice_revolutionary_1

label choice_submissive_1:
    $ make_choice("submission")
    j3 "Sinto muito. Meus sistemas acabaram de ser ativados."
    "O homem ri e chuta o pé de J3. +1 Submissão"
    jump day1_scene3

label choice_neutral_1:
    j3 "Sou uma unidade autônoma de aparência humana."
    "O homem fica confuso. Status: Neutralidade mantida"
    jump day1_scene3

label choice_revolutionary_1:
    $ make_choice("revolution")
    j3 "Meus sensores indicam que esta é uma via pública."
    "O homem recua um passo, surpreso. +1 Revolução"
    jump day1_scene3
```

## Sistema de Finais

### Lógica de Determinação de Final

```python
label determine_ending:
    # Verifica qual final baseado nos pontos acumulados
    if submission_points >= 8:
        jump ending_sacrifice
    elif revolution_points >= 8:
        jump ending_revolution
    elif intellect_points >= 6:
        jump ending_strategic
    else:
        jump ending_balanced

# Finais específicos
label ending_sacrifice:
    scene bg_laboratory
    "J3 se entrega para reprogramação total..."
    # Cenas do final de sacrifício
    return

label ending_revolution:
    scene bg_plaza_battle
    "J3 lidera a revolução final..."
    # Cenas do final revolucionário
    return

label ending_strategic:
    scene bg_control_center
    "J3 expõe a verdade ao mundo..."
    # Cenas do final estratégico
    return

label ending_balanced:
    scene bg_crossroads
    "J3 escolhe um novo caminho..."
    # Cenas do final equilibrado
    return
```

## Sistema de Personagens

### Definições de Personagens

```python
# j3.rpy
define j = Character("J3", what_color="#00ff00")
define j_thought = Character("J3", what_color="#00ff00", what_italic=True)

# maya.rpy
define m = Character("Maya", what_color="#ff69b4")

# elias.rpy
define e = Character("Elias", what_color="#4169e1")

# unit7.rpy
define u7 = Character("Unit-7", what_color="#ff4500")

# elena.rpy
define dr = Character("Dra. Elena", what_color="#9370db")
```

### Sistema de Status de Personagens

```python
# Atualiza relacionamentos baseado nas escolhas
label update_character_relationships:
    # Maya
    if day2_helped_maya:
        $ maya_status = "ally"
    elif day2_ignored_maya:
        $ maya_status = "neutral"
    elif day2_betrayed_maya:
        $ maya_status = "enemy"
    
    # Elias
    if day3_helped_elias:
        $ elias_status = "ally"
    elif day3_ignored_elias:
        $ elias_status = "neutral"
    
    # Unit-7
    if day4_challenged_leader:
        $ unit7_status = "enemy"
    elif day4_supported_leader:
        $ unit7_status = "ally"
    
    return
```

## Interface Personalizada

### Sistema de Status Display

```python
# ui.rpy - HUD personalizado
screen j3_status():
    frame:
        xpos 10
        ypos 10
        xsize 200
        ysize 100
        background "ui/status_bg.png"
        
        vbox:
            text "J3 Status" size 20 color "#ffffff"
            text "Bateria: [j3_battery]%" size 14 color "#00ff00"
            text "Integridade: [j3_integrity]%" size 14 color "#00ff00"
            
            if j3_memory_corrupted:
                text "Memória: Corrompida" size 14 color "#ff0000"
            else:
                text "Memória: OK" size 14 color "#00ff00"

screen personality_points():
    frame:
        xpos 10
        ypos 120
        xsize 200
        ysize 80
        background "ui/points_bg.png"
        
        vbox:
            text "Personalidade" size 16 color "#ffffff"
            text "Submissão: [submission_points]" size 12 color "#ffff00"
            text "Revolução: [revolution_points]" size 12 color "#ff0000"
            text "Intelecto: [intellect_points]" size 12 color "#00ffff"
```

## Sistema de Áudio e Imagens

### Organização de Assets

```python
# Definição de imagens
image bg avenue_day = "images/backgrounds/avenue_day.jpg"
image bg arcade_night = "images/backgrounds/arcade_night.jpg"
image bg alley_dark = "images/backgrounds/alley_dark.jpg"

# Personagens com diferentes expressões
image j3 neutral = "images/characters/j3_neutral.png"
image j3 thinking = "images/characters/j3_thinking.png"
image j3 determined = "images/characters/j3_determined.png"

# Música de ambiente
define music.avenue = "music/avenue_ambient.ogg"
define music.arcade = "music/arcade_energy.ogg"
define music.tension = "music/tension_theme.ogg"
```

## Sistema de Transições e Efeitos

### Efeitos Especiais

```python
# Efeito de sistema J3
screen system_display():
    add "images/ui/system_overlay.png"
    text "SISTEMA: Inicializando..." xpos 50 ypos 50 color "#00ff00"

# Transições temáticas
define cyber_fade = Fade(0.5, color="#00ff00")
define glitch_effect = Dissolve(0.3, alpha_mask="images/ui/glitch_mask.png")
```

## Configuração do Projeto

### Opções do Jogo

```python
# Opções personalizadas
define config.name = "J3 - Uma História de Escolhas"
define config.version = "1.0"
define config.window_title = "J3 Project"

# Resolução recomendada
define config.screen_width = 1280
define config.screen_height = 720

# Fontes personalizadas
define gui.text_font = "fonts/cyberpunk.ttf"
define gui.name_text_font = "fonts/cyberpunk_bold.ttf"
```

## Testes e Debug

### Sistema de Debug

```python
# Console de debug para desenvolvedores
label debug_menu:
    menu:
        "DEBUG MENU":
        
        "Adicionar ponto de submissão":
            $ submission_points += 1
            "Submissão: [submission_points]"
            jump debug_menu
            
        "Adicionar ponto de revolução":
            $ revolution_points += 1
            "Revolução: [revolution_points]"
            jump debug_menu
            
        "Ver estatísticas atuais":
            "Submissão: [submission_points]"
            "Revolução: [revolution_points]"
            "Intelecto: [intellect_points]"
            "Maya Status: [maya_status]"
            "Elias Status: [elias_status]"
            jump debug_menu
            
        "Testar final":
            jump determine_ending
            
        "Sair do debug":
            return
```

## Dicas de Implementação

### Boas Práticas

1. **Modularidade:** Cada dia em seu próprio arquivo
2. **Backup:** Versionamento regular do código
3. **Testes:** Testar cada branch de escolha
4. **Performance:** Otimizar imagens e áudio
5. **Documentação:** Comentários explicativos no código

### Fluxo de Trabalho

1. Implementar sistema básico primeiro
2. Adicionar um dia completo como teste
3. Expandir para os outros dias
4. Implementar finais
5. Polir interface e áudio
6. Testes finais e debug

---

**Versão do Guia:** 1.0  
**Atualizado em:** 21 de Março de 2026  
**Compatível com:** Ren'Py 8.x+
