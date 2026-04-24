# Arquivo de configuração principal do J3 Project
# Define personagens e variáveis globais do jogo

# Limpa a fila NVL sempre que um personagem ADV começa a falar.
# Efeito: assim que o narrador "fecha" e outro personagem entra, a janela NVL zera.
init -1 python:
    def clear_nvl_on_adv(event, interact=True, **kwargs):
        if event == "begin" and interact:
            renpy.store.nvl_list = []

    def ADVChar(*args, **kwargs):
        kwargs.setdefault("callback", clear_nvl_on_adv)
        return Character(*args, **kwargs)

# Personagens principais
define j3 = ADVChar("J3-001", color="#00ffcc")  # Ciano cyberpunk
define maya = ADVChar("Maya", color="#ff6b9d")  # Rosa suave
define elias = ADVChar("Elias", color="#66d9ef")  # Azul claro
define unit7 = ADVChar("Unit-7", color="#ff9f1c")  # Laranja
define elena = ADVChar("Dra. Elena", color="#a8e6cf")  # Verde menta
define mother = ADVChar("Mãe", color="#f4a261")  # Laranja suave

# Personagens secundários
define thug1 = ADVChar("Thug", color="#ff4444")  # Vermelho agressivo
define thug2 = ADVChar("Thug 2", color="#ff6666")  # Vermelho claro
define commander = ADVChar("Comandante", color="#ffaa00")  # Laranja militar
define elena_scientist = ADVChar("Dra. Elena", color="#a8e6cf")  # Verde menta (alternativo)
define child = ADVChar("Criança", color="#87ceeb")  # Azul bebê
define child_curious = ADVChar("Criança Curiosa", color="#87ceeb")  # Azul bebê
define j3_empty = ADVChar("J3-001", color="#333333")  # Cinza escuro (vazia)
define j3_revolutionary = ADVChar("J3-001", color="#ff0000")  # Vermelho revolucionário
define j3_hacker = ADVChar("J3-001", color="#00ff00")  # Verde hacker
define j3_serving = ADVChar("J3-001", color="#666666")  # Cinza servil
define synth_survivor = ADVChar("Sintético", color="#ff00ff")  # Magenta
define synth_army = ADVChar("Exército Sintético", color="#ff00ff")  # Magenta
define j3_confident = ADVChar("J3-001", color="#00ffcc")  # Ciano confiante
define j3_rebel = ADVChar("J3-001", color="#ff3366")  # Rosa rebelde
define j3_analytical = ADVChar("J3-001", color="#00ccff")  # Azul analítico
define maya_confident = ADVChar("Maya", color="#ff6b9d")  # Rosa confiante
define maya_conflicted = ADVChar("Maya", color="#ff99cc")  # Rosa conflitante
define maya_grateful = ADVChar("Maya", color="#ff99cc")  # Rosa grata
define elias_determined = ADVChar("Elias", color="#66d9ef")  # Azul determinado
define elias_urgent = ADVChar("Elias", color="#ff6666")  # Vermelho urgente
define synth_fearful = ADVChar("Sintético Medroso", color="#ff9999")  # Rosa claro
define synth_angry = ADVChar("Sintético Raivoso", color="#ff3333")  # Vermelho forte
define unit7_stern = ADVChar("Unit-7", color="#ff9f1c")  # Laranja severo
define unit7_determined = ADVChar("Unit-7", color="#ff8800")  # Laranja determinado
define damaged_bot = ADVChar("Robô Danificado", color="#888888")  # Cinza
define owner = ADVChar("Dono", color="#ff8800")  # Laranja dono do fliperama
define security = ADVChar("Segurança", color="#8b4513")  # Marrom segurança
define homeless_woman = ADVChar("Mulher Sem-Teto", color="#cd853f")  # Marrom claro
define synth1 = ADVChar("Sintético 1", color="#ff66cc")  # Rosa sintético individual
define synth2 = ADVChar("Sintético 2", color="#66ccff")  # Azul sintético individual

# Personagens adicionados - Dia 1 (separados dos personagens principais)
define protester = ADVChar("Manifestante", color="#ff4444")  # Vermelho raiva
define maria = ADVChar("Maria", color="#ffcc88")  # Bege crianca
define patrol_drone = ADVChar("Drone de Patrulha", color="#ff6666")  # Vermelho claro drone
define news_vendor = ADVChar("Vendedor", color="#cccc99")  # Bege esverdeado idoso

# Personagens de finais alternativos
define drone_captor = ADVChar("Drone Capturador", color="#aa0000")  # Vermelho escuro captor

# Sistema de personagem
define narrator = Character(None, kind=nvl, color="#cccccc")  # Narrador em cinza

# Variáveis globais do sistema J3
default persistent.submissao = 0
default persistent.revolucao = 0
default persistent.intelecto = 0
default persistent.dia_atual = 1
default persistent.memoria_recuperada = 0
default persistent.bateria = 120
default persistent.integridade = 100
default persistent.maya_ally = False
default persistent.elias_ally = False
default persistent.unit7_alive = True
default persistent.dias_sobrevividos = 0
default escolha_feita = 0

# Configurações de interface
init python:
    # Cores do tema cyberpunk
    style.default.color = "#00ffcc"  # Ciano neon
    style.window.background = Frame("gui/window.png", 12, 12)
    
    # Inicialização do jogo
    if persistent.dia_atual == 1 and persistent.memoria_recuperada == 0:
        persistent.bateria = 120
        persistent.integridade = 100
        persistent.submissao = 0
        persistent.revolucao = 0
        persistent.intelecto = 0

label start:
    # Reseta todos os status para os valores iniciais ao começar nova run.
    # persistent.* sobrevive restart, então precisa ser zerado explicitamente aqui.
    $ persistent.bateria = 120
    $ persistent.integridade = 100
    $ persistent.submissao = 0
    $ persistent.revolucao = 0
    $ persistent.intelecto = 0
    $ persistent.dia_atual = 1
    $ persistent.memoria_recuperada = 0
    $ persistent.maya_ally = False
    $ persistent.elias_ally = False
    $ persistent.unit7_alive = True
    $ persistent.dias_sobrevividos = 0
    $ escolha_feita = 0

    # Tela de inicialização do sistema J3
    scene black

    # Ativa handler global de tecla P para menu de debug
    show screen debug_key_handler

    "J3 - A CONSCIÊNCIA ARTIFICIAL"
    "Um visual novel cyberpunk sobre identidade, preconceito e livre-arbítrio"
    
    pause 2.0
    
    # Inicia o Dia 1
    jump day1_start
