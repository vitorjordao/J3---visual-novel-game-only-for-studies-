# Sistema J3 - Versão com mecânicas de sobrevivência

init python:
    # Estado de gameplay vive no store (default X em script.rpy) — assim sofre rollback.
    # Aqui dentro de init python: temos que qualificar com store.X para mutar o store
    # de verdade (caso contrário criaríamos variável local da função).
    def modificar_personalidade(atributo, valor):
        if atributo == "submissao":
            store.submissao = max(0, min(10, store.submissao + valor))
        elif atributo == "revolucao":
            store.revolucao = max(0, min(10, store.revolucao + valor))
        elif atributo == "intelecto":
            store.intelecto = max(0, min(10, store.intelecto + valor))

    def _disparar_final_critico():
        # Verifica recursos e pula para o final alternativo imediato.
        # Chamado toda vez que consumimos bateria/integridade.
        if store.bateria <= 0:
            renpy.jump("final_0a_desligamento")
        elif store.integridade <= 0:
            renpy.jump("final_0b_colapso")
        elif store.bateria <= 10 and store.integridade <= 20:
            renpy.jump("final_0c_captura")

    def consumir_bateria(valor):
        store.bateria = max(0, store.bateria - valor)
        _disparar_final_critico()
        if store.bateria <= 0:
            return "critical_battery"
        elif store.bateria <= 10:
            return "warning_battery"
        elif store.bateria <= 20:
            return "low_battery"
        return "normal"

    def consumir_integridade(valor):
        store.integridade = max(0, store.integridade - valor)
        _disparar_final_critico()
        if store.integridade <= 0:
            return "critical_integrity"
        elif store.integridade <= 20:
            return "warning_integrity"
        elif store.integridade <= 30:
            return "low_integrity"
        return "normal"

    def recarregar_bateria(valor):
        store.bateria = min(100, store.bateria + valor)

    def reparar_integridade(valor):
        store.integridade = min(100, store.integridade + valor)

    def verificar_final_critico():
        if store.bateria <= 0:
            return "final_0a_desligamento"
        elif store.integridade <= 0:
            return "final_0b_colapso"
        elif store.bateria <= 10 and store.integridade <= 20:
            return "final_0c_captura"
        return "Normal"

    def get_status_bateria():
        if store.bateria <= 10:
            return "CRÍTICA"
        elif store.bateria <= 20:
            return "BAIXA"
        elif store.bateria <= 50:
            return "MODERADA"
        else:
            return "BOA"

    def get_status_integridade():
        if store.integridade <= 20:
            return "CRÍTICA"
        elif store.integridade <= 30:
            return "DANIFICADA"
        elif store.integridade <= 70:
            return "COMPROMETIDA"
        else:
            return "ESTÁVEL"

    def atualizar_status():
        return consumir_bateria(1)

    def get_personalidade_dominante():
        atributos = {
            "Submissão": store.submissao,
            "Revolução": store.revolucao,
            "Intelecto": store.intelecto
        }
        return max(atributos, key=atributos.get)

init python:
    def _status_color(value, low_threshold, mid_threshold):
        if value <= low_threshold:
            return "#ff3344"
        elif value <= mid_threshold:
            return "#ffaa22"
        else:
            return "#22ff99"

screen j3_hud:
    zorder 100

    $ bat_color = _status_color(bateria, 20, 50)
    $ int_color = _status_color(integridade, 30, 70)
    $ bat_critical = bateria <= 10
    $ int_critical = integridade <= 20

    frame:
        xalign 0.02
        yalign 0.02
        xsize 380
        background "#0a0a1ef2"
        padding (14, 12)
        vbox:
            spacing 8

            hbox:
                spacing 6
                text "{b}SISTEMA J3-001{/b}" color "#00ffcc" size 20 font "gui/fonts/Orbitron-Variable.ttf"
                text "v2.3" color "#5577aa" size 11 yalign 1.0 font "gui/fonts/Rajdhani-Medium.ttf"

            # BATERIA
            frame:
                xsize 350
                background "#001122dd"
                padding (10, 6)
                vbox:
                    spacing 3
                    hbox:
                        spacing 6
                        text "[[BAT]" color "#00ffcc" size 14 bold True font "gui/fonts/Orbitron-Variable.ttf"
                        text "[bateria]%" color bat_color size 20 bold True font "gui/fonts/Orbitron-Variable.ttf"
                        text "[get_status_bateria()]" color bat_color size 12 yalign 1.0 font "gui/fonts/Rajdhani-Medium.ttf"
                    bar:
                        value bateria
                        range 100
                        xsize 330
                        ysize 14
                        left_bar Solid(bat_color)
                        right_bar Solid("#111")

            # INTEGRIDADE
            frame:
                xsize 350
                background "#001122dd"
                padding (10, 6)
                vbox:
                    spacing 3
                    hbox:
                        spacing 6
                        text "[[INT]" color "#00ffcc" size 14 bold True font "gui/fonts/Orbitron-Variable.ttf"
                        text "[integridade]%" color int_color size 20 bold True font "gui/fonts/Orbitron-Variable.ttf"
                        text "[get_status_integridade()]" color int_color size 12 yalign 1.0 font "gui/fonts/Rajdhani-Medium.ttf"
                    bar:
                        value integridade
                        range 100
                        xsize 330
                        ysize 14
                        left_bar Solid(int_color)
                        right_bar Solid("#111")

            if bat_critical or int_critical:
                frame:
                    xsize 350
                    background "#550000dd"
                    padding (8, 4)
                    text "!!! ALERTA CRÍTICO !!!" color "#ff5555" size 16 bold True xalign 0.5 font "gui/fonts/Orbitron-Variable.ttf" at hud_alert_pulse

transform hud_alert_pulse:
    alpha 1.0
    linear 0.4 alpha 0.3
    linear 0.4 alpha 1.0
    repeat

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

# Drones pairam no alto da tela para não ficarem escondidos pela caixa de diálogo.
transform drone_hover:
    xalign 0.5 yalign 0.22

transform drone_hover_loop:
    # patrol_drone.png tem dois drones desenhados no canvas (topo grande + base pequeno).
    # Sem o crop, o drone de baixo aparece exatamente atrás da caixa de diálogo.
    crop (0, 0, 800, 540)
    xalign 0.5 yalign 0.22
    linear 1.0 yalign 0.19
    linear 1.0 yalign 0.22
    repeat

screen debug_key_handler:
    key "p" action Function(toggle_debug_menu)

screen debug_menu:
    zorder 200
    modal True
    key "p" action Hide("debug_menu")
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
                    text "Bateria: [bateria]%" color "#ff6b6b" size 11
                    text "Integridade: [integridade]%" color "#ff6b6b" size 11
            
            frame:
                xsize 330
                background "#0a1a0a"
                vbox:
                    spacing 2
                    text "=== PERSONALIDADE ===" color "#ffffff" size 12
                    text "Submissão: [submissao]/10" color "#666666" size 11
                    text "Revolução: [revolucao]/10" color "#666666" size 11
                    text "Intelecto: [intelecto]/10" color "#666666" size 11
                    text "Dominante: [get_personalidade_dominante()]" color "#00ffcc" size 11
            
            frame:
                xsize 330
                background "#0a1a0a"
                vbox:
                    spacing 2
                    text "=== ALIADOS ===" color "#ffffff" size 12
                    text "Maya: [maya_ally]" color "#666666" size 11
                    text "Elias: [elias_ally]" color "#666666" size 11
                    text "Unit-7 Vivo: [unit7_alive]" color "#666666" size 11
            
            frame:
                xsize 330
                background "#0a1a0a"
                vbox:
                    spacing 2
                    text "=== SOBREVIVÊNCIA ===" color "#ffffff" size 12
                    text "Dias Sobrevividos: [persistent.dias_sobrevividos]" color "#666666" size 11
                    text "Final Crítico: [verificar_final_critico()]" color "#ff6b6b" size 11
            
            textbutton "Executar Testes" action Jump("run_comprehensive_tests") xalign 0.5
            textbutton "Fechar (P)" action Hide("debug_menu") xalign 0.5
