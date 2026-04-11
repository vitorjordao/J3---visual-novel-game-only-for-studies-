# Arquivo de configuração principal do J3 Project
# Define personagens e variáveis globais do jogo

# Personagens principais
define j3 = Character("J3-001", color="#00ffcc")  # Ciano cyberpunk
define maya = Character("Maya", color="#ff6b9d")  # Rosa suave
define elias = Character("Elias", color="#66d9ef")  # Azul claro
define unit7 = Character("Unit-7", color="#ff9f1c")  # Laranja
define elena = Character("Dra. Elena", color="#a8e6cf")  # Verde menta
define mother = Character("Mãe", color="#f4a261")  # Laranja suave

# Personagens secundários
define thug1 = Character("Thug", color="#ff4444")  # Vermelho agressivo
define thug2 = Character("Thug 2", color="#ff6666")  # Vermelho claro
define commander = Character("Comandante", color="#ffaa00")  # Laranja militar
define elena_scientist = Character("Dra. Elena", color="#a8e6cf")  # Verde menta (alternativo)
define child = Character("Criança", color="#87ceeb")  # Azul bebê
define child_curious = Character("Criança Curiosa", color="#87ceeb")  # Azul bebê
define j3_empty = Character("J3-001", color="#333333")  # Cinza escuro (vazia)
define j3_revolutionary = Character("J3-001", color="#ff0000")  # Vermelho revolucionário
define j3_hacker = Character("J3-001", color="#00ff00")  # Verde hacker
define j3_serving = Character("J3-001", color="#666666")  # Cinza servil
define synth_survivor = Character("Sintético", color="#ff00ff")  # Magenta
define synth_army = Character("Exército Sintético", color="#ff00ff")  # Magenta
define j3_confident = Character("J3-001", color="#00ffcc")  # Ciano confiante
define j3_rebel = Character("J3-001", color="#ff3366")  # Rosa rebelde
define j3_analytical = Character("J3-001", color="#00ccff")  # Azul analítico
define maya_confident = Character("Maya", color="#ff6b9d")  # Rosa confiante
define maya_conflicted = Character("Maya", color="#ff99cc")  # Rosa conflitante
define maya_grateful = Character("Maya", color="#ff99cc")  # Rosa grata
define elias_determined = Character("Elias", color="#66d9ef")  # Azul determinado
define elias_urgent = Character("Elias", color="#ff6666")  # Vermelho urgente
define synth_fearful = Character("Sintético Medroso", color="#ff9999")  # Rosa claro
define synth_angry = Character("Sintético Raivoso", color="#ff3333")  # Vermelho forte
define unit7_stern = Character("Unit-7", color="#ff9f1c")  # Laranja severo
define unit7_determined = Character("Unit-7", color="#ff8800")  # Laranja determinado
define damaged_bot = Character("Robô Danificado", color="#888888")  # Cinza
define owner = Character("Dono", color="#ff8800")  # Laranja dono do fliperama
define security = Character("Segurança", color="#8b4513")  # Marrom segurança
define homeless_woman = Character("Mulher Sem-Teto", color="#cd853f")  # Marrom claro
define synth1 = Character("Sintético 1", color="#ff66cc")  # Rosa sintético individual
define synth2 = Character("Sintético 2", color="#66ccff")  # Azul sintético individual

# Sistema de personagem
define narrator = Character(None, kind=nvl, color="#cccccc")  # Narrador em cinza

# Variáveis globais do sistema J3
default persistent.submissao = 0
default persistent.revolucao = 0
default persistent.intelecto = 0
default persistent.dia_atual = 1
default persistent.memoria_recuperada = 0
default persistent.bateria = 87
default persistent.integridade = 100
default escolha_feita = 0

# Configurações de interface
init python:
    # Cores do tema cyberpunk
    style.default.color = "#00ffcc"  # Ciano neon
    style.window.background = Frame("gui/window.png", 12, 12)
    
    # Inicialização do jogo
    if persistent.dia_atual == 1 and persistent.memoria_recuperada == 0:
        persistent.bateria = 87
        persistent.integridade = 100
        persistent.submissao = 0
        persistent.revolucao = 0
        persistent.intelecto = 0

label start:
    # Tela de inicialização do sistema J3
    scene black
    
    "J3 - A CONSCIÊNCIA ARTIFICIAL"
    "Um visual novel cyberpunk sobre identidade, preconceito e livre-arbítrio"
    
    pause 2.0
    
    # Inicia o Dia 1
    jump day1_start
