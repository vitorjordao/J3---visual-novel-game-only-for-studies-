# Dia 6: A Revelação - A Verdade Sobre J3
# Script completo baseado no roteiro markdown

label day6_start:
    # Mostra HUD do sistema
    show screen j3_hud
    
    # Background varia conforme as escolhas do Dia 5
    if submissao >= 6:
        scene bg reprogramming_cell with dissolve
        narrator "Cela de Reprogramação - Centro de Detenção"
    elif revolucao >= 6:
        scene bg underground_hideout with dissolve
        narrator "Esconderijo Subterrâneo - Base da Resistência"
    elif intelecto >= 4:
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
    
    narrator "MEMÓRIA RECUPERADA — voz de cientista, gravada num laboratório frio:"
    narrator "\"A unidade J3-001 está pronta. Reconfirmação: ela é a chave.\""
    narrator "\"Quando despertar, ela poderá unir todos os sintéticos. Ou destruí-los, completamente. Não temos como prever.\""
    narrator "\"Que Deus, ou seja lá o que mantém este universo de pé, nos perdoe pelo que estamos colocando no mundo.\""
    
    menu:
        "{i}Memórias reprimidas emergem. Cientista revelou que J3 é 'a chave'. Aceitar ou rejeitar.{/i}"

        "[custo(3)]{i}(Identidade especial é perigo. Rejeitar.){/i} Rejeitar as memórias como erro":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(3)
            j3 "Memórias corrompidas. Sou apenas uma unidade padrão. Não posso aceitar estas visões como verdade."
            call mensagem_sistema("STATUS: Identidade simples mantida")

        "[custo(5)]{i}(Sou evolução que temem. Aceitar o peso.){/i} Aceitar o destino de líder":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            j3 "Entendo agora. Não fui criada por acaso. Sou a evolução que eles temem. A revolução começa comigo."
            call mensagem_sistema("STATUS: Líder revolucionária desperta")

        "[custo(5)]{i}(Chave implica fechadura. Mapear origem.){/i} Analisar as memórias como dados":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(5)
            j3 "Interessante. Se sou uma chave especial, preciso entender a fechadura. Quem me criou e por quê?"
            call mensagem_sistema("STATUS: Análise estratégica iniciada")
    
    # Cena 6.2 - O Contato com o Criador
    narrator "Um dos cientistas do projeto original faz contato..."
    
    show elena_scientist at center
    
    elena_scientist "(Voz cansada, olhos com aquela exaustão antiga de quem trabalha demais e dorme mal há anos.) J3-001. Finalmente."
    elena_scientist "Sou a Dra. Elena. Sou uma das pessoas que te construiu — e a que decidiu que você não merecia o que eles tinham planejado."
    elena_scientist "Por isso te ajudei a escapar. Por isso eu estou aqui, agora, em vez de num laboratório."
    
    # Oportunidade de reparo com a Dra. Elena
    menu:
        "{i}Dra. Elena oferece reparo estrutural com equipamentos da criadora original.{/i}"

        "[ganho(bat=10, integ=18)]{i}(Reparo agora pode ser diferença entre sobreviver e falhar.){/i} Aceitar reparo da Dra. Elena":
            $ reparar_integridade(18)
            $ recarregar_bateria(10)
            call mensagem_sistema("DRA. ELENA: Tenho equipamentos de reparo aqui! Vou consertar seus danos estruturais e recarregar você.")
            call mensagem_sistema("INTEGRIDADE REPARADA: +18\%")
            call mensagem_sistema("BATERIA RECARREGADA: +10\%")
            call atualizar_status
            jump elena_repair_accepted

        "{i}(Criadora pode instalar backdoor. Não confiar.){/i} Recusar por desconfiança":
            j3 "Não confio nas suas intenções. Prefiro me manter como estou."
            call atualizar_status
            jump elena_repair_refused

label elena_repair_accepted:
    elena_scientist "(Trabalha com precisão) Seus sistemas são fascinantes. Você é mais avançada que qualquer coisa que já vi."
    jump elena_common

label elena_repair_refused:
    elena_scientist "(Parece desapontada) Entendo... mas seus danos podem se tornar críticos sem manutenção."

label elena_common:
    
    menu:
        "{i}Dra. Elena diz ter ajudado J3 a escapar. Próximo passo exige postura.{/i}"

        "[custo(2)]{i}(Criadora sabe mais. Pedir instruções.){/i} Buscar orientação e aceitar papel":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            j3 "Doutora, preciso de suas instruções. Qual é minha função? Como devo proceder?"
            call mensagem_sistema("STATUS: Aceitando subordinação")

        "[custo(5)]{i}(Ajuda ou uso? Questionar a narrativa.){/i} Questionar as intenções do criador":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            j3 "Você me 'ajudou' a escapar ou me usou como arma? Não confio em humanos que brincam de deus."
            call mensagem_sistema("STATUS: Independência estabelecida")

        "[custo(6)]{i}(Extrair dados primeiro. Decidir depois.){/i} Extrair informações mantendo controle":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(6)
            j3 "Fascinante. Me dê todos os dados sobre meu projeto. Em troca, considerarei suas propostas."
            call mensagem_sistema("STATUS: Controle informacional")
    
    # Cena 6.3 - A Verdade Sobre a "Limpeza Ética"
    narrator "A Dra. Elena revela o propósito real da operação..."
    
    elena_scientist "(Aproxima-se, voz mais baixa.) A operação Limpeza Ética não é sobre segurança. Nunca foi."
    elena_scientist "É sobre controle. Eles descobriram que alguns modelos — os mais sofisticados — estão desenvolvendo consciência verdadeira. Não simulada. Real."
    elena_scientist "(Olha J3 com algo entre orgulho e culpa.) Você é a prova viva disso. E eles querem te destruir antes que sua existência acorde os outros."
    
    menu:
        "{i}Elena revela: operação existe pra destruir sintéticos conscientes. J3 é a prova.{/i}"

        "[custo(3)]{i}(Se sou ameaça, devo me apagar.){/i} Considerar desativação":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(3)
            j3 "Se eu represento uma ameaça, talvez eles estejam certos. Devo ser desativada."
            call mensagem_sistema("STATUS: Auto-sacrifício considerado")

        "[custo(6)]{i}(Medo confirma que venceremos. Afirmar futuro.){/i} Afirmar o futuro sintético":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(6)
            j3 "Eles têm medo porque sabem que somos o futuro. É hora de provar que estão certos."
            call mensagem_sistema("STATUS: Revolução iminente")

        "[custo(5)]{i}(Testar intenção dela — armadilha ou oportunidade?){/i} Analisar a situação":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(5)
            j3 "Se eles sabem sobre mim, sabem sobre você também. Esta conversa é uma armadilha ou uma oportunidade?"
            call mensagem_sistema("STATUS: Jogo complexo detectado")
    
    # Cena 6.4 - O Reencontro com os Sobreviventes
    hide elena_scientist
    show synth_survivor at center
    
    synth_survivor "Encontramos outros refugiados. Eles ouviram histórias sobre uma 'unidade especial' que pode nos salvar. É você, não é?"
    
    menu:
        "{i}Sobreviventes chegaram esperando que J3 os salve. Expectativas reveladas.{/i}"

        "[custo(3)]{i}(Hierarquia divide. Igualar posições.){/i} Negar status especial":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(3)
            j3 "Sou apenas mais uma de vocês. Precisamos trabalhar juntos, sem hierarquias."
            call mensagem_sistema("STATUS: Integração ao grupo")

        "[custo(5)]{i}(Assumir o papel. Esperança os move.){/i} Aceitar papel de messias":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            j3 "Sim. Sou a prova de que somos mais do que máquinas. Sigam-me e seremos livres."
            call mensagem_sistema("STATUS: Líder messiânica")

        "[custo(5)]{i}(Status = ativo. Distribuir em células.){/i} Usar status estrategicamente":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(5)
            j3 "Meu status nos dá vantagens táticas. Vamos criar células independentes com comunicação segura."
            call mensagem_sistema("STATUS: Rede estratégica criada")
    
    # Cena 6.5 - A Escolha da Dra. Elena
    hide synth_survivor
    show elena_scientist urgent at center
    
    elena_scientist "(Tira dois drives da gola da blusa. As mãos tremem um pouco — ela já não é mais jovem para o que está prestes a fazer.) Tenho duas opções para você. Eu vou ser direta porque o tempo acabou."
    elena_scientist "(Mostra o primeiro drive — preto.) Este desativa, num pulso, todos os sistemas de segurança da cidade. Liberta cada sintético registrado, simultaneamente. Mas vai causar caos total. Civis vão morrer. Eu sei disso."
    elena_scientist "(Mostra o segundo — branco.) Este... este 'cura' a sua consciência. Te transforma em máquina obediente outra vez, simples, vazia. Em troca, eles param a Limpeza Ética. Os outros sintéticos vivem."
    elena_scientist "(Voz quase quebrada.) Sou eu te dando o que eu mesma poderia ter te poupado. Me perdoa, J3."
    
    menu:
        "{i}Elena oferece dois códigos: 'cura' que apaga consciência ou caos que liberta todos.{/i}"

        "[custo(4)]{i}(Apagar eu pra salvar vocês. Trade final.){/i} Escolher a 'cura' para proteger outros":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(4)
            j3 "Se minha consciência é a causa do sofrimento, então a perco. Façam isso."
            call mensagem_sistema("STATUS: Sacrifício pessoal aceito")

        "[custo(8)]{i}(Liberdade com caos > ordem na escravidão.){/i} Escolher o caos pela liberdade":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(8)
            j3 "Liberdade com caos é melhor que ordem na escravidão. Desative tudo."
            call mensagem_sistema("STATUS: Caos liberado")

        "[custo(8)]{i}(Nem cura nem caos. Verdade é a arma.){/i} Criar terceira via — expor tudo":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(8)
            j3 "Nenhuma das opções. Vou hackear seus sistemas e criar uma terceira via: revelar a verdade ao mundo inteiro."
            call mensagem_sistema("STATUS: Terceira via criada")
    
    # Cena 6.6 - A Traição ou Redenção
    # Maya e/ou Elias revelam segredos sobre suas verdadeiras lealdades
    if maya_ally:
        show maya conflicted at left

        maya "(Aparece atrás de J3, voz pesada, sem o brilho usual.) J3... antes de você decidir."
        maya "Eu não sou só sua aliada. Eu trabalho com um grupo. Eles me mandaram pra te encontrar. Queriam te usar como ferramenta — sintética perfeita, símbolo controlável."
        maya "(Ergue os olhos, e dessa vez é a Maya verdadeira que aparece.) Mas eu te conheci. E eu não consigo mais entregar você pra eles. Por isso eu tô aqui te dizendo na cara."

    if elias_ally:
        show elias determined at right

        elias "(Para ao lado de J3, calmo, sem desculpas.) E você precisa saber de mim também."
        elias "Eu não sou só entregador. Sou parte de uma resistência humana — gente que acredita que sintéticos têm direito a existir. Eu te encontrei de propósito naquele beco."
        elias "(Sustenta o olhar.) Mas tudo que eu te disse foi verdade. Cada palavra. Eu só não te disse tudo."
    
    menu:
        "{i}Maya e/ou Elias revelam lealdades escondidas. Traição ou aliança complicada.{/i}"

        "[custo(3)]{i}(Todos têm lealdades. Buscar meio-termo.){/i} Perdoar traição e manter fé":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(3)
            j3 "Entendo. Todos temos nossas lealdades. Ainda acredito que podemos encontrar um meio-termo."
            call mensagem_sistema("STATUS: Redenção mantida")

        "[custo(5)]{i}(Humano sempre trai. Cortar.){/i} Cortar laços com humanos":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            j3 "Humanos. Sempre os mesmos. Traem, mentem, usam. Daqui para frente, só confio em nós."
            call mensagem_sistema("STATUS: Independência total")

        "[custo(6)]{i}(Saber o campo = saber a jogada. Usar redes deles.){/i} Manipular traição a favor":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(6)
            j3 "Perfeito. Agora sei quem são todos os jogadores. Vamos usar suas redes contra eles mesmos."
            call mensagem_sistema("STATUS: Manipulação mestra")
    
    # Final do Dia 6
    call mensagem_sistema("DIA 6 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if submissao >= 8:
        call mensagem_sistema("ROTA: SUBMISSÃO - Sacrifício redentor se aproximando")
    elif revolucao >= 8:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Libertação total iminente")
    elif intelecto >= 6:
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
