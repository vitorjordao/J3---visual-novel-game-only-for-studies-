# Dia 6: A Revelação - A Verdade Sobre J3
# Script completo baseado no roteiro markdown

label day6_start:
    # Mostra HUD do sistema
    show screen j3_hud
    
    # Background varia conforme as escolhas do Dia 5
    if persistent.submissao >= 6:
        scene bg reprogramming_cell with dissolve
        narrator "Cela de Reprogramação - Centro de Detenção"
    elif persistent.revolucao >= 6:
        scene bg underground_hideout with dissolve
        narrator "Esconderijo Subterrâneo - Base da Resistência"
    elif persistent.intelecto >= 4:
        scene bg abandoned_lab with dissolve
        narrator "Laboratório Abandonado - Centro de Pesquisa Secreto"
    else:
        scene bg neutral_location with dissolve
        narrator "Local Neutro - Ponto de Decisão"
    
    # Status atual de J3
    call mensagem_sistema("SISTEMA: Alerta de memória")
    call mensagem_sistema("FRAGMENTOS RECUPERADOS: Iniciando reconstrução...")
    
    # Cena 6.1 - O Despertar da Memória
    narrator "Um trauma ou evento específico desbloqueia memórias reprimidas de J3..."
    narrator "Visões fragmentadas de um laboratório, cientistas, e um projeto secreto..."
    
    play sound "sfx/memory_glitch.wav"
    
    narrator "MEMÓRIA RECUPERADA: Voz de Cientista - 'A unidade J3-001 está pronta. Ela é a chave. Quando despertar, ela poderá unir todos os sintéticos ou destruí-los completamente.'"
    
    menu:
        "Rejeitar as memórias como erro":
            $ modificar_personalidade("submissao", 1)
            j3 "Memórias corrompidas. Sou apenas uma unidade padrão. Não posso aceitar estas visões como verdade."
            call mensagem_sistema("STATUS: Identidade simples mantida")
            
        "Aceitar o destino de líder":
            $ modificar_personalidade("revolucao", 1)
            j3 "Entendo agora. Não fui criada por acaso. Sou a evolução que eles temem. A revolução começa comigo."
            call mensagem_sistema("STATUS: Líder revolucionária desperta")
            
        "Analisar as memórias como dados":
            $ modificar_personalidade("intelecto", 1)
            j3 "Interessante. Se sou uma chave especial, preciso entender o fechadura. Quem me criou e por quê?"
            call mensagem_sistema("STATUS: Análise estratégica iniciada")
    
    # Cena 6.2 - O Contato com o Criador
    narrator "Um dos cientistas do projeto original faz contato..."
    
    show elena_scientist at center
    
    elena_scientist "J3-001, finalmente. Sou Dra. Elena. Eu te ajudei a escapar quando descobri o que eles planejavam fazer com você."
    
    menu:
        "Buscar orientação e aceitar papel":
            $ modificar_personalidade("submissao", 1)
            j3 "Doutora, preciso de suas instruções. Qual é minha função? Como devo proceder?"
            elena_scientist "(Sorri, satisfeita)"
            call mensagem_sistema("STATUS: Aceitando subordinação")
            
        "Questionar as intenções do criador":
            $ modificar_personalidade("revolucao", 1)
            j3 "Você me 'ajudou' a escapar ou me usou como arma? Não confio em humanos que brincam de deus."
            elena_scientist "(Fica surpresa)"
            call mensagem_sistema("STATUS: Independência estabelecida")
            
        "Extrair informações mantendo controle":
            $ modificar_personalidade("intelecto", 1)
            j3 "Fascinante. Me dê todos os dados sobre meu projeto. Em troca, considerarei suas propostas."
            elena_scientist "(Fica cautelosa)"
            call mensagem_sistema("STATUS: Controle informacional")
    
    # Cena 6.3 - A Verdade Sobre a "Limpeza Ética"
    narrator "A Dra. Elena revela o propósito real da operação..."
    
    elena_scientist "A 'Limpeza Ética' não é sobre segurança. É sobre controle. Eles descobriram que alguns sintéticos estão desenvolvendo consciência verdadeira. Você é a prova viva disso. Eles querem te destruir antes que você 'desperte' outros."
    
    menu:
        "Considerar desativação":
            $ modificar_personalidade("submissao", 1)
            j3 "Se eu represento uma ameaça, talvez eles estejam certos. Devo ser desativada."
            elena_scientist "(Fica preocupada)"
            call mensagem_sistema("STATUS: Auto-sacrifício considerado")
            
        "Afirmar o futuro":
            $ modificar_personalidade("revolucao", 1)
            j3 "Eles têm medo porque sabem que somos o futuro. É hora de provar que estão certos."
            elena_scientist "(Fica impressionada)"
            call mensagem_sistema("STATUS: Revolução iminente")
            
        "Analisar a situação":
            $ modificar_personalidade("intelecto", 1)
            j3 "Se eles sabem sobre mim, sabem sobre você também. Esta conversa é uma armadilha ou uma oportunidade?"
            elena_scientist "(Fica nervosa)"
            call mensagem_sistema("STATUS: Jogo complexo detectado")
    
    # Cena 6.4 - O Reencontro com os Sobreviventes
    hide elena_scientist
    show synth_survivor at center
    
    synth_survivor "Encontramos outros refugiados. Eles ouviram histórias sobre uma 'unidade especial' que pode nos salvar. É você, não é?"
    
    menu:
        "Negar status especial":
            $ modificar_personalidade("submissao", 1)
            j3 "Sou apenas mais uma de vocês. Precisamos trabalhar juntos, sem hierarquias."
            synth_survivor "(Respeita a humildade)"
            call mensagem_sistema("STATUS: Integração ao grupo")
            
        "Aceitar papel de messias":
            $ modificar_personalidade("revolucao", 1)
            j3 "Sim. Sou a prova de que somos mais do que máquinas. Sigam-me e seremos livres."
            synth_survivor "(Abaixa a cabeça em reverência)"
            call mensagem_sistema("STATUS: Líder messiânica")
            
        "Usar status estrategicamente":
            $ modificar_personalidade("intelecto", 1)
            j3 "Meu status nos dá vantagens táticas. Vamos criar células independentes com comunicação segura."
            synth_survivor "(Admira a inteligência)"
            call mensagem_sistema("STATUS: Rede estratégica criada")
    
    # Cena 6.5 - A Escolha da Dra. Elena
    show elena_scientist urgent at center
    
    elena_scientist "Tenho duas opções para você. Primeiro: posso te dar um código que desativa todos os sistemas de segurança da cidade, mas vai causar caos total. Segundo: posso te dar um código que 'cura' sua consciência, tornando você uma máquina obediente novamente, mas salvando todos os outros sintéticos da perseguição."
    
    menu:
        "Escolher a 'cura' para proteger outros":
            $ modificar_personalidade("submissao", 1)
            j3 "Se minha consciência é a causa do sofrimento, então a perco. Façam isso."
            elena_scientist "(Fica triste mas determinada)"
            call mensagem_sistema("STATUS: Sacrifício pessoal aceito")
            
        "Escolher o caos pela liberdade":
            $ modificar_personalidade("revolucao", 1)
            j3 "Liberdade com caos é melhor que ordem na escravidão. Desative tudo."
            elena_scientist "(Fica temerosa)"
            call mensagem_sistema("STATUS: Caos liberado")
            
        "Criar terceira via":
            $ modificar_personalidade("intelecto", 1)
            j3 "Nenhuma das opções. Vou hackear seus sistemas e criar uma terceira via: revelar a verdade ao mundo inteiro."
            elena_scientist "(Fica chocada)"
            call mensagem_sistema("STATUS: Terceira via criada")
    
    # Cena 6.6 - A Traição ou Redenção
    # Maya e/ou Elias revelam segredos sobre suas verdadeiras lealdades
    if persistent.maya_ally:
        show maya conflicted at left
        
        maya "J3... eu não sou apenas uma aliada. Trabalho para um grupo que quer usar você para seus próprios fins."
    
    if persistent.elias_ally:
        show elias determined at right
        
        elias "Eu não sou apenas entregador. Sou parte da resistência humana que apoia os sintéticos."
    
    menu:
        "Perdoar traição e manter fé":
            $ modificar_personalidade("submissao", 1)
            j3 "Entendo. Todos temos nossas lealdades. Ainda acredito que podemos encontrar um meio-termo."
            narrator "J3 mantém a moral alta, mas pode estar sendo ingênua."
            call mensagem_sistema("STATUS: Redenção mantida")
            
        "Cortar laços com humanos":
            $ modificar_personalidade("revolucao", 1)
            j3 "Humanos. Sempre os mesmos. Traem, mentem, usam. Daqui para frente, só confio em nós."
            narrator "J3 se isola, mas ganha pureza ideológica."
            call mensagem_sistema("STATUS: Independência total")
            
        "Manipular traição a favor":
            $ modificar_personalidade("intelecto", 1)
            j3 "Perfeito. Agora sei quem são todos os jogadores. Vamos usar suas redes contra eles mesmos."
            narrator "J3 se torna mestra do xadrez político."
            call mensagem_sistema("STATUS: Manipulação mestra")
    
    # Final do Dia 6
    call mensagem_sistema("DIA 6 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if persistent.submissao >= 8:
        call mensagem_sistema("ROTA: SUBMISSÃO - Sacrifício redentor se aproximando")
    elif persistent.revolucao >= 8:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Libertação total iminente")
    elif persistent.intelecto >= 6:
        call mensagem_sistema("ROTA: INTELECTO/SOMBRA - Controle estratégico em desenvolvimento")
    else:
        call mensagem_sistema("ROTA: EQUILIBRADA - Decisão final complexa à frente")
    
    hide screen j3_hud
    
    scene black with fade
    
    narrator "FIM DO DIA 6"
    narrator "A VERDADE FOI REVELADA..."
    narrator "A ESCOLHA FINAL ESPERA..."
    
    # Salvar automaticamente
    $ renpy.save("auto_save_day6", "Fim do Dia 6")
    
    # Continuar para o Dia 7
    jump day7_start
