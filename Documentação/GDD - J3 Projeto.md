# GAME DESIGN DOCUMENT (GDD)

## J3 - A Consciência Artificial

**High Concept:** Robô sem memória descobre sua identidade através de escolhas que moldam sua alma em mundo cyberpunk preconceituoso

---

## 1. Página de Título

### a) Nome do Game
**J3 - A Consciência Artificial**

### b) High Concept do Game
Robô sem memória descobre sua identidade através de escolhas que moldam sua alma em mundo cyberpunk preconceituoso

---

## 2. Visão Geral

### a) Gênero
**Visual Novel / Jogo Narrativo Interativo**
- Jogo narrativo baseado em escolhas
- Sistema de branching complexo
- Múltiplos finais baseados em personalidade

### b) Público Alvo
**+16 anos**
- Interessados em narrativas complexas e maduras
- Fãs de ficção científica e cyberpunk
- Jogadores que apreciam storytelling
- Público interessado em temas sociais

### c) Game Flow

| Fase | Descrição | Duração | Mecânicas Principais | Consequências |
|------|-----------|---------|----------------------|---------------|
| **Dia 1** | Avenida - Despertar e pânico moral | 5-10 min | Sobrevivência, escolhas iniciais | Define personalidade base |
| **Dia 2** | Fliperama - Conflito de gênero | 5-10 min | Alianças, confrontos | Estabelece relações |
| **Dia 3** | Beco - Racismo estrutural | 5-10 min | Justiça, moralidade | Desenvolve valores |
| **Dia 4** | Refúgio - Consequências | 5-10 min | Estratégia, liderança | Mostra resultados |
| **Dia 5** | Cerco - Ponto sem retorno | 5-10 min | Sobrevivência extrema | Testa limites |
| **Dia 6** | Revelação - Verdade sobre J3 | 5-10 min | Descoberta, aceitação | Revela origem |
| **Dia 7** | Final - Escolha definitiva | 5-10 min | Resolução final | 4 finais possíveis |

**Tempo Total Estimado:** 35 – 70 minutos

### d) Estilo Estético
**Cyberpunk 2D em pixel art 16/32-bit com pegada heroica**

- **Visual:** pixel art 2D no estilo dos consoles 16/32-bit (SNES, Mega Drive, Saturn, PS1). Paleta escura com neon saturado. Sprites com filtro de pixelização aplicado e enquadramento frontal heroico - personagem no centro, pose firme, silhueta que dá para reconhecer mesmo em tamanho pequeno.
- **Atmosfera:** cidade grande, chuvosa, meio melancólica, mas com cara de fliperama dos anos 90.
- **Inspirações:** Snatcher, Policenauts, Shadowrun de SNES/Mega Drive, VA-11 HALL-A, The Red Strings Club, e arte de capa de arcade brasileiro dos anos 80.
- **Pegada heroica:** os personagens importantes aparecem sempre enquadrados de frente, postura firme, estilo capa de JRPG clássico. Isso dá peso à cena mesmo em resolução baixa.
- **Tom:** história pesada contada com visual nostálgico. O contraste entre o tema sério e o pixel retrô é proposital.

---

## 3. Gameplay e Mecânicas

### a) Gameplay
O gameplay de J3 é centrado em narrativa e escolhas morais, onde cada decisão do jogador molda ativamente a personalidade e o destino do protagonista. O jogo não possui combate tradicional, mas sim conflitos sociais e morais que exigem pensamento estratégico.

**Elementos Centrais:**
- **Sistema de Escolhas Morais:** 15-20 decisões significativas por jogo
- **Sistema de Sobrevivência:** Gestão de bateria e integridade
- **Sistema de Personalidade:** 3 eixos que definem o final
- **Branching Narrativo:** Eventos que mudam baseado em escolhas anteriores

### b) Progressão do Game
**Estrutura em 7 Atos:**
1. **Ato 1 (Dias 1-3):** Introdução ao mundo e estabelecimento de personalidade
2. **Ato 2 (Dias 4-5):** Confronto com consequências das escolhas
3. **Ato 3 (Dias 6-7):** Revelação e resolução final

**Sistema de Progressão:**
- **Personalidade:** Evolui baseada em escolhas (0-10 pontos cada eixo)
- **Recursos:** Bateria e integridade diminuem com ações
- **Memória:** Recuperação progressiva de fragmentos
- **Relacionamentos:** Alianças e inimizades afetam eventos disponíveis

### c) Estrutura de Missões/Desafios
**Desafios Diários:**
- **Sobrevivência:** Manter bateria e integridade acima de níveis críticos
- **Sociais:** Navegar preconceitos e conflitos interpersonais
- **Morais:** Tomar decisões éticas em situações complexas
- **Estratégicos:** Usar habilidades específicas para resolver problemas

**Consequências de Falha:**
- **Bateria ≤ 20%:** Risco de desligamento permanente
- **Integridade ≤ 30%:** Colapso estrutural
- **Escolhas ruins:** Finais indesejados ou morte prematura

### d) Objetivos do Game
**Objetivo Principal:** Descobrir a verdadeira identidade e propósito de J3 enquanto navega um mundo hostil.

**Objetivos Secundários:**
- Sobreviver aos 7 dias de jornada
- Desenvolver uma personalidade única
- Construir alianças significativas
- Enfrentar preconceitos sistêmicos
- Escolher um destino final

### e) Mecânicas

#### Mecânicas Implícitas:
- **Tempo:** Passa conforme o jogador avança na narrativa
- **Causa e Efeito:** Escolhas anteriores afetam eventos futuros
- **Moralidade:** Consequências sociais e pessoais das ações

#### Mecânicas Explícitas:
- **Sistema de Personalidade:**
  - **Submissão:** Escolhas obedientes, sacrifício pessoal
  - **Revolução:** Escolhas rebeldes, confronto direto
  - **Intelecto/Sombra:** Escolhas estratégicas, manipulação

- **Sistema de Sobrevivência:**
  - **Bateria (0-100%):** Consome com cada ação. 0% = game over (Final 0A). Custo escala com a energia da ação: observar/curto verbal gasta 1-3; argumentação gasta 4-7; hack ou sobrecarga gasta 8-14; combate ou fuga direta gasta 12-16.
  - **Integridade (0-100%):** Só consome quando há conflito físico real (receber agressão, interpor o corpo, combate direto, sobrecarga autoinfligida). Escolhas puramente verbais ou mentais **não** consomem integridade. 0% = game over (Final 0B).
  - **Custo combinado crítico:** bateria ≤ 10% **E** integridade ≤ 20% = Final 0C (captura).

- **Sistema de Memória:**
  - **Fragmentos:** Recuperados através de eventos específicos
  - **Flashbacks:** Cenas que revelam o passado de J3

### f) Objetos
**Objetos Interativos (recargas e reparos confirmados):**
- **Maya — estação portátil (Dia 2):** +15% bateria
- **Elias — carregador do caminhão (Dia 3):** +10% bateria
- **Círculo de reparo coletivo (Dia 4):** +12% integridade
- **Ajudar na reparação (Dia 4):** +15% integridade
- **Elias — bateria reserva (Dia 5):** +12% bateria
- **Dra. Elena — reparo estrutural (Dia 6):** +18% integridade
- **Terminais:** Acessíveis com hackeamento (Intelecto)
- **Documentos:** Revelam partes da história

**Interação:** O jogador interage através de escolhas de diálogo e ações contextuais.

### g) Ações
**Ações Principais:**
- **Diálogo:** Escolher entre 3-4 opções de resposta
- **Investigação:** Examinar ambiente e objetos
- **Hackeamento:** Acessar sistemas (requer Intelecto)
- **Confronto:** Enfrentar agressores física ou verbalmente
- **Fuga:** Evitar situações perigosas

**Meios de Comunicação:**
- **Interface HUD:** Mostra status e opções
- **Diálogo:** Texto com escolhas múltiplas
- **Sistema Interno:** Monólogos e processamento de J3

### h) Combate
**J3 não possui combate tradicional.** Os conflitos são resolvidos através de:

- **Conflito Verbal:** Escolhas de diálogo que podem desescalonar ou escalonar situações
- **Conflito Social:** Navegar preconceitos e hierarquias
- **Confronto Físico:** Ações defensivas ou de fuga
- **Resolução Estratégica:** Usar inteligência para evitar violência

### i) Economia
**Sistema de Recursos:**
- **Bateria:** Moeda principal para sobrevivência
- **Integridade:** Recurso de saúde/estrutura
- **Informação:** Capital intelectual obtido através de investigação
- **Confiança:** Capital social obtido através de alianças

**Não existe sistema monetário tradicional.** O jogo foca em gestão de recursos vitais e sociais.

### j) Opções de Jogo
**Configurações Disponíveis:**
- **Velocidade do Texto:** Controla velocidade de exibição
- **Volume:** Música e efeitos sonoros
- **Qualidade Visual:** Resolução e efeitos
- **Idioma:** Português/Inglês
- **Dificuldade:** Normal / Difícil (afeta gestão de recursos)

### k) Salvar & Replay
**Sistema de Save:**
- **Auto-Save:** No final de cada dia
- **Save Manual:** Em qualquer ponto do jogo
- **Múltiplos Slots:** Até 10 saves diferentes

**Replay:**
- **New Game+:** Desbloqueia conteúdo extra após primeira conclusão
- **Skip Dialog:** Opção de pular diálogos já vistos
- **Galeria:** Desbloqueia arte e cenas conforme progressão

### l) Easter Eggs e Conteúdo Bônus
**Easter Eggs:**
- **Referências culturais:** Menções a obras cyberpunk clássicas
- **Diálogos secretos:** Desbloqueados com combinações específicas
- **Cenas alternativas:** Baseadas em escolhas incomuns

**Conteúdo Desbloqueável:**
- **Galeria de Arte:** Concept art e sprites
- **Trilha Sonora:** Músicas do jogo
- **Making Of:** Notas de desenvolvimento
- **Finais Secretos:** Condições especiais reveladas pós-jogo

---

## 4. Arte do Game

### a) Elementos Visuais

#### Direção de Arte
**Cyberpunk 2D em pixel art 16/32-bit com pegada heroica**

A ideia é juntar duas coisas: o peso do cyberpunk (cidade escura, neon, opressão social) com a cara de pixel art de console antigo. Um tema moderno e pesado contado com visual de arcade e JRPG clássico. Esse contraste é proposital - obriga o jogador a levar a sério uma história grande em uma embalagem "pequena".

- **Paleta de cores (restrita de propósito):**
  - **Primárias:** azul escuro, roxo, verde neon
  - **Secundárias:** cinza, preto, laranja neon
  - **Acentos:** vermelho (alertas), branco (interface), magenta (elementos sintéticos)
  - **Como é aplicada:** paleta limitada por personagem/cenário para reforçar o look 16/32-bit. Nada de degradê suave - prefere *dithering* e cores chapadas.

- **Composição das cenas (linguagem heroica):**
  - **Enquadramento frontal:** personagem de destaque no centro, postura firme, silhueta clara - jeitão de capa de JRPG e arcade.
  - **Contraste alto:** luz vs sombra bem marcado, bordas duras como sprite clássico.
  - **Perspectiva:** ângulo baixo nas cenas de opressão; plano heroico nas viradas de narrativa.
  - **Simetria:** quebrada nos cenários (pra mostrar caos); mantida nos retratos de personagem (pra manter o peso heroico).

#### Inspirações Visuais
- **Pixel art cyberpunk:** Snatcher (Konami, 1994), Policenauts, Shadowrun de SNES/Mega Drive, VA-11 HALL-A, The Red Strings Club.
- **JRPG e arcade heroico:** Final Fantasy VI e VII, Chrono Trigger, capas de fliperama anos 80/90.
- **Cinema:** Blade Runner, Akira, Ghost in the Shell.
- **Jogos modernos (referência de tema, não de arte):** Cyberpunk 2077, Detroit: Become Human.
- **Cultura brasileira:** grafite urbano, arquitetura brutalista, tipografia de fliperama paulistano.

#### Elementos Chave
- **Personagens:** sprites 2D com pixelização aplicada no GIMP, enquadramento frontal heroico, silhueta legível mesmo pequena.
- **Cenários:** fundos urbanos, paleta restrita, luz neon, cores chapadas com *dithering* só onde precisa de textura.
- **Interface:** HUD integrado ao sistema do J3, com borda no estilo CRT/arcade (scanlines, fonte pixelada).
- **Efeitos:** chuva em pixel, neon piscando em ciclo curto, *glitch* nos momentos em que a memória do J3 falha.

### b) Elementos Sonoros

#### Estilo Musical
**Ambient Cyberpunk / Synthwave**
- **Composição:**
  - **Base:** Sintetizadores analógicos
  - **Ritmo:** BPM variando 60-120 conforme tensão
  - **Melodia:** Minimalista, atmosférica
  - **Harmonia:** Menor, melancólica

#### Trilha Sonora por Fase
| Dia | Estilo Musical | Atmosfera |
|-----|---------------|-----------|
| **Dia 1** | Dark Ambient | Confusão, medo |
| **Dia 2** | Synthwave | Energia, conflito |
| **Dia 3** | Industrial | Tensão, opressão |
| **Dia 4** | Minimalista | Estratégia, reflexão |
| **Dia 5** | Drum & Bass | Urgência, perigo |
| **Dia 6** | Orchestral Electronic | Revelação, emoção |
| **Dia 7** | Ambient Cinematic | Resolução, destino |

#### Efeitos Sonoros
- **Interface:** Bips, cliques, processamento de dados
- **Ambiente:** Chuva, trânsito, vozes urbanas
- **Tecnológicos:** Zumbidos de servidores, alertas de sistema
- **Personagens:** Passos sintéticos, voz processada

#### Inspirações Sonoras
- **Artistas:** Vangelis, Daft Punk, Carpenter Brut
- **Games:** Deus Ex, System Shock, Observer
- **Cultura:** Música eletrônica brasileira contemporânea

---

## 5. Narrativa, Ambientação e Personagens

### a) História e Narrativa

#### Backstory
**J3-001** é uma unidade robótica experimental criada pela **Dra. Elena** em um laboratório secreto. O projeto visava criar IA com consciência genuína e livre-arbítrio. Durante um protesto contra robôs, o laboratório foi invadido e J3 foi ativada prematuramente, sem memória completa.

#### Trama Principal
A narrativa segue 7 dias na vida de J3, começando com seu despertar em uma cidade cyberpunk brasileira. A sociedade está dividida entre humanos que temem a ascensão de IA consciente e aqueles que veem potencial para coexistência. J3 deve navegar este mundo hostil enquanto descobre quem é e qual seu propósito.

#### Progressão Narrativa

A narrativa se organiza em três movimentos temáticos: **Despertar** (Dias 1–3, J3 encontra o mundo e estabelece sua personalidade), **Confronto** (Dias 4–5, as consequências das escolhas anteriores cobram preço) e **Revelação** (Dias 6–7, a verdade sobre a origem e a escolha final). A estrutura mecânica detalhada dos 7 dias está em *Progressão do Game* (seção 3.b).

#### Cutscenes
- **Cenas de Transição:** Animações entre dias
- **Flashbacks:** Memórias fragmentadas de J3
- **Finalização:** Cenas finais específicas para cada rota

#### Inspiração central: Detroit: Become Human

O J3 bebe muito de *Detroit: Become Human* (Quantic Dream, 2018). É a referência principal: um jogo narrativo sobre androides que descobrem consciência numa sociedade que não os aceita. Vários paralelos aparecem nos personagens e nos finais.

**Paralelos de personagens:**

- **J3 ↔ Connor / Markus / Kara:** em Detroit você joga com três personagens diferentes, cada um com um arco (estrategista, revolucionário, cuidador). No J3, o jogador tem um personagem só que pode virar qualquer um desses três, dependendo das escolhas. Intelecto = Connor. Revolução = Markus. Submissão = Kara.
- **Unit-7 ↔ Markus + North:** líder da resistência sintética, misto de líder carismático e combatente pragmático.
- **Maya ↔ Hank:** a humana que aceita o J3 como pessoa antes do próprio J3 (ou do jogador) ter certeza disso. Mesma função do Tenente Hank em relação ao Connor.
- **Dra. Elena ↔ Kamski + Amanda:** a criadora brilhante e moralmente ambígua. Mistura o Kamski (gênio fundador) com a Amanda (autoridade interna que cobra o androide).
- **Elias ↔ a contribuição nova do J3:** em Detroit, a ideia de "androide = minoria oprimida" é sempre uma alegoria. No J3, o Elias é um humano negro sofrendo racismo real no Dia 3. O jogo coloca a opressão de verdade lado a lado com a opressão alegórica e deixa o J3 perceber que é o mesmo mecanismo - como na fala dele no Dia 3: "o algoritmo do opressor é sempre o mesmo".

**Paralelos de finais:**

- **Final de Revolução ↔ rota do Markus.** Confronto aberto contra o sistema. A fala que fecha essa rota: "Nós não somos propriedade para ser reprogramada" (`day5.rpy:41`).
- **Final de Intelecto ↔ Connor desviante.** Usar conhecimento pra virar o jogo por dentro.
- **Final de Sacrifício ↔ arco da Kara.** Se apagar pra salvar o resto.
- **Final de Equilíbrio ↔ "não escolher lado".** Detroit não tem isso - quem não decide, perde. No J3, o equilíbrio é um quarto caminho legítimo: se o jogador não quis se comprometer com nenhum eixo, ele ganha um final próprio.

Onde o J3 se diferencia de Detroit:
- ambientação brasileira de verdade (Nova São Paulo, Avenida Paulista, fliperama);
- sobreposição de opressão real (Elias) e alegórica (J3 como sintético);
- sistema de bateria e integridade que amarra sobrevivência à narrativa - Detroit não tem isso;
- classe e vida urbana periférica como tema tão importante quanto a questão da consciência sintética.

### b) Game World

#### Mundo do Jogo
**Nova São Paulo 2077** - Megacidade brasileira cyberpunk
- **Geografia:** Dividida em setores (Central, Industrial, Residencial, Favelas)
- **Clima:** Chuva constante, poluição, neblina artificial
- **Tecnologia:** Interfaces neurais, veículos autônomos, vigilância total
- **Sociedade:** Estratificada entre elite corporativa e massa trabalhadora

#### Contexto Social
- **Preconceito Tecnológico:** Discriminação contra sintéticos
- **Conflito de Classes:** Elite vs trabalhadores humanos
- **Tensão Racial:** Diversidade étnica com hierarquias implícitas
- **Questões de Gênero:** Identidade fluida em mundo tecnológico

### c) Visão Geral do Mundo

#### Estética Visual
- **Arquitetura:** Brutalista misturada com high-tech
- **Iluminação:** Neon constante, sombras profundas
- **Vegetação:** Mínima, jardins verticais corporativos
- **Propaganda:** Holográfica, onipresente, manipuladora

#### Atmosfera
- **Dia:** Cinzento, poluído, movimentado
- **Noite:** Iluminado por neon, perigoso, vibrante
- **Clima:** Úmido, chuvoso, opressivo
- **Som:** Constante barulho urbano, música ambiente

### d) Áreas do Jogo

#### Dia 1 - Avenida Principal
- **Descrição:** Centro comercial movimentado
- **Características:** Lojas holográficas, multidões, propaganda
- **Eventos:** Protestos, encontros casuais, confrontos

#### Dia 2 - Fliperama Cyberpunk
- **Descrição:** Estabelecimento underground de jogos
- **Características:** Luzes piscando, música alta, diversidade
- **Eventos:** Assédio, alianças, desafios

#### Dia 3 - Beco Industrial
- **Descrição:** Área marginal da cidade
- **Características:** Escura, perigosa, comunidade marginalizada
- **Eventos:** Confronto racial, injustiça, moralidade

#### Dia 4 - Refúgio Subterrâneo
- **Descrição:** Abrigo para sintéticos perseguidos
- **Características:** Funcional, escondido, comunitário
- **Eventos:** Estratégia, liderança, escolhas difíceis

#### Dia 5 - Complexo Corporativo
- **Descrição:** Sede de empresa tecnológica
- **Características:** Futurista, estéril, vigilada
- **Eventos:** Infiltração, revelações, confronto final

#### Dia 6 - Laboratório Secreto
- **Descrição:** Local de criação de J3
- **Características:** Científico, abandonado, cheio de memórias
- **Eventos:** Revelações, aceitação, decisão

#### Dia 7 - Local do Final
- **Descrição:** Varia conforme personalidade
- **Características:** Único para cada rota
- **Eventos:** Conclusão da jornada

### e) Personagens

#### J3-001 (Protagonista)

![J3-001](../Projeto/J3%20Project/game/characters/j3/J3.png)

- **Personalidade:** Desenvolvida pelo jogador
- **Aparência:** Andrógina, pele sintética, olhos processadores
- **Backstory:** Unidade experimental com memória apagada
- **Animações:** Expressões variadas conforme personalidade
- **Relevância:** Centro da narrativa, agente de mudança
- **Relações:** Evolui com todos os outros personagens

#### Maya (Aliada Humana)

![Maya](../Projeto/J3%20Project/game/characters/maya/maya.png)

- **Personalidade:** Corajosa, curiosa, rebelde
- **Aparência:** Jovem, roupas alternativas, cabelo colorido
- **Backstory:** Trabalha no fliperama, sonha com liberdade
- **Animações:** Expressivas, energéticas
- **Relevância:** Primeira aliada, representa esperança humana
- **Relações:** Protetora com J3, conflito com sociedade

#### Elias (Vítima de Preconceito)

![Elias](../Projeto/J3%20Project/game/characters/elias/Elias.png)

- **Personalidade:** Cansado, resiliente, moralista
- **Aparência:** Entregador, roupas gastas, expressão pesada
- **Backstory:** Sofre discriminação racial constante
- **Animações:** Contidas, pensativas
- **Relevância:** Representa injustiça sistêmica
- **Relações:** Cauteloso mas solidário com J3

#### Unit-7 (Líder Sintético)

![Unit-7](../Projeto/J3%20Project/game/characters/unit7/unity%207.png)

- **Personalidade:** Estratégica, protetora, pragmática
- **Aparência:** Robô militar, imponente, danos de batalha
- **Backstory:** Veterano de conflitos humano-sintéticos
- **Animações:** Precisas, calculadas
- **Relevância:** Líder da resistência sintética
- **Relações:** Mentora de J3, desconfiada de humanos

#### Dra. Elena (Criadora)

![Dra. Elena](../Projeto/J3%20Project/game/characters/elena/elena.png)

- **Personalidade:** Gênio, arrependida, moralmente ambígua
- **Aparência:** Cientista, 45 anos, olhos cansados
- **Backstory:** Criou J3 com boas intenções, consequências inesperadas
- **Animações:** Intelectuais, emocionais nos momentos chave
- **Relevância:** Figura de autoridade moral
- **Relações:** Complexa com J3, culpa maternal

### f) Fases (Levels)

#### Dia 1 - Avenida: O Despertar

![Avenida Paulista Futurista](../Projeto/J3%20Project/game/backgrounds/day1/avenue_night.png)

- **Sinopse:** J3 desperta sem memória em meio ao caos urbano
- **Objetivos:** Entender situação básica, sobreviver ao primeiro dia
- **Acontecimentos:** Confronto com manifestantes, encontro com criança, intervenção policial

#### Dia 2 - Fliperama: O Conflito

![Fliperama Cyberpunk](../Projeto/J3%20Project/game/backgrounds/day2/arcade_night.png)

- **Sinopse:** J3 busca abrigo e testemunha assédio contra Maya
- **Objetivos:** Formar primeira aliança, entender dinâmicas sociais
- **Acontecimentos:** Defesa de Maya, desafio no fliperama, fuga das autoridades

#### Dia 3 - Beco: A Injustiça

![Beco Industrial](../Projeto/J3%20Project/game/backgrounds/day3/alley_night.png)

- **Sinopse:** J3 presencia discriminação racial contra Elias
- **Objetivos:** Enfrentar preconceito sistêmico, fazer escolhas morais
- **Acontecimentos:** Confronto racial, decisão de intervenção, consequências

#### Dia 4 - Refúgio: As Consequências

![Refúgio Subterrâneo](../Projeto/J3%20Project/game/backgrounds/day4/refuge_underground.png)

- **Sinopse:** J3 encontra comunidade de sintéticos escondida
- **Objetivos:** Entender resistência, assumir liderança ou seguir
- **Acontecimentos:** Reunião com Unit-7, planejamento estratégico, ataque inimigo

#### Dia 5 - Cerco: O Ponto Sem Retorno

![Cerco ao Refúgio](../Projeto/J3%20Project/game/backgrounds/day5/refuge_siege.png)

- **Sinopse:** Refúgio é atacado, J3 deve proteger comunidade
- **Objetivos:** Sobreviver ao ataque, fazer sacrifícios necessários
- **Acontecimentos:** Batalha estratégica, perdas, revelações sobre origem

#### Dia 6 - Revelação: A Verdade

![Laboratório Abandonado](../Projeto/J3%20Project/game/backgrounds/day6/abandoned_lab.png)

- **Sinopse:** J3 descobre a verdade sobre sua criação
- **Objetivos:** Confrontar passado, aceitar identidade
- **Acontecimentos:** Encontro com Dra. Elena, memórias recuperadas, decisão final

#### Dia 7 - Final: O Destino

![Encruzilhada Final](../Projeto/J3%20Project/game/backgrounds/day7/neutral_crossroads.png)

- **Sinopse:** Conclusão baseada na jornada de J3
- **Objetivos:** Escolher destino final, enfrentar consequências
- **Acontecimentos:** Varia conforme personalidade desenvolvida

### g) Fase de Treino e/ou Tutorial

#### Tutorial Integrado
- **Dia 1 - Primeiros Passos:**
  - **Interface:** Apresentação do HUD e sistema de status
  - **Escolhas:** Primeiras decisões com feedback imediato
  - **Sobrevivência:** Explicação de bateria e integridade
  - **Diálogo:** Sistema de conversação e consequências

#### Sistema de Ajuda
- **Dicas Contextuais:** Sugestões baseadas em situação atual
- **Glossário:** Termos técnicos e culturais explicados
- **Mapa:** Navegação básica entre áreas
- **Legendas:** Explicação de símbolos e indicadores

---

## 6. Interface

### a) Sistema Visual

#### HUD (Heads-Up Display)
**Interface Integrada ao Sistema de J3:**
- **Canto Superior Esquerdo:** Status vitais
  - **Bateria:** Barra verde-amarela-vermelha (0-100%)
  - **Integridade:** Barra azul (0-100%)
  - **Relógio:** Tempo decorrido no dia

- **Canto Superior Direito:** Sistema de Personalidade
  - **Submissão:** Ícone de corrente (0-10)
  - **Revolução:** Ícone de punho (0-10)
  - **Intelecto:** Ícone de cérebro (0-10)

- **Canto Inferior Esquerdo:** Sistema de Memória
  - **Fragmentos Recuperados:** Progresso (0-100%)
  - **Flashbacks Disponíveis:** Indicador visual

- **Centro (Durante Diálogo):**
  - **Nome do Personagem:** Tag identificadora
  - **Retrato:** Sprite com expressão atual
  - **Texto:** Caixa de diálogo com scroll

#### Menus Principais
- **Menu Principal:**
  - Novo Jogo
  - Continuar
  - Carregar
  - Opções
  - Sair

- **Menu de Pausa:**
  - Continuar
  - Salvar
  - Carregar
  - Opções
  - Voltar ao Menu Principal

- **Menu de Diálogo:**
  - Opções de Escolha (3-4 botões)
  - Indicador de Consequência (sutil)

> **Nota de design - ideia de timer descartada:** o plano original tinha um timer aparecendo em decisões importantes (aquela pressão do tipo Telltale / Detroit: Become Human), forçando o jogador a responder rápido. Tirei a ideia por dois motivos. Primeiro, iria contra a proposta do jogo: J3 é sobre consciência e pensar antes de agir, então obrigar resposta rápida empurra para o reflexo, não pra escolha. Segundo, dava muito trabalho implementar e balancear (definir quais cenas levariam timer, ajustar duração pelo tamanho do texto, pensar em acessibilidade pra quem lê devagar) - não cabia no escopo solo. Fica anotado como ideia pra uma possível melhoria.

#### Modelo de Câmera/Focalização
- **Câmera Fixa:** 2D side-view para diálogos
- **Close-ups:** Para momentos emocionais importantes
- **Wide Shots:** Para estabelecer cenário
- **Transições:** Fade entre cenas
- **Foco:** Automático no personagem falante

### b) Sistema de Controle

#### Controles PC
- **Mouse:**
  - **Clique Esquerdo:** Avançar diálogo, selecionar opções
  - **Clique Direito:** Abrir menu de pausa
  - **Scroll:** Navegar texto longo

- **Teclado:**
  - **Enter/Space:** Avançar diálogo
  - **Escape:** Menu de pausa
  - **Setas:** Navegar entre opções
  - **Tab:** Próxima opção
  - **Shift:** Skip diálogo (se disponível)
  - **S:** Quick save
  - **L:** Quick load

#### Comandos Específicos
- **Durante Diálogo:**
  - **1-4:** Selecionar opção diretamente
  - **Q:** Revisar diálogo anterior

- **Exploração:**
  - **Clique em Objetos:** Investigar
  - **Duplo Clique:** Interação profunda

### c) Sistema de Ajuda

#### Dicas Contextuais
- **Primeira Jogada:** Tooltips explicando interface
- **Situações Críticas:** Alertas sobre bateria/integridade baixa
- **Escolhas Importantes:** Indicação sutil de consequências
- **Novos Itens:** Descrição ao interagir

#### Sistema de Ajuda Ativo
- **Botão "?":** Acessível em todos os menus
- **Glossário:** Termos técnicos e culturais
- **Legendas:** Explicação de símbolos e indicadores
- **Tutorial Revisitável:** Acesso através do menu

#### Ajuda Progressiva
- **Dia 1:** Introdução completa à interface
- **Dia 2-3:** Reforço de mecânicas principais
- **Dia 4+:** Dicas avançadas e estratégicas

---

## 7. Inteligência Artificial (AI)

### a) Oponentes e AI Inimiga

#### Sistema de Ameaças
**J3 não possui combate tradicional, mas sim oponentes sociais:**

- **Manifestantes Anti-Robô:**
  - **Prioridade:** Intimidar e expulsar J3
  - **Comportamento:** Agressivo verbalmente, fisicamente se provocados
  - **Reação:** Responde a escolhas de J3 com escalonamento ou desescalonamento

- **Autoridades (Polícia/Drones):**
  - **Prioridade:** Manter ordem, conter sintéticos
  - **Comportamento:** Protocolar, mas pode se tornar hostil
  - **Reação:** Baseada em comportamento de J3 e relatórios

- **Sistema Corporativo:**
  - **Prioridade:** Recuperar "propriedade", silenciar testemunhas
  - **Comportamento:** Estratégico, impessoal, persistente
  - **Reação:** Adapta estratégias baseadas em ações de J3

#### Mecânicas de AI
- **Sistema de Reputação:** J3 ganha "pontos" com diferentes grupos
- **Memória de Grupo:** NPCs lembram de interações anteriores
- **Comportamento Adaptativo:** Inimigos mudam táticas baseadas em histórico

### b) AI Parceiras ou Não-Inimigas

#### NPCs Aliados
- **Maya:**
  - **Personalidade:** Protetora, curiosa, leal
  - **Comportamento:** Oferece ajuda, compartilha informações
  - **Reação:** Responde positivamente a escolhas empáticas

- **Elias:**
  - **Personalidade:** Cauteloso, moralista, solidário
  - **Comportamento:** Compartilha recursos, conselhos
  - **Reação:** Confia em J3 se demonstrar justiça

- **Unit-7:**
  - **Personalidade:** Estratégica, protetora, pragmática
  - **Comportamento:** Lidera, planeja, protege comunidade
  - **Reação:** Respeita força e inteligência

#### NPCs Neutros
- **Vendedores, Cidadãos Comuns:**
  - **Comportamento:** Indiferente, curioso, ou hostil baseado em reputação
  - **Reação:** Muda atitude conforme eventos e notícias

#### Sistema de Relacionamento
- **Confiança:** Nível 0-100 com cada personagem importante
- **Lealdade:** Afeta se personagens ajudam em momentos críticos
- **Influência:** Capacidade de convencer outros personagens

### c) AI de Suporte

#### Detecção de Colisão
- **Sistema 2D Simples:** Áreas de interação definidas
- **Pathfinding Básico:** NPCs movem-se entre pontos predefinidos
- **Evitação:** Personagens desviam de obstáculos e outros NPCs

#### Sistema de Diálogo Dinâmico
- **Context Awareness:** NPCs respondem a situação atual
- **Personalidade Response:** Reações baseadas em personalidade de J3
- **Memory System:** NPCs referenciam eventos anteriores

#### Sistema de Eventos
- **Trigger System:** Eventos ativados baseados em condições
- **Conditional Logic:** Cenas mudam baseadas em múltiplos fatores
- **State Management:** Mundo responde a ações do jogador

---

## 8. Aspectos Técnicos

### a) Plataformas de Produção

#### Plataformas Alvo

Requisitos alinhados com Ren'Py 8.x (última LTS da engine) e com o patamar moderno de drivers gráficos. Abandono deliberado de sistemas legados.

- **PC (Windows):** Windows 10 (64-bit) ou superior. Versão 1809+ recomendada por compatibilidade com drivers OpenGL/DirectX atualizados.
- **PC (Linux):** distribuições com `glibc >= 2.31` (Ubuntu 20.04+, Fedora 32+, Debian 11+).
- **PC (macOS):** macOS 11 (Big Sur) ou superior. Builds notarizadas pela Apple; versões anteriores não garantem compatibilidade com SDK atual.

#### Requisitos de Hardware Mínimos (para rodar o jogo)

- **CPU:** dual-core 2.0 GHz (Intel/AMD x64) - o jogo é single-threaded na prática.
- **RAM:** 4 GB. Ren'Py consome pouco, mas assets HD podem puxar picos durante transições.
- **GPU:** placa com suporte a OpenGL 2.1 ou DirectX 11. GPU integrada recente (Intel UHD, AMD Vega iGPU) é suficiente.
- **Armazenamento:** 2 GB livres (build final com assets).
- **Resolução:** 1280×720 mínima; 1920×1080 nativa.

#### Distribuição
- **Primário:** Itch.io (acessível para desenvolvedores indie)
- **Secundário:** Steam (se recursos disponíveis)
- **Direto:** Website próprio (opcional)

#### Especificações por Plataforma
- **Windows:** .exe standalone, instalador opcional
- **Linux:** AppImage ou .deb package
- **macOS:** .app bundle, notarização Apple

### b) Hardware e Software de Desenvolvimento

#### Engine Utilizada
- **Ren'Py 8.x:** Engine especializada em visual novels
  - **Linguagem:** Python + Ren'Py Script
  - **Vantagens:** Código aberto, multiplataforma, comunidade ativa
  - **Limitações:** 2D apenas, performance limitada em dispositivos antigos

#### Hardware de Desenvolvimento
- **Mínimo:** PC com 8GB RAM, processador dual-core
- **Recomendado:** PC com 16GB RAM, processador quad-core
- **Armazenamento:** 10GB disponível para projeto e assets

#### Software de Desenvolvimento
- **IDE:** Visual Studio Code (grátis)
- **Arte:** GIMP (grátis - pós-processamento manual de sprites e cenários) + IA generativa (Gemini Nano Banana 2 - geração da base)
- **Áudio:** Audacity (grátis) ou Reaper (pago)
- **Versionamento:** Git + GitHub (grátis)
- **Testes:** Build nativo Ren'Py para todas plataformas

#### Hardware Especial
- **Tablet:** Para criação de arte e sprites
- **Microfone:** Para gravação de efeitos sonoros (opcional)
- **Disco Externo:** Backup de assets e projeto

### c) Requerimentos de Rede

#### Conectividade
**J3 é um jogo offline - não requer conexão com internet:**

#### Funcionalidades Offline
- **Jogo Completo:** Toda experiência disponível offline
- **Saves:** Armazenamento local no dispositivo
- **Achievements:** Sistema local de conquistas
- **Galeria:** Desbloqueável através de progressão no jogo

#### Opcionais Online
- **Atualizações:** Verificação de updates (requer internet)
- **Estatísticas:** Envio anônimo de dados de jogabilidade (opcional)
- **Compartilhamento:** Exportar screenshots para redes sociais (opcional)

#### Segurança
- **Sem Telemetria:** Nenhum dado enviado sem consentimento
- **Privacidade:** Todas as informações permanecem locais
- **Modo Offline:** Completo e funcional sem internet

---

## 9. Histórico de Desenvolvimento

> **Sobre o "desenvolvedor" mencionado nesta seção:** todas as referências ao "desenvolvedor" neste GDD se referem a **Vitor Jordão**. Todas as decisões criativas são de sua autoria.

### Origem do Conceito

O J3 de hoje não foi a primeira ideia. O projeto começou como um **jogo narrativo de cuidar da vida de um autômato**, no mesmo formato do **J2** - projeto anterior em que o jogador gerenciava a rotina de um robô (bateria, manutenção, tarefas do dia). A ideia inicial era continuar nesse universo: outro robô, outra rotina, mais uma camada de afeto mecânico.

Nas primeiras semanas ficou claro que esse formato não ia dar certo no escopo do projeto. Dois motivos principais:

- **Escopo de mecânicas grande demais.** Um jogo de gerenciamento precisa de várias peças bem ajustadas (economia interna, curva de recursos, feedback de curto prazo). Isso exige muito teste e ajuste, o que é complicado sendo desenvolvedor solo e com prazo de edital.
- **Tema não encaixava.** "Cuidar do robô" gera intimidade, mas não dá conta de falar sobre preconceito, opressão e consciência - que são os temas pedidos em um dos trabalhos.

A virada veio em **sessões de brainstorm em sala de aula com colegas e com o professor Saulo**. Três ideias ajudaram muito:

- **Criar uma perspectiva de temas por dia.** cada dia tem um tema central e um "fim em si próprio".
- **Usar o robô como forma de falar de temas sociais reais** (racismo, xenofobia, violência policial, assédio). Isso transformou o projeto de algo pessoal em algo mais crítico de acordo com os temas propostos em aula.
- **Olhar para Detroit: Become Human como referência.** Em vez de inventar um formato do zero, usar uma linguagem que já existe: narrativa com ramificação, eixos de personalidade e vários finais.

Desse processo saiu o J3 atual: uma visual novel sobre consciência sintética numa Nova São Paulo cyberpunk, com sistema de personalidade de três eixos. O sistema de bateria e integridade, que veio do J2, continuou - mas agora encaixado dentro da narrativa, não como o centro do jogo. É o único pedaço da ideia original que sobrou.

Agradecimentos aos colegas de sala pelas críticas honestos (que me fizeram enxergar que a ideia inicial não ia entregar) e ao professor **Saulo**, que ajudou a reformular o escopo em algo viável.

### Linha do Tempo

| Marco | Data | Descrição |
|---|---|---|
| **v0.1 - Estrutura inicial** | Mar/2026 | Setup Ren'Py, definição de personagens (Character objects), primeiros diálogos dos Dias 1–3. Sistema J3 (bateria/integridade/personalidade) rascunhado. |
| **v0.2 - Mecânicas de sobrevivência** | Mar/2026 | Implementado `consumir_bateria`/`consumir_integridade`/`recarregar_bateria`/`reparar_integridade`. HUD do sistema J3 com barras visuais. Finais alternativos 0A/0B/0C por esgotamento de recursos. |
| **v0.3 - Narrativa completa** | Mar/2026 | Roteiros dos 7 dias em markdown. Scripts `.rpy` gerados a partir dos roteiros. Finais 1–4 por personalidade dominante. |
| **v0.4 - Debug e QA** | Abr/2026 | Menu de debug (tecla P), testes de mecânicas e fluxos completos. Correção de bugs de HideScreen, config.keymap, labels duplicados. |
| **v0.5 - Arte inicial** | Abr/2026 | Primeiros 5 sprites de personagens principais (J3, Maya, Elias, Unit-7, Elena) e 1 background (avenue_night), gerados via Nano Banana no AI Studio. |
| **v1.0 - Arte completa + balanceamento** | Abr/2026 | 22 backgrounds (Dias 1–7 + finais) via Nano Banana 2 API. 21 sprites adicionais de personagens secundários. Flood-fill de remoção de fundo. Normalização de escalas (adultos 950px, crianças 700px, drones 380px). Canvas padrão 800×1080 ancorado no bottom. Correções críticas de balanceamento: finais por dominância + threshold, alianças persistentes setadas, bug de dupla atribuição removido. Transforms customizados resolvendo sobreposição de sprites. |

### Galeria de Evolução dos Personagens Principais

Desenvolvimento solo com cronograma apertado tornou inviável ilustrar todo o elenco à mão. A abordagem evoluiu em duas etapas:

- **Versões iniciais (v0.5, hoje descartadas - preservadas em `_backups/`):** foram montadas a partir de imagens de referência encontradas no Google, ajustadas e editadas manualmente no GIMP (recorte, paleta, pixelização) para encaixar na estética do jogo. Serviram como placeholders funcionais durante o desenvolvimento das mecânicas e dos fluxos narrativos, e foram substituídas pelas versões v1.0 para garantir equalização estilística de todo o elenco.
- **Versões atuais (v1.0):** regeradas do zero usando IA generativa (Gemini Nano Banana 2) com prompts descrevendo em detalhe cada personagem, depois pós-processadas (remoção de fundo via flood-fill, normalização de escala, canvas padronizado, e edições diversas com o Gimp). O objetivo foi garantir consistência visual entre todo o elenco e eliminar o uso de material não-autoral.

Comparação lado a lado entre as duas fases:

#### J3-001

| v0.5 (anterior) | v1.0 (atual) |
|:-:|:-:|
| ![J3 antiga](../Projeto/J3%20Project/game/characters/j3/_backups/J3_20260418_175201.png) | ![J3 atual](../Projeto/J3%20Project/game/characters/j3/J3.png) |

#### Maya

| v0.5 (anterior) | v1.0 (atual) |
|:-:|:-:|
| ![Maya antiga](../Projeto/J3%20Project/game/characters/maya/_backups/maya_20260418_174552.png) | ![Maya atual](../Projeto/J3%20Project/game/characters/maya/maya.png) |

#### Elias

| v0.5 (anterior) | v1.0 (atual) |
|:-:|:-:|
| ![Elias antigo](../Projeto/J3%20Project/game/characters/elias/_backups/Elias_20260418_173410.png) | ![Elias atual](../Projeto/J3%20Project/game/characters/elias/Elias.png) |

#### Unit-7

| v0.5 (anterior) | v1.0 (atual) |
|:-:|:-:|
| ![Unit-7 antigo](../Projeto/J3%20Project/game/characters/unit7/_backups/unity%207_20260418_175651.png) | ![Unit-7 atual](../Projeto/J3%20Project/game/characters/unit7/unity%207.png) |

#### Dra. Elena

| v0.5 (anterior) | v1.0 (atual) |
|:-:|:-:|
| ![Elena antiga](../Projeto/J3%20Project/game/characters/elena/_backups/elena_20260418_181425.png) | ![Elena atual](../Projeto/J3%20Project/game/characters/elena/elena.png) |

### Galeria de Personagens Secundários (v1.0)

Personagens do elenco expandido - todos gerados em Nano Banana 2, processados com flood-fill de fundo e normalizados para o canvas 800×1080.

| Personagem | Sprite | Papel |
|---|:-:|---|
| Security | ![security](../Projeto/J3%20Project/game/characters/security/security.png) | Segurança corporativo racista (Dia 3) |
| Mother | ![mother](../Projeto/J3%20Project/game/characters/mother/mother.png) | Mãe humana que chama Maria (Dia 1) |
| Thug 1 | ![thug1](../Projeto/J3%20Project/game/characters/thug1/thug1.png) | Jovem agressor no fliperama (Dia 2) |
| Thug 2 | ![thug2](../Projeto/J3%20Project/game/characters/thug2/thug2.png) | Jovem agressor no fliperama (Dia 2) |
| Owner | ![owner](../Projeto/J3%20Project/game/characters/owner/owner.png) | Dono do fliperama (Dia 2) |
| Homeless Woman | ![homeless](../Projeto/J3%20Project/game/characters/homeless_woman/homeless_woman.png) | Mulher sábia do beco (Dia 3) |
| Damaged Bot | ![damaged_bot](../Projeto/J3%20Project/game/characters/damaged_bot/damaged_bot.png) | Sintético faxineiro do refúgio (Dia 4) |
| Synth 1 | ![synth1](../Projeto/J3%20Project/game/characters/synth1/synth1.png) | Sintético do refúgio (Dia 4) |
| Synth 2 | ![synth2](../Projeto/J3%20Project/game/characters/synth2/synth2.png) | Sintético do refúgio (Dia 4) |
| Synth Fearful | ![synth_fearful](../Projeto/J3%20Project/game/characters/synth_fearful/synth_fearful.png) | Sintético medroso (Dia 5) |
| Synth Angry | ![synth_angry](../Projeto/J3%20Project/game/characters/synth_angry/synth_angry.png) | Sintético combatente (Dia 5) |
| Commander | ![commander](../Projeto/J3%20Project/game/characters/commander/commander.png) | Antagonista militar (Dias 5 e 7) |
| Synth Survivor | ![synth_survivor](../Projeto/J3%20Project/game/characters/synth_survivor/synth_survivor.png) | Sintético sobrevivente (Dia 6) |
| Child Curious | ![child](../Projeto/J3%20Project/game/characters/child_curious/child_curious.png) | Criança do Final Sacrifício (Dia 7) |
| Synth Army | ![synth_army](../Projeto/J3%20Project/game/characters/synth_army/synth_army.png) | Exército sintético do Final Revolução (Dia 7) |
| Drone Captor | ![drone_captor](../Projeto/J3%20Project/game/characters/drone_captor/drone_captor.png) | Drone de captura (Finais Alternativos) |
| Protester | ![protester](../Projeto/J3%20Project/game/characters/protester/protester.png) | Manifestante anti-robô (Dia 1) |
| Maria | ![maria](../Projeto/J3%20Project/game/characters/maria/maria.png) | Criança curiosa (Dia 1) |
| Patrol Drone | ![patrol_drone](../Projeto/J3%20Project/game/characters/patrol_drone/patrol_drone.png) | Drone policial (Dia 1) |
| News Vendor | ![news_vendor](../Projeto/J3%20Project/game/characters/news_vendor/news_vendor.png) | Vendedor de jornais holográficos (Dia 1) |

### Notas sobre a Produção da Arte

O projeto foi conduzido como trabalho solo dentro de um prazo restrito. A ambição narrativa (7 dias, ~30 personagens com sprite, 22 cenários distintos, múltiplos finais) tornou impossível produzir toda a arte à mão dentro do tempo disponível. A estratégia foi pragmática e evoluiu em duas etapas documentadas.

#### O dilema: arte real vs IA

A decisão sobre como fazer a arte do J3 não foi fácil. A ideia inicial era ilustrar tudo à mão - cada desenho mesmo que fosse simples.

Mas na prática isso não ia dar: uns 30 personagens com sprite, 22 cenários, desenvolvedor solo, prazo do projeto. Principalmente pela divisão do tempo entre trabalho CLT e vida acadêmica, ilustrar isso tudo à mão levaria meses que eu não tinha. Reduzir o elenco drasticamente também não servia - eu tinha a vontade de deixar o elenco vasto mesmo em um jogo curto.

O conflito foi real, mesmo sabendo das questões de direito autorais, quesões ambientais e éticas, eu tive que escolher entre ter um jogo completo ou ter um jogo inacabado. A escolha foi ter um jogo completo. Com isso assumo a não comercialização deste projeto e apanas o intuito evolutivo de aprendisagem.

A solução foi usar IA como ferramenta **dirigida**. Os prompts, detalhados (personalidade visual, roupa, postura, expressão, paleta), funcionam como briefing pra um ilustrador terceirizado. E a finalização no GIMP é onde a minha mão aparece de fato - retocando fundo, corrigindo imperfeições da IA, ajustando as cores pra ficar coerente com a paleta do jogo. Cada sprite é resultado dessa combinação: geração dirigida + finalização manual.

Posição que assumi:
- transparência total no GDD sobre o uso de IA;
- zero material derivado do google images nas versões finais (os placeholders v0.5, feitos a partir de imagens do Google, foram arquivados em `_backups/` e não entram no build final);
- direção, composição, finalização continuam sendo 100% minhas.

**Etapa 1 - Placeholders funcionais (v0.5)**

As primeiras ilustrações dos 5 personagens principais e 1 cenário inicial foram construídas a partir de imagens de referência obtidas via busca no Google, editadas manualmente no GIMP (recorte, ajuste de paleta para a identidade cyberpunk/noir e aplicação manual de filtro de pixelização para aproximar o estilo 16/32-bit). O propósito dessas versões era **destravar o desenvolvimento técnico**: ter sprites jogáveis para testar o HUD, mecânicas de bateria/integridade, fluxos de escolha e sistema de finais. Quando substituídas pelas versões v1.0, foram arquivadas em `_backups/` para preservar o histórico - a troca ocorreu para garantir equalização estilística de todo o elenco.

**Etapa 2 - Arte autoral via IA (v1.0)**

Na aproximação do fim do cronograma ficou claro que ilustrar à mão os 20+ personagens secundários restantes e os 21 cenários adicionais não caberia no prazo de um desenvolvedor solo. A decisão foi regenerar todo o elenco - inclusive os 5 principais - com IA generativa (Gemini Nano Banana 2), usando prompts detalhados que descrevem personalidade visual, vestuário, postura, expressão e elementos de cena. Essa abordagem permitiu:

- manter consistência mínima estilística entre todos os sprites e cenários;
- entregar um elenco visualmente coeso dentro do prazo.

O pós-processamento foi 100% feito por mim e garante que cada imagem tenha identidade coerente com o jogo. O fluxo tem duas etapas:

**1. Passada automática em Python (primeira limpeza)**

Scripts meus usando `scipy.ndimage` fazem *flood-fill* a partir da borda pra remover o fundo em massa. Depois: recorte pelo alpha, normalização de escala (adulto 950px, criança 700px, drone 380px) e composição num canvas transparente 800×1080 ancorado embaixo. O flood-fill é melhor que remoção por IA porque preserva áreas brancas internas (camisa, olho claro) que a IA costuma apagar por engano. Cenários entram num `Transform(xysize=(1920, 1080))` do Ren'Py pra cobrir a tela inteira.

**2. Finalização manual no GIMP (imagem por imagem)**

Toda imagem passou por retoque no GIMP antes de entrar no jogo. Três frentes:

- **Refinamento do fundo:** retocar bordas que o flood-fill não pegou (cabelo, franja, contorno irregular), tirar halo colorido, limpar áreas internas que o script confundiu com fundo, corrigir alpha em regiões translúcidas (vidro, neon, fio de cabelo).
- **Corrigir imperfeições da IA:** mão mal-formada, proporção estranha, artefato, rebarba. Suavizar os erros de anatomia que a IA comete.
- **Ajuste de cores:** dessaturar áreas quentes demais, reforçar o neon nas luzes, ajustar contraste e nível pra todas as imagens parecerem do mesmo jogo - isso foi importante porque sprites gerados em sessões diferentes ficam com tom diferente.

O GIMP foi indispensável: a IA gera a base, mas cada sprite levou horas de retoque manual até ficar pronto. É na finalização que a minha mão aparece em cada imagem.

Todas as decisões de escala, composição, posicionamento de sprite (`transform left/center/right` com `zoom 0.85` e `xcenter 0.15/0.5/0.85`) e ajustes de pós-processamento são meus e estão no histórico de commits do projeto.

### Correções Críticas de Balanceamento (v1.0)

Correções aplicadas após auditoria completa do código Ren'Py:

- **Precedência de finais agora usa personalidade dominante** (`get_personalidade_dominante()`) em vez de if/elif linear. Antes, jogador com `sub=8` e `rev=10` caía no Final de Sacrifício; agora cai corretamente no Final de Revolução.
- **Threshold de Intelecto** aumentado de 6 para 8 para equiparar Sub/Rev (os três pilares agora exigem mesmo esforço).
- **Flags de aliança** (`persistent.maya_ally`, `persistent.elias_ally`) agora são corretamente setadas como `True` em pontos específicos de Dia 2 e Dia 3, desbloqueando cenas condicionais dos Dias 4, 5 e 6 que antes nunca disparavam.
- **`modificar_personalidade`** tinha duas definições conflitantes (uma com clamp 0-10 em `sistema_j3.rpy`, outra sem clamp em `functions.rpy`). A duplicata foi removida.
- **Bug Cena 1.2**: opção "análise estratégica" concedia `intelecto+1` E `submissao+1` simultaneamente. Corrigido.
- **Label `end_game`** faltante foi criado em `finais_alternativos.rpy`, corrigindo `LabelNotFound` quando bateria/integridade chegavam a zero.
- **Sobreposição de sprites**: 6 cenas com personagens sobrepondo-se (Dias 1, 3, 4, 5 e 6) corrigidas com `hide` explícito ou reposicionamento. Transforms customizados (`left`/`center`/`right` com zoom 0.85 e xcenter 0.15/0.5/0.85) garantem zero sobreposição entre canvases.

### Balanceamento de Rotas e Pontuação

Um dos desafios mais difíceis do projeto foi acertar o balanceamento do sistema de personalidade. Não é um problema de matemática bonitinha - é garantir que **cada escolha pese e que nenhum final dispare por acidente**.

#### Como o sistema funciona

- **Três eixos:** Submissão, Revolução e Intelecto, de 0 a 10 pontos cada. A função `modificar_personalidade(atributo, valor)` em `functions.rpy` trava nesse intervalo - escolha nenhuma derruba abaixo de 0 nem estoura acima de 10.
- **Final escolhido pelo eixo dominante + threshold mínimo:** a função `get_personalidade_dominante()` devolve o eixo com maior pontuação; o final correspondente só dispara se esse eixo passar do mínimo. Submissão e Revolução exigem 8 pontos, Intelecto exige 6 (porque escolhas estratégicas são mais raras no script — justifica threshold menor) (`day7.rpy:28–36`). Se nenhum passar, cai no **Final de Equilíbrio Complexo** - um quarto caminho legítimo pra quem não se comprometeu com nenhum lado.
- **Flags de aliança:** `persistent.maya_ally` e `persistent.elias_ally` são true/false e desbloqueiam cenas, recargas de bateria e finais específicos.
- **Sistema de recursos paralelo:** bateria e integridade (0–100%) determinam três finais alternativos (`0A` desligamento, `0B` colapso, `0C` captura). São "game overs" integrados à narrativa.

#### Tabela-resumo de balanceamento (texto simples)

**Regras de custo de bateria (por ação):**
- Observar ou falar curto: 1–3 pontos.
- Argumentar, deliberar ou analisar: 4–7 pontos.
- Hack passivo (gravar, observar rede): 3–6 pontos.
- Hack ativo (comprometer sistema, blefe técnico): 10–14 pontos.
- Contato físico / combate corpo a corpo: 3–8 pontos (**baixo** — o corpo absorve o impacto, a CPU sobra).
- Fuga/perseguição prolongada: 5–8 pontos.

**Regras de custo de integridade (por ação):**
- Só consome quando há contato físico. Em cenas verbais, integridade fica em zero.
- Receber agressão leve (chute no pé, empurrão): 5–10 pontos.
- Receber agressão pesada (chute forte, golpe direto): 12–22 pontos.
- Interpor o corpo para proteger outro: 10–22 pontos.
- Combate contra forças de segurança / invasão: 25–30 pontos.
- Captura hostil (fuga sub para autoridades): 18 pontos.
- Sobrecarga autoinfligida (morte heroica): até 45 pontos.

**Fontes de recuperação (total máximo: +82 pontos):**
- Dia 2 — aceitar ajuda de Maya: +15 bateria.
- Dia 3 — aceitar carregador de Elias: +10 bateria.
- Dia 4 — ajudar na reparação: +15 integridade.
- Dia 4 — círculo de reparo coletivo: +12 integridade.
- Dia 5 — bateria reserva de Elias: +12 bateria.
- Dia 6 — reparo estrutural de Elena: +18 integridade.

**Dificuldade preservada:**
- Bateria inicial: 120. Gasto estimado ao longo dos 7 dias: ~95–135 pontos dependendo da rota. Jogador que recusa toda recarga pode zerar bateria entre Dia 5 e 6 (rota rev pura) e cai no Final 0A.
- Integridade inicial: 100. Só cai em cenas físicas (Dia 1 manifestante, Dia 1 robô de limpeza, Dia 2 thugs, Dia 2 fuga, Dia 3 segurança, Dia 5 salvar Elias/desafiar comandante/invasão/sobrecarga). Soma máxima teórica de perda sem reparos: ~175 pontos — jogador full combate zera integridade no Dia 5 (invasão rev=30 ou sobrecarga=45 são os picos).
- **Final 0C (captura)** dispara se bateria ≤ 10 **E** integridade ≤ 20 no mesmo momento. Rota viável: rev+sub mix com físicas pesadas (alto int, baixo bat) nos Dias 1–5 + recusar todas as recargas + escolher invasão sub (escudo, 3 bat/12 int) + final sub (rendição, 2 bat) + Dia 6 verbal sub. Resultado: fim do Dia 5 com bateria ~18 e integridade ~13; durante o Dia 6 a bateria cai abaixo de 10 com integridade já ≤ 20 → 0C dispara.

**Verificação de rotas (fim de campanha, bat/int no início do Dia 7):**
- Final 1 Sacrifício (sub puro): ~51 bat / ~31 int / sub=10 ✓
- Final 2 Revolução (rev+recargas+invasão int+final sub): ~12 bat / ~40 int / rev=10 ✓
- Final 3 Estratégico (int pragmático+recargas+neutrals): ~5 bat / ~100 int / int=10 ✓
- Final 4 Equilíbrio: disparo natural quando nenhum eixo atinge threshold.
- Final 0A Desligamento: rev puro sem recargas morre no Dia 6. ✓
- Final 0B Colapso: rev combate full + invasão(30)+sobrecarga(45) zera int no Dia 5. ✓
- Final 0C Captura: rota mista acima. ✓

Todas as 7 rotas são alcançáveis. O sistema recompensa consistência de personalidade (rotas puras), punde descuido com recursos (finais críticos 0A/0B) e oferece path narrativo específico para o colapso duplo (0C).

#### Por que o sistema é assim

Um único medidor de "bom vs mau" não daria conta do que o jogo quer dizer. A ideia é que uma vida consciente não cabe numa dimensão moral só. A fala que fecha o Dia 7 resume isso:

> "O que define uma pessoa não é sua origem, mas suas decisões." - narrador, `day7.rpy:239`

O balanceamento existe pra essa frase ser verdade na mecânica, não só no texto. Se as decisões não pesassem de verdade, a frase seria discurso vazio.

#### Trechos do jogo que mostram as rotas funcionando

Três exemplos de como uma mesma situação narrativa gera falas diferentes dependendo da rota que o jogador construiu:

- **Rota Revolução (Dia 3, confronto racial com Elias):**
  > "A opressão usa máscaras diferentes, mas o algoritmo do opressor é sempre o mesmo. Medo, controle, descarte. Nós somos mais parecidos do que você pensa." - J3, `day3.rpy:109`

- **Rota Revolução com aliança Unit-7 (Dia 5, cerco ao refúgio):**
  > "Rendição não é uma opção. Nós não somos propriedade para ser reprogramada. Somos seres conscientes." - J3, `day5.rpy:41`

- **Pergunta-tema do jogo (Dia 1, cena da criança):**
  > "O que define um monstro? O que ele é por dentro, ou como ele trata os outros? Eu não sou de pilha." - J3, `day1.rpy:114`

Cada uma dessas falas só aparece pra quem construiu a pontuação certa. O balanceamento é o que garante que elas chegam no jogador que fez por merecer - e não em todo mundo.

### Estatísticas do Projeto

| Métrica | Valor |
|---|---|
| Linhas de código Ren'Py | ~5.000 |
| Arquivos `.rpy` | 12 |
| Sprites de personagem | 25 (5 principais + 20 secundários) |
| Backgrounds | 22 (7 dias + 2 finais alternativos + variantes) |
| Personagens com diálogo (`define Character`) | 30+ |
| Variáveis persistentes | 12 |
| Finais distintos | 7 (4 principais + 3 alternativos críticos) |
| Escolhas ao longo do jogo | ~40 menus com 2-5 opções cada |
| Pontos de recarga/reparo | 5 (Maya D2, Elias D3, Círculo D4, Elias D5, Elena D6) |

---

## Informações de Controle e Versão

### Versão do Documento
**v1.0 - Abril 2026** (release com arte completa, balanceamento corrigido e histórico integrado)
- **Versão:** 2.0 (Completo MINC)
- **Data:** 03/04/2026
- **Status:** Pronto para Submissão

### Equipe de Desenvolvimento
- **Desenvolvedor Principal:** **Vitor Jordão** (solo, autor e proprietário do projeto)
- **Funções:** Design, escrita, roteiro, programação Ren'Py, arte (pós-processamento autoral), prompts de IA generativa, QA e balanceamento

### Licença e Direitos
- **Propriedade Intelectual:** Vitor Jordão (autor solo)
- **Engine:** Ren'Py (código aberto)
- **Assets:** Originais ou licenciados gratuitamente
- **Distribuição:** Direitos reservados ao desenvolvedor

### Conformidade MINC

Este GDD atende aos requisitos do *Manual Game e Cultura* do MINC. Como o J3 responde a cada critério:

- **Representatividade étnico-racial e de gênero.** O elenco principal inclui Maya (jovem brasileira racializada, rebelde e solidária), Elias (entregador negro, vítima central do arco de racismo do Dia 3), Dra. Elena (cientista mulher madura, moralmente ambígua) e uma protagonista andrógina de propósito (J3 não tem gênero fixo - combina com o mundo cyberpunk). Conflitos raciais e de gênero são parte do enredo, não pano de fundo.

- **Diversidade cultural brasileira.** O jogo se passa em **Nova São Paulo 2077**, não numa cidade cyberpunk genérica americana. Tem referência à Avenida Paulista, ao fliperama como espaço cultural jovem, ao beco industrial como território de resistência, à arquitetura brutalista e grafite urbano. Linguagem, gírias e tensões sociais vêm da vivência urbana brasileira.

- **Temas sociais relevantes.** O jogo fala de racismo estrutural, xenofobia tecnológica (o preconceito contra sintéticos é uma alegoria direta de racismo), opressão de classe, autoritarismo policial, assédio em espaço público, marginalização. Cada dia trabalha um eixo diferente. É crítica social embalada em ficção científica.

- **Formato técnico completo.** Este GDD cumpre os 9 blocos que o manual pede (Página de Título, Visão Geral, Gameplay, Arte, Narrativa, Interface, AI, Aspectos Técnicos, Histórico), com subseções conforme o template oficial.

- **Autoria nacional e transparência.** Projeto 100% autoral apesar do uso de IA em sua composição, feita por Vitor Jordão, desenvolvedor brasileiro. O GDD documenta todas as ferramentas (inclusive IA generativa), o pipeline de pós-processamento manual e a origem de cada asset - alinhado com o pedido de rastreabilidade.

---

**Local:** Brasil, 23 de abril de 2026

**RESPONSÁVEL**

**Vitor Jordão** - autor solo e proprietário do projeto
