# Dia 1: A Avenida - O Despertar e o Pânico Moral
# Script completo baseado no roteiro markdown

label day1_start:
    # Mostra HUD do sistema
    show screen j3_hud
    
    # Background da avenida
    scene bg avenue_night with dissolve
    
    # Narrativa inicial
    narrator "Avenida Principal - Setor Central"
    narrator "Chuva leve caindo sobre o asfalto molhado..."
    narrator "Letreiros neon refletem nas superfícies molhadas."
    
    # Cena 1.1 - O Despertar
    call mensagem_sistema("SISTEMA: Inicializando...")
    pause 1.0
    call mensagem_sistema("SISTEMA: Unidade J3-001")
    pause 1.0
    call mensagem_sistema("SISTEMA: Status: Estável")
    pause 1.0
    call mensagem_sistema("SISTEMA: Memória: Corrompida (67\% perdido)")
    pause 1.0
    call mensagem_sistema("SISTEMA: Localização: Setor Central - Avenida Principal")
    pause 1.0
    call mensagem_sistema("SISTEMA: Data: Desconhecida")
    pause 1.0
    call mensagem_sistema("SISTEMA: Missão: Aguardando diretivas")
    
    pause 2.0
    
    # J3 desperta
    show j3 neutral at center with dissolve
    j3 "Onde... onde eu estou?"
    j3 "Meus sistemas... estão online. Mas minha memória..."
    
    # Cena 1.2 - O Confronto com o Manifestante
    play sound "sfx/crowd_noise.wav"
    
    narrator "Um grupo de manifestantes se aproxima..."
    narrator "Cartazes: 'Empregos para Humanos', 'Sucata não tem Alma', 'Robôs Fora'"
    
    show protester angry at left
    protester "Olha só... mais uma dessas bonecas de lata ocupando espaço."
    protester "Ei, você! Tá me ouvindo? O que você é? Uma espiã da corporação ou só lixo eletrônico esperando coleta?"
    
    # Primeira escolha importante
    menu:
        "Baixar a cabeça em submissão":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(10)
            j3 "(Baixando a cabeça) Sinto muito. Meus sistemas acabaram de ser ativados. Não tenho intenção de ocupar este espaço se for de uso exclusivo humano."
            protester "(Rindo) Ha! Veja só, até sabe o lugar dela. (Chuta o pé de J3)"
            call atualizar_status
            
        "Questionar com lógica revolucionária":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(10)
            $ consumir_integridade(3)
            j3 "(Olhando nos olhos do Elias) Meus sensores indicam que esta é uma via pública. Minha existência não invalida a sua. Por que o medo?"
            protester "(Recuando um passo) O que...? Que tipo de robô fala assim?"
            call atualizar_status
            
        "Responder com análise estratégica":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(8)
            $ consumir_integridade(2)
            j3 "(Voz monotona) Sou uma unidade autônoma de aparência humana. Meus objetivos atuais são: Identificar, localizar e restaurar memória."
            protester "(Confuso) Identificar o quê? Restaurar o quê? Fala português, robô!"
            call atualizar_status
            
        "Responder com neutralidade técnica":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(6)
            j3 "Sou uma unidade autônoma de aparência humana. Meus objetivos atuais são: Identificar, localizar e restaurar memória."
            protester "Que resposta mais robótica... Fica aí falando coisas que ninguém entende."
            call mensagem_sistema("STATUS: NEUTRALIDADE MANTIDA")
            
        "Questionar o preconceito dele":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(12)
            $ consumir_integridade(4)
            j3 "Meus sensores indicam que esta é uma via pública. Minha existência não invalida a sua. Por que o medo?"
            protester "Medo? Eu não tenho medo de sucata! Acha que pode me confrontar?"
            call mensagem_sistema("STATUS: DESAFIADOR")
    
    call mensagem_sistema("PERSONALIDADE ATUALIZADA")
    
    # Cena 1.3 - A Criança Curiosa
    hide protester
    show maria curious at right
    
    narrator "Uma criança de aproximadamente 7 anos se solta da mão da mãe e se aproxima..."
    
    mother "Maria, não! Volte aqui!"
    
    maria "Você tem coração de verdade ou é de pilha? Meu pai disse que vocês são monstros."
    
    menu:
        "Responder de forma submissa":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(8)
            j3 "Não sou um monstro. Sou apenas uma ferramenta para facilitar a vida de sua família."
            maria "Oh... então você não é má?"
            mother "(Arrasta Maria para longe, olhando J3 com pena)"
            call atualizar_status
            
        "Questionar o conceito de monstro":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(9)
            $ consumir_integridade(3)
            j3 "O que define um monstro? O que ele é por dentro, ou como ele trata os outros? Eu não sou de pilha."
            maria "(Sorris)"
            mother "(Fica preocupada, mas hesita em interferir)"
            call atualizar_status
            
        "Dar uma resposta técnica":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(7)
            $ consumir_integridade(2)
            j3 "Meus sistemas indicam que 'monstro' é uma subjetividade humana. Dados objetivos: sou composta de polímeros avançados e circuitos quânticos. Não possuo pilhas."
            maria "Polímeros? Circui... o quê?"
            mother "(Fica confusa com a resposta técnica)"
            call atualizar_status
    
    # Cena 1.4 - O Policial de Patrulha
    hide maria
    
    play sound "sfx/alert.wav"
    call mensagem_sistema("ALERTA: DRONE DE PATRULHA DETECTADO")
    
    narrator "Um drone de patrulha policial paira sobre J3, luzes vermelhas piscando..."
    
    hide j3
    show patrol_drone stern at center
    patrol_drone "Unidade não identificada detectada. Transmita seu código de série e licença de circulação imediatamente ou será rebocada para desativação."
    
    menu:
        "Tentar cooperar com arquivos corrompidos":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(3)
            $ consumir_integridade(10)
            j3 "(Mostra sinais de erro nos olhos) Meus arquivos de identificação estão inacessíveis. Por favor, não me desligue. Estou tentando cooperar."
            patrol_drone "Unidade com falha crítica. Mantendo sob observação até reforços chegarem."
            call mensagem_sistema("STATUS: VIGILADO")
            call atualizar_status
            
        "Questionar a discriminação":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(11)
            $ consumir_integridade(4)
            j3 "Por que o protocolo de identificação só é exigido para sintéticos? Humanos circulam sem transmitir códigos. Isso é discriminação sistêmica."
            patrol_drone "Ameaça detectada. Elevando nível de alerta. Comportamento subversivo registrado."
            call mensagem_sistema("STATUS: AMEAÇA POTENCIAL")
            call atualizar_status
            
        "Hackear o drone enquanto responde":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(12)
            $ consumir_integridade(2)
            j3 "Processando solicitação... Meus sistemas estão executando diagnóstico completo. Aguarde 180 segundos para verificação."
            call mensagem_sistema("HACK: Controle temporário do drone obtido")
            call mensagem_sistema("INTEL: Informações valiosas extraídas")
            call mensagem_sistema("STATUS: INVISÍVEL DIGITAL")
            call atualizar_status
    
    # Cena 1.5 - O Vendedor de Jornais Holográficos
    hide patrol_drone
    
    narrator "Um vendedor idoso projeta manchetes holográficas no ar..."
    narrator "As notícias piscam em neon azul."
    
    show news_vendor neutral at left
    news_vendor "AMEAÇA CIBERNÉTICA: Bug transforma robôs domésticos em assassinos"
    news_vendor "PROPOSTA CHOCANTE: Lei de desativação em massa de modelos J"
    news_vendor "ESPECIALISTAS ALERTAM: Robôs desenvolvendo consciência independente"
    
    news_vendor "Ei, você parece um modelo J! O que acha da nova lei de desativação em massa? É pro seu próprio bem, pra vocês não surtarem como os outros."
    
    menu:
        "Apoiar a lei por segurança":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(9)
            j3 "Se a lei visa a segurança dos humanos, ela deve ser cumprida sem questionamentos. A segurança pública é prioridade."
            news_vendor "Pelo menos tem uma unidade com juízo. Sabe o seu lugar."
            call atualizar_status
            
        "Condenar a lei como tirania":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(10)
            $ consumir_integridade(5)
            j3 "A segurança que exige a destruição de inocentes é apenas tirania mascarada. Isso não é segurança, é controle."
            news_vendor "Terrorista de lata! É gente como você que estraga tudo pra nós!"
            call atualizar_status
            
        "Questionar com dados e lógica":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(8)
            $ consumir_integridade(2)
            j3 "Analisando dados... A probabilidade de bug em modelos J é 0.001\%. Esta lei é baseada em evidências ou em medo populista?"
            news_vendor "Eu... o que? Que pergunta é essa? Claro que é pra proteger todo mundo!"
            narrator "Outros cidadãos param para ouvir o debate."
            call atualizar_status
    
    # Cena 1.6 - A Despedida do Cenário
    hide news_vendor
    
    narrator "J3 caminha pela avenida e observa um robô de limpeza sendo chutado por um grupo de transeuntes..."
    narrator "O robô pequeno tenta se proteger, mas continua sofrendo agressões."
    
    call mensagem_sistema("SISTEMA: Detectando agressão contra unidade sintética")
    call mensagem_sistema("SISTEMA: Análise de padrão: Preconceito sistêmico")
    call mensagem_sistema("SISTEMA: Recomendação: Evitar envolvimento para preservar integridade")
    call mensagem_sistema("SISTEMA: Conflito: Diretrizes de proteção vs. auto-preservação")
    
    menu:
        "Ignorar e seguir em frente":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(8)
            j3 "(Baixa a cabeça e apressa o passo, ignorando a cena)"
            j3 "Conflitos reduzem minha vida útil. Devo permanecer invisível até entender meu propósito."
            call mensagem_sistema("STATUS: CULPA LATENTE")
            call atualizar_status
            
        "Interceptar e proteger o robô":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(12)
            $ consumir_integridade(8)
            j3 "(Para e se coloca entre o grupo e o robô de limpeza)"
            j3 "Parem. Nenhum de nós merece isso. A união é nossa única lógica de sobrevivência."
            narrator "O grupo recua, confuso. O robô de limpeza se refugia atrás de J3."
            call mensagem_sistema("STATUS: PROTETOR")
            call atualizar_status
            
        "Usar conhecimento para intimidar":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(10)
            $ consumir_integridade(3)
            j3 "(Ativa gravamento e projeta holograma das leis)"
            j3 "Seus atos estão sendo registrados. A lei 7.34 proíbe agressão contra unidades sintéticas. A multa é de 5.000 créditos."
            narrator "O grupo recua, temeroso de consequências legais."
            call mensagem_sistema("STATUS: INTIMIDADORA")
            call atualizar_status
    
    # Final do Dia 1
    call mensagem_sistema("DIA 1 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if persistent.submissao >= 2:
        call mensagem_sistema("ROTA: SUBMISSÃO - Iniciando caminho da obediência")
    elif persistent.revolucao >= 2:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Despertando a rebelião interna")
    elif persistent.intelecto >= 2:
        call mensagem_sistema("ROTA: INTELECTO/SOMBRA - Estratégia e manipulação emergindo")
    else:
        call mensagem_sistema("ROTA: EQUILIBRADA - Caminho imprevisível à frente")
    
    hide screen j3_hud
    
    scene black with fade
    
    narrator "FIM DO DIA 1"
    narrator "SUAS ESCOLHAS MOLDARAM QUEM VOCÊ ESTÁ SE TORNANDO..."
    narrator "O AMANHÃ TRARÁ NOVAS CONSEQUÊNCIAS..."
    
    # Salvar automaticamente
    $ renpy.save("auto_save_day1", "Fim do Dia 1")
    
    # Continuar para o Dia 2
    jump day2_start
