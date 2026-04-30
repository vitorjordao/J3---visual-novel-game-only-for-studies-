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
# Estado de gameplay vai para o store (default X) — assim o rollback restaura.
# persistent.* só para estatísticas que devem sobreviver entre runs.
default submissao = 0
default revolucao = 0
default intelecto = 0
default dia_atual = 1
default memoria_recuperada = 0
default bateria = 120
default integridade = 100
default maya_ally = False
default elias_ally = False
default unit7_alive = True
default elena_alive = True
default persistent.dias_sobrevividos = 0
default escolha_feita = 0

# Configurações de interface
init python:
    # Cores do tema cyberpunk
    style.default.color = "#00ffcc"  # Ciano neon
    style.window.background = Frame("gui/window.png", 12, 12)

label start:
    # Reset explícito ao iniciar nova run. Variáveis de store já têm default,
    # mas saves/restarts podem deixá-las em estado inesperado se algum dia o boot
    # cair direto aqui sem passar pelo default.
    $ bateria = 120
    $ integridade = 100
    $ submissao = 0
    $ revolucao = 0
    $ intelecto = 0
    $ dia_atual = 1
    $ memoria_recuperada = 0
    $ maya_ally = False
    $ elias_ally = False
    $ unit7_alive = True
    $ elena_alive = True
    $ persistent.dias_sobrevividos = 0
    $ escolha_feita = 0

    # Tela de inicialização do sistema J3
    scene black

    # Ativa handler global de tecla P para menu de debug
    show screen debug_key_handler

    # Tagline de impacto (ADV padrão, curta)
    "{size=+18}{color=#00ffcc}J3{/color}{/size}"
    "{i}A consciência artificial.{/i}"

    pause 1.5

    scene black with fade

    # Abertura atmosférica em NVL (tela cheia, imersiva)
    # O callback clear_nvl_on_adv limpa esta janela quando J3 falar no Dia 1.
    narrator "É noite no Setor Central."
    narrator "A chuva escorre pelos letreiros neon como se a cidade tivesse aprendido a sangrar em cores."
    narrator "No alto, um plenário vota. Lá embaixo, uma lei começa a ter dentes."
    narrator "Os jornais chamam de \"Limpeza Ética\". As ruas chamam pelo que é: o começo de um extermínio silencioso."

    pause 1.0

    narrator "E numa calçada qualquer, encharcada e sem nome, alguma coisa que jamais deveria despertar — desperta."
    narrator "Esta é a primeira noite dela."

    pause 2.0

    # Inicia o Dia 1
    jump day1_start
