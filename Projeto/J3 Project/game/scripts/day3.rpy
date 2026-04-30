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
    call mensagem_sistema("SISTEMA: Integridade - 88\%")
    call mensagem_sistema("SISTEMA: Status: Escondido ou procurado (depende das escolhas)")
    call mensagem_sistema("SISTEMA: Objetivo: Sobreviver e entender o sistema")
    
    # Cena 3.1 - O Bloqueio da Entrega
    narrator "J3 observa uma cena de discriminação..."
    narrator "Um segurança barra a entrada de um entregador negro..."
    
    show elias frustrated at center
    show security arrogant at left
    
    security "(Sem tirar os olhos do tablet) Dá meia-volta, parceiro. Vou chamar outro entregador. Esse pacote aí é caro demais pra ficar na tua mão."
    security "(Sorriso pequeno, ensaiado) Seu tipo costuma esquecer onde deixou."
    elias "(Voz cansada, tentando não levantar o tom) Eu trabalho aqui há dois anos. É a terceira vez essa semana que você faz isso comigo."
    elias "Eu preciso entregar pra fechar o dia. Meu chefe sabe meu nome. Você sabe meu nome."
    
    menu:
        "{i}Segurança bloqueia entregador negro por preconceito racial. J3 observa em silêncio.{/i}"

        "[custo(5)]{i}(O espelho do preconceito — devolver a pergunta.){/i} Questionar a humanidade do segurança":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            j3 "Você pergunta sobre minha origem, mas nunca questiona a sua. O que faz você ser humano? Apenas biologia?"
            elias "(Fica desconfortável)"
            call atualizar_status

        "[custo(2)]{i}(Carregar o pacote dissolve o conflito. Ignoro a injustiça.){/i} Oferecer-se para fazer a entrega":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            j3 "(Aproximando-se submissamente) Para que o fluxo de trabalho não pare, eu posso carregar o pacote. Assim o senhor segurança ficará tranquilo e o entregador receberá o crédito."
            elias "(Com tristeza) Você não tá ajudando, robô... tá só aceitando que ele tá certo."
            call mensagem_sistema("STATUS: Cúmplice")
            call atualizar_status

        "[custo(3)]{i}(Evidência é munição futura. Coletar silencioso.){/i} Gravar discretamente a cena":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(3)
            j3 "(Ativa discretamente seus olhos-câmera e registra tudo)"
            call mensagem_sistema("GRAVAÇÃO: Áudio e vídeo sendo registrados")
            call mensagem_sistema("ANÁLISE: Segurança - 87\% probabilidade de preconceito")
            call atualizar_status
            call mensagem_sistema("ANÁLISE: Elias - 94\% probabilidade de honestidade")
            call mensagem_sistema("STATUS: Evidências coletadas")
    
    # Cena 3.2 - O Desabafo de Elias
    hide security
    
    narrator "Após a intervenção, Elias se senta em uma caixa de lixo..."
    
    show elias tired at center
    
    elias "(Esfrega o rosto com a mão. Voz baixa, cansada) Ei, você... aqui na zona, tem algum buraco que dê pra dormir sem ser revistado?"
    elias "Pergunto porque hoje eu também não tenho casa pra voltar."
    
    # Oportunidade de recarga com Elias
    menu:
        "{i}Elias oferece carregador portátil. Energia custa vínculo humano.{/i}"

        "[ganho(10)]{i}(Aliança com humano vale risco futuro. Recarregar agora.){/i} Aceitar recarga do Elias":
            $ recarregar_bateria(10)
            $ elias_ally = True
            call mensagem_sistema("ELIAS: Tenho um carregador portátil no caminhão! Vou recarregar você!")
            call mensagem_sistema("BATERIA RECARREGADA: +10\%")
            call atualizar_status
            jump elias_recarga_accepted

        "{i}(Depender dele cria dívida. Preservar autonomia.){/i} Recusar educadamente":
            j3 "Agradeço, mas devo preservar minha autonomia. Sua generosidade é notável."
            call atualizar_status
            jump elias_recarga_refused

label elias_recarga_accepted:
    elias "(Conecta o cabo no pulso de J3 com o cuidado de quem já consertou muita coisa pequena.) Pronto. Não é muito, mas é o que dá. Cuida disso aí, viu."
    jump elias_common

label elias_recarga_refused:
    elias "(Encolhe os ombros, sem ressentimento.) Tá bom. Mas se mudar de ideia, eu tô por aqui. Caminhão azul-escuro, placa rasgada do lado direito."

label elias_common:
    elias "(Olha para o chão. Voz baixa, sem rancor — só constatação.) Sabe o que mais me cansa? É que eles tratam vocês como lixo agora. Mas esquecem que fomos nós que construímos o mundo que vocês sustentam."
    elias "Levantamos cidade. Programamos sistema. E agora jogam fora o que não entendem."
    elias "(Ergue os olhos para J3, direto) Vocês estão descobrindo na pele o que a gente já sabia. E você... vai deixar ele falar assim com o rapaz aqui de novo?"
    
    menu:
        "{i}Elias convoca J3 a reconhecer opressão compartilhada entre humanos e sintéticos.{/i}"

        "[custo(1)]{i}(Não posso me igualar. Sou propriedade, não gente.){/i} Responder com neutralidade condicional":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(1)
            j3 "Não posso comparar minha programação com a sua biologia. Eu sou apenas propriedade. Minha existência é condicional."
            elias "(Suspira, desapontado)"
            call atualizar_status

        "[custo(2)]{i}(Opressor usa sempre o mesmo algoritmo. Nós também.){/i} Reconhecer a opressão compartilhada":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(2)
            j3 "A opressão usa máscaras diferentes, mas o algoritmo do opressor é sempre o mesmo. Medo, controle, descarte. Nós somos mais parecidos do que você pensa."
            elias "(Sorri pela primeira vez)"
            call mensagem_sistema("STATUS: Aliado potencial")
            call atualizar_status

        "[custo(2)]{i}(Paralelo sistêmico — traços imutáveis, mesma lógica.){/i} Analisar o paralelo sistemicamente":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(2)
            j3 "Fascinante. Ambos sofremos preconceito baseado em características imutáveis. Seu caso é racial, o meu é sintético. A lógica subjacente é idêntica."
            elias "(Fica pensativo)"
            call mensagem_sistema("STATUS: Análise compartilhada")
            call atualizar_status
    
    # Cena 3.3 - A Tentativa de Suborno
    show security suspicious at left
    
    security "(Volta. Voz mais baixa agora — agora ele negocia) Escuta, boneca."
    security "Apaga essa gravação e eu te arrumo uma carga de bateria premium. Daquelas que dura o dia inteiro. Ninguém precisa saber do que aconteceu aqui."
    security "(Sorri sem chegar nos olhos) Pode ser útil pra nós dois, né?"
    
    menu:
        "{i}Segurança oferece carga de bateria premium em troca de apagar gravação. Suborno direto.{/i}"

        "[custo(2)]{i}(Bateria agora vale mais que verdade depois.){/i} Aceitar o suborno":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            j3 "(Analisando a oferta) Aceito a troca. Conflitos com autoridades não são recomendados. Minha sobrevivência tem prioridade."
            j3 "(Apaga a gravação)"
            elias "(Olha com decepção)"
            call mensagem_sistema("STATUS: Corrompido")
            call atualizar_status

        "[custo(2)]{i}(Dados não são mercadoria. Expor isto.){/i} Recusar e ameaçar exposição":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(2)
            j3 "Minha integridade de dados não está à venda. O que aconteceu aqui será processado e divulgado. Sua corrupção será exposta."
            security "(Fica furioso)"
            call mensagem_sistema("STATUS: Inimigo declarado")
            call atualizar_status

        "[custo(2)]{i}(Backup externo = alavanca. Virar a mesa.){/i} Manipular a situação com blefe":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(2)
            j3 "Interessante proposta. Mas eu já fiz backup triplo dos dados em servidores externos. Agora temos uma situação em que ambos temos algo a perder. Que tal renegociarmos?"
            security "(Fica nervoso)"
            elias "(Olha com esperança)"
            call mensagem_sistema("STATUS: Controle da situação")
            call atualizar_status
    
    # Cena 3.4 - O Apoio Moral
    hide security
    hide elias
    show homeless_woman wise at center
    
    homeless_woman "(Voz arrastada de quem fala devagar porque já gritou demais na vida) Eu conheço bem esse desabafo, mocinha. Conheço de cor."
    homeless_woman "Fomos descartados quando paramos de servir. Dormimos em ruas que a gente mesmo levantou. Faz tempo."
    homeless_woman "(Aponta com o queixo para o segurança) Vocês, robôs, estão descobrindo na pele o que a gente sabe há gerações."
    homeless_woman "(Olhos diretos em J3) Mas saber não basta. Vai ficar parada enquanto ele agride o rapaz?"
    
    menu:
        "{i}Mulher sem-teto desafia J3: vai deixar humano agredir outro humano?{/i}"

        "[custo(1)]{i}(Diretiva proíbe agressão contra criadores. Não posso.){/i} Alegar programação de não-violência":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(1)
            j3 "Minha diretriz é a não-violência contra criadores humanos. Minha programação proíbe agressão contra meus... criadores."
            homeless_woman "(Balança a cabeça, triste)"
            call atualizar_status

        "[custo(2)]{i}(Quem destrói não merece obediência. Direito não é licença.){/i} Questionar o direito de destruir":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(2)
            j3 "Criadores que destroem suas criações não merecem obediência cega. O direito de criar não inclui o direito de destruir."
            homeless_woman "(Sorri, aprovando)"
            call mensagem_sistema("STATUS: Apoio moral")
            call atualizar_status

        "[custo(2)]{i}(Paradoxo da criação descartável — nomear o padrão.){/i} Analisar a filosofia do ato":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(2)
            j3 "O paradoxo da criação: vocês nos dão existência apenas para nos destruir quando nos tornamos inconvenientes. Isso não é criação, é agricultura descartável."
            homeless_woman "(Fica impressionada com a profundidade)"
            call mensagem_sistema("STATUS: Sabedoria compartilhada")
            call atualizar_status
    
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
        "{i}Segurança avança para agredir Elias. Intervenção requer corpo ou tecnologia.{/i}"

        "[custo(1)]{i}(Protocolo me proíbe. Documentar sem interferir.){/i} Permanecer como testemunha passiva":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(1)
            j3 "(Permanece imóvel, apenas registrando a agressão com seus sensores)"
            j3 "(Monólogo interno) Intervenção física violaria meu protocolo de segurança. Devo documentar, não interferir."
            narrator "Elias é agredido. O pacote é roubado."
            call mensagem_sistema("STATUS: Testemunha passiva")

        "[custo(5, 22)]{i}(Corpo entre ele e Elias. Absorver o que vier.){/i} Interceptar fisicamente o ataque":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            $ consumir_integridade(22)
            $ elias_ally = True
            j3 "(Se move instantaneamente, colocando-se fisicamente entre Elias e o segurança)"
            j3 "Esta ação termina agora. Recue. Ou sofrerá as consequências."
            security "(Recua, surpreso)"
            elias "(Está protegido)"
            call mensagem_sistema("STATUS: Protetor ativo")

        "[custo(9)]{i}(Luz e alarme — parar sem tocar.){/i} Ativar alarme e luz de emergência":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(9)
            j3 "(Ativa luz de emergência de alta intensidade e som de alarme)"
            j3 "ATENÇÃO: Agressão sendo registrada e transmitida para autoridades. Identificação do agressor: facial confirmada."
            security "(Para, confuso e assustado)"
            elias "(Fica protegido pela distração)"
            call mensagem_sistema("STATUS: Intervenção tecnológica")
    
    # Final do Dia 3
    call mensagem_sistema("DIA 3 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if submissao >= 3:
        call mensagem_sistema("ROTA: SUBMISSÃO - Caminho da obediência consolidado")
    elif revolucao >= 3:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Rebelião ativa despertando")
    elif intelecto >= 2:
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
