# Sistema J3 - Versão com mecânicas de sobrevivência

init python:
    def modificar_personalidade(atributo, valor):
        if atributo == "submissao":
            persistent.submissao = max(0, min(10, persistent.submissao + valor))
        elif atributo == "revolucao":
            persistent.revolucao = max(0, min(10, persistent.revolucao + valor))
        elif atributo == "intelecto":
            persistent.intelecto = max(0, min(10, persistent.intelecto + valor))
    
    def consumir_bateria(valor):
        persistent.bateria = max(0, persistent.bateria - valor)
        if persistent.bateria <= 0:
            return "critical_battery"
        elif persistent.bateria <= 10:
            return "warning_battery"
        elif persistent.bateria <= 20:
            return "low_battery"
        return "normal"
    
    def consumir_integridade(valor):
        persistent.integridade = max(0, persistent.integridade - valor)
        if persistent.integridade <= 0:
            return "critical_integrity"
        elif persistent.integridade <= 20:
            return "warning_integrity"
        elif persistent.integridade <= 30:
            return "low_integrity"
        return "normal"
    
    def recarregar_bateria(valor):
        persistent.bateria = min(100, persistent.bateria + valor)
    
    def reparar_integridade(valor):
        persistent.integridade = min(100, persistent.integridade + valor)
    
    def verificar_final_critico():
        if persistent.bateria <= 0:
            return "final_0a_desligamento"
        elif persistent.integridade <= 0:
            return "final_0b_colapso"
        elif persistent.bateria <= 10 and persistent.integridade <= 20:
            return "final_0c_captura"
        return None
    
    def get_status_bateria():
        if persistent.bateria <= 10:
            return "CRITICA"
        elif persistent.bateria <= 20:
            return "BAIXA"
        elif persistent.bateria <= 50:
            return "MODERADA"
        else:
            return "BOA"
    
    def get_status_integridade():
        if persistent.integridade <= 20:
            return "CRITICA"
        elif persistent.integridade <= 30:
            return "DANIFICADA"
        elif persistent.integridade <= 70:
            return "COMPROMETIDA"
        else:
            return "ESTAVEL"
    
    def atualizar_status():
        return consumir_bateria(1)
    
    def get_personalidade_dominante():
        atributos = {
            "Submissão": persistent.submissao,
            "Revolução": persistent.revolucao,
            "Intelecto": persistent.intelecto
        }
        return max(atributos, key=atributos.get)

screen j3_hud:
    zorder 100
    frame:
        xalign 0.02
        yalign 0.02
        xsize 320
        background "#1a1a2e99"
        vbox:
            spacing 5
            text "SISTEMA J3-001" color "#00ffcc" size 16
            
            frame:
                xsize 280
                background "#0a1a0a"
                vbox:
                    spacing 2
                    text "Bateria: [persistent.bateria]% ([get_status_bateria()])" color "#ff6b6b" size 12
                    bar value persistent.bateria range 100 xsize 260 ysize 8
            
            frame:
                xsize 280
                background "#0a1a0a"
                vbox:
                    spacing 2
                    text "Integridade: [persistent.integridade]% ([get_status_integridade()])" color "#ff6b6b" size 12
                    bar value persistent.integridade range 100 xsize 260 ysize 8
            
            if persistent.bateria <= 10 or persistent.integridade <= 20:
                text "ALERTA CRITICO" color "#ff0000" size 14

label mensagem_sistema(mensagem):
    show screen system_text(mensagem)
    pause 2.0
    hide screen system_text
    return

screen system_text(mensagem):
    zorder 90
    frame:
        xalign 0.5
        yalign 0.8
        xsize 600
        background "#000000cc"
        text mensagem color "#00ffcc" size 18 xalign 0.5

label escolha_j3(pergunta, opcoes):
    "Escolha uma opção:"
    
    menu:
        "Opção 1":
            $ modificar_personalidade(opcoes[0][1], opcoes[0][2])
            $ escolha_feita = 0
        "Opção 2":
            $ modificar_personalidade(opcoes[1][1], opcoes[1][2])
            $ escolha_feita = 1
        "Opção 3":
            $ modificar_personalidade(opcoes[2][1], opcoes[2][2])
            $ escolha_feita = 2
    
    call atualizar_status
    return escolha_feita

label atualizar_status:
    $ atualizar_status()
    return

transform system_boot:
    alpha 0.0
    zoom 0.8
    linear 0.5 alpha 1.0 zoom 1.0

screen debug_key_handler:
    key "d" action Function(toggle_debug_menu)

screen debug_menu:
    zorder 200
    modal True
    key "d" action HideScreen("debug_menu")
    frame:
        xalign 0.98
        yalign 0.02
        xsize 350
        background "#1a1a2ecc"
        vbox:
            spacing 5
            text "DEBUG MENU" color "#00ffcc" size 16 xalign 0.5
            
            frame:
                xsize 330
                background "#0a1a0a"
                vbox:
                    spacing 2
                    text "=== STATUS ===" color "#ffffff" size 12
                    text "Bateria: [persistent.bateria]%" color "#ff6b6b" size 11
                    text "Integridade: [persistent.integridade]%" color "#ff6b6b" size 11
            
            frame:
                xsize 330
                background "#0a1a0a"
                vbox:
                    spacing 2
                    text "=== PERSONALIDADE ===" color "#ffffff" size 12
                    text "Submissão: [persistent.submissao]/10" color "#666666" size 11
                    text "Revolução: [persistent.revolucao]/10" color "#666666" size 11
                    text "Intelecto: [persistent.intelecto]/10" color "#666666" size 11
                    text "Dominante: [get_personalidade_dominante()]" color "#00ffcc" size 11
            
            frame:
                xsize 330
                background "#0a1a0a"
                vbox:
                    spacing 2
                    text "=== ALIADOS ===" color "#ffffff" size 12
                    text "Maya: [persistent.maya_ally]" color "#666666" size 11
                    text "Elias: [persistent.elias_ally]" color "#666666" size 11
                    text "Unit-7 Vivo: [persistent.unit7_alive]" color "#666666" size 11
            
            frame:
                xsize 330
                background "#0a1a0a"
                vbox:
                    spacing 2
                    text "=== SOBREVIVÊNCIA ===" color "#ffffff" size 12
                    text "Dias Sobrevividos: [persistent.dias_sobrevividos]" color "#666666" size 11
                    text "Final Crítico: [verificar_final_critico()]" color "#ff6b6b" size 11
            
            textbutton "Fechar [D]" action HideScreen("debug_menu") xalign 0.5
