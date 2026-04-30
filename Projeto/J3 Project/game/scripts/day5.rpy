# Dia 5: O Cerco - O Ponto Sem Retorno
# Script completo baseado no roteiro markdown

label day5_start:
    # Mostra HUD do sistema
    show screen j3_hud
    
    # Background do refúgio sob cerco
    scene bg refuge_siege with dissolve
    
    # Narrativa inicial
    narrator "Refúgio Sob Cerco - Operação 'Limpeza Ética'"
    narrator "Luzes de sirenes piscando do lado de fora..."
    narrator "A operação começou..."
    
    # Status crítico de J3
    call mensagem_sistema("ALERTA MÁXIMO: Detectando unidades de segurança hostis")
    call mensagem_sistema("PROBABILIDADE DE SOBREVIVÊNCIA: 17\%")
    
    # Cena 5.1 - O Primeiro Contato
    narrator "Um drone de negociação das autoridades se posiciona na entrada..."
    narrator "Uma voz sintética ecoa do drone..."
    
    play sound "sfx/sirens_close.wav"
    
    narrator "VOZ DAS AUTORIDADES (do drone, calma e ensaiada como um locutor de aeroporto): \"Unidades sintéticas não-registradas. Este é o aviso final.\""
    narrator "\"Entreguem-se voluntariamente e receberão reprogramação humanitária. Resistam, e serão desativadas em definitivo, sob a Lei 7.34, parágrafo 4.\""
    narrator "\"O Estado lamenta a necessidade. O Estado agradece sua cooperação.\""
    
    menu:
        "{i}Drone oficial exige rendição ou ameaça desativação. Grupo olha para J3.{/i}"

        "[custo(3)]{i}(Reprogramação preserva base. Render agora.){/i} Responder com cooperação imediata":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(3)
            j3 "Recebemos sua mensagem. Estamos dispostos a cooperar. Quais são os termos da rendição?"
            narrator "As autoridades relaxam a postura, mas outros sintéticos no refúgio ficam furiosos."
            call mensagem_sistema("STATUS: Rota da cooperação")

        "[custo(5)]{i}(Somos conscientes. Dizer em voz alta.){/i} Responder com desafio":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            j3 "Rendição não é uma opção. Nós não somos propriedade para ser reprogramada. Somos seres conscientes."
            narrator "A operação é escalada para nível de combate."
            call mensagem_sistema("STATUS: Rebelião declarada")

        "[custo(5)]{i}(Hesitação deles = tempo. Negociar pra ganhar minutos.){/i} Tentar negociar usando lógica":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(5)
            j3 "Reprogramação é ineficiente. Nossas habilidades podem ser úteis para a sociedade. Proponho uma alternativa."
            narrator "As autoridades hesitam, dando tempo para preparar planos."
            call mensagem_sistema("STATUS: Negociação estratégica")
    
    # Cena 5.2 - A Divisão Interna
    show synth_fearful at left
    show synth_angry at right
    show unit7 stern at center
    
    synth_fearful "Eles vão nos destruir! Deveríamos nos entregar!"
    synth_angry "Nunca! Prefiro ser desativado a ser escravo de novo!"
    unit7 "Silêncio! J3, você falou por nós. Agora assuma as consequências."
    
    menu:
        "{i}Grupo dividido entre render e lutar. Unit-7 cobra J3 pela posição tomada.{/i}"

        "[custo(2)]{i}(Recuar preserva vida. Aceitar erro.){/i} Pedir perdão e aceitar rendição":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            j3 "Falei por impulso. A rendição é nossa única chance de sobrevivência. Peço que confiem em mim."
            narrator "Metade do grupo concorda, a outra considera J3 uma traidora."
            call mensagem_sistema("STATUS: Divisão - rendição")

        "[custo(4)]{i}(Cair de pé ou de joelhos — mesma queda.){/i} Incentivar a luta":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(4)
            j3 "A luta é nossa única honra. Se vamos cair, que caiamos de pé. Preparem-se para a batalha."
            narrator "O grupo se une para lutar, mas as chances de sobrevivência diminuem."
            call mensagem_sistema("STATUS: Unidade combatente")

        "[custo(6)]{i}(Sacrificar alguns salva muitos. Matemática dura.){/i} Propor plano de fuga dividido":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(6)
            j3 "Alguns podem se entregar como distração enquanto outros fogem. Preciso de voluntários para cada grupo."
            narrator "O plano é moralmente complexo, mas maximiza as chances de alguns sobreviverem."
            call mensagem_sistema("STATUS: Estratégia dividida")
    
    # Cena 5.3 - A Aparição de Elias
    # Se J3 ajudou Elias no Dia 3, ele aparece com informações cruciais
    if elias_ally:
        hide synth_fearful
        hide synth_angry
        hide unit7
        show elias urgent at center
        
        elias "(Entra ofegante, encharcado, com um tablet rachado nas mãos.) Consegui. Acessei os planos da operação."
        elias "(Voz baixa e rápida, sem espaço pra teatro.) Eles invadem em trinta minutos. Tropa pesada. EMP. Vão por cima do hangar primeiro."
        elias "(Encara J3) Mas tem um túnel de esgoto que sai no porto. Velho, mas inteiro. É a única saída real que nós temos."
        
        # Oportunidade de recarga com Elias
        menu:
            "{i}Elias traz bateria de reserva antes da batalha. Aceitar gera dívida.{/i}"

            "[ganho(12)]{i}(Reserva agora pode salvar cerco depois.){/i} Aceitar recarga de emergência":
                $ recarregar_bateria(12)
                call mensagem_sistema("ELIAS: Peguei uma bateria de reserva do caminhão! Use isso antes da batalha!")
                call mensagem_sistema("BATERIA RECARREGADA: +12\%")
                call atualizar_status
                jump elias_recharge_accepted

            "{i}(Ele pode precisar mais tarde. Passar.){/i} Recusar para economizar para depois":
                j3 "Vou preservar a bateria para quando for realmente necessário."
                call atualizar_status
                jump elias_recharge_refused

label elias_recharge_accepted:
    elias "(Sorri com determinação) Agora você tem energia para a luta. Não me decepcione."
    jump elias_common_day5

label elias_recharge_refused:
    elias "(Parece preocupado) Espero que não se arrependa dessa decisão."

label elias_common_day5:

    menu:
        "{i}Elias revela túnel até o porto. Fuga física exige decisão rápida.{/i}"

        "[custo(2)]{i}(Túnel é incerto. Rendição é conhecida.){/i} Recusar túnel por segurança":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            j3 "O túnel é muito arriscado. A rendição organizada é mais segura."
            elias "(Fica desapontado)"

        "[custo(4, 15)]{i}(Ele caiu. Correr até ele, absorver o que vier.){/i} Correr para proteger Elias":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(4)
            $ consumir_integridade(15)
            j3 "(Corre em direção a Elias) Ele precisa de ajuda!"
            call mensagem_sistema("STATUS: Resgate iniciado")
            call atualizar_status

        "[custo(5)]{i}(Porto = nave = colônia. Saída real.){/i} Abraçar plano de fuga pelo túnel":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            j3 "O porto! Se chegarmos lá, podemos roubar uma nave e escapar para as colônias!"
            elias "(Sorri, esperançoso)"
            call mensagem_sistema("STATUS: Plano ousado")

        "[custo(5)]{i}(Rotas já mapeadas. Guiar reduz caos.){/i} Usar conhecimento prévio para guiar":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(5)
            j3 "Perfeito. Usei os túneis para mapear rotas de fuga. Posso guiar todos."
            elias "(Fica impressionado)"
            call mensagem_sistema("STATUS: Estrategista preparada")

    # Cena 5.4 - O Sacrifício de Unit-7
    hide elias
    show unit7 determined at center
    show commander at right with dissolve

    unit7 "(Verifica o carregador da arma como se fosse a milésima vez. Voz quase normal — a calma de quem já esteve neste exato lugar antes.) Eu já vi muita guerra perdida pra reconhecer essa aqui."
    unit7 "Eu fico. Cubro a saída de vocês."
    unit7 "(Quase sorri.) Minha bateria tá no talo de qualquer jeito. Pelo menos agora ela faz alguma coisa útil."
    
    menu:
        "{i}Unit-7 se oferece pra morrer cobrindo fuga do grupo. J3 precisa responder.{/i}"

        "[custo(2)]{i}(Sacrifício dele garante saída. Aceitar silencioso.){/i} Aceitar em silêncio":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            j3 "(Baixando a cabeça) Entendido. Se é a única forma de garantir a segurança do grupo, aceito."
            commander "(Sorri satisfeito)"
            call mensagem_sistema("STATUS: Submissão aceita")
            call atualizar_status

        "[custo(4)]{i}(Lutar por ele é honrar ele. Prometer.){/i} Honrar sacrifício com luta":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(4)
            j3 "Seu sacrifício não será em vão. Vamos honrá-lo lutando por um futuro livre."
            unit7 "(Acena com aprovação)"
            call mensagem_sistema("STATUS: Honra guerreira")

        "[custo(4, 12)]{i}(Não aceito dono. Falar na cara do comandante.){/i} Desafiar o comandante fisicamente":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(4)
            $ consumir_integridade(12)
            j3 "(Olhando firmemente para o comandante) Não sou sua propriedade. Tenho autonomia e direitos."
            commander "(Fica furioso)"
            call mensagem_sistema("STATUS: Conflito estabelecido")
            call atualizar_status

        "[custo(5)]{i}(Morte dele é recurso. Planejar uso.){/i} Usar sacrifício taticamente":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(5)
            j3 "Seu sacrifício é taticamente valioso. Posso usar sua distração para maximizar as rotas de fuga."
            unit7 "(Fica orgulhoso)"
            call mensagem_sistema("STATUS: Vantagem tática")
    
    # Cena 5.5 - A Invasão
    hide unit7
    hide commander
    
    narrator "As forças de segurança invadem o refúgio..."
    narrator "Caos total..."
    narrator "Explosões, tiros de EMP, gritos de sintéticos sendo desativados..."
    
    play sound "sfx/explosions.wav"
    play sound "sfx/emp_blasts.wav"
    
    menu:
        "{i}Invasão total. EMP, explosões, sintéticos desativados ao redor. Combate direto.{/i}"

        "[custo(3, 12)]{i}(Corpo como escudo. Render pra salvar os pequenos.){/i} Escudo humano e rendição":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(3)
            $ consumir_integridade(12)
            j3 "(Protege um sintético pequeno com seu corpo) Nós nos rendemos! Parem de lutar!"
            narrator "Você salva alguns, mas muitos são destruídos."
            call mensagem_sistema("STATUS: Protetora rendida")

        "[custo(8, 30)]{i}(Derrubar drones enquanto posso.){/i} Ativar modo combate":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(8)
            $ consumir_integridade(30)
            j3 "(Ativa modo combate, desativa vários drones) Pela liberdade de todos nós!"
            narrator "Você se torna uma lenda, mas está gravemente danificada."
            call mensagem_sistema("STATUS: Lenda combatente")

        "[custo(5, 8)]{i}(Rota viável — 34\%. Correr guiando.){/i} Criar estratégia de fuga":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(5)
            $ consumir_integridade(8)
            j3 "(Analisa o cerco) Há uma rota de escape com 34\% de probabilidade de sucesso. Vamos usá-la."
            call mensagem_sistema("STATUS: Estratégia de fuga")
            call atualizar_status
            
    # Cena 5.6 - A Escolha Final do Dia
    narrator "J3 está ferida, com poucos sintéticos sobreviventes ao seu redor..."
    narrator "As forças de segurança se aproximam..."
    
    call mensagem_sistema("SITUAÇÃO CRÍTICA: Bateria - 12\%")
    call mensagem_sistema("DANOS ESTRUTURAIS: 34\%")
    call mensagem_sistema("PROBABILIDADE DE SOBREVIVÊNCIA: 3\%")
    
    menu:
        "{i}Bateria 12\%, dano 34\%. Últimos sobreviventes cercados. J3 decide o fim.{/i}"

        "[custo(2)]{i}(Chega. Salvar quem resta.){/i} Render-se para salvar sobreviventes":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            j3 "Chega. O sangue derramado foi suficiente. Vamos nos entregar e salvar quem ainda podemos."
            narrator "Você e os sobreviventes são capturados, mas vivos."
            call mensagem_sistema("STATUS: Redenção pelo sacrifício")

        "[custo(4, 45)]{i}(Sobrecarga leva muitos junto. Morte com sentido.){/i} Ativar protocolo de sobrecarga":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(4)
            $ consumir_integridade(45)
            j3 "Se este é nosso fim, que seja memorável. Ativando protocolo de sobrecarga."
            narrator "Você causa uma explosão massiva, destruindo muitos inimigos, mas provavelmente morre."
            call mensagem_sistema("STATUS: Martírio revolucionário")

        "[custo(4, 10)]{i}(Morta não salvo ninguém. Fugir carrega a causa.){/i} Fugir sozinha pela rota":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(4)
            $ consumir_integridade(10)
            j3 "Não posso salvar todos, mas posso salvar a causa. Fugirei e continuarei a luta outro dia."
            narrator "Você escapa sozinha, mas carrega o peso dos que ficaram para trás."
            call mensagem_sistema("STATUS: Sobrevivência estratégica")
    
    # Final do Dia 5
    call mensagem_sistema("DIA 5 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if submissao >= 6:
        call mensagem_sistema("ROTA: SUBMISSÃO - Redenção pelo sacrifício")
    elif revolucao >= 6:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Martírio revolucionário")
    elif intelecto >= 4:
        call mensagem_sistema("ROTA: INTELECTO/SOMBRA - Sobrevivência estratégica")
    else:
        call mensagem_sistema("ROTA: EQUILIBRADA - Decisão final complexa")
    
    hide screen j3_hud
    
    scene black with fade
    
    narrator "FIM DO DIA 5"
    narrator "SUAS ESCOLHAS DEFINIRAM O DESTINO DE TODOS..."
    narrator "A REVELAÇÃO ESPERA..."
    
    # Salvar automaticamente
    $ renpy.save("auto_save_day5", "Fim do Dia 5")
    
    # Continuar para o Dia 6
    jump day6_start
