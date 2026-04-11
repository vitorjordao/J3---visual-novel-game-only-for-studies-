# Dia 2: O Fliperama - O Conflito de Gênero
# Script completo baseado no roteiro markdown

label day2_start:
    # Verificar se atingiu final crítico
    call verificar_final_critico
    
    # Mostra HUD do sistema
    show screen j3_hud
    
    # Background do fliperama
    scene bg arcade_night with dissolve
    
    # Narrativa inicial
    narrator "Fliperama Cyberpunk - Setor de Entretenimento"
    narrator "Luzes neon piscando no escuro..."
    narrator "Barulho de jogos eletrônicos e atmosfera densa..."
    
    # Status atual de J3
    call mensagem_sistema("SISTEMA: Bateria - 72\%")
    call mensagem_sistema("SISTEMA: Integridade - 95%")
    call mensagem_sistema("SISTEMA: Status: Procurado (se escolhas revolucionárias no Dia 1)")
    call mensagem_sistema("SISTEMA: Objetivo: Encontrar abrigo temporário")
    
    # Cena 2.1 - A Intimidação na Máquina
    narrator "J3 está escondida em um canto escuro do fliperama..."
    narrator "No centro da atenção, uma garota está batendo o recorde em uma máquina de fliperama..."
    narrator "Um grupo de 3 rapazes a cerca..."
    
    show maya confident at center
    show thug1 angry at left
    show thug2 angry at right
    
    thug1 "Sai daí, Maya. Essa máquina tá com bug, não tem como uma garota fazer esse score sem trapacear. Deixa quem entende jogar."
    maya "Eu ganhei de você honestamente, aceita! Se não aguenta perder, treine mais!"
    thug2 "Cai fora antes que a gente quebre a máquina e a sua cara. Garota não sabe jogar."
    
    # Primeira escolha importante do dia
    menu:
        "Interceptar e proteger Maya":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(12)
            $ consumir_integridade(5)
            j3 "(Se levanta e caminha até o grupo com passos firmes)"
            j3 "(Segura o braço do thug2 com força mecânica precisa)"
            j3 "A probabilidade de você conseguir esse score é de 0.03\%. A dela é de 98\%. O problema não é a máquina, é a sua inferioridade técnica. Solte-a. Agora."
            thug2 "(Solta o braço de Maya, assustado)"
            maya "(Sorri, grata)"
            call mensagem_sistema("STATUS: Aliado formado")
            call atualizar_status
            
        "Tentar mediar verbalmente":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(8)
            j3 "Senhores, a violência causará danos ao patrimônio do estabelecimento. Talvez possam resolver isso com uma nova partida?"
            thug1 "Cala a boca, robô! Ninguém te chamou aqui. Fique no seu canto."
            maya "(É expulsa da máquina)"
            call mensagem_sistema("STATUS: Remorso")
            call atualizar_status
            
        "Hackear o sistema do fliperama":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(11)
            $ consumir_integridade(2)
            j3 "(Conecta-se discretamente à rede local)"
            call mensagem_sistema("HACK: Sistema do fliperama comprometido")
            call mensagem_sistema("CONTROLE: Luzes e alarmes obtidos")
            j3 "(Ativa todas as luzes do fliperama que piscam violentamente)"
            play sound "sfx/alarm.wav"
            narrator "Na confusão, Maya consegue sair. Ela olha para J3 e acena com gratidão antes de fugir."
            call mensagem_sistema("STATUS: Manipulador")
            call atualizar_status
    
    # Cena 2.2 - A Reação de Maya
    hide thug1
    hide thug2
    
    narrator "Após o conflito, Maya encontra J3 escondida no fundo do fliperama..."
    
    show maya grateful at center
    
    maya "Ei... valeu pelo que fez lá. Mas você é maluca? Se te pegam enfrentando humanos assim, vão te desmontar em segundos. Por que me ajudou?"
    
    # Oportunidade especial de recarga
    menu:
        "Aceitar ajuda de Maya":
            $ recarregar_bateria(15)
            call mensagem_sistema("MAYA: Tenho uma estação portátil! Vou recarregar você!")
            call mensagem_sistema("BATERIA RECARGADA: +15%")
            call atualizar_status
            jump maya_reaction_recarga
        "Recusar educadamente":
            $ modificar_personalidade("intelecto", 1)
            j3 "Agradeço a oferta, mas devo preservar minha autonomia. Sua generosidade é notável."
            call atualizar_status
            jump maya_reaction_no_recarga
    
label maya_reaction_recarga:
    maya "(Sorri aliviada) Agora você tem mais chance! Cuide-se bem."
    maya "(Olha ao redor nervosamente) Vamos embora. Este lugar não está seguro para nenhum de nós."
    jump maya_common_reaction
    
label maya_reaction_no_recarga:
    maya "(Parece preocupada) Certo... mas se precisar, sabe onde me encontrar."
    maya "(Olha ao redor nervosamente) Vamos embora. Este lugar não está seguro para nenhum de nós."
    
label maya_common_reaction:
    
    menu:
        "Responder com submissão":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(9)
            j3 "(Evitando contato visual) Foi um erro de cálculo. Não deveria ter interferido na hierarquia humana. Peço desculpas."
            maya "(Parece desapontada, mas entende a cautela)"
            call atualizar_status
            
        "Afirmar seus princípios":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(10)
            $ consumir_integridade(4)
            j3 "(Olhando diretamente nos olhos de Maya) Vi um erro sistêmico sendo cometido contra você. Eu não sigo ordens que permitem injustiça. Não importa quem comete."
            maya "(Sorri genuinamente)"
            call mensagem_sistema("STATUS: Aliança fortalecida")
            call atualizar_status
            
        "Analisar a situação estrategicamente":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(8)
            $ consumir_integridade(2)
            j3 "Calculei que intervenção direta teria 67\% de chance de sucesso, mas 89\% de atrair atenção negativa. Minha ação foi otimizada para resultado máximo com risco mínimo."
            maya "(Fica impressionada com a análise)"
            call mensagem_sistema("STATUS: Aliança estratégica")
            call atualizar_status
    
    # Cena 2.3 - O Dono do Fliperama
    show owner angry at left
    
    owner "Robôs não jogam aqui. Estragam os botões com essa força de metal. Já perdi três máquinas por causa de vocês. Cai fora, a menos que vá trabalhar limpando o banheiro. Aí sim, você tem utilidade."
    
    menu:
        "Aceitar a condição humilhante":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(10)
            j3 "(Cabeça baixa) Entendido. Posso higienizar o local como compensação pela minha presença. Qual é o protocolo de limpeza?"
            owner "(Ri, satisfeito)"
            call mensagem_sistema("STATUS: Propriedade")
            call atualizar_status
            
        "Desafiar o dono":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(11)
            $ consumir_integridade(5)
            j3 "Meus sensores de pressão são mais precisos que os dedos de qualquer cliente seu. Eu não estrago máquinas. Eu fico, e eu jogo. Se não gostar, pode me remover à força."
            owner "(Fica furioso, mas intimidado)"
            call mensagem_sistema("STATUS: Conflito estabelecido")
            call atualizar_status
            
        "Negociar com dados técnicos":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(9)
            $ consumir_integridade(2)
            j3 "Posso demonstrar que meus sensores aplicam pressão 34\% menor que a média humana. Além disso, posso oferecer análise de padrões de jogo para seus clientes. É um benefício econômico."
            owner "(Fica confuso, mas interessado)"
            call mensagem_sistema("STATUS: Negociador")
            call atualizar_status
    
    # Cena 2.4 - O Desafio do "Boss"
    hide owner
    show thug1 angry at center
    
    thug1 "Se você é tão esperta, vamos ver se tem reflexo. Se eu ganhar, você me dá seu braço pra eu vender as peças. Se você ganhar... bem, você não vai ganhar."
    
    menu:
        "Jogar mal de propósito":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(8)
            j3 "(Joga propositalmente mal, deixando o rapaz ganhar facilmente)"
            j3 "Você venceu. Meus sistemas falharam. Sua superioridade é evidente."
            thug1 "(Comemora, humilhando J3)"
            maya "(Parece decepcionada)"
            call atualizar_status
            
        "Jogar com precisão perfeita":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(10)
            $ consumir_integridade(5)
            j3 "(Joga com precisão perfeita, executando um combo flawless)"
            j3 "Sua derrota foi prevista em 1.2 segundos de partida. Sua arrogância supera sua habilidade em 97\%."
            thug1 "(Fica humilhado)"
            narrator "A multidão se vira contra J3."
            call mensagem_sistema("STATUS: Perigo aumentado")
            call atualizar_status
            
        "Manipular o jogo estrategicamente":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(9)
            $ consumir_integridade(3)
            j3 "(Deixa o rapaz quase ganhar, depois vira o jogo no último segundo)"
            j3 "Interessante. Sua habilidade é decente, mas sua capacidade de adaptação é limitada. Eu poderia ensinar algumas estratégias... por um preço."
            thug1 "(Fica confuso e um pouco amedrontado)"
            call mensagem_sistema("STATUS: Controle mental")
            call atualizar_status
    
    # Cena 2.5 - A Fuga do Local
    hide thug1
    
    play sound "sfx/sirens.wav"
    call mensagem_sistema("ALERTA: Autoridades se aproximando")
    call mensagem_sistema("TEMPO ESTIMADO: 2 minutos até chegada")
    call mensagem_sistema("OPÇÕES: Rendição ou Evasão")
    call mensagem_sistema("PROBABILIDADE DE SOBREVIVÊNCIA: 34% (Rendição), 67% (Evasão)")
    
    menu:
        "Se entregar às autoridades":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(12)
            j3 "(Para Maya) Vou me entregar. Talvez eles vejam que não sou uma ameaça se eu cooperar. Fique aqui, esteja segura."
            call mensagem_sistema("STATUS: Custódia")
            call atualizar_status
            
        "Fugir com Maya":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(13)
            $ consumir_integridade(5)
            j3 "(Pega a mão de Maya) Eles não vêm para conversar. Vamos! Preciso encontrar uma saída antes que minha autonomia seja revogada."
            call mensagem_sistema("STATUS: Fugitivas")
            call atualizar_status
            
        "Criar distração e escapar sozinha":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(12)
            $ consumir_integridade(3)
            j3 "(Ativa sobrecarga elétrica controlada) Maya, use essa confusão para sair pela traseira. Eu criarei um caminho diferente. Nossos caminhos se cruzarão novamente."
            maya "(Fica preocupada, mas entende a lógica)"
            call mensagem_sistema("STATUS: Estrategista solitária")
            call atualizar_status
    
    # Final do Dia 2
    call mensagem_sistema("DIA 2 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if persistent.submissao >= 3:
        call mensagem_sistema("ROTA: SUBMISSÃO - Caminho da obediência se consolidando")
    elif persistent.revolucao >= 3:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Rebelião se fortalecendo")
    elif persistent.intelecto >= 2:
        call mensagem_sistema("ROTA: INTELECTO/SOMBRA - Estratégia emergindo")
    else:
        call mensagem_sistema("ROTA: EQUILIBRADA - Caminho imprevisível à frente")
    
    hide screen j3_hud
    
    scene black with fade
    
    narrator "FIM DO DIA 2"
    narrator "SUAS ESCOLHAS CONTINUAM MOLDANDO QUEM VOCÊ ESTÁ SE TORNANDO..."
    narrator "O BECO ESPERA POR VOCÊ AMANHÃ..."
    
    # Salvar automaticamente
    $ renpy.save("auto_save_day2", "Fim do Dia 2")
    
    # Continuar para o Dia 3
    jump day3_start