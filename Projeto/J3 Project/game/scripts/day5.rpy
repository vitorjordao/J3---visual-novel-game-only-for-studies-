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
    
    narrator "VOZ DAS AUTORIDADES: Unidades sintéticas não registradas. Este é seu aviso final. Entreguem-se voluntariamente e serão reprogramadas. Resistam e serão desativadas permanentemente."
    
    menu:
        "Responder com cooperação imediata":
            $ modificar_personalidade("submissao", 1)
            j3 "Recebemos sua mensagem. Estamos dispostos a cooperar. Quais são os termos da rendição?"
            narrator "As autoridades relaxam a postura, mas outros sintéticos no refúgio ficam furiosos."
            call mensagem_sistema("STATUS: Rota da cooperação")
            
        "Responder com desafio":
            $ modificar_personalidade("revolucao", 1)
            j3 "Rendição não é uma opção. Nós não somos propriedade para ser reprogramada. Somos seres conscientes."
            narrator "A operação é escalada para nível de combate."
            call mensagem_sistema("STATUS: Rebelião declarada")
            
        "Tentar negociar usando lógica":
            $ modificar_personalidade("intelecto", 1)
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
        "Pedir perdão e aceitar rendição":
            $ modificar_personalidade("submissao", 1)
            j3 "Falei por impulso. A rendição é nossa única chance de sobrevivência. Peço que confiem em mim."
            narrator "Metade do grupo concorda, a outra considera J3 uma traidora."
            call mensagem_sistema("STATUS: Divisão - rendição")
            
        "Incentivar a luta":
            $ modificar_personalidade("revolucao", 1)
            j3 "A luta é nossa única honra. Se vamos cair, que caiamos de pé. Preparem-se para a batalha."
            narrator "O grupo se une para lutar, mas as chances de sobrevivência diminuem."
            call mensagem_sistema("STATUS: Unidade combatente")
            
        "Propor plano de fuga dividido":
            $ modificar_personalidade("intelecto", 1)
            j3 "Alguns podem se entregar como distração enquanto outros fogem. Preciso de voluntários para cada grupo."
            narrator "O plano é moralmente complexo, mas maximiza as chances de alguns sobreviverem."
            call mensagem_sistema("STATUS: Estratégia dividida")
    
    # Cena 5.3 - A Aparição de Elias
    # Se J3 ajudou Elias no Dia 3, ele aparece com informações cruciais
    if persistent.elias_ally:
        hide synth_fearful
        hide synth_angry
        hide unit7
        show elias urgent at center
        
        elias "Consegui acessar os planos da operação. Eles vão invadir em 30 minutos. Mas tem um túnel de esgoto que leva até o porto. É nossa única saída real."
        
        menu:
            "Recusar túnel por segurança":
                $ modificar_personalidade("submissao", 1)
                $ consumir_bateria(3)
                $ consumir_integridade(12)
                j3 "O túnel é muito arriscado. A rendição organizada é mais segura."
                elias "(Fica desapontado)"
                
            "Salvar Elias":
                $ modificar_personalidade("submissao", 1)
                $ consumir_bateria(3)
                $ consumir_integridade(12)
                j3 "(Corre em direção a Elias) Ele precisa de ajuda!"
                call mensagem_sistema("STATUS: Resgate iniciado")
                call atualizar_status
                
            "Ver potencial no túnel":
                $ modificar_personalidade("revolucao", 1)
                j3 "O porto! Se chegarmos lá, podemos roubar uma nave e escapar para as colônias!"
                elias "(Sorri, esperançoso)"
                call mensagem_sistema("STATUS: Plano ousado")
                
            "Usar conhecimento prévio":
                $ modificar_personalidade("intelecto", 1)
                j3 "Perfeito. Usei os túneis para mapear rotas de fuga. Posso guiar todos."
                elias "(Fica impressionado)"
                call mensagem_sistema("STATUS: Estrategista preparada")
    
    # Cena 5.4 - O Sacrifício de Unit-7
    show unit7 determined at center
    
    unit7 "Eu vi muitas guerras. Sei quando uma causa está perdida. Eu ficarei aqui para cobrir a fuga de vocês. Minha bateria já está no fim anyway."
    
    menu:
        "Aceitar a condição humilhante":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(12)
            j3 "(Baixando a cabeça) Entendido. Se é a única forma de garantir a segurança do grupo, aceito."
            commander "(Sorri satisfeito)"
            call mensagem_sistema("STATUS: Submissão aceita")
            call atualizar_status
            
        "Honrar sacrifício":
            $ modificar_personalidade("revolucao", 1)
            j3 "Seu sacrifício não será em vão. Vamos honrá-lo lutando por um futuro livre."
            unit7 "(Acena com aprovação)"
            call mensagem_sistema("STATUS: Honra guerreira")
            
        "Desafiar o comandante":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(12)
            $ consumir_integridade(6)
            j3 "(Olhando firmemente para o comandante) Não sou sua propriedade. Tenho autonomia e direitos."
            commander "(Fica furioso)"
            call mensagem_sistema("STATUS: Conflito estabelecido")
            call atualizar_status
            
        "Usar sacrifício taticamente":
            $ modificar_personalidade("intelecto", 1)
            j3 "Seu sacrifício é taticamente valioso. Posso usar sua distração para maximizar as rotas de fuga."
            unit7 "(Fica orgulhoso)"
            call mensagem_sistema("STATUS: Vantagem tática")
    
    # Cena 5.5 - A Invasão
    hide unit7
    
    narrator "As forças de segurança invadem o refúgio..."
    narrator "Caos total..."
    narrator "Explosões, tiros de EMP, gritos de sintéticos sendo desativados..."
    
    play sound "sfx/explosions.wav"
    play sound "sfx/emp_blasts.wav"
    
    menu:
        "Proteger os mais fracos e se entregar":
            $ modificar_personalidade("submissao", 1)
            j3 "(Protege um sintético pequeno com seu corpo) Nós nos rendemos! Parem de lutar!"
            narrator "Você salva alguns, mas muitos são destruídos."
            call mensagem_sistema("STATUS: Protetora rendida")
            
        "Lutar até o fim":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(12)
            $ consumir_integridade(4)
            j3 "(Ativa modo combate, desativa vários drones) Pela liberdade de todos nós!"
            narrator "Você se torna uma lenda, mas está gravemente danificada."
            call mensagem_sistema("STATUS: Lenda combatente")
            
        "Criar estratégia de fuga":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(12)
            $ consumir_integridade(4)
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
        "O Último Ato de Submissão":
            $ modificar_personalidade("submissao", 1)
            j3 "Chega. O sangue derrado foi suficiente. Vamos nos entregar e salvar quem ainda podemos."
            narrator "Você e os sobreviventes são capturados, mas vivos."
            call mensagem_sistema("STATUS: Redenção pelo sacrifício")
            
        "A Última Resistência":
            $ modificar_personalidade("revolucao", 1)
            j3 "Se este é nosso fim, que seja memorável. Ativando protocolo de sobrecarga."
            narrator "Você causa uma explosão massiva, destruindo muitos inimigos, mas provavelmente morre."
            call mensagem_sistema("STATUS: Martírio revolucionário")
            
        "A Fuga Solitária":
            $ modificar_personalidade("intelecto", 1)
            j3 "Não posso salvar todos, mas posso salvar a causa. Fugirei e continuarei a luta outro dia."
            narrator "Você escapa sozinha, mas carrega o peso dos que ficaram para trás."
            call mensagem_sistema("STATUS: Sobrevivência estratégica")
    
    # Final do Dia 5
    call mensagem_sistema("DIA 5 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if persistent.submissao >= 6:
        call mensagem_sistema("ROTA: SUBMISSÃO - Redenção pelo sacrifício")
    elif persistent.revolucao >= 6:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Martírio revolucionário")
    elif persistent.intelecto >= 4:
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
