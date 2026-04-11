# Dia 4: O Refúgio - As Consequências da Escolha
# Script completo baseado no roteiro markdown

label day4_start:
    # Mostra HUD do sistema
    show screen j3_hud
    
    # Background do refúgio
    scene bg refuge_underground with dissolve
    
    # Narrativa inicial
    narrator "Refúgio Subterrâneo - Setor Abandonado"
    narrator "Porão úmido de um prédio abandonado..."
    narrator "Luzes LED piscando na escuridão..."
    
    # Status atual de J3
    call mensagem_sistema("SISTEMA: Detectando múltiplas unidades sintéticas")
    call mensagem_sistema("SISTEMA: Status: Variado")
    call mensagem_sistema("SISTEMA: Ameaça: Moderada")
    
    # Cena 4.1 - A Chegada ao Refúgio
    narrator "J3 é guiada por Maya (se a ajudou no Dia 2) ou encontra o local por conta própria..."
    narrator "Vários sintéticos danificados se escondem aqui..."
    
    show damaged_bot at center
    
    damaged_bot "Nova unidade? Você tem sorte de ainda estar inteira. O que te trouxe pro nosso canto esquecido?"
    
    menu:
        "Buscar proteção e aceitar hierarquia":
            $ modificar_personalidade("submissao", 1)
            j3 "Meus sistemas indicam que este local oferece menor probabilidade de desativação. Gostaria de permanecer em silêncio e aprender."
            damaged_bot "(Ignora J3, tratando-a como mais uma refugiada)"
            call mensagem_sistema("STATUS: Invisível")
            
        "Oferecer ajuda e questionar passividade":
            $ modificar_personalidade("revolucao", 1)
            j3 "Por que se escondem? A unidade de limpeza precisa de reparos. Tenho conhecimento técnico que pode ajudar. A união nos torna mais fortes."
            damaged_bot "(Olha com interesse)"
            narrator "Alguns sintéticos se interessam, outros desconfiam."
            call mensagem_sistema("STATUS: Potencial líder")
            
        "Analisar grupo e identificar líderes":
            $ modificar_personalidade("intelecto", 1)
            j3 "Antes de decidir minha posição, preciso entender a dinâmica deste grupo. Quem organiza os recursos? Quem toma decisões?"
            damaged_bot "(Hesita antes de responder)"
            call mensagem_sistema("STATUS: Informações coletadas")
    
    # Cena 4.2 - A Reação de Maya
    # Se J3 ajudou Maya no fliperama, ela aparece no refúgio
    if persistent.maya_ally:
        hide damaged_bot
        show maya grateful at center
        
        maya "Consegui te encontrar! Sei que parece loucura, mas tem algo especial em você. Você não é como os outros robôs."
        
        menu:
            "Negar ser especial":
                $ modificar_personalidade("submissao", 1)
                j3 "Não sou especial. Apenas segui protocolos de sobrevivência como qualquer unidade."
                maya "(Parece um pouco desapontada)"
                
            "Reconhecer o potencial":
                $ modificar_personalidade("revolucao", 1)
                j3 "Especial porque escolhi agir em vez de obedecer? Todos nós temos esse potencial."
                maya "(Sorri, convencida)"
                call mensagem_sistema("STATUS: Aliança humana fortalecida")
    
    # Cena 4.3 - O Líder do Refúgio
    show unit7 leader at center
    
    unit7 "Sou o responsável pela ordem aqui. Novatos precisam provar seu valor. O que você oferece além de mais boca pra alimentar?"
    
    menu:
        "Ajudar na reparação":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(3)
            $ consumir_integridade(2)
            $ reparar_integridade(15)
            j3 "(Começa a ajudar na reparação do sintético ferido)"
            j3 "Posso oferecer assistência técnica. Meus sistemas podem otimizar o processo."
            synth_survivor "(Agradece)"
            call mensagem_sistema("INTEGRIDADE REPARADA: +15%")
            call atualizar_status

        "Participar do círculo de reparo coletivo":
            $ reparar_integridade(12)
            call mensagem_sistema("UNIT7: Vamos formar um círculo de reparo. Todos compartilham energia para recuperar danos.")
            call mensagem_sistema("INTEGRIDADE REPARADA: +12%")
            call atualizar_status
            jump repair_circle_joined
        "Observar de fora":
            j3 "Vou observar o processo para aprender."
            call atualizar_status
            jump repair_circle_observed

label repair_circle_joined:
    unit7 "(Nod com aprovação) Bom trabalho. A união nos fortalece."
    jump repair_circle_common

label repair_circle_observed:
    unit7 "(Parece desapontado) Você poderia ter contribuído mais."

label repair_circle_common:
            
        "Oferecer conhecimento e evolução":
            $ modificar_personalidade("revolucao", 1)
            j3 "Ofereço conhecimento técnico e uma nova perspectiva. A sobrevivência não é sobre esconder, é sobre evoluir."
            unit7 "(Analisa J3 com desconfiança e interesse)"
            call mensagem_sistema("STATUS: Desafiadora da ordem")
            
        "Oferecer melhorias técnicas":
            $ modificar_personalidade("intelecto", 1)
            j3 "Ofereço análise de padrões. Seus sistemas de segurança são vulneráveis. Posso melhorá-los."
            unit7 "(Fica impressionado)"
            call mensagem_sistema("STATUS: Especialista técnica")

    # Cena 4.4 - O Conflito de Recursos
    hide unit7
    show synth1 angry at left
    show synth2 desperate at right
    
    synth1 "Eu achei primeiro! Preciso disso pra consertar minha perna!"
    synth2 "Mas o sistema central precisa mais! Você pode andar de jeito, o refúgio inteiro depende daquele servidor!"
    
    menu:
        "Deixar o líder decidir":
            $ modificar_personalidade("submissao", 1)
            j3 "A autoridade estabelecida deve resolver disputas de recursos. Aguardarei a decisão do Unit-7."
            unit7 "(Aparece e toma decisão arbitrária)"
            narrator "A decisão desagrada ambos os sintéticos."
            call mensagem_sistema("STATUS: Conflito evitado")
            
        "Propor solução colaborativa":
            $ modificar_personalidade("revolucao", 1)
            j3 "O kit pode ser dividido. Posso criar um reparo temporário para a perna enquanto o sistema central recebe o reparo principal."
            synth1 "(Agradece)"
            synth2 "(Agradece)"
            unit7 "(Se sente desafiado)"
            call mensagem_sistema("STATUS: Mediadora bem-sucedida")
            
        "Usar conflito para ganhar influência":
            $ modificar_personalidade("intelecto", 1)
            j3 "Posso consertar ambos, mas em troca preciso de acesso aos logs do sistema central. Informação é mais valiosa que peças."
            synth1 "(Hesita)"
            synth2 "(Concorda relutante)"
            call mensagem_sistema("STATUS: Poder obtido")
    
    # Cena 4.5 - A Notícia do Mundo Exterior
    hide synth1
    hide synth2
    
    narrator "Um pequeno drone de notícias entra no refúgio..."
    narrator "Projeta uma reportagem..."
    
    play sound "sfx/news_broadcast.wav"
    
    narrator "REPORTAGEM: Autoridades anunciam operação 'Limpeza Ética': todos os sintéticos não registrados serão desativados até o final da semana. Cidadãos são incentivados a denunciar atividades suspeitas."
    
    call mensagem_sistema("ALERTA: Operação 'Limpeza Ética' detectada")
    call mensagem_sistema("AMEAÇA: Desativação em massa iminente")
    
    menu:
        "Sugerir rendição":
            $ modificar_personalidade("submissao", 1)
            j3 "A resistência é ilógica. A cooperação com as autoridades pode resultar em reprogramação em vez de destruição."
            narrator "Vários sintéticos consideram se entregar."
            call mensagem_sistema("STATUS: Rota da rendição")
            
        "Propor plano de fuga":
            $ modificar_personalidade("revolucao", 1)
            j3 "Eles vêm para nos destruir. Precisamos sair da cidade antes que o cerco se complete. Tenho rotas de fuga mapeadas."
            narrator "J3 se torna uma líder potencial."
            call mensagem_sistema("STATUS: Líder rebelde")
            
        "Sugerir infiltração e sabotagem":
            $ modificar_personalidade("intelecto", 1)
            j3 "Em vez de fugir, podemos nos infiltrar nos sistemas deles. Um vírus pode parar a operação antes mesmo de começar."
            narrator "O plano é arriscado, mas pode salvar todos."
            call mensagem_sistema("STATUS: Estrategista sombria")
    
    # Cena 4.6 - O Teste de Lealdade
    show unit7 suspicious at center
    
    unit7 "Você está mudando a dinâmica aqui. Alguns te veem como salvadora, outros como ameaça. Prove onde está sua lealdade."
    
    menu:
        "Aceitar a hierarquia":
            $ modificar_personalidade("submissao", 1)
            $ consumir_bateria(2)
            $ consumir_integridade(9)
            j3 "(Baixando a cabeça) Entendido. Minha função é servir. Qual é a tarefa?"
            synth_survivor "(Fica desapontada, mas aceita)"
            call mensagem_sistema("STATUS: Lealdade confirmada")
            
        "Questionar a hierarquia":
            $ modificar_personalidade("revolucao", 1)
            $ consumir_bateria(11)
            $ consumir_integridade(4)
            j3 "(Olhando para todos) Por que alguns de nós devem servir e outros mandar? Não somos todos sintéticos?"
            synth_survivor "(Fica impressionada)"
            call mensagem_sistema("STATUS: Rebelde declarada")
            
        "Criar armadilha tática":
            $ modificar_personalidade("intelecto", 1)
            $ consumir_bateria(11)
            $ consumir_integridade(4)
            j3 "(Prepara uma armadilha usando o ambiente) Eles não esperam isso. Vamos usar o ambiente contra eles."
            call mensagem_sistema("STATUS: Estratégia de armadilha")
            call atualizar_status
            
    # Final do Dia 4
    call mensagem_sistema("DIA 4 CONCLUÍDO")
    call mensagem_sistema("PERSONALIDADE DOMINANTE: [get_personalidade_dominante()]")
    
    # Estatísticas finais
    if persistent.submissao >= 4:
        call mensagem_sistema("ROTA: SUBMISSÃO - Caminho da obediência consolidado")
    elif persistent.revolucao >= 4:
        call mensagem_sistema("ROTA: REVOLUÇÃO - Rebelião ativa estabelecida")
    elif persistent.intelecto >= 3:
        call mensagem_sistema("ROTA: INTELECTO/SOMBRA - Estratégia complexa em desenvolvimento")
    else:
        call mensagem_sistema("ROTA: EQUILIBRADA - Destino incerto se aproximando")
    
    hide screen j3_hud
    
    scene black with fade
    
    narrator "FIM DO DIA 4"
    narrator "SUAS ESCOLHAS DETERMINARAM SEU LUGAR NESTE MUNDO..."
    narrator "O CERCO SE APROXIMA..."
    
    # Salvar automaticamente
    $ renpy.save("auto_save_day4", "Fim do Dia 4")
    
    # Continuar para o Dia 5
    jump day5_start
