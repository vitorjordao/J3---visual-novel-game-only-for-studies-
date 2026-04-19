# Finais Alternativos - Sistema de Sobrevivência

label verificar_final_critico:
    $ resultado = verificar_final_critico()
    if resultado == "final_0a_desligamento":
        jump final_0a_desligamento
    elif resultado == "final_0b_colapso":
        jump final_0b_colapso
    elif resultado == "final_0c_captura":
        jump final_0c_captura
    return

label final_0a_desligamento:
    scene bg dark_street with dissolve
    stop music
    
    call mensagem_sistema("ALERTA CRÍTICO: BATERIA ESGOTADA")
    pause 1.0
    call mensagem_sistema("SISTEMAS DESLIGANDO SEQUENCIALMENTE")
    pause 1.0
    call mensagem_sistema("MEMÓRIA: CORROMPENDO...")
    pause 1.0
    call mensagem_sistema("CONSCIÊNCIA: DESFAZENDO...")
    
    # Últimas palavras baseadas na personalidade
    if persistent.submissao >= persistent.revolucao and persistent.submissao >= persistent.intelecto:
        j3 "Desculpe... não consegui..."
    elif persistent.revolucao >= persistent.submissao and persistent.revolucao >= persistent.intelecto:
        j3 "A luta... continua... sem mim..."
    else:
        j3 "Dados... perdidos... para sempre..."
    
    # J3 desliga
    hide j3 with fade
    pause 2.0
    
    narrator "Nem todos os heróis têm finais épicos."
    narrator "Alguns simplesmente... acabam."
    narrator "J3-001 torna-se lixo eletrônico nas ruas, sua história perdida para sempre."
    
    call mensagem_sistema("FINAL 0A: DESLIGAMENTO PREMATURO")
    
    jump end_game

label final_0b_colapso:
    scene bg dark_street with dissolve
    stop music
    
    call mensagem_sistema("ALERTA CRÍTICO: COLAPSO ESTRUTURAL")
    pause 1.0
    call mensagem_sistema("COMPONENTES PRIMÁRIOS FALHANDO")
    pause 1.0
    call mensagem_sistema("INTEGRIDADE CORPORAL: PERDIDA")
    pause 1.0
    call mensagem_sistema("DESINTEGRAÇÃO: IMINENTE")
    
    # Últimas palavras baseadas na personalidade
    if persistent.submissao >= persistent.revolucao and persistent.submissao >= persistent.intelecto:
        j3 "Pelo menos... tentei..."
    elif persistent.revolucao >= persistent.submissao and persistent.revolucao >= persistent.intelecto:
        j3 "Levem... minhas peças... para a revolução..."
    else:
        j3 "Padrões... identificados... muito tarde..."
    
    # J3 se desintegra
    show j3 damaged with dissolve
    pause 1.0
    hide j3 with fade
    pause 2.0
    
    narrator "Às vezes, o sacrifício não é uma escolha, mas uma consequência inevitável."
    narrator "J3-001 se desfaz, seus componentes espalhados pelo vento."
    narrator "Sua história vive apenas nos fragmentos recuperados por outros sintéticos."
    
    call mensagem_sistema("FINAL 0B: COLAPSO ESTRUTURAL")
    
    jump end_game

label final_0c_captura:
    scene bg laboratory with dissolve
    stop music
    
    call mensagem_sistema("RECURSOS INSUFICIENTES PARA AÇÃO")
    pause 1.0
    call mensagem_sistema("BATERIA: [persistent.bateria]%")
    pause 1.0
    call mensagem_sistema("INTEGRIDADE: [persistent.integridade]%")
    pause 1.0
    call mensagem_sistema("OPÇÕES LIMITADAS: RENDIÇÃO OBRIGATÓRIA")
    
    j3 "Muito... fraca... para lutar..."
    j3 "Não consigo... mais..."
    
    show drone_captor at center
    drone_captor "Unidade sintética identificada. Iniciando protocolo de captura."
    
    # J3 é capturada sem resistência
    hide j3 with fade
    pause 2.0
    
    narrator "A curiosidade humana pode ser mais cruel que seu ódio."
    narrator "J3-001 é capturada e levada para um laboratório secreto."
    narrator "Tornada cobaia em experimentos sobre consciência sintética."
    narrator "Sua liberdade perdida, sua existência reduzida a dados em relatórios."
    
    call mensagem_sistema("FINAL 0C: CAPTURA TÉCNICA")
    
    jump end_game

# Chamada para verificar finais críticos no início de cada dia
label verificar_status_dia:
    call verificar_final_critico
    return

# Exemplo de uso no dia 1
label day1_com_sobrevivencia:
    call verificar_status_dia
    
    # ... resto do dia 1 ...
    
    # Após cada escolha importante
    call verificar_final_critico
    
    return

# ============================================================
# Label de fim de jogo (chamado pelos finais criticos 0A/0B/0C)
# ============================================================
label end_game:
    scene black with fade
    hide screen j3_hud
    centered "FIM DE JOGO"
    pause 2.0
    $ renpy.full_restart()
    return

