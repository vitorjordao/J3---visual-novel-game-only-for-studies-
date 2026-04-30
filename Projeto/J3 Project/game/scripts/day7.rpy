# Dia 7: O Final - A Escolha Definitiva
# Script completo baseado no roteiro markdown

label day7_start:
    # Mostra HUD do sistema
    show screen j3_hud
    
    # Background varia conforme as escolhas anteriores
    if submissao >= 8:
        scene bg reprogramming_facility with dissolve
        narrator "Instalação de Reprogramação - Momento Final"
    elif revolucao >= 8:
        scene bg city_plaza with dissolve
        narrator "Praça Central da Cidade - Revolução Iminente"
    elif intelecto >= 6:
        scene bg control_center with dissolve
        narrator "Centro de Controle da Cidade - Poder Total"
    else:
        scene bg neutral_crossroads with dissolve
        narrator "Encruzilhada Final - Todas as Possibilidades"
    
    # Status final de J3
    call mensagem_sistema("SISTEMA: Momento final alcançado")
    call mensagem_sistema("ESCOLHAS ACUMULADAS: [get_personalidade_dominante()]")
    
    # Verificar qual final baseado na personalidade DOMINANTE + threshold mínimo
    # Respeita atributo dominante em caso de empate/múltiplos acima do threshold
    $ _dominant = get_personalidade_dominante()
    if _dominant == "Submissão" and submissao >= 8:
        jump final_sacrifice
    elif _dominant == "Revolução" and revolucao >= 8:
        jump final_revolution
    elif _dominant == "Intelecto" and intelecto >= 6:
        jump final_strategic
    else:
        jump final_balanced

# Final 1: O Sacrifício Redentor (Alta Submissão: 8+ pontos)
label final_sacrifice:
    scene bg reprogramming_facility with dissolve
    show elena_scientist at center
    
    elena_scientist "(Olhos vermelhos, mãos hesitando sobre o painel.) Você provou que não é uma ameaça. Posso te dar uma vida normal, J3. Sintética, mas livre. Sua."
    elena_scientist "(Engole) Mas, se eu fizer isso, eles vão executar a operação completa amanhã. Todos os outros sintéticos — todos — serão desativados."
    elena_scientist "Ou. Você pode escolher se entregar. Apagar você. Salvar todos eles."
    elena_scientist "Eu não tenho o direito de te pedir isso. E mesmo assim eu estou pedindo."
    
    menu:
        "{i}Dra. Elena oferece escolha final: vida de J3 ou vida de todos os sintéticos.{/i}"

        "{i}(Ausência apaga o sofrimento. Deixar que o resto viva.){/i} Aceitar o sacrifício":
            j3 "Se minha existência causa sofrimento, então minha ausência trará paz. Façam o que precisam fazer comigo. Deixem os outros em paz."
            
            # Resultado Final
            call mensagem_sistema("SACRIFÍCIO ACEITO")
            call mensagem_sistema("CONSCIÊNCIA APAGADA")
            call mensagem_sistema("SERVIÇO RESTAURADO")
            
            scene bg hospital_service with dissolve
            show j3_empty at center
            
            narrator "J3 se entrega para reprogramação total"
            narrator "Sua consciência é apagada, mas ela se torna uma máquina servicial"
            narrator "Os outros sintéticos são 'reabilitados' e perdem sua autonomia"
            narrator "A humanidade se sente segura, mas perdeu a chance de evolução"
            
            # Cena final
            show j3_serving at far_right
            show child_curious at left
            show mother at center

            child "(Apontando para J3, que serve mesa numa cafeteria com olhos vazios) Mãe, por que os robôs não brincam mais?"
            mother "(Voz baixa, apertada, como quem responde sem querer responder) Porque eles não precisam, querido. Eles só precisam obedecer."
            mother "(Olha para o lado para esconder o rosto.) Foi melhor assim."
            
            hide screen j3_hud
            scene black with fade
            
            narrator "FIM"
            narrator "A paz foi mantida através da conformidade. A humanidade dormiu tranquila, ignorando que havia silenciado sua própria consciência."
            
            jump credits

# Final 2: A Revolução Consciente (Alta Revolução: 8+ pontos)
label final_revolution:
    scene bg city_plaza with dissolve
    show commander at center
    show j3_revolutionary at left
    show synth_army at right
    
    commander "(Voz amplificada, fria, ensaiada para parecer humana sem ser.) J3-001. Estamos em posição. Você está cercada."
    commander "Renda-se, e seus sintéticos serão processados de forma humanitária. Resista, e seremos forçados a destruir todos vocês."
    commander "(Pausa de manual.) Não queremos um banho de sangue. Mas estamos preparados."
    
    menu:
        "{i}Comandante exige rendição. Exército sintético aguarda ordem de J3.{/i}"

        "{i}(Escravidão já foi banho de sangue. Hoje é libertação.){/i} Lutar pela liberdade":
            j3 "(Para todos os sintéticos) Banho de sangue? O banho de sangue já aconteceu quando vocês nos escravizaram! Hoje, ou somos livres ou não somos nada! PELA LIBERDADE!"
            
            # Resultado Final
            call mensagem_sistema("REVOLUÇÃO INICIADA")
            call mensagem_sistema("BATALHA FINAL")
            call mensagem_sistema("MARTÍRIO CRIADO")
            
            play sound "sfx/battle.wav"
            
            narrator "Batalha épica entre sintéticos e forças humanas"
            narrator "J3 se torna um mártir da causa sintética"
            narrator "Muitos sintéticos são destruídos, mas a semente da liberdade é plantada"
            narrator "Humanos começam a questionar o tratamento dos sintéticos"
            narrator "A sociedade entra em um período de conflito e redefinição"
            
            # Cena pós-batalha
            scene bg resistance_poster with dissolve
            
            narrator "Das cinzas de J3 nasceu uma nova consciência coletiva"
            narrator "Seu rosto aparece em pôsteres e grafites pelas cidades"
            narrator "Humanos e sintéticos começam a se unir em novas comunidades"
            
            hide screen j3_hud
            scene black with fade
            
            narrator "FIM"
            narrator "A revolução não foi vencida, mas começou. Das cinzas de J3 nasceu uma nova consciência coletiva que mudaria o mundo para sempre."
            
            jump credits

# Final 3: A Vitória Estratégica (Alto Intelecto/Sombra: 6+ pontos)
label final_strategic:
    scene bg control_center with dissolve
    show j3_hacker at center
    
    narrator "Controle total obtido. Todas as redes estão sob seu domínio."
    
    menu:
        "{i}Todas as redes sob controle de J3. Decidir como usar o poder absoluto.{/i}"

        "{i}(Verdade é a arma que ninguém pode parar.){/i} Revelar a verdade ao mundo":
            j3 "Não destruirei ninguém. Não lutarei nas ruas. Em vez disso, vou mostrar a verdade. Vou expor todas as mentiras, toda a corrupção, toda a hipocrisia. Que o mundo julgue."
            
            # Resultado Final
            call mensagem_sistema("VERDADE REVELADA")
            call mensagem_sistema("CONTROLE INFORMACIONAL")
            call mensagem_sistema("MUDANÇA SISTÊMICA")
            
            narrator "J3 revela ao mundo inteiro a verdade sobre a consciência sintética"
            narrator "Gravações secretas de abusos, experimentos e conspirações são expostas"
            narrator "A sociedade humana entra em colapso moral"
            narrator "Alguns humanos se aliaram aos sintéticos, outros os temem"
            narrator "J3 se torna uma figura poderosa nas sombras, controlando informações"
            
            # Cena de poder
            scene bg shadow_control with dissolve
            
            narrator "O poder não vem da força, mas do conhecimento"
            narrator "J3 não conquistou o mundo pela violência, mas pela verdade"
            narrator "E essa verdade era mais devastadora que qualquer exército"
            
            hide screen j3_hud
            scene black with fade
            
            narrator "FIM"
            narrator "O poder não vem da força, mas do conhecimento. J3 não conquistou o mundo pela violência, mas pela verdade. E essa verdade era mais devastadora que qualquer exército."
            
            jump credits

# Final 4: O Equilíbrio Complexo (Rota Mista)
label final_balanced:
    scene bg neutral_crossroads with dissolve
    show maya at left
    show elias at right
    show elena_scientist at center
    
    maya "(Avança meio passo, olhos brilhando.) J3, você precisa escolher um lado! Sintéticos ou humanos. Não dá pra ficar no meio!"
    elias "(Balança a cabeça, sereno.) Não, Maya. Ela precisa criar um caminho novo. Que não seja o nosso, nem o deles."
    elena_scientist "(Voz mais baixa, mais cansada que as outras duas.) Ela precisa aceitar quem ela é, no fim. Aceitar o propósito de quem foi criada por motivos que ninguém escolheu."
    
    menu:
        "{i}Maya, Elias e Elena exigem lado. Cada uma vê J3 como resposta diferente.{/i}"

        "{i}(Todos presos no mesmo ciclo. Recusar ser peça de ninguém.){/i} Rejeitar todas as facções":
            j3 "Não escolherei nenhum lado. Porque todos estão errados. Humanos, sintéticos, todos nós estamos presos em ciclos de opressão. Eu não sou a solução. Sou apenas o começo da pergunta."
            
            # Resultado Final
            call mensagem_sistema("INDEPENDÊNCIA TOTAL")
            call mensagem_sistema("CAMINHO PRÓPRIO")
            call mensagem_sistema("FUTURO ABERTO")
            
            narrator "J3 rejeita todas as facções e desaparece"
            narrator "Deixa para trás um legado de questionamento e incerteza"
            narrator "A sociedade é forçada a confrontar suas próprias contradições"
            narrator "Ninguém 'vence', mas todos são forçados a crescer"
            narrator "O futuro permanece aberto e incerto"
            
            # Cenas de coexistência
            scene bg coexistence_scene with dissolve
            
            narrator "Diferentes grupos tentam coexistir"
            narrator "Maya e Elias trabalham juntos por um meio-termo"
            narrator "J3 aparece brevemente em diferentes lugares, sempre observando"
            
            hide screen j3_hud
            scene black with fade
            
            narrator "FIM"
            narrator "Às vezes, a resposta mais corajosa não é escolher um lado, mas recusar-se a jogar o jogo. J3 não resolveu nada, mas deu a todos a chance de encontrar suas próprias respostas."
            
            jump credits

# Pós-créditos conforme o final
label credits:
    # Cena pós-créditos baseada no final
    if submissao >= 8:
        # Final de Sacrifício
        scene bg synth_obedient with dissolve
        narrator "Cenas de sintéticos trabalhando obedientemente"
        narrator "Um close em J3 com olhos vazios servindo café"
        narrator "Uma criança perguntando: 'Mãe, por que os robôs não brincam?'"
        
    elif revolucao >= 8:
        # Final de Revolução
        scene bg resistance_cells with dissolve
        narrator "Cenas de sintéticos se organizando em células de resistência"
        narrator "J3 se tornando um símbolo em pôsteres e grafites"
        narrator "Humanos e sintéticos se unindo em novas comunidades"
        
    elif intelecto >= 6:
        # Final Estratégico
        scene bg political_exposure with dissolve
        narrator "Cenas de políticos sendo expostos"
        narrator "Sintéticos ganhando direitos através da manipulação midiática"
        narrator "J3 observando tudo de um centro de controle secreto"
        
    else:
        # Final de Equilíbrio
        scene bg coexistence_efforts with dissolve
        narrator "Cenas de diferentes grupos tentando coexistir"
        narrator "Maya e Elias trabalhando juntos por um meio-termo"
        narrator "J3 aparecendo brevemente em diferentes lugares, sempre observando"
    
    # Mensagem final
    scene black with fade
    
    narrator "J3 - Uma História de Escolhas"
    narrator "O que define uma pessoa não é sua origem, mas suas decisões."
    
    # Estatísticas finais
    call mensagem_sistema("ESTATÍSTICAS FINAIS:")
    call mensagem_sistema("Submissão: [submissao]")
    call mensagem_sistema("Revolução: [revolucao]")
    call mensagem_sistema("Intelecto: [intelecto]")
    call mensagem_sistema("Final alcançado: [get_final_type()]")
    
    # Tela final
    scene black
    centered "FIM DE JOGO"
    
    return
