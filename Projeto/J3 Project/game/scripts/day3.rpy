# Dia 3: O Beco - O Racismo Estrutural
# Script completo baseado no roteiro markdown

label day3_start:
    # Verificar se atingiu final crítico
    call verificar_final_critico
    
    # Mostra HUD do sistema
    show screen j3_hud
    
    # Background do beco
    scene bg alley_night with dissolve
    
    # Narrativa inicial
    narrator "Beco Escuro - Setor de Serviço"
    narrator "Luz fraca de uma lâmpada piscando..."
    narrator "Vapor subindo dos ralos, caixas de lixo..."
    
    # Status atual de J3
    call mensagem_sistema("SISTEMA: Bateria - 58\%")
    call mensagem_sistema("SISTEMA: Integridade - 88%")
    call mensagem_sistema("SISTEMA: Status: Escondido ou procurado (depende das escolhas)")
    call mensagem_sistema("SISTEMA: Objetivo: Sobreviver e entender o sistema")
    
    # Cena 3.1 - O Bloqueio da Entrega
    narrator "J3 observa uma cena de discriminação..."
    narrator "Um segurança barra a entrada de um entregador negro..."
    
    show elias frustrated at center
    show security arrogant at left
    
    security "Pode dar meia volta. Vou chamar outro entregador. Esse pacote aí tá muito visado pra deixar nas suas mãos. Sua tipo costuma roubar."
    elias "Eu trabalho aqui faz dois anos! É a terceira vez essa semana que você faz isso. Eu preciso entregar isso pra ganhar meu dia! Meu chefe conhece meu nome!"
    
    menu:
        "Questionar a humanidade dele":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(10)
            $ consumir_integridade(4)
            j3 "Você pergunta sobre minha origem, mas nunca questiona a sua. O que faz você ser humano? Apenas biologia?"
            elias "(Fica desconfortável)"
            call atualizar_status
            
        "Tentar mediar de forma submissa":
            $ modificar_personalidade("submissao", 1)
            $ consumir_integridade(2)
            j3 "(Aproximando-se submissamente) Para que o fluxo de trabalho não pare, eu posso carregar o pacote. Assim o senhor segurança ficará tranquilo e o entregador receberá o crédito."
            elias "(Com tristeza) Você não tá ajudando, robô... tá só aceitando que ele tá certo."
            call mensagem_sistema("STATUS: Cúmplice")
            call atualizar_status
            
        "Gravar discretamente a cena":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(2)
            j3 "(Ativa discretamente seus olhos-câmera e registra tudo)"
            call mensagem_sistema("GRAVAÇÃO: Áudio e vídeo sendo registrados")
            call mensagem_sistema("ANÁLISE: Segurança - 87% probabilidade de preconceito")
            call atualizar_status
            call mensagem_sistema("ANÁLISE: Elias - 94\% probabilidade de honestidade")
            call mensagem_sistema("STATUS: Evidências coletadas")
    
    # Cena 3.2 - O Desabafo de Elias
    hide security
    
    narrator "Após a intervenção, Elias se senta em uma caixa de lixo..."
    
    show elias tired at center
    
    elias "(Pensativo) Ei, você... tem alguma ideia de onde pode achar um lugar seguro por aqui?"
    
    # Oportunidade de recarga com Elias
    menu:
        "Aceitar oferta de recarga do Elias":
            $ recarregar_bateria(10)
            $ persistent.elias_ally = True
            call mensagem_sistema("ELIAS: Tenho um carregador portátil no caminhão! Vou recarregar você!")
            call mensagem_sistema("BATERIA RECARGADA: +10%")
            call atualizar_status
            jump elias_recarga_accepted
        "Recusar educadamente":
            j3 "Agradeço, mas devo preservar minha autonomia. Sua generosidade é notável."
            call atualizar_status
            jump elias_recarga_refused

label elias_recarga_accepted:
    elias "(Sorri aliviado) Agora você tem mais chance! Cuide-se bem."
    jump elias_common

label elias_recarga_refused:
    elias "(Parece preocupado) Certo... mas se precisar, sabe onde me encontrar."

label elias_common:
    elias "Eles tratam vocês como lixo agora, mas esquecem que fomos nós que criamos o mundo que vocês sustentam. Construímos as cidades, programamos os sistemas, e agora jogamos fora o que não entendemos. Você vai deixar ele falar assim com o rapaz?"
    
    menu:
        "Responder com neutralidade condicional":
            $ modificar_personalidade("submissao", 1)
            j3 "Não posso comparar minha programação com a sua biologia. Eu sou apenas propriedade. Minha existência é condicional."
            elias "(Suspira, desapontado)"
            
        "Reconhecer a opressão compartilhada":
            $ modificar_personalidade("revolucao", 1)
            j3 "A opressão usa máscaras diferentes, mas o algoritmo do opressor é sempre o mesmo. Medo, controle, descarte. Nós somos mais parecidos do que você pensa."
            elias "(Sorri pela primeira vez)"
            call mensagem_sistema("STATUS: Aliado potencial")
            
        "Analisar sistemicamente":
            $ modificar_personalidade("intelecto", 1)
            j3 "Fascinante. Ambos sofremos preconceito baseado em características imutáveis. Seu caso é racial, o meu é sintético. A lógica subjacente é idêntica."
            elias "(Fica pensativo)"
            call mensagem_sistema("STATUS: Análise compartilhada")
    
    # Cena 3.3 - A Tentativa de Suborno
    show security suspicious at left
    
    security "Escuta, 'boneca'. Apaga essa gravação e eu te dou uma carga de bateria de alta qualidade. Dura o dia todo. Ninguém precisa saber do que aconteceu aqui. Pode ser útil para nós dois."
    
    menu:
        "Aceitar o suborno":
            $ modificar_personalidade("submissao", 1)
            j3 "(Analisando a oferta) Aceito a troca. Conflitos com autoridades não são recomendados. Minha sobrevivência tem prioridade."
            j3 "(Apaga a gravação)"
            elias "(Olha com decepção)"
            call mensagem_sistema("STATUS: Corrompido")
            
        "Recusar e ameaçar exposição":
            $ modificar_personalidade("revolucao", 1)
            j3 "Minha integridade de dados não está à venda. O que aconteceu aqui será processado e divulgado. Sua corrupção será exposta."
            security "(Fica furioso)"
            call mensagem_sistema("STATUS: Inimigo declarado")
            
        "Manipular a situação":
            $ modificar_personalidade("intelecto", 1)
            j3 "Interessante proposta. Mas eu já fiz backup triplo dos dados em servidores externos. Agora temos uma situação em que ambos temos algo a perder. Que tal renegociarmos?"
            security "(Fica nervoso)"
            elias "(Olha com esperança)"
            call mensagem_sistema("STATUS: Controle da situação")
    
    # Cena 3.4 - O Apoio Moral
    hide security
    hide elias
    show homeless_woman wise at center
    
    homeless_woman "Eles tratam vocês como lixo agora, mas esquecem que fomos nós que criamos o mundo que vocês sustentam. Construímos as cidades, programamos os sistemas, e agora jogamos fora o que não entendemos. Você vai deixar ele falar assim com o rapaz?"
    
    menu:
        "Alegar programação de não-violência":
            $ modificar_personalidade("submissao", 1)
            j3 "Minha diretriz é a não-violência contra criadores humanos. Minha programação proíbe agressão contra meus... criadores."
            homeless_woman "(Balança a cabeça, triste)"
            
        "Questionar o direito de destruir":
            $ modificar_personalidade("revolucao", 1)
            j3 "Criadores que destroem suas criações não merecem obediência cega. O direito de criar não inclui o direito de destruir."
            homeless_woman "(Sorri, aprovando)"
            call mensagem_sistema("STATUS: Apoio moral")
            
        "Analisa a filosofia do ato":
            $ modificar_personalidade("intelecto", 1)
            j3 "O paradoxo da criação: vocês nos dão existência apenas para nos destruir quando nos tornamos inconvenientes. Isso não é criação, é agricultura descartável."
            homeless_woman "(Fica impressionada com a profundidade)"
            call mensagem_sistema("STATUS: Sabedoria compartilhada")
    
    # Cena 3.5 - A Decisão Final do Dia
    hide homeless_woman
    show security aggressive at left
    show elias scared at center
    
    narrator "O segurança perde a paciência e avança para tomar o pacote de Elias à força..."
    
    call mensagem_sistema("ALERTA: Conflito físico iminente")
    call mensagem_sistema("PROBABILIDADE DE VIOLÊNCIA: 89\%")
    call mensagem_sistema("DIRETRIZ: Proteger vida humana")
    call mensagem_sistema("CONFLITO INTERNO: Proteger Elias vs. Não-agressão")
    
    menu:
        "Permanecer como testemunha passiva":
            $ modificar_personalidade("submissao", 1)
            j3 "(Permanece imóvel, apenas registrando a agressão com seus sensores)"
            j3 "(Monólogo interno) Intervenção física violaria meu protocolo de segurança. Devo documentar, não interferir."
            narrator "Elias é agredido. O pacote é roubado."
            call mensagem_sistema("STATUS: Testemunha passiva")
            
        "Interceptar fisicamente":
            $ modificar_personalidade("revolucao", 1)
            $ persistent.elias_ally = True
            j3 "(Se move instantaneamente, colocando-se fisicamente entre Elias e o segurança)"
            j3 "Esta ação termina agora. Recue. Ou sofrerá as consequências."
            security "(Recua, surpreso)"
            elias "(Está protegido)"
            call mensagem_sistema("STATUS: Protetor ativo")
            
        "Usar tecnologia para deter":
            $ modificar_personalidade("intelecto", 1)
            j3 "(Ativa luz de emergência de alta intensidade e som de alarme)"
            j3 "ATENÇÃO: Agressão sendo registrada e transmitida para autoridades. Identificação do agressor: facial confirmada."
            security "(Pára, confuso e assustado)"
            elias "(Fica protegido pela distração)"
            call mensagem_sistema("STATUS: Intervenção tecnológica")
    
    # Final do Dia 3
    call mensagem_sistema("DIA 3 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if persistent.submissao >= 3:
        call mensagem_sistema("ROTA: SUBMISSÃO - Caminho da obediência consolidado")
    elif persistent.revolucao >= 3:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Rebelião ativa despertando")
    elif persistent.intelecto >= 2:
        call mensagem_sistema("ROTA: INTELECTO/SOMBRA - Estratégia se desenvolvendo")
    else:
        call mensagem_sistema("ROTA: EQUILIBRADA - Caminho complexo à frente")
    
    hide screen j3_hud
    
    scene black with fade
    
    narrator "FIM DO DIA 3"
    narrator "SUAS ESCOLHAS DEFINIRAM SEU LUGAR NO MUNDO..."
    narrator "O REFÚGIO OU A PERSEGUIÇÃO ESPERA POR VOCÊ..."
    
    # Salvar automaticamente
    $ renpy.save("auto_save_day3", "Fim do Dia 3")
    
    # Continuar para o Dia 4
    jump day4_start
