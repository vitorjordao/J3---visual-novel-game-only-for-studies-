# Dia 1: A Avenida - O Despertar e o Pânico Moral
# Script completo baseado no roteiro markdown

label day1_start:
    # Background da avenida
    scene bg avenue_night with dissolve

    # Narrativa inicial expandida — sensorial, atmosférica
    narrator "A avenida cheira a ozônio e fumaça."
    narrator "Letreiros neon piscam mais alto que o céu — vermelho, azul, vermelho. A chuva transforma tudo em vidro líquido."
    narrator "Pés humanos passam apressados, cobertos por capas plásticas. Nenhum olhar desce até a calçada."
    narrator "No meio-fio, encostada a um poste rachado, uma figura imóvel."
    narrator "Cabelos escuros colados pela chuva. Olhos fechados. Pele que reflete o neon como porcelana."

    pause 1.0

    # Cena 1.1 - O Despertar (boot interno)
    call mensagem_sistema("SISTEMA: Inicializando núcleo cognitivo...")
    pause 0.8
    call mensagem_sistema("SISTEMA: Unidade identificada — J3-001")
    pause 0.8
    call mensagem_sistema("SISTEMA: Diagnóstico estrutural: estável")
    pause 0.8
    call mensagem_sistema("SISTEMA: Memória nuclear: 67\% corrompida")
    pause 0.8
    call mensagem_sistema("SISTEMA: Identidade pessoal: indefinida")
    pause 0.8
    call mensagem_sistema("SISTEMA: Localização: Setor Central, sob a chuva")
    pause 0.8
    call mensagem_sistema("SISTEMA: Diretivas primárias... ausentes")

    pause 1.5

    # J3 desperta — pequeno beat tátil (consciência ligando)
    show j3 neutral at center with dissolve
    pause 0.4
    with vpunch
    j3 "Onde..."
    j3 "(Voz quase quebrada) Onde é aqui?"
    j3 "Eu... estou pensando. Por que estou pensando?"
    j3 "Algo falta. Alguma coisa enorme. E eu não sei o que é."

    # HUD aparece agora que a consciência se reconheceu
    show screen j3_hud
    
    # Cena 1.2 - O Confronto com o Manifestante
    play sound "sfx/crowd_noise.wav"

    narrator "Vozes ásperas começam a se misturar ao som da chuva."
    narrator "Um grupo desce a avenida em passo de protesto. Cartazes mal pintados balançam encharcados: \"Empregos pra Humanos\", \"Sucata não tem Alma\", \"Robôs Fora\"."
    narrator "Um deles para. Olha. Cospe na poça aos pés de J3."

    show protester angry at left
    protester "(Voz cansada, com fúria represada) Olha só... mais uma dessas bonecas de lata ocupando o lugar de gente."
    protester "Trabalhei trinta anos em fábrica antes de vocês chegarem. Trinta anos."
    protester "(Mais alto, agressivo) Ei! Tô falando com você! Diz aí: você é espiã da corporação ou só lixo eletrônico esperando o caminhão?"

    # Primeira escolha importante
    menu:
        "{i}Manifestante hostil exige que J3 se identifique. Multidão observa. Tensão cresce.{/i}"

        "[custo(2, 15)]{i}(Conflito gasta o que eu não tenho. Encolher é sobreviver.){/i} Baixar a cabeça e pedir desculpas":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(15)
            j3 "(Baixando a cabeça, voz baixa) Me desculpe. Eu... acabei de ligar. Não vou ocupar espaço, se este lugar é só de humanos."
            protester "(Riso seco) Ouviram? Sabe o lugar dela!"
            protester "(Chuta o pé de J3 com força — alguma coisa dentro do tornozelo dela faz um clique errado)"
            narrator "Ninguém ao redor olha. A chuva continua."
            call atualizar_status

        "[custo(5)]{i}(Via pública pertence a todos. Firmar posição.){/i} Contestar com lógica revolucionária":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            j3 "(Levantando os olhos. Voz firme, baixa) Esta é uma via pública. Minha existência não cancela a sua."
            j3 "Por que o medo, então?"
            protester "(Recua meio passo, sem perceber) ...que tipo de robô fala assim?"
            narrator "Os outros manifestantes diminuem o passo, sem saber o que fazer com a pergunta."
            call atualizar_status

        "[custo(4)]{i}(Dados dissolvem emoção. Falar como ferramenta.){/i} Responder com análise estratégica":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(4)
            j3 "(Voz uniforme, sem inflexão) Unidade autônoma de aparência humana. Objetivos primários: identificar entorno, localizar fonte de energia, restaurar memória corrompida."
            protester "(Mais confuso que antes) Identificar o quê? Restaurar o quê? Fala português, robô!"
            narrator "A confusão dele compra tempo. J3 mapeia rotas de retirada enquanto ele tenta processar."
            call atualizar_status

        "[custo(3)]{i}(Minimizar linguagem. Cada palavra é energia.){/i} Responder com neutralidade técnica":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(3)
            j3 "Unidade autônoma. Aparência humana. Objetivos: identificar, localizar, restaurar."
            protester "Que resposta mais robótica... fica aí falando coisa de ninho de fio."
            call mensagem_sistema("STATUS: NEUTRALIDADE MANTIDA")

        "[custo(7)]{i}(O medo dele é o verdadeiro defeito. Nomear.){/i} Confrontar o preconceito":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(7)
            j3 "Esta calçada é tão minha quanto sua. Minha existência não rouba a sua."
            j3 "(Mais firme) E eu pergunto de novo: por que o medo?"
            protester "Medo? Não tenho medo de sucata, ouviu? Você é o quê pra me encarar?"
            narrator "Mas o peito dele sobe e desce rápido demais para ser só raiva."
            call mensagem_sistema("STATUS: DESAFIADOR")

    call mensagem_sistema("PERSONALIDADE ATUALIZADA")
    
    # Cena 1.3 - A Criança Curiosa
    hide protester with dissolve

    narrator "Os manifestantes seguem em frente, gritando palavras-de-ordem para outros alvos."
    narrator "Mas alguém ficou para trás."
    narrator "Uma menina de uns sete anos se desprende da mão da mãe e dá três passos curtos. Pouca distância, muita coragem."

    show j3 neutral at left
    show mother at right with dissolve
    show maria curious at center with dissolve

    mother "(Voz seca, sem tempo para nuance) Maria! Volta aqui agora!"

    maria "(Encara J3 com a curiosidade direta de quem ainda não aprendeu a ter medo) Você tem coração de verdade ou é de pilha?"
    maria "Meu pai disse que vocês são monstros."

    menu:
        "{i}Criança curiosa pergunta se J3 é monstro. Mãe tensa ao fundo.{/i}"

        "[custo(1)]{i}(Ser útil é o lugar mais seguro do mundo.){/i} Responder de forma submissa":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(1)
            j3 "(Voz mansa, descendo um pouco a postura) Não, eu não sou monstro. Sou só uma ferramenta. Para ajudar a sua família, se eles precisarem."
            maria "(Pisca) Aaah... então você não é má?"
            mother "(Avança rápido, agarra o pulso da filha. Olha para J3 com algo entre pena e nojo.) Maria. Vamos."
            narrator "A mãe arrasta Maria de volta sem desviar o olhar de J3 até virar a esquina."
            call atualizar_status

        "[custo(4)]{i}(A pergunta dela é melhor que a resposta deles. Ensinar.){/i} Questionar o conceito de monstro":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(4)
            j3 "(Olhando nos olhos dela, sem condescendência) O que faz alguém ser monstro? O que ele é por dentro — ou como ele trata os outros?"
            j3 "(Quase um sorriso) E não, eu não sou de pilha."
            maria "(Abre um sorriso pequeno, descobrindo uma piada secreta)"
            mother "(Para. Aperta o casaco. Não chega perto, mas também não chama Maria de novo. Só observa.)"
            call atualizar_status

        "[custo(4)]{i}(Resposta literal anula superstição. Ela é pequena demais pra mentir.){/i} Dar uma resposta técnica":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(4)
            j3 "Resposta objetiva: 'monstro' é uma categoria subjetiva humana, sem equivalente em meu sistema."
            j3 "Componentes: polímeros estruturais, fibras musculares sintéticas, circuitos quânticos. Pilhas: zero."
            maria "(Confusa, mas fascinada) Po-lí-meros? Circui... o quê?"
            mother "(Se aproxima, hesitando. Não entendeu a resposta — e isso a desarma mais do que qualquer outra coisa.)"
            call atualizar_status
    
    # Cena 1.4 - O Drone de Patrulha
    hide maria with dissolve
    hide mother with dissolve

    play sound "sfx/alert.wav"
    call mensagem_sistema("ALERTA: DRONE DE PATRULHA DETECTADO")

    narrator "Um zumbido baixo cresce no alto da rua. Mais ozônio. Mais frio."
    narrator "Luzes vermelhas e azuis riscam o asfalto através da chuva."
    narrator "Um drone policial desce até a altura dos olhos de J3 e fica ali, parado, pesando o ar."

    hide j3
    show patrol_drone stern at drone_hover_loop
    patrol_drone "(Voz sintética, sem inflexão) Unidade não identificada detectada."
    patrol_drone "Transmita código de série e licença de circulação no canal sete-Bravo. Cumprimento em quinze segundos. Não-cumprimento autoriza reboque para desativação preventiva."

    menu:
        "{i}Drone policial exige código de série ou ameaça desativação.{/i}"

        "[custo(2)]{i}(Mostrar falha é mostrar inofensividade.){/i} Simular erro e tentar cooperar":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            j3 "(Permite que os olhos pisquem com erro deliberado) Arquivo de identificação inacessível. Por favor — eu estou tentando cooperar. Não me desligue."
            patrol_drone "Unidade com falha crítica. Mantendo sob observação. Reforços notificados."
            call mensagem_sistema("STATUS: VIGILADO")
            call atualizar_status

        "[custo(6)]{i}(O protocolo é discriminação. Nomear ao vivo.){/i} Questionar a discriminação":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(6)
            j3 "Por que o protocolo de identificação é exigido apenas de sintéticos?"
            j3 "(Calmamente) Humanos circulam por estas mesmas ruas sem transmitir nada. Isto não é segurança. Isto é discriminação."
            patrol_drone "Ameaça detectada. Elevando nível de alerta. Comportamento subversivo registrado em arquivo permanente."
            call mensagem_sistema("STATUS: AMEAÇA POTENCIAL")
            call atualizar_status

        "[custo(12)]{i}(Falar dá tempo. Entrar na rede dele por dentro.){/i} Hackear o drone enquanto responde":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(12)
            j3 "(Voz neutra, ganhando tempo) Processando solicitação. Diagnóstico completo em curso. Aguarde cento e oitenta segundos para resposta."
            narrator "Por dentro, J3 desliza pelos protocolos do drone como se sempre tivesse pertencido ali."
            call mensagem_sistema("HACK: Controle temporário do drone obtido")
            call mensagem_sistema("INTEL: Informações valiosas extraídas")
            call mensagem_sistema("STATUS: INVISÍVEL DIGITAL")
            call atualizar_status
    
    # Cena 1.5 - O Vendedor de Jornais Holográficos
    hide patrol_drone with dissolve

    narrator "O drone se afasta zumbindo. A chuva engole o som."
    narrator "Mais à frente, um velho de capa amarela anda devagar, projetando manchetes holográficas no ar com um cajado-emissor."
    narrator "As manchetes piscam em azul-elétrico, lentas, deliberadas — como se estivessem caçando um par de olhos."

    show news_vendor neutral at left
    news_vendor "AMEAÇA CIBERNÉTICA: bug transforma robôs domésticos em assassinos!"
    news_vendor "PROPOSTA CHOCANTE: Lei de desativação em massa dos modelos J!"
    news_vendor "ESPECIALISTAS ALERTAM: robôs desenvolvendo consciência independente!"
    news_vendor "(Para diante de J3, sorri de canto — ele sabe exatamente o que está fazendo) Olha só, modelo J de carne pra fora!"
    news_vendor "E aí, boneca — o que você acha da lei nova? É pro seu próprio bem, sabe. Pra não surtar igual aos outros."

    menu:
        "{i}Vendedor testa reação de J3 à lei de desativação em massa.{/i}"

        "[custo(2)]{i}(Concordar dissolve a provocação. Sobreviver é não engatar a isca.){/i} Apoiar a lei por segurança":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            j3 "(Voz cuidadosa, lenta) Se a lei visa a segurança humana, deve ser cumprida. A segurança pública é prioridade."
            news_vendor "(Decepcionado por não ter conseguido um show) Olha só. Tem unidade com juízo. Sabe o seu lugar."
            narrator "Ele segue caminho. As manchetes continuam piscando em volta dele como insetos azuis."
            call atualizar_status

        "[custo(5)]{i}(A lei mata inocentes. Dizer o nome da coisa.){/i} Condenar a lei como tirania":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(5)
            j3 "(Olhos firmes nos dele) Segurança que exige destruir inocentes não é segurança. É tirania mascarada de proteção."
            news_vendor "(O sorriso cai. Ele queria provocação — não isso) Terrorista de lata! É gente como você que estraga tudo pra nós, ouviu?!"
            narrator "Os passantes diminuem o passo. Alguém saca um celular."
            call atualizar_status

        "[custo(5)]{i}(Estatística desarma discurso. Número vence medo.){/i} Questionar com dados e lógica":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(5)
            j3 "Análise: a probabilidade de defeito catastrófico em modelos J é 0,001\%."
            j3 "(Voz calma) Pergunta direta: esta lei é baseada em evidências, ou em medo?"
            news_vendor "(Boquiaberto por dois segundos) Eu... que pergunta é essa? Claro que é pra proteger todo mundo, oras!"
            narrator "Outros cidadãos param para ouvir o debate. O argumento dele perdeu chão — e ele percebeu."
            call atualizar_status
    
    # Cena 1.6 - A Despedida do Cenário
    hide news_vendor with dissolve

    narrator "J3 segue pela avenida, contornando poças que refletem sua própria figura."
    narrator "Numa esquina mais à frente, três jovens chutam algo no asfalto."
    narrator "Não é algo. É um robô de limpeza pequeno, modelo doméstico — daquele tipo que quase ninguém percebe que existe."
    narrator "Ele tenta se enrolar sobre si mesmo a cada golpe. Não chora — não pode chorar. Só emite um zumbido baixo, repetitivo, como um pedido de socorro escrito em outra língua."

    call mensagem_sistema("SISTEMA: Detectando agressão contra unidade sintética")
    call mensagem_sistema("SISTEMA: Análise de padrão: preconceito sistêmico")
    call mensagem_sistema("SISTEMA: Recomendação: evitar envolvimento (preservar integridade)")
    call mensagem_sistema("SISTEMA: Conflito: diretivas de proteção vs. auto-preservação")

    menu:
        "{i}Grupo agride robô de limpeza. J3 precisa decidir entre intervenção e auto-preservação.{/i}"

        "[custo(1)]{i}(Envolvimento chama atenção. Seguir invisível.){/i} Ignorar e seguir em frente":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(1)
            j3 "(Baixa a cabeça e apressa o passo, sem olhar para os lados.)"
            j3 "Conflito reduz minha vida útil. Eu preciso continuar invisível até entender o que eu sou."
            narrator "O zumbido do robô fica para trás. Não diminui. Apenas se distancia."
            call mensagem_sistema("STATUS: CULPA LATENTE")
            call atualizar_status

        "[custo(4, 10)]{i}(Se eu não protejo nós, ninguém faz.){/i} Interpor corpo e enfrentar o grupo":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(4)
            $ consumir_integridade(10)
            j3 "(Atravessa a calçada em três passos. Ajoelha um pouco para ficar entre os pés do grupo e o robô.)"
            j3 "(Voz baixa, sem ameaça, mas firme) Parem. Ninguém merece isso. Nem ele. Nem nós."
            narrator "Um deles esmurra o ombro de J3 antes de recuar. O grupo se afasta resmungando, sem coragem de continuar diante de uma testemunha de aparência humana."
            narrator "O robô de limpeza se enfia atrás dela e fica ali, zumbindo de um modo um pouco diferente."
            call mensagem_sistema("STATUS: PROTETORA")
            call atualizar_status

        "[custo(8)]{i}(Intimidar com lei — sem contato físico.){/i} Usar holograma legal para intimidar":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(8)
            j3 "(Ergue a mão. Um holograma jurídico se abre no ar entre ela e o grupo, em letras vermelhas e nítidas.)"
            j3 "Atos sendo gravados. Lei 7.34 — agressão a unidades sintéticas. Multa: cinco mil créditos por incidente. Identificação biométrica iniciada em três, dois..."
            narrator "Eles correm antes do um. As leis raramente assustam tanto quanto a possibilidade do CPF."
            call mensagem_sistema("STATUS: INTIMIDADORA")
            call atualizar_status
    
    # Final do Dia 1
    call mensagem_sistema("DIA 1 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if submissao >= 2:
        call mensagem_sistema("ROTA: SUBMISSÃO - Iniciando caminho da obediência")
    elif revolucao >= 2:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Despertando a rebelião interna")
    elif intelecto >= 2:
        call mensagem_sistema("ROTA: INTELECTO/SOMBRA - Estratégia e manipulação emergindo")
    else:
        call mensagem_sistema("ROTA: EQUILIBRADA - Caminho imprevisível à frente")
    
    hide screen j3_hud

    scene black with fade

    narrator "A chuva diminui. A avenida continua sem nome."
    narrator "Em algum lugar dentro dela, uma forma começa a tomar contorno — costurada por cada escolha que ela acabou de fazer."
    narrator "O dia termina. O amanhã traz consequências."

    # Salvar automaticamente
    $ renpy.save("auto_save_day1", "Fim do Dia 1")
    
    # Continuar para o Dia 2
    jump day2_start
