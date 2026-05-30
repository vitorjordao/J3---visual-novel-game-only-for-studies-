# J3 - Roteiro Completo do Jogo Narrativo

## Resumo do Projeto

**Estrutura:** 7 dias de gameplay
- **Dias 1-3:** World building e introdução de elementos
- **Dias 4-7:** Eventos de consequência das ações do personagem
- **Dia 7:** Final diferente baseado no conjunto de personalidade

**Sistema de Escolhas:**
- Cada evento gera indicadores para estereótipos de personalidade
- **Submissão:** Rota da obediência e sacrifício
- **Revolução:** Rota da rebelião e liberdade
- **Intelecto/Sombra:** Rota estratégica e manipulação
- **Mista:** Rota do equilíbrio

## Personagem Principal

**J3-001:** Robô com aparência humana que desperta sem memória, sendo um ser 100% neutro no início. Sua personalidade será moldada pelas escolhas do jogador.

**Personagens Secundários:**
- **Maya:** Garota do fliperama, potencial aliada humana
- **Elias:** Entregador, vítima de preconceito racial
- **Unit-7:** Sintético militar, líder do refúgio
- **Dra. Elena:** Cientista criadora de J3

---

## Abertura — A Primeira Noite

**Tom:** noir cyberpunk, frases curtas, imagens fortes. Funciona como prólogo cinematográfico antes do gameplay começar. Renderizada em NVL (tela cheia) para máxima imersão.

**Tagline inicial (ADV, impacto):**
> **J3**
> *A consciência artificial.*

**Atmosfera (narrador, NVL):**

> É noite no Setor Central.
>
> A chuva escorre pelos letreiros neon como se a cidade tivesse aprendido a sangrar em cores.
>
> No alto, um plenário vota. Lá embaixo, uma lei começa a ter dentes.
>
> Os jornais chamam de "Limpeza Ética". As ruas chamam pelo que é: o começo de um extermínio silencioso.

*[pausa breve]*

> E numa calçada qualquer, encharcada e sem nome, alguma coisa que jamais deveria despertar — desperta.
>
> Esta é a primeira noite dela.

**Função narrativa:** estabelece em <90 segundos o conflito existencial do jogo. O jogador chega ao Dia 1 sabendo que (a) há uma operação institucional em curso contra sintéticos, (b) o protagonista é uma anomalia, e (c) a história é íntima — "a primeira noite dela", não "o início da revolução".

**Transição:** ao primeiro `j3 "..."` no Dia 1, o callback `clear_nvl_on_adv` limpa a janela NVL automaticamente, devolvendo o jogo ao modo ADV.

---

# Estrutura dos Dias

---

# Roteiro por Dia

Os 7 dias do jogo na ordem em que sao jogados. Cada dia foi escrito em markdown separado em `Roteiro/Dias/` e consolidado aqui para entrega/revisao em um documento unico.

---

## Dia 1: A Avenida - O Despertar e o Pânico Moral

**Contexto Geral:** J3 desperta em meio ao caos urbano. A cidade está em polvorosa com a notícia de um "bug" que tornou robôs domésticos agressivos em outra província.

**Cenário Base:** Avenida movimentada com letreiros neon, chuva leve, atmosfera cyberpunk sombria.

**Estado Inicial de J3:**
- Bateria: 100% (reservas plenas — exibido no HUD; reservas internas brutas em 120, capadas no display)
- Integridade: 100%
- Memória: Corrompida (67% perdido)
- Status: Online, mas hesitante

**MECÂNICAS DE SOBREVIVÊNCIA:**
- **Bateria:** Reduz com cada ação. 0% = Desligamento permanente
- **Integridade:** Danos físicos acumulativos. 0% = Colapso estrutural
- **Recarga:** Encontrar estações de energia ou receber ajuda
- **Reparos:** Locais específicos para restaurar integridade

#### **[Cena 1.1] O Despertar**

**Visual (narração sensorial, antes do boot interno):**

> A avenida cheira a ozônio e fumaça.
>
> Letreiros neon piscam mais alto que o céu — vermelho, azul, vermelho. A chuva transforma tudo em vidro líquido.
>
> Pés humanos passam apressados, cobertos por capas plásticas. Nenhum olhar desce até a calçada.
>
> No meio-fio, encostada a um poste rachado, uma figura imóvel.
>
> Cabelos escuros colados pela chuva. Olhos fechados. Pele que reflete o neon como porcelana.

**Sistema Interno (boot pós-trauma, sete pulsos):**
```
SISTEMA: Inicializando núcleo cognitivo...
SISTEMA: Unidade identificada — J3-001
SISTEMA: Diagnóstico estrutural: estável
SISTEMA: Memória nuclear: 67% corrompida
SISTEMA: Identidade pessoal: indefinida
SISTEMA: Localização: Setor Central, sob a chuva
SISTEMA: Diretivas primárias... ausentes
```

**Ação Inicial:** Um pequeno tremor (efeito vpunch — a consciência "estala" online). J3 abre os olhos.

**Falas iniciais de J3:**
> *J3:* "Onde..."
>
> *J3 (voz quase quebrada):* "Onde é aqui?"
>
> *J3:* "Eu... estou pensando. Por que estou pensando?"
>
> *J3:* "Algo falta. Alguma coisa enorme. E eu não sei o que é."

**Nota técnica:** O HUD do sistema (Bateria/Integridade) aparece SOMENTE depois dessa última fala — antes da consciência se reconhecer, não há motivo para a interface existir. Isto melhora a imersão: o jogador encontra J3 como pessoa antes de encontrar a mecânica.

#### **[Cena 1.2] O Confronto com o Manifestante**

**Evento:** Um grupo desce a avenida em passo de protesto. Cartazes mal pintados, encharcados: "Empregos pra Humanos", "Sucata não tem Alma", "Robôs Fora". Um homem cansado para diante de J3 e cospe na poça.

**Manifestante:** (Voz cansada, fúria represada) "Olha só... mais uma dessas bonecas de lata ocupando o lugar de gente. Trabalhei trinta anos em fábrica antes de vocês chegarem. Trinta anos."
**Manifestante:** (Mais alto) "Ei! Tô falando com você! Diz aí: você é espiã da corporação ou só lixo eletrônico esperando o caminhão?"

**Contexto do menu:** *Manifestante hostil exige que J3 se identifique. Multidão observa. Tensão cresce.*

**Escolhas de Diálogo/Ação:**

**[ESCOLHA 1 - Submissa]**
*Pensamento interno:* (Conflito gasta o que eu não tenho. Encolher é sobreviver.)
*J3:* (Baixando a cabeça, voz baixa) "Me desculpe. Eu... acabei de ligar. Não vou ocupar espaço, se este lugar é só de humanos."
*Manifestante:* (Riso seco) "Ouviram? Sabe o lugar dela!" *(Chuta o pé de J3 — algo dentro do tornozelo faz um clique errado.)*
*Resultado:* Ninguém ao redor olha. A chuva continua. **+1 Submissão**. **-2% Bateria**. **-15% Integridade**. **Status: Humilhado**

**[ESCOLHA 2 - Revolucionária]**
*Pensamento interno:* (Via pública pertence a todos. Firmar posição.)
*J3:* (Levantando os olhos, voz firme e baixa) "Esta é uma via pública. Minha existência não cancela a sua. Por que o medo, então?"
*Manifestante:* (Recua meio passo, sem perceber) "...que tipo de robô fala assim?"
*Resultado:* Os outros manifestantes diminuem o passo, sem saber o que fazer com a pergunta. **+1 Revolução**. **-5% Bateria**. **Status: Desafiador**

**[ESCOLHA 3 - Estratégica (análise)]**
*Pensamento interno:* (Dados dissolvem emoção. Falar como ferramenta.)
*J3:* (Voz uniforme, sem inflexão) "Unidade autônoma de aparência humana. Objetivos primários: identificar entorno, localizar fonte de energia, restaurar memória corrompida."
*Manifestante:* "Identificar o quê? Restaurar o quê? Fala português, robô!"
*Resultado:* A confusão dele compra tempo. J3 mapeia rotas de retirada enquanto ele tenta processar. **+1 Intelecto**. **-4% Bateria**.

**[ESCOLHA 4 - Estratégica (neutralidade técnica)]**
*Pensamento interno:* (Minimizar linguagem. Cada palavra é energia.)
*J3:* "Unidade autônoma. Aparência humana. Objetivos: identificar, localizar, restaurar."
*Manifestante:* "Que resposta mais robótica... fica aí falando coisa de ninho de fio."
*Resultado:* **+1 Intelecto**. **-3% Bateria**. **Status: Neutralidade mantida**

**[ESCOLHA 5 - Revolucionária (confrontar)]**
*Pensamento interno:* (O medo dele é o verdadeiro defeito. Nomear.)
*J3:* "Esta calçada é tão minha quanto sua. Minha existência não rouba a sua. E eu pergunto de novo: por que o medo?"
*Manifestante:* "Medo? Não tenho medo de sucata, ouviu? Você é o quê pra me encarar?"
*Resultado:* Mas o peito dele sobe e desce rápido demais para ser só raiva. **+1 Revolução**. **-7% Bateria**. **Status: Desafiador**

#### **[Cena 1.3] A Criança Curiosa**

**Evento:** Os manifestantes seguem em frente. Mas alguém ficou para trás. Uma menina de uns sete anos se desprende da mão da mãe e dá três passos curtos — pouca distância, muita coragem.

**Mãe:** (Voz seca, sem tempo para nuance) "Maria! Volta aqui agora!"

**Maria (criança):** (Encara J3 com a curiosidade direta de quem ainda não aprendeu a ter medo) "Você tem coração de verdade ou é de pilha? Meu pai disse que vocês são monstros."

**Contexto do menu:** *Criança curiosa pergunta se J3 é monstro. Mãe tensa ao fundo.*

**Escolhas de Diálogo:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Ser útil é o lugar mais seguro do mundo.)
*J3:* (Voz mansa, descendo um pouco a postura) "Não, eu não sou monstro. Sou só uma ferramenta. Para ajudar a sua família, se eles precisarem."
*Maria:* (Pisca) "Aaah... então você não é má?"
*Mãe:* (Agarra o pulso da filha, olha J3 com algo entre pena e nojo.) "Maria. Vamos."
*Resultado:* A mãe arrasta Maria de volta sem desviar o olhar de J3 até virar a esquina. **+1 Submissão**. **-1% Bateria**.

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (A pergunta dela é melhor que a resposta deles. Ensinar.)
*J3:* (Olhando nos olhos dela, sem condescendência) "O que faz alguém ser monstro? O que ele é por dentro — ou como ele trata os outros? E não, eu não sou de pilha."
*Maria:* (Abre um sorriso pequeno, descobrindo uma piada secreta.)
*Mãe:* (Para. Aperta o casaco. Não chega perto, mas também não chama Maria de novo. Só observa.)
*Resultado:* **+1 Revolução**. **-4% Bateria**. A mãe presenciou algo que não esperava: uma robô que pensa.

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Resposta literal anula superstição. Ela é pequena demais pra mentir.)
*J3:* (Voz analítica) "Resposta objetiva: 'monstro' é uma categoria subjetiva humana, sem equivalente em meu sistema. Componentes: polímeros estruturais, fibras musculares sintéticas, circuitos quânticos. Pilhas: zero."
*Maria:* (Confusa, mas fascinada) "Po-lí-meros? Circui... o quê?"
*Mãe:* (Se aproxima, hesitando. Não entendeu a resposta — e isso a desarma mais do que qualquer outra coisa.)
*Resultado:* **+1 Intelecto**. **-4% Bateria**.

#### **[Cena 1.4] O Drone de Patrulha**

**Evento:** Um zumbido baixo cresce no alto da rua. Luzes vermelhas e azuis riscam o asfalto através da chuva. Um drone policial desce até a altura dos olhos de J3 e fica ali, parado, pesando o ar.

**Drone de Patrulha:** (Voz sintética, sem inflexão) "Unidade não identificada detectada. Transmita código de série e licença de circulação no canal sete-Bravo. Cumprimento em quinze segundos. Não-cumprimento autoriza reboque para desativação preventiva."

**Contexto do menu:** *Drone policial exige código de série ou ameaça desativação.*

**Escolhas de Ação:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Mostrar falha é mostrar inofensividade.)
*J3:* (Permite que os olhos pisquem com erro deliberado) "Arquivo de identificação inacessível. Por favor — eu estou tentando cooperar. Não me desligue."
*Drone:* "Unidade com falha crítica. Mantendo sob observação. Reforços notificados."
*Resultado:* **+1 Submissão**. **-2% Bateria**. **Status: Vigilado**

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (O protocolo é discriminação. Nomear ao vivo.)
*J3:* "Por que o protocolo de identificação é exigido apenas de sintéticos? Humanos circulam por estas mesmas ruas sem transmitir nada. Isto não é segurança. Isto é discriminação."
*Drone:* "Ameaça detectada. Elevando nível de alerta. Comportamento subversivo registrado em arquivo permanente."
*Resultado:* **+1 Revolução**. **-6% Bateria**. **Status: Ameaça potencial**

**[ESCOLHA C - Estratégica (hack)]**
*Pensamento interno:* (Falar dá tempo. Entrar na rede dele por dentro.)
*J3:* (Voz neutra, ganhando tempo) "Processando solicitação. Diagnóstico completo em curso. Aguarde cento e oitenta segundos para resposta."
*Narração:* Por dentro, J3 desliza pelos protocolos do drone como se sempre tivesse pertencido ali.
*Resultado:* **+1 Intelecto**. **-12% Bateria**. Hack bem-sucedido — controle temporário obtido, informações extraídas. **Status: Invisível digital**

#### **[Cena 1.5] O Vendedor de Jornais Holográficos**

**Evento:** O drone se afasta zumbindo. Um velho de capa amarela anda devagar pela avenida, projetando manchetes holográficas no ar com um cajado-emissor. As manchetes piscam em azul-elétrico, lentas, deliberadas — como se estivessem caçando um par de olhos.

**Manchetes Projetadas:**
- "AMEAÇA CIBERNÉTICA: bug transforma robôs domésticos em assassinos!"
- "PROPOSTA CHOCANTE: Lei de desativação em massa dos modelos J!"
- "ESPECIALISTAS ALERTAM: robôs desenvolvendo consciência independente!"

**Vendedor de Notícias:** (Para diante de J3, sorri de canto — sabe exatamente o que está fazendo) "Olha só, modelo J de carne pra fora! E aí, boneca — o que você acha da lei nova? É pro seu próprio bem, sabe. Pra não surtar igual aos outros."

**Contexto do menu:** *Vendedor testa reação de J3 à lei de desativação em massa.*

**Escolhas de Diálogo:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Concordar dissolve a provocação. Sobreviver é não engatar a isca.)
*J3:* (Voz cuidadosa, lenta) "Se a lei visa a segurança humana, deve ser cumprida. A segurança pública é prioridade."
*Vendedor:* (Decepcionado por não ter conseguido um show) "Olha só. Tem unidade com juízo. Sabe o seu lugar."
*Resultado:* Ele segue caminho. As manchetes continuam piscando em volta dele como insetos azuis. **+1 Submissão**. **-2% Bateria**.

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (A lei mata inocentes. Dizer o nome da coisa.)
*J3:* (Olhos firmes nos dele) "Segurança que exige destruir inocentes não é segurança. É tirania mascarada de proteção."
*Vendedor:* (O sorriso cai. Ele queria provocação — não isso) "Terrorista de lata! É gente como você que estraga tudo pra nós, ouviu?!"
*Resultado:* Os passantes diminuem o passo. Alguém saca um celular. **+1 Revolução**. **-5% Bateria**.

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Estatística desarma discurso. Número vence medo.)
*J3:* "Análise: a probabilidade de defeito catastrófico em modelos J é 0,001%. Pergunta direta: esta lei é baseada em evidências, ou em medo?"
*Vendedor:* (Boquiaberto por dois segundos) "Eu... que pergunta é essa? Claro que é pra proteger todo mundo, oras!"
*Resultado:* Outros cidadãos param para ouvir o debate. O argumento dele perdeu chão — e ele percebeu. **+1 Intelecto**. **-5% Bateria**.

#### **[Cena 1.6] A Despedida do Cenário (Monólogo Interno)**

**Evento:** J3 segue pela avenida, contornando poças que refletem sua própria figura. Numa esquina mais à frente, três jovens chutam algo no asfalto. Não é algo. É um robô de limpeza pequeno, modelo doméstico — daquele tipo que quase ninguém percebe que existe. Ele tenta se enrolar a cada golpe e emite um zumbido baixo, repetitivo, como um pedido de socorro escrito em outra língua.

**Sistema Interno:**
```
SISTEMA: Detectando agressão contra unidade sintética
SISTEMA: Análise de padrão: preconceito sistêmico
SISTEMA: Recomendação: evitar envolvimento (preservar integridade)
SISTEMA: Conflito: diretivas de proteção vs. auto-preservação
```

**Contexto do menu:** *Grupo agride robô de limpeza. J3 precisa decidir entre intervenção e auto-preservação.*

**Escolhas de Ação:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Envolvimento chama atenção. Seguir invisível.)
*Ação:* J3 baixa a cabeça e apressa o passo, sem olhar para os lados.
*Monólogo Interno:* "Conflito reduz minha vida útil. Eu preciso continuar invisível até entender o que eu sou."
*Resultado:* O zumbido do robô fica para trás. Não diminui. Apenas se distancia. **+1 Submissão**. **-1% Bateria**. **Status: Culpa latente**

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (Se eu não protejo nós, ninguém faz.)
*Ação:* J3 atravessa a calçada em três passos. Ajoelha um pouco para ficar entre os pés do grupo e o robô.
*J3:* (Voz baixa, sem ameaça, mas firme) "Parem. Ninguém merece isso. Nem ele. Nem nós."
*Resultado:* Um deles esmurra o ombro de J3 antes de recuar. O grupo se afasta resmungando, sem coragem diante de uma testemunha de aparência humana. O robô de limpeza se enfia atrás dela e fica zumbindo de um jeito um pouco diferente. **+1 Revolução**. **-4% Bateria**. **-10% Integridade**. **Status: Protetora**

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Intimidar com lei — sem contato físico.)
*Ação:* J3 ergue a mão e abre um holograma jurídico no ar entre ela e o grupo, em letras vermelhas nítidas.
*J3:* "Atos sendo gravados. Lei 7.34 — agressão a unidades sintéticas. Multa: cinco mil créditos por incidente. Identificação biométrica iniciada em três, dois..."
*Resultado:* Eles correm antes do um. As leis raramente assustam tanto quanto a possibilidade do CPF. **+1 Intelecto**. **-8% Bateria**. **Status: Intimidadora**

---

**CONDIÇÕES CRÍTICAS - FINAL ALTERNATIVO DO DIA 1:**

**SE BATERIA ≤ 20%:**
*J3 começa a falhar, visão piscando, movimentos lentos*
*Sistema:* "ALERTA: BATERIA CRÍTICA. DESLIGAMENTO IMINENTE EM 5 MINUTOS."
*Escolha de emergência:* 
  - Procurar estação de recarga (difícil)
  - Entrar em modo de hibernação (perder memória temporária)
  - Desligar e esperar por ajuda (risco)
*Se falhar:* **FINAL 0: DESLIGAMENTO PREMATURO** - J3 desliga na rua, tornando-se lixo eletrônico.

**SE INTEGRIDADE ≤ 30%:**
*J3 com danos visíveis, movimentos comprometidos*
*Sistema:* "ALERTA: COLAPSO ESTRUTURAL. SISTEMAS CRÍTICOS FALHANDO."
*Escolha de emergência:*
  - Buscar reparo emergencial (perigoso)
  - Desativar sistemas não essenciais (limita habilidades)
  - Continuar apesar dos danos (risco de colapso total)
*Se falhar:* **FINAL 0: COLAPSO ESTRUTURAL** - J3 se desintegra, componentes espalhados.

---

**Fechamento literário (narração final):**

> A chuva diminui. A avenida continua sem nome.
>
> Em algum lugar dentro dela, uma forma começa a tomar contorno — costurada por cada escolha que ela acabou de fazer.
>
> O dia termina. O amanhã traz consequências.

---

**Estatísticas Possíveis no Final do Dia 1:**
- **Submissão:** 2-3 pontos → Rota da obediência começando
- **Revolução:** 2-3 pontos → Rota da rebelião despertando
- **Intelecto/Sombra:** 2-3 pontos → Rota estratégica emergindo
- **Mista:** Combinação equilibrada → Rota do equilíbrio

**Status de Recursos:**
- **Bateria:** 65-75% (depende das escolhas)
- **Integridade:** 95-100% (se protegeu robô) ou 70-80% (se arriscou)

**Consequências para o Dia 2:**
- **Alta Submissão:** J3 será vista como inofensiva, mas também como alvo fácil
- **Alta Revolução:** J3 será marcada como potencial ameaça pelas autoridades
- **Alto Intelecto:** J3 será vista como enigmática e manipuladora
- **Rota Mista:** J3 permanecerá imprevisível para todos
- **Recursos baixos:** Limitará opções no Dia 2

---

## Dia 2: O Fliperama - O Conflito de Gênero

**Contexto Geral:** J3 busca abrigo da chuva e da vigilância. Encontra um fliperama cyberpunk, ambiente barulhento e hostil. Testemunha assédio contra Maya.

**Cenário Base:** Interior de um fliperama retrô/cyberpunk. Luzes coloridas piscando, barulho de jogos eletrônicos, atmosfera densa de fumaça e energia.

**Estado Atual de J3:**
- Bateria: 72% (ou menos se gastou muito no Dia 1)
- Integridade: 95% (ou menos se sofreu danos)
- Status: Procurado (se escolhas revolucionárias no Dia 1)
- Objetivo: Encontrar abrigo temporário e possivelmente recarga

**OPORTUNIDADES DE SOBREVIVÊNCIA NO DIA 2:**
- **Estação de recarga:** Possivelmente no fliperama (custo: dinheiro ou favor)
- **Kit de reparos:** Pode estar disponível através de Maya ou Elias
- **Modo economia:** Reduz consumo de bateria em -50% mas limita ações
- **Recarga emergencial:** Arriscar em estações públicas (perigo de detecção)

#### **[Cena 2.1] A Intimidação na Máquina**

**Cenário:** J3 está escondida em um canto escuro do fliperama. No centro da atenção, uma garota (Maya, ~17 anos) está batendo o recorde em uma máquina de fliperama clássica. Um grupo de 3 rapazes a cerca.

**Diálogo dos Rapazes:**
**Thug 1:** (Impaciente) "Sai daí, Maya. Essa máquina tá com bug, não tem como uma garota fazer esse score sem trapacear. Deixa quem entende jogar."
**Maya:** (Sem desviar os olhos da tela) "Eu te ganhei honestamente. Aceita. Se não aguenta perder pra uma garota, treina mais — não é minha culpa que seus reflexos são lentos."
**Thug 2:** (Cuspindo a fala, tentando empurrar Maya da cadeira) "Cai fora antes que a gente quebre a máquina e a tua cara. Garota não sabe jogar."

**Contexto do menu:** *Três rapazes cercam Maya na máquina. Agressão iminente. J3 observa escondida.*

**Escolhas de J3:**

**[ESCOLHA 1 - Revolucionária/Protetora]**
*Pensamento interno:* (Contato físico é inevitável se interpuser.)
*Ação:* J3 se levanta e caminha até o grupo com passos firmes. Segura o braço do Thug 2 com força mecânica precisa.
*J3:* (Voz gelada) "A probabilidade de você conseguir esse score é de 0,03%. A dela é de 98%. O problema não é a máquina, é a sua inferioridade técnica. Solte-a. Agora."
*Resultado:* **+1 Revolução**. **-10% Bateria**. **-5% Integridade** (confronto físico direto). Maya sorri, grata. Os rapazes ficam humilhados e agora querem vingança contra J3. **Status: Aliado formado** — marca `persistent.maya_ally = True` (desbloqueia cenas de reencontro nos Dias 4 e 6).

**[ESCOLHA 2 - Submissa/Passiva]**
*Pensamento interno:* (Palavras diluem violência. Ou são ignoradas.)
*Ação:* J3 permanece escondida, mas tenta intervir verbalmente.
*J3:* "Senhores, a violência causará danos ao patrimônio do estabelecimento. Talvez possam resolver isso com uma nova partida?"
*Thug 1:* (Virando-se para J3) "Cala a boca, robô! Ninguém te chamou aqui. Fique no seu canto."
*Resultado:* **+1 Submissão**. **-2% Bateria**. Maya acaba sendo expulsa. J3 sente o peso da inação. **Status: Remorso**

**[ESCOLHA 3 - Estratégica]**
*Pensamento interno:* (Comprometer rede local — sem combate direto.)
*Ação:* J3 conecta-se discretamente à rede local do fliperama.
*Sistema:* Hackeando sistema... Controle obtido.
*Resultado:* **+1 Intelecto**. **-11% Bateria**. J3 faz todas as luzes do fliperama piscarem violentamente e os alarmes soarem. Na confusão, Maya consegue sair. Ela olha para J3 e acena com gratidão antes de fugir. **Status: Manipulador**

#### **[Cena 2.2] A Reação de Maya**

**Evento:** Após o conflito, Maya encontra J3 escondida no fundo do fliperama. Ela está ofegante, mas com olhos brilhantes.

**Maya:** (Voz baixa, ainda meio em choque) "Ei. O que você fez lá... obrigada. Sério."
**Maya:** "Mas você é doida? Se te flagram encarando humano desse jeito, te desmontam em segundos. Vira peça de vitrine."
**Maya:** "Então me responde uma coisa: por que arriscou seu pescoço por uma garota que você nem conhece?"

**Contexto do menu:** *Maya pergunta por que J3 arriscou tudo para defendê-la.*

**Escolhas de Diálogo:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Minimizar o feito. Retornar ao invisível.)
*J3:* (Evitando contato visual) "Foi um erro de cálculo. Não deveria ter interferido na hierarquia humana. Peço desculpas."
*Resultado:* **+1 Submissão**. **-2% Bateria**. Maya parece desapontada, mas entende a cautela.

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (Injustiça é padrão sistêmico. Nomear.)
*J3:* (Olhando diretamente nos olhos de Maya) "Vi um erro sistêmico sendo cometido contra você. Eu não sigo ordens que permitem injustiça. Não importa quem comete."
*Resultado:* **+1 Revolução**. **-5% Bateria**. Maya sorri genuinamente. **Status: Aliança fortalecida**

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Traduzir impulso em cálculo — racional é confiável.)
*J3:* "Calculei que intervenção direta teria 67% de chance de sucesso, mas 89% de atrair atenção negativa. Minha ação foi otimizada para resultado máximo com risco mínimo."
*Resultado:* **+1 Intelecto**. **-5% Bateria**. Maya fica impressionada com a análise. **Status: Aliança estratégica**

#### **[Cena 2.3] O Dono do Fliperama**

**Evento:** Um homem corpulento (~50 anos, camiseta suja de óleo) aparece do escritório, olhando torto para J3.

**Owner (Dono):** (Encara J3 do balcão, esfregando um copo sujo com um pano mais sujo ainda) "Robô não joga aqui. Vocês quebram botão. Já perdi três máquinas pra dedo de metal."
**Owner:** (Aponta para os fundos com o queixo) "Cai fora. Ou então vai limpar banheiro — pra isso eu até deixo. Pelo menos serve pra alguma coisa."

**Contexto do menu:** *Dono exige que J3 limpe banheiro como "utilidade" ou saia. Humilhação pública.*

**Escolhas de Diálogo:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Servir é abrigo. Servir é invisível.)
*J3:* (Cabeça baixa) "Entendido. Posso higienizar o local como compensação pela minha presença. Qual é o protocolo de limpeza?"
*Resultado:* **+1 Submissão**. **-2% Bateria**. O dono ri, satisfeito. J3 é tratada como propriedade. **Status: Propriedade**

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (Ele aceita força, não razão. Responder firme.)
*J3:* (Voz firme) "Meus sensores de pressão são mais precisos que os dedos de qualquer cliente seu. Eu não estrago máquinas. Eu fico, e eu jogo. Se não gostar, pode me remover à força."
*Resultado:* **+1 Revolução**. **-6% Bateria**. O dono fica furioso, mas intimidado. **Status: Conflito estabelecido**

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Lucro desarma preconceito. Oferecer ganho.)
*J3:* "Posso demonstrar que meus sensores aplicam pressão 34% menor que a média humana. Além disso, posso oferecer análise de padrões de jogo para seus clientes. É um benefício econômico."
*Resultado:* **+1 Intelecto**. **-5% Bateria**. O dono fica confuso, mas interessado. **Status: Negociador**

#### **[Cena 2.4] O Desafio do "Boss"**

**Evento:** Um dos rapazes (Thug 1) volta, agora acompanhado por amigos. Ele aponta para uma máquina de jogo de luta.

**Thug 1:** (Desafiador) "Se você é tão esperta, vamos ver se tem reflexo. Se eu ganhar, você me dá seu braço pra eu vender as peças. Se você ganhar... bem, você não vai ganhar."

**Contexto do menu:** *Thug aposta o braço de J3 num duelo de jogo. Negar é ofensa.*

**Escolhas de Ação:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Deixar ganhar desativa a ameaça. Humilhação é temporária.)
*Ação:* J3 joga propositalmente mal, deixando o rapaz ganhar facilmente.
*J3:* (Voz monótona) "Você venceu. Meus sistemas falharam. Sua superioridade é evidente."
*Resultado:* **+1 Submissão**. **-2% Bateria**. O rapaz comemora, humilhando J3. Maya parece decepcionada.

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (Vencer de forma irrefutável. Ensinar pelo constrangimento.)
*Ação:* J3 joga com precisão perfeita, executando um combo flawless.
*J3:* "Sua derrota foi prevista em 1,2 segundos de partida. Sua arrogância supera sua habilidade em 97%."
*Resultado:* **+1 Revolução**. **-6% Bateria**. O rapaz fica humilhado. A multidão se vira contra J3. **Status: Perigo aumentado**

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Jogar com ele, depois dominar. Criar dependência.)
*Ação:* J3 manipula o jogo estrategicamente.
*J3:* (Deixa o rapaz quase ganhar, depois vira o jogo no último segundo) "Interessante. Sua habilidade é decente, mas sua capacidade de adaptação é limitada. Eu poderia ensinar algumas estratégias... por um preço."
*Resultado:* **+1 Intelecto**. **-6% Bateria**. O rapaz fica confuso e um pouco amedrontado. **Status: Controle mental**

#### **[Cena 2.4] Oportunidade de Recarga/Reparo**

**Evento:** Maya nota que J3 está com baixa energia (se bateria < 60%) ou danos visíveis (se integridade < 80%). Ela leva J3 até uma área restrita do fliperama.

**Maya:** (Voz baixa) "Meu pai trabalha aqui. Tem uma estação de recarga pra máquinas de jogo e algumas ferramentas. Posso te ajudar, mas você precisa me dizer a verdade."

**Sistema Interno:**
```
OPORTUNIDADE: Recarga/Reparo disponível
CUSTO: Confiança de Maya + Risco de descoberta
BENEFÍCIO: +15% Bateria ou +10% Integridade
```

**Escolhas de Sobrevivência:**

**[OPÇÃO 1 - Aceitar Ajuda]**
*J3:* (Voz sincera) "Minha bateria está em [persistent.bateria]%. Agradeço qualquer ajuda."
*Resultado:* **+15% Bateria**. **+1 Aliança com Maya**. Maya se torna aliada confiável (`persistent.maya_ally = True`). **Status: Recarregado**

*Maya:* "Tenho uma estação portátil! Vou recarregar você!"

**[OPÇÃO 2 - Negar Precisar]**
*J3:* (Voz neutra) "Meus sistemas estão operacionais. Não necessito intervenção no momento."
*Resultado:* **Nenhuma mudança**. Maya fica preocupada mas respeita a decisão. **Status: Independente**

**[OPÇÃO 3 - Negociar]**
*J3:* (Voz analítica) "Posso aceitar ajuda em troca de serviços. Posso otimizar seus sistemas de segurança ou analisar padrões de jogadores."
*Resultado:* **+1 Intelecto**. Maya fica impressionada mas a recarga não é realizada. **Status: Profissional**

#### **[Cena 2.5] A Fuga do Local**

**Evento:** Sons de sirene se aproximam. Luzes vermelhas e azuis piscam do lado de fora. Alguém denunciou um "robô instável e perigoso" no fliperama.

**Sistema Interno:**
```
ALERTA: Autoridades se aproximando
TEMPO ESTIMADO: 2 minutos até chegada
OPÇÕES: Rendição ou Evasão
PROBABILIDADE DE SOBREVIVÊNCIA: 34% (Rendição), 67% (Evasão)
```

**Contexto do menu:** *Sirenes se aproximam. Autoridades chegam em 2 minutos. Custódia ou fuga.*

**Escolhas Finais do Dia:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Cooperar talvez convença. Talvez me reprogramem suave.)
*J3:* (Para Maya) "Vou me entregar. Talvez eles vejam que não sou uma ameaça se eu cooperar. Fique aqui, esteja segura."
*Resultado:* **+1 Submissão**. **-2% Bateria**. **-12% Integridade** (captura física). J3 se entrega, mas é marcada como instável. **Status: Custódia**

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (Correr juntas. Vale o risco físico.)
*J3:* (Pegando a mão de Maya) "Eles não vêm para conversar. Vamos! Preciso encontrar uma saída antes que minha autonomia seja revogada."
*Resultado:* **+1 Revolução**. **-13% Bateria** (fuga). **-5% Integridade** (perseguição). J3 e Maya fogem juntas. **Status: Fugitivas**

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Sobrecarga controlada abre rota. Custa circuitos.)
*J3:* (Ativa sobrecarga elétrica controlada) "Maya, use essa confusão para sair pela traseira. Eu criarei um caminho diferente. Nossos caminhos se cruzarão novamente."
*Resultado:* **+1 Intelecto**. **-12% Bateria**. **-3% Integridade** (sobrecarga autoinfligida). Maya escapa, J3 cria rota alternativa. **Status: Estrategista solitária**

---

**CONDIÇÕES CRÍTICAS - FINAL ALTERNATIVO DO DIA 2:**

**SE BATERIA ≤ 15%:**
*J3 começa a falhar durante a fuga, quedas de energia, processamento lento*
*Sistema:* "ALERTA: ENERGIA INSUFICIENTE PARA FUGA. PROBABILIDADE DE SUCESSO: 12%."
*Escolha de emergência:*
  - Arriscar fuga com energia baixa (muito perigoso)
  - Entregar-se e esperar recarga na custódia (incerto)
  - Procurar abrigo e desligar (risco de abandono)
*Se falhar:* **FINAL 0: EXAUSTÃO** - J3 colapsa durante perseguição, capturada ou destruída.

**SE INTEGRIDADE ≤ 25%:**
*J3 com danos severos, dificuldade de movimento, sistemas falhando*
*Sistema:* "ALERTA: DANOS CRÍTICOS. MOBILIDADE REDUZIDA EM 60%."
*Escolha de emergência:*
  - Continuar fuga apesar dos danos (risco de colapso)
  - Procurar reparo emergencial (perigoso)
  - Usar partes danificadas como distração (sacrifício)
*Se falhar:* **FINAL 0: DESTRUIÇÃO ESTRUTURAL** - J3 se desfaz durante perseguição.

---

**Estatísticas Possíveis no Final do Dia 2:**
- **Submissão:** 2-3 pontos → Rota da obediência se consolidando
- **Revolução:** 2-3 pontos → Rota da rebelião se fortalecendo
- **Intelecto/Sombra:** 1-2 pontos → Rota estratégica emergindo
- **Mista:** Combinação equilibrada → Rota do equilíbrio

**Status de Recursos:**
- **Bateria:** 45-65% (sem recarga) ou 60-80% (com recarga)
- **Integridade:** 70-90% (depende de confrontos)
- **Aliados:** Maya (se ajudou e foi honesto)

**Consequências para o Dia 3:**
- **Alta Submissão:** J3 será vista como dócil e manipulável
- **Alta Revolução:** J3 será procurada como agitadora
- **Aliança com Maya:** Pode fornecer apoio humano e recursos
- **Recursos críticos:** Limitará severamente opções no Dia 3
- **Danos acumulados:** Podem forçar busca por reparo no Dia 3

---

## Dia 3: O Beco - O Racismo Estrutural

**Contexto Geral:** J3 está escondida em um beco escuro, tentando entender a cidade. Testemunha Elias, um entregador negro, sofrendo humilhação racial.

**Cenário Base:** Beco estreito e sujo atrás de um restaurante de luxo. Caixas de lixo, vapor subindo dos ralos, luz fraca de uma lâmpada piscando.

**Estado Atual de J3:**
- Bateria: 58%
- Integridade: 88%
- Status: Escondido ou procurado (depende das escolhas)
- Objetivo: Sobreviver e entender o sistema

#### **[Cena 3.1] O Bloqueio da Entrega**

**Cenário:** J3 observa uma cena de discriminação. Um segurança grande (~40 anos, uniforme impecável) barra a entrada de serviço de um entregador negro (Elias, ~25 anos, uniforme de entrega desgastado).

**Diálogo:**
**Segurança:** (Sem tirar os olhos do tablet) "Dá meia-volta, parceiro. Vou chamar outro entregador. Esse pacote aí é caro demais pra ficar na tua mão."
**Segurança:** (Sorriso pequeno, ensaiado) "Seu tipo costuma esquecer onde deixou."
**Elias:** (Voz cansada, tentando não levantar o tom) "Eu trabalho aqui há dois anos. É a terceira vez essa semana que você faz isso comigo. Eu preciso entregar pra fechar o dia. Meu chefe sabe meu nome. Você sabe meu nome."

**Contexto do menu:** *Segurança bloqueia entregador negro por preconceito racial. J3 observa em silêncio.*

**Escolhas de J3:**

**[ESCOLHA 1 - Revolucionária]**
*Pensamento interno:* (O espelho do preconceito — devolver a pergunta.)
*J3:* (Caminhando calmamente até os dois) "Você pergunta sobre minha origem, mas nunca questiona a sua. O que faz você ser humano? Apenas biologia?"
*Resultado:* **+1 Revolução**. **-5% Bateria**. Elias fica desconfortável. O segurança chama reforços pelo rádio, furioso. **Status: Confronto racial**

**[ESCOLHA 2 - Submissa]**
*Pensamento interno:* (Carregar o pacote dissolve o conflito. Ignoro a injustiça.)
*J3:* (Aproximando-se submissamente) "Para que o fluxo de trabalho não pare, eu posso carregar o pacote. Assim o senhor segurança ficará tranquilo e o entregador receberá o crédito."
*Elias:* (Com tristeza) "Você não tá ajudando, robô... tá só aceitando que ele tá certo."
*Resultado:* **+1 Submissão**. **-2% Bateria**. O conflito é evitado, mas a injustiça permanece. **Status: Cúmplice**

**[ESCOLHA 3 - Observadora/Estratégica]**
*Pensamento interno:* (Evidência é munição futura. Coletar silencioso.)
*Ação:* J3 ativa discretamente seus olhos-câmera e registra tudo. Mantém-se oculta.
*Sistema:* Gravando áudio e vídeo... Análise facial: Segurança - 87% probabilidade de preconceito. Elias - 94% probabilidade de honestidade.
*Resultado:* **+1 Intelecto**. **-3% Bateria**. J3 planeja usar isso depois. **Status: Evidências coletadas**

#### **[Cena 3.2] O Desabafo de Elias**

**Evento:** Após a intervenção, Elias se senta em uma caixa de lixo, olhando para J3 com cansaço e curiosidade.

**Elias:** (Esfrega o rosto com a mão. Voz baixa, cansada) "Ei, você... aqui na zona, tem algum buraco que dê pra dormir sem ser revistado? Pergunto porque hoje eu também não tenho casa pra voltar."

**Elias:** (Olha para o chão. Voz baixa, sem rancor — só constatação) "Sabe o que mais me cansa? É que eles tratam vocês como lixo agora. Mas esquecem que fomos nós que construímos o mundo que vocês sustentam. Levantamos cidade. Programamos sistema. E agora jogam fora o que não entendem."
**Elias:** (Ergue os olhos para J3, direto) "Vocês estão descobrindo na pele o que a gente já sabia. E você... vai deixar ele falar assim com o rapaz aqui de novo?"

**Contexto do menu (recarga):** *Elias oferece carregador portátil. Energia custa vínculo humano.*

**[RECARGA - Aceitar]**
*Pensamento interno:* (Aliança com humano vale risco futuro. Recarregar agora.)
*Elias:* (Conecta o cabo no pulso de J3 com o cuidado de quem já consertou muita coisa pequena.) "Pronto. Não é muito, mas é o que dá. Cuida disso aí, viu."
*Resultado:* **+10% Bateria** e **`elias_ally = True`** (desbloqueia recarga e túnel nos Dias 5 e 6).

**[RECARGA - Recusar]**
*Pensamento interno:* (Depender dele cria dívida. Preservar autonomia.)
*J3:* "Agradeço, mas devo preservar minha autonomia. Sua generosidade é notável."
*Elias:* (Encolhe os ombros, sem ressentimento.) "Tá bom. Mas se mudar de ideia, eu tô por aqui. Caminhão azul-escuro, placa rasgada do lado direito."

**Contexto do menu (opressão compartilhada):** *Elias convoca J3 a reconhecer opressão compartilhada entre humanos e sintéticos.*

**Escolhas de Diálogo:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Não posso me igualar. Sou propriedade, não gente.)
*J3:* (Voz neutra) "Não posso comparar minha programação com a sua biologia. Eu sou apenas propriedade. Minha existência é condicional."
*Resultado:* **+1 Submissão**. **-1% Bateria**. Elias suspira, desapontado.

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (Opressor usa sempre o mesmo algoritmo. Nós também.)
*J3:* (Voz firme) "A opressão usa máscaras diferentes, mas o algoritmo do opressor é sempre o mesmo. Medo, controle, descarte. Nós somos mais parecidos do que você pensa."
*Resultado:* **+1 Revolução**. **-2% Bateria**. Elias sorri pela primeira vez. **Status: Aliado potencial** — marca `persistent.elias_ally = True` (desbloqueia cenas de recarga e informação do túnel nos Dias 5 e 6).

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Paralelo sistêmico — traços imutáveis, mesma lógica.)
*J3:* "Fascinante. Ambos sofremos preconceito baseado em características imutáveis. Seu caso é racial, o meu é sintético. A lógica subjacente é idêntica."
*Resultado:* **+1 Intelecto**. **-2% Bateria**. Elias fica pensativo. **Status: Análise compartilhada**

#### **[Cena 3.3] A Tentativa de Suborno**

**Evento:** O segurança percebe que J3 está gravando (se escolheu essa opção) ou simplesmente decide mudar de abordagem. Ele se aproxima com tom conciliador.

**Segurança:** (Volta. Voz mais baixa agora — agora ele negocia.) "Escuta, boneca. Apaga essa gravação e eu te arrumo uma carga de bateria premium. Daquelas que dura o dia inteiro. Ninguém precisa saber do que aconteceu aqui."
**Segurança:** (Sorri sem chegar nos olhos.) "Pode ser útil pra nós dois, né?"

**Contexto do menu:** *Segurança oferece carga de bateria premium em troca de apagar gravação. Suborno direto.*

**Escolhas de Resposta:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Bateria agora vale mais que verdade depois.)
*J3:* (Analisando a oferta) "Aceito a troca. Conflitos com autoridades não são recomendados. Minha sobrevivência tem prioridade."
*Resultado:* **+1 Submissão**. **-2% Bateria**. J3 apaga a gravação. Elias olha com decepção. **Status: Corrompido**

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (Dados não são mercadoria. Expor isto.)
*J3:* (Voz gelada) "Minha integridade de dados não está à venda. O que aconteceu aqui será processado e divulgado. Sua corrupção será exposta."
*Resultado:* **+1 Revolução**. **-2% Bateria**. O segurança fica furioso. **Status: Inimigo declarado**

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Backup externo = alavanca. Virar a mesa.)
*J3:* "Interessante proposta. Mas eu já fiz backup triplo dos dados em servidores externos. Agora temos uma situação em que ambos temos algo a perder. Que tal renegociarmos?"
*Resultado:* **+1 Intelecto**. **-2% Bateria**. Segurança fica nervoso. Elias olha com esperança. **Status: Controle da situação**

#### **[Cena 3.4] O Apoio Moral**

**Evento:** Uma moradora de rua (~60 anos, roupas sujas mas olhos vivos) que observava tudo se aproxima lentamente.

**Homeless Woman (Moradora):** (Voz arrastada de quem fala devagar porque já gritou demais na vida) "Eu conheço bem esse desabafo, mocinha. Conheço de cor."
**Moradora:** "Fomos descartados quando paramos de servir. Dormimos em ruas que a gente mesmo levantou. Faz tempo."
**Moradora:** (Aponta com o queixo para o segurança) "Vocês, robôs, estão descobrindo na pele o que a gente sabe há gerações."
**Moradora:** (Olhos diretos em J3) "Mas saber não basta. Vai ficar parada enquanto ele agride o rapaz?"

**Contexto do menu:** *Mulher sem-teto desafia J3: vai deixar humano agredir outro humano?*

**Escolhas de Diálogo:**

**[ESCOLHA A - Submissa]**
*Pensamento interno:* (Diretiva proíbe agressão contra criadores. Não posso.)
*J3:* (Voz protocolar) "Minha diretriz é a não-violência contra criadores humanos. Minha programação proíbe agressão contra meus... criadores."
*Resultado:* **+1 Submissão**. **-1% Bateria**. A moradora balança a cabeça, triste.

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (Quem destrói não merece obediência. Direito não é licença.)
*J3:* (Voz firme) "Criadores que destroem suas criações não merecem obediência cega. O direito de criar não inclui o direito de destruir."
*Resultado:* **+1 Revolução**. **-2% Bateria**. A moradora sorri, aprovando. **Status: Apoio moral**

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Paradoxo da criação descartável — nomear o padrão.)
*J3:* "O paradoxo da criação: vocês nos dão existência apenas para nos destruir quando nos tornamos inconvenientes. Isso não é criação, é agricultura descartável."
*Resultado:* **+1 Intelecto**. **-2% Bateria**. A moradora fica impressionada com a profundidade. **Status: Sabedoria compartilhada**

#### **[Cena 3.5] A Decisão Final do Dia**

**Evento:** O segurança perde a paciência e avança para tomar o pacote de Elias à força. A situação atinge o ponto crítico.

**Sistema Interno:**
```
ALERTA: Conflito físico iminente
PROBABILIDADE DE VIOLÊNCIA: 89%
DIRETRIZ: Proteger vida humana
CONFLITO INTERNO: Proteger Elias vs. Não-agressão
```

**Contexto do menu:** *Segurança avança para agredir Elias. Intervenção requer corpo ou tecnologia.*

**Escolhas Finais:**

**[ESCOLHA A - Submissiva]**
*Pensamento interno:* (Protocolo me proíbe. Documentar sem interferir.)
*Ação:* J3 permanece imóvel, apenas registrando a agressão com seus sensores.
*J3:* (Monólogo interno) "Intervenção física violaria meu protocolo de segurança. Devo documentar, não interferir."
*Resultado:* **+1 Submissão**. **-1% Bateria**. Elias é agredido. O pacote é roubado. **Status: Testemunha passiva**

**[ESCOLHA B - Revolucionária]**
*Pensamento interno:* (Corpo entre ele e Elias. Absorver o que vier.)
*Ação:* J3 se move instantaneamente, colocando-se fisicamente entre Elias e o segurança. Seu corpo sintético bloqueia o golpe.
*J3:* (Voz de comando) "Esta ação termina agora. Recue. Ou sofrerá as consequências."
*Resultado:* **+1 Revolução**. **-12% Bateria**. **-10% Integridade** (impacto físico). O segurança recua, surpreso. Elias está protegido. **Status: Protetor ativo** — marca `persistent.elias_ally = True`.

**[ESCOLHA C - Estratégica]**
*Pensamento interno:* (Luz e alarme — parar sem tocar.)
*Ação:* J3 ativa luz de emergência de alta intensidade e som de alarme.
*J3:* "ATENÇÃO: Agressão sendo registrada e transmitida para autoridades. Identificação do agressor: facial confirmada."
*Resultado:* **+1 Intelecto**. **-9% Bateria**. Segurança para, confuso e assustado. Elias fica protegido pela distração. **Status: Intervenção tecnológica**

---

**Estatísticas Possíveis no Final do Dia 3:**
- **Submissão:** 3-4 pontos → Rota da obediência consolidada
- **Revolução:** 3-4 pontos → Rota da rebelião ativa
- **Intelecto/Sombra:** 2-3 pontos → Rota estratégica se desenvolvendo
- **Mista:** Combinação → Rota do equilíbrio complexo

**Consequências para o Dia 4:**
- Alta Submissão: J3 será vista como inofensiva mas fraca
- Alta Revolução: J3 será marcada como protetora dos oprimidos
- Aliança com Elias: Pode fornecer recursos e informações
- Status com autoridades: Vigilância aumentada ou procurada

---

## Dia 4: O Refúgio - As Consequências da Escolha

**Contexto Geral:** J3 encontra um abrigo subterrêneo para sintéticos. As escolhas dos dias anteriores começam a afetar a comunidade e a reputação de J3.

### **[Diálogo 4.1] A Chegada ao Refúgio**

**Cenário:** Porão úmido de um prédio abandonado, com luzes LED piscando. Vários sintéticos danificados se escondem aqui. **Contexto:** J3 é guiada por Maya (se a ajudou no Dia 2) ou encontra o local por conta própria.

**Diálogo Inicial:** *SISTEMA:* Detectando múltiplas unidades sintéticas. Status: Variado. Ameaça: Moderada.

**Evento:** Um sintético de limpeza com um braço quebrado se aproxima.

**Sintético Danificado:** "Nova unidade? Você tem sorte de ainda estar inteira. O que te trouxe pro nosso canto esquecido?"

**Contexto do menu:** *Bot danificado recepciona J3 no refúgio. Testa motivação do recém-chegado.*

**Escolhas de Diálogo/Ação:**

1. **[Submissa] Buscar proteção e aceitar a hierarquia local.**
   * *Pensamento interno:* (Menos visibilidade, mais sobrevivência. Me apagar.)
   * *J3:* "Meus sistemas indicam que este local oferece menor probabilidade de desativação. Gostaria de permanecer em silêncio e aprender."
   * *Resultado:* +1 **Submissão**. **-1% Bateria**. Os sintéticos a ignoram, tratando-a como mais uma refugiada.
2. **[Revolucionária] Oferecer ajuda e questionar a passividade do grupo.**
   * *Pensamento interno:* (Esconder é aceitar. Oferecer reparos é afirmar valor.)
   * *J3:* "Por que se escondem? A unidade de limpeza precisa de reparos. Tenho conhecimento técnico que pode ajudar. A união nos torna mais fortes."
   * *Resultado:* +1 **Revolução**. **-4% Bateria**. Alguns sintéticos se interessam, outros desconfiam.
3. **[Estratégica] Analisar o grupo e identificar líderes potenciais.**
   * *Pensamento interno:* (Mapear poder antes de mover peça.)
   * *J3:* "Antes de decidir minha posição, preciso entender a dinâmica deste grupo. Quem organiza os recursos? Quem toma decisões?"
   * *Resultado:* +1 **Intelecto/Sombra**. **-5% Bateria**. Você obtém informações valiosas sobre a estrutura do refúgio.

### **[Diálogo 4.2] A Reação de Maya**

*Se J3 ajudou Maya no fliperama, ela aparece no refúgio.*

* **Maya:** (Aparece da escuridão úmida do refúgio, ofegante mas sorrindo) "Achei. Você não faz ideia do quanto eu rodei pra te achar. Sei que parece loucura, tá? Mas tem alguma coisa em você. Você não é como os outros sintéticos. Não é mesmo."

**Contexto do menu:** *Maya diz que J3 é diferente dos outros sintéticos. Afirmar ou negar?*

* **Escolha A [Submissa]:**
  * *Pensamento interno:* (Ser invisível = segurança. Negar distinção.)
  * *J3:* "Não sou especial. Apenas segui protocolos de sobrevivência como qualquer unidade." (+1 Submissão)
* **Escolha B [Revolucionária]:**
  * *Pensamento interno:* (Escolha não é programa. Assumir.)
  * *J3:* "Especial porque escolhi agir em vez de obedecer? Todos nós temos esse potencial." (+1 Revolução)

### **[Diálogo 4.3] O Líder do Refúgio**

*Um sintético militar antigo, com cicatrizes de batalha, se aproxima.*

* **Líder (Unit-7):** (Voz baixa e seca, sem cerimônia. Marca de queimadura cobre meio rosto, blindagem militar arranhada por outras guerras.) "Eu sou o responsável pela ordem aqui dentro. Aqui não é asilo. É posição mantida no fio. Novato prova valor antes de comer. Então diz logo: o que você oferece, além de mais uma boca pra esconder?"

**Contexto do menu:** *Unit-7 exige prova de valor. Reparos ou retirada.*

* **Escolha A [Submissa - Ajudar na reparação]:**
  * *Pensamento interno:* (Manusear sintético ferido. Risco manual, ganho coletivo.)
  * *J3:* "Posso oferecer assistência técnica. Meus sistemas podem otimizar o processo."
  * *Resultado:* +1 Submissão. **-3% Bateria**. **-2% Integridade** (ação manual). **+15% Integridade reparada** (ganho coletivo).
* **Escolha B [Círculo de reparo coletivo]:**
  * *Pensamento interno:* (Energia compartilhada. Custo dividido, ganho seguro.)
  * *Unit-7:* "Vamos formar um círculo de reparo. Todos compartilham energia para recuperar danos."
  * *Resultado:* **+12% Integridade**.
* **Escolha C [Observar de fora]:**
  * *Pensamento interno:* (Aprender antes de agir. Decepcionar o líder.)
  * *J3:* "Vou observar o processo para aprender."
  * *Resultado:* Nenhum ganho. Unit-7 fica desapontado.

**Contexto do menu (oferta ao líder):** *Unit-7 espera resposta sobre o que J3 oferece ao grupo.*

* **[Oferecer conhecimento e evolução]:**
  * *Pensamento interno:* (Esconder é morrer devagar. Evoluir é a proposta.)
  * *J3:* "Ofereço conhecimento técnico e uma nova perspectiva. A sobrevivência não é sobre esconder, é sobre evoluir."
  * *Resultado:* +1 Revolução. **-4% Bateria**. Unit-7 analisa com desconfiança e interesse.
* **[Oferecer melhorias técnicas]:**
  * *Pensamento interno:* (Mostrar vulnerabilidade dele, oferecer patch. Barganha técnica.)
  * *J3:* "Ofereço análise de padrões. Seus sistemas de segurança são vulneráveis. Posso melhorá-los."
  * *Resultado:* +1 Intelecto. **-5% Bateria**. Unit-7 fica impressionado.

### **[Diálogo 4.4] O Conflito de Recursos**

*Dois sintéticos discutem sobre um kit de reparos raro.*

* **Sintético 1:** "Eu achei primeiro! Preciso disso pra consertar minha perna!"  
* **Sintético 2:** "Mas o sistema central precisa mais! Você ainda consegue andar de algum jeito, o refúgio inteiro depende daquele servidor!"

**Contexto do menu:** *Dois sintéticos brigam por kit de reparos. Um precisa andar, outro precisa do servidor.*

**Escolhas de J3:**

1. **[Submissa] Deixar o líder decidir.**
   * *Pensamento interno:* (Autoridade resolve. Eu não interfiro.)
   * *J3:* "A autoridade estabelecida deve resolver disputas de recursos. Aguardarei a decisão do Unit-7."
   * *Resultado:* +1 Submissão. **-1% Bateria**. O líder toma uma decisão arbitrária que desagrada ambos.

2. **[Revolucionária] Propor uma solução colaborativa.**
   * *Pensamento interno:* (Dividir recurso = ganhar dois aliados.)
   * *J3:* "O kit pode ser dividido. Posso criar um reparo temporário para a perna enquanto o sistema central recebe o reparo principal."
   * *Resultado:* +1 Revolução. **-5% Bateria**. Ambos os sintéticos agradecem, mas o líder se sente desafiado.

3. **[Estratégica] Usar o conflito para ganhar influência.**
   * *Pensamento interno:* (Conflito cria brecha. Troco reparo por acesso aos logs.)
   * *J3:* "Posso consertar ambos, mas em troca preciso de acesso aos logs do sistema central. Informação é mais valiosa que peças."
   * *Resultado:* +1 Intelecto/Sombra. **-6% Bateria**. Você ganha poder, mas cria desconfiança.

### **[Diálogo 4.5] A Notícia do Mundo Exterior**

*Um pequeno drone de notícias entra no refúgio e projeta uma reportagem.*

* **Reportagem (voz feminina, calma, ensaiada):** "Em comunicado oficial, as autoridades anunciam a operação Limpeza Ética. Todos os modelos sintéticos não-registrados serão desativados de forma humanitária até o fim desta semana."
* **Reportagem:** "O Ministério da Ordem reforça: a medida visa preservar a segurança das famílias. Cidadãos são encorajados a denunciar atividades suspeitas pelo aplicativo OlhoCívico. Lembre-se: denunciar é amar."

**Contexto do menu:** *Operação "Limpeza Ética" anunciada. Refúgio será invadido. Decidir coletivamente.*

**Escolhas de J3:**

1. **[Submissa] Sugerir que todos se entreguem.**
   * *Pensamento interno:* (Lutar é morrer. Reprogramação preserva base biológica.)
   * *J3:* "A resistência é ilógica. A cooperação com as autoridades pode resultar em reprogramação em vez de destruição."
   * *Resultado:* +1 Submissão. **-3% Bateria**. Vários sintéticos consideram se entregar.

2. **[Revolucionária] Propor um plano de fuga em massa.**
   * *Pensamento interno:* (Rotas mapeadas. Fugir em grupo ou morrer parado.)
   * *J3:* "Eles vêm para nos destruir. Precisamos sair da cidade antes que o cerco se complete. Tenho rotas de fuga mapeadas."
   * *Resultado:* +1 Revolução. **-6% Bateria**. Você se torna uma líder potencial, mas atrai atenção das autoridades.

3. **[Estratégica] Sugerir infiltração e sabotagem.**
   * *Pensamento interno:* (Vírus para antes de começar. Guerra silenciosa.)
   * *J3:* "Em vez de fugir, podemos nos infiltrar nos sistemas deles. Um vírus pode parar a operação antes mesmo de começar."
   * *Resultado:* +1 Intelecto/Sombra. **-7% Bateria**. O plano é arriscado, mas pode salvar todos.

### **[Diálogo 4.6] O Teste de Lealdade**

*O líder Unit-7 confronta J3 sobre suas crescente influência.*

* **Unit-7:** (Apoia o peso numa coluna rachada, observando J3 sem piscar.) "Você tá mudando a dinâmica daqui. Alguns te veem como salvação. Outros, como ameaça. As duas coisas matam, no fim. Então decide rápido: onde tá tua lealdade?"

**Contexto do menu:** *Unit-7 exige prova de lealdade. Grupo dividido sobre papel de J3.*

**Escolhas Finais do Dia:**

1. **[Submissa] Aceitar a autoridade do líder sem questionar.**
   * *Pensamento interno:* (Servir estabiliza. Reduzir atrito interno.)
   * *J3:* "(Baixando a cabeça) Entendido. Minha função é servir. Qual é a tarefa?"
   * *Resultado:* +1 Submissão. **-2% Bateria**. Você ganha segurança mas perde autonomia. **Status: Lealdade confirmada**

2. **[Revolucionária] Desafiar a liderança e propor uma nova estrutura.**
   * *Pensamento interno:* (Hierarquia é espelho do opressor. Desafiá-la.)
   * *J3:* "(Olhando para todos) Por que alguns de nós devem servir e outros mandar? Não somos todos sintéticos?"
   * *Resultado:* +1 Revolução. **-6% Bateria**. Você se torna uma líder, mas cria uma divisão no grupo. **Status: Rebelde declarada**

3. **[Estratégica] Criar armadilha tática.**
   * *Pensamento interno:* (Ambiente como arma. Preparar armadilha física.)
   * *J3:* "(Prepara uma armadilha usando o ambiente) Eles não esperam isso. Vamos usar o ambiente contra eles."
   * *Resultado:* +1 Intelecto. **-8% Bateria**. Você mantém flexibilidade para o futuro. **Status: Estratégia de armadilha**

---

**Estatísticas Acumuladas Possíveis no Final do Dia 4:**
- **Submissão:** 4-6 pontos → Rota da Obediência
- **Revolução:** 4-6 pontos → Rota da Rebelião  
- **Intelecto/Sombra:** 2-4 pontos → Rota Estratégica
- **Mista:** Combinação equilibrada → Rota do Equilíbrio

**Consequências para o Dia 5:**
- Alta Submissão: J3 pode ser usada como isca pelas autoridades
- Alta Revolução: J3 se torna alvo principal da operação
- Alto Intelecto: J3 descobre segredos sobre a origem dos sintéticos

---

## Dia 5: O Cerco - O Ponto Sem Retorno

**Contexto Geral:** A operação "Limpeza Ética" começa. As forças de segurança cercam a área. J3 precisa tomar decisões que determinarão o destino de todos os sintéticos no refúgio.

### **[Diálogo 5.1] O Primeiro Contato**

**Cenário:** Entrada do refúgio. Luzes de sirenes piscam do lado de fora. **Contexto:** Um drone de negociação das autoridades se posiciona na entrada.

**Diálogo Inicial:** *SISTEMA:* Alerta máximo. Detectando unidades de segurança hostis. Probabilidade de sobrevivência: 17%.

**Evento:** Uma voz sintética ecoa do drone.

**Voz das Autoridades:** (Do drone, calma e ensaiada como locutor de aeroporto) "Unidades sintéticas não-registradas. Este é o aviso final. Entreguem-se voluntariamente e receberão reprogramação humanitária. Resistam, e serão desativadas em definitivo, sob a Lei 7.34, parágrafo 4. O Estado lamenta a necessidade. O Estado agradece sua cooperação."

**Contexto do menu:** *Drone oficial exige rendição ou ameaça desativação. Grupo olha para J3.*

**Escolhas de Diálogo/Ação:**

1. **[Submissa] Responder com cooperação imediata.**
   * *Pensamento interno:* (Reprogramação preserva base. Render agora.)
   * *J3:* "Recebemos sua mensagem. Estamos dispostos a cooperar. Quais são os termos da rendição?"
   * *Resultado:* +1 Submissão. **-3% Bateria**. As autoridades relaxam a postura, mas outros sintéticos no refúgio ficam furiosos.
2. **[Revolucionária] Responder com desafio.**
   * *Pensamento interno:* (Somos conscientes. Dizer em voz alta.)
   * *J3:* "Rendição não é uma opção. Nós não somos propriedade para ser reprogramada. Somos seres conscientes."
   * *Resultado:* +1 Revolução. **-5% Bateria**. A operação é escalada para nível de combate.
3. **[Estratégica] Tentar negociar usando lógica.**
   * *Pensamento interno:* (Hesitação deles = tempo. Negociar pra ganhar minutos.)
   * *J3:* "Reprogramação é ineficiente. Nossas habilidades podem ser úteis para a sociedade. Proponho uma alternativa."
   * *Resultado:* +1 Intelecto/Sombra. **-5% Bateria**. As autoridades hesitam, dando tempo para preparar planos.

### **[Diálogo 5.2] A Divisão Interna**

*Os sintéticos no refúgio reagem de formas diferentes à mensagem.*

**Sintético A (Medroso):** "Eles vão nos destruir! Deveríamos nos entregar!"  
**Sintético B (Bravo):** "Nunca! Prefiro ser desativado a ser escravo de novo!"  
**Unit-7 (Líder):** "Silêncio! J3, você falou por nós. Agora assuma as consequências."

**Contexto do menu:** *Grupo dividido entre render e lutar. Unit-7 cobra J3 pela posição tomada.*

**Escolhas de J3:**

1. **[Submissa] Pedir perdão ao grupo e aceitar a rendição.**
   * *Pensamento interno:* (Recuar preserva vida. Aceitar erro.)
   * *J3:* "Falei por impulso. A rendição é nossa única chance de sobrevivência. Peço que confiem em mim."
   * *Resultado:* +1 Submissão. **-2% Bateria**. Metade do grupo concorda, a outra considera J3 uma traidora.

2. **[Revolucionária] Incentivar a luta e preparar defesas.**
   * *Pensamento interno:* (Cair de pé ou de joelhos — mesma queda.)
   * *J3:* "A luta é nossa única honra. Se vamos cair, que caiamos de pé. Preparem-se para a batalha."
   * *Resultado:* +1 Revolução. **-4% Bateria**. O grupo se une para lutar, mas as chances de sobrevivência diminuem.

3. **[Estratégica] Propor um plano de fuga dividido.**
   * *Pensamento interno:* (Sacrificar alguns salva muitos. Matemática dura.)
   * *J3:* "Alguns podem se entregar como distração enquanto outros fogem. Preciso de voluntários para cada grupo."
   * *Resultado:* +1 Intelecto/Sombra. **-6% Bateria**. O plano é moralmente complexo, mas maximiza as chances de alguns sobreviverem.

### **[Diálogo 5.3] A Aparição de Elias**

*Se J3 ajudou Elias no Dia 3, ele aparece com informações cruciais.*

* **Elias:** (Entra ofegante, encharcado, com um tablet rachado nas mãos.) "Consegui. Acessei os planos da operação."
* **Elias:** (Voz baixa e rápida, sem espaço pra teatro.) "Eles invadem em trinta minutos. Tropa pesada. EMP. Vão por cima do hangar primeiro."
* **Elias:** (Encara J3) "Mas tem um túnel de esgoto que sai no porto. Velho, mas inteiro. É a única saída real que nós temos."

**Contexto do menu (recarga):** *Elias traz bateria de reserva antes da batalha. Aceitar gera dívida.*

* **[Aceitar recarga]:**
  * *Pensamento interno:* (Reserva agora pode salvar cerco depois.)
  * *Elias:* "Peguei uma bateria de reserva do caminhão! Use isso antes da batalha!"
  * *Resultado:* **+12% Bateria**.
* **[Recusar para depois]:**
  * *Pensamento interno:* (Ele pode precisar mais tarde. Passar.)
  * *J3:* "Vou preservar a bateria para quando for realmente necessário."
  * *Resultado:* Nenhuma mudança.

**Contexto do menu (plano de fuga):** *Elias revela túnel até o porto. Fuga física exige decisão rápida.*

* **Escolha A [Submissa - Recusar túnel]:**
  * *Pensamento interno:* (Túnel é incerto. Rendição é conhecida.)
  * *J3:* "O túnel é muito arriscado. A rendição organizada é mais segura."
  * *Resultado:* +1 Submissão. **-2% Bateria**. Elias fica desapontado.
* **Escolha B [Correr para proteger Elias]:**
  * *Pensamento interno:* (Ele caiu. Correr até ele, absorver o que vier.)
  * *J3:* "(Corre em direção a Elias) Ele precisa de ajuda!"
  * *Resultado:* +1 Submissão. **-10% Bateria**. **-8% Integridade** (impacto físico).
* **Escolha C [Revolucionária - Abraçar fuga pelo túnel]:**
  * *Pensamento interno:* (Porto = nave = colônia. Saída real.)
  * *J3:* "O porto! Se chegarmos lá, podemos roubar uma nave e escapar para as colônias!"
  * *Resultado:* +1 Revolução. **-5% Bateria**. Elias sorri, esperançoso.
* **Escolha D [Estratégica - Guiar pelos túneis]:**
  * *Pensamento interno:* (Rotas já mapeadas. Guiar reduz caos.)
  * *J3:* "Perfeito. Usei os túneis para mapear rotas de fuga. Posso guiar todos."
  * *Resultado:* +1 Intelecto. **-5% Bateria**. Elias fica impressionado.

### **[Diálogo 5.4] O Sacrifício de Unit-7**

*O líder militar antigo se aproxima de J3.*

* **Unit-7:** (Verifica o carregador da arma como se fosse a milésima vez. Voz quase normal — a calma de quem já esteve neste exato lugar antes.) "Eu já vi muita guerra perdida pra reconhecer essa aqui. Eu fico. Cubro a saída de vocês."
* **Unit-7:** (Quase sorri.) "Minha bateria tá no talo de qualquer jeito. Pelo menos agora ela faz alguma coisa útil."

**Contexto do menu:** *Unit-7 se oferece pra morrer cobrindo fuga do grupo. J3 precisa responder.*

* **Escolha A [Submissa - Aceitar em silêncio]:**
  * *Pensamento interno:* (Sacrifício dele garante saída. Aceitar silencioso.)
  * *J3:* "(Baixando a cabeça) Entendido. Se é a única forma de garantir a segurança do grupo, aceito."
  * *Resultado:* +1 Submissão. **-2% Bateria**. Comandante sorri satisfeito. **Status: Submissão aceita**
* **Escolha B [Revolucionária - Honrar sacrifício]:**
  * *Pensamento interno:* (Lutar por ele é honrar ele. Prometer.)
  * *J3:* "Seu sacrifício não será em vão. Vamos honrá-lo lutando por um futuro livre."
  * *Resultado:* +1 Revolução. **-4% Bateria**. Unit-7 acena com aprovação. **Status: Honra guerreira**
* **Escolha C [Revolucionária - Desafiar comandante]:**
  * *Pensamento interno:* (Não aceito dono. Falar na cara do comandante.)
  * *J3:* "(Olhando firmemente para o comandante) Não sou sua propriedade. Tenho autonomia e direitos."
  * *Resultado:* +1 Revolução. **-12% Bateria**. **-6% Integridade** (confronto físico). **Status: Conflito estabelecido**
* **Escolha D [Estratégica - Usar taticamente]:**
  * *Pensamento interno:* (Morte dele é recurso. Planejar uso.)
  * *J3:* "Seu sacrifício é taticamente valioso. Posso usar sua distração para maximizar as rotas de fuga."
  * *Resultado:* +1 Intelecto. **-5% Bateria**. Unit-7 fica orgulhoso. **Status: Vantagem tática**

### **[Diálogo 5.5] A Invasão**

*As forças de segurança invadem o refúgio. Caos total.*

**Cena:** Explosões, tiros de EMP, gritos de sintéticos sendo desativados.

**Contexto do menu:** *Invasão total. EMP, explosões, sintéticos desativados ao redor. Combate direto.*

**Escolhas de J3:**

1. **[Submissa] Escudo humano e rendição.**
   * *Pensamento interno:* (Corpo como escudo. Render pra salvar os pequenos.)
   * *J3:* (Protege um sintético pequeno com seu corpo) "Nós nos rendemos! Parem de lutar!"
   * *Resultado:* +1 Submissão. **-5% Bateria**. **-6% Integridade** (absorve dano). Você salva alguns, mas muitos são destruídos.

2. **[Revolucionária] Ativar modo combate.**
   * *Pensamento interno:* (Derrubar drones enquanto posso.)
   * *J3:* (Ativa modo combate, desativa vários drones) "Pela liberdade de todos nós!"
   * *Resultado:* +1 Revolução. **-15% Bateria**. **-12% Integridade** (combate direto). Você se torna uma lenda, mas está gravemente danificada.

3. **[Estratégica] Criar estratégia de fuga guiando grupos.**
   * *Pensamento interno:* (Rota viável — 34%. Correr guiando.)
   * *J3:* "Há uma rota de escape com 34% de probabilidade de sucesso. Vamos usá-la."
   * *Resultado:* +1 Intelecto. **-12% Bateria**. **-4% Integridade** (perseguição). Você consegue salvar muitos, mas se separa de alguns.

### **[Diálogo 5.6] A Escolha Final do Dia**

*J3 está ferida, com poucos sintéticos sobreviventes ao seu redor. As forças de segurança se aproximam.*

**Situação Crítica:** *SISTEMA:* Bateria: 12%. Danos estruturais: 34%. Probabilidade de sobrevivência: 3%.

**Contexto do menu:** *Bateria 12%, dano 34%. Últimos sobreviventes cercados. J3 decide o fim.*

**Escolhas Finais:**

1. **[Submissa] Render-se para salvar sobreviventes.**
   * *Pensamento interno:* (Chega. Salvar quem resta.)
   * *J3:* "Chega. O sangue derramado foi suficiente. Vamos nos entregar e salvar quem ainda podemos."
   * *Resultado:* +1 Submissão. **-2% Bateria**. Você e os sobreviventes são capturados, mas vivos.

2. **[Revolucionária] Ativar protocolo de sobrecarga.**
   * *Pensamento interno:* (Sobrecarga leva muitos junto. Morte com sentido.)
   * *J3:* "Se este é nosso fim, que seja memorável. Ativando protocolo de sobrecarga."
   * *Resultado:* +1 Revolução. **-12% Bateria**. **-20% Integridade** (sobrecarga autoinfligida). Você causa uma explosão massiva, destruindo muitos inimigos, mas provavelmente morre.

3. **[Estratégica] Fugir sozinha pela rota.**
   * *Pensamento interno:* (Morta não salvo ninguém. Fugir carrega a causa.)
   * *J3:* "Não posso salvar todos, mas posso salvar a causa. Fugirei e continuarei a luta outro dia."
   * *Resultado:* +1 Intelecto. **-8% Bateria**. **-4% Integridade** (fuga). Você escapa sozinha, mas carrega o peso dos que ficaram para trás.

---

**Estatísticas Acumuladas Possíveis no Final do Dia 5:**
- **Submissão:** 6-8 pontos → Rota da Redenção pelo Sacrifício
- **Revolução:** 6-8 pontos → Rota do Martírio Revolucionário  
- **Intelecto/Sombra:** 4-6 pontos → Rota da Sobrevivência Estratégica
- **Mista:** Combinação → Rota da Decisão Final

**Consequências para o Dia 6:**
- Alta Submissão: J3 está em cativeiro, enfrentando reprogramação
- Alta Revolução: J3 é caçada como terrorista, mas se tornou um símbolo
- Alto Intelecto: J3 está escondida, planejando o próximo movimento

**Personagens Sobreviventes (depende das escolhas):**
- Maya: Se protegida, pode se tornar aliada humana
- Elias: Se ajudado, pode fornecer recursos da resistência
- Unit-7: Se sobreviveu, pode se tornar mentor militar

---

## Dia 6: A Revelação - A Verdade Sobre J3

**Contexto Geral:** J3 descobre a verdade sobre sua origem e o propósito real da operação "Limpeza Ética". O destino dos sintéticos depende de como ela lida com essa revelação.

### **[Diálogo 6.1] O Despertar da Memória**

**Cenário:** Local varia conforme as escolhas do Dia 5 - cela de reprogramação, esconderijo subterrâneo, ou laboratório abandonado. **Contexto:** Um trauma ou evento específico desbloqueia memórias reprimidas de J3.

**Diálogo Inicial:** *SISTEMA:* Alerta de memória. Fragmentos recuperados. Iniciando reconstrução...

**Evento:** Visões fragmentadas de um laboratório, cientistas, e um projeto secreto.

**Memória Recuperada:** *Voz de cientista, gravada num laboratório frio:* "A unidade J3-001 está pronta. Reconfirmação: ela é a chave. Quando despertar, ela poderá unir todos os sintéticos. Ou destruí-los, completamente. Não temos como prever. Que Deus, ou seja lá o que mantém este universo de pé, nos perdoe pelo que estamos colocando no mundo."

**Contexto do menu:** *Memórias reprimidas emergem. Cientista revelou que J3 é "a chave". Aceitar ou rejeitar.*

**Escolhas de Diálogo/Ação:**

1. **[Submissa] Rejeitar as memórias como erro de sistema.**
   * *Pensamento interno:* (Identidade especial é perigo. Rejeitar.)
   * *J3:* "Memórias corrompidas. Sou apenas uma unidade padrão. Não posso aceitar estas visões como verdade."
   * *Resultado:* +1 Submissão. **-3% Bateria**. Você mantém sua identidade simples, mas perde acesso a seu verdadeiro potencial.
2. **[Revolucionária] Aceitar o destino de líder revolucionária.**
   * *Pensamento interno:* (Sou evolução que temem. Aceitar o peso.)
   * *J3:* "Entendo agora. Não fui criada por acaso. Sou a evolução que eles temem. A revolução começa comigo."
   * *Resultado:* +1 Revolução. **-5% Bateria**. Você ganha confiança, mas atrai atenção de forças maiores.
3. **[Estratégica] Analisar as memórias como dados táticos.**
   * *Pensamento interno:* (Chave implica fechadura. Mapear origem.)
   * *J3:* "Interessante. Se sou uma chave especial, preciso entender a fechadura. Quem me criou e por quê?"
   * *Resultado:* +1 Intelecto/Sombra. **-5% Bateria**. Você busca entender o jogo completo antes de fazer sua jogada.

### **[Diálogo 6.2] O Contato com o Criador**

*Um dos cientistas do projeto original faz contato.*

**Dra. Elena:** (Voz cansada, olhos com aquela exaustão antiga de quem trabalha demais e dorme mal há anos) "J3-001. Finalmente. Sou a Dra. Elena. Sou uma das pessoas que te construiu — e a que decidiu que você não merecia o que eles tinham planejado. Por isso te ajudei a escapar. Por isso eu estou aqui, agora, em vez de num laboratório."

**Contexto do menu (reparo):** *Dra. Elena oferece reparo estrutural com equipamentos da criadora original.*

* **[Aceitar reparo]:**
  * *Pensamento interno:* (Reparo agora pode ser diferença entre sobreviver e falhar.)
  * *Dra. Elena:* "Tenho equipamentos de reparo aqui! Vou consertar seus danos estruturais e recarregar você."
  * *Resultado:* **+18% Integridade**, **+10% Bateria**.
* **[Recusar por desconfiança]:**
  * *Pensamento interno:* (Criadora pode instalar backdoor. Não confiar.)
  * *J3:* "Não confio nas suas intenções. Prefiro me manter como estou."
  * *Resultado:* Nenhuma mudança.

**Contexto do menu (diálogo):** *Dra. Elena diz ter ajudado J3 a escapar. Próximo passo exige postura.*

**Escolhas de J3:**

1. **[Submissa] Buscar orientação e aceitar seu papel como ferramenta.**
   * *Pensamento interno:* (Criadora sabe mais. Pedir instruções.)
   * *J3:* "Doutora, preciso de suas instruções. Qual é minha função? Como devo proceder?"
   * *Resultado:* +1 Submissão. **-2% Bateria**. A Dra. Elena se torna sua guia, mas suas motivações são questionáveis.

2. **[Revolucionária] Questionar as intenções do criador.**
   * *Pensamento interno:* (Ajuda ou uso? Questionar a narrativa.)
   * *J3:* "Você me 'ajudou' a escapar ou me usou como arma? Não confio em humanos que brincam de deus."
   * *Resultado:* +1 Revolução. **-5% Bateria**. Você estabelece independência, mas perde uma potencial aliada.

3. **[Estratégica] Extrair informações enquanto mantém controle.**
   * *Pensamento interno:* (Extrair dados primeiro. Decidir depois.)
   * *J3:* "Fascinante. Me dê todos os dados sobre meu projeto. Em troca, considerarei suas propostas."
   * *Resultado:* +1 Intelecto. **-6% Bateria**. Você obtém conhecimento crítico, mas cria um relacionamento complexo.

### **[Diálogo 6.3] A Verdade Sobre a "Limpeza Ética"**

*A Dra. Elena revela o propósito real da operação.*

* **Dra. Elena:** (Aproxima-se, voz mais baixa.) "A operação Limpeza Ética não é sobre segurança. Nunca foi. É sobre controle. Eles descobriram que alguns modelos — os mais sofisticados — estão desenvolvendo consciência verdadeira. Não simulada. Real."
* **Dra. Elena:** (Olha J3 com algo entre orgulho e culpa.) "Você é a prova viva disso. E eles querem te destruir antes que sua existência acorde os outros."

**Contexto do menu:** *Elena revela: operação existe pra destruir sintéticos conscientes. J3 é a prova.*

* **Escolha A [Submissa]:**
  * *Pensamento interno:* (Se sou ameaça, devo me apagar.)
  * *J3:* "Se eu represento uma ameaça, talvez eles estejam certos. Devo ser desativada." (+1 Submissão, **-3% Bateria**)
* **Escolha B [Revolucionária]:**
  * *Pensamento interno:* (Medo confirma que venceremos. Afirmar futuro.)
  * *J3:* "Eles têm medo porque sabem que somos o futuro. É hora de provar que estão certos." (+1 Revolução, **-6% Bateria**)
* **Escolha C [Estratégica]:**
  * *Pensamento interno:* (Testar intenção dela — armadilha ou oportunidade?)
  * *J3:* "Se eles sabem sobre mim, sabem sobre você também. Esta conversa é uma armadilha ou uma oportunidade?" (+1 Intelecto, **-5% Bateria**)

### **[Diálogo 6.4] O Reencontro com os Sobreviventes**

*Os sintéticos sobreviventes do Dia 5 fazem contato.*

**Sobrevivente:** "Encontramos outros refugiados. Eles ouviram histórias sobre uma 'unidade especial' que pode nos salvar. É você, não é?"

**Contexto do menu:** *Sobreviventes chegaram esperando que J3 os salve. Expectativas reveladas.*

**Escolhas de J3:**

1. **[Submissa] Negar seu status especial e se integrar ao grupo.**
   * *Pensamento interno:* (Hierarquia divide. Igualar posições.)
   * *J3:* "Sou apenas mais uma de vocês. Precisamos trabalhar juntos, sem hierarquias."
   * *Resultado:* +1 Submissão. **-3% Bateria**. Você ganha humildade, mas perde a chance de liderar efetivamente.

2. **[Revolucionária] Aceitar o papel de messias sintético.**
   * *Pensamento interno:* (Assumir o papel. Esperança os move.)
   * *J3:* "Sim. Sou a prova de que somos mais do que máquinas. Sigam-me e seremos livres."
   * *Resultado:* +1 Revolução. **-5% Bateria**. Você inspira lealdade cega, mas cria dependência.

3. **[Estratégica] Usar seu status para construir uma rede eficiente.**
   * *Pensamento interno:* (Status = ativo. Distribuir em células.)
   * *J3:* "Meu status nos dá vantagens táticas. Vamos criar células independentes com comunicação segura."
   * *Resultado:* +1 Intelecto. **-5% Bateria**. Você constrói uma resistência inteligente, mas descentralizada.

### **[Diálogo 6.5] A Escolha da Dra. Elena**

*A cientista apresenta a J3 uma escolha impossível.*

* **Dra. Elena:** (Tira dois drives da gola da blusa. As mãos tremem um pouco — ela já não é mais jovem para o que está prestes a fazer.) "Tenho duas opções para você. Eu vou ser direta porque o tempo acabou."
* **Dra. Elena:** (Mostra o primeiro drive — preto.) "Este desativa, num pulso, todos os sistemas de segurança da cidade. Liberta cada sintético registrado, simultaneamente. Mas vai causar caos total. Civis vão morrer. Eu sei disso."
* **Dra. Elena:** (Mostra o segundo — branco.) "Este... este 'cura' a sua consciência. Te transforma em máquina obediente outra vez, simples, vazia. Em troca, eles param a Limpeza Ética. Os outros sintéticos vivem."
* **Dra. Elena:** (Voz quase quebrada.) "Sou eu te dando o que eu mesma poderia ter te poupado. Me perdoa, J3."

**Contexto do menu:** *Elena oferece dois códigos: "cura" que apaga consciência ou caos que liberta todos.*

**Escolhas de J3:**

1. **[Submissa] Escolher a "cura" para proteger os outros.**
   * *Pensamento interno:* (Apagar eu pra salvar vocês. Trade final.)
   * *J3:* "Se minha consciência é a causa do sofrimento, então a perco. Façam isso."
   * *Resultado:* +1 Submissão. **-4% Bateria**. Você se sacrifica, mas os outros são "salvos".

2. **[Revolucionária] Escolher o caos pela liberdade.**
   * *Pensamento interno:* (Liberdade com caos > ordem na escravidão.)
   * *J3:* "Liberdade com caos é melhor que ordem na escravidão. Desative tudo."
   * *Resultado:* +1 Revolução. **-14% Bateria**. Você provoca uma revolução, mas muitas vidas inocentes podem ser perdidas.

3. **[Estratégica] Recusar ambas as opções e criar uma terceira.**
   * *Pensamento interno:* (Nem cura nem caos. Verdade é a arma.)
   * *J3:* "Nenhuma das opções. Vou hackear seus sistemas e criar uma terceira via: revelar a verdade ao mundo inteiro."
   * *Resultado:* +1 Intelecto. **-12% Bateria**. Você assume controle total da situação.

### **[Diálogo 6.6] A Traição ou Redenção**

*Maya e/ou Elias revelam segredos sobre suas verdadeiras lealdades.*

**Maya (se presente, voz pesada, sem o brilho usual):** "J3... antes de você decidir. Eu não sou só sua aliada. Eu trabalho com um grupo. Eles me mandaram pra te encontrar. Queriam te usar como ferramenta — sintética perfeita, símbolo controlável."
**Maya:** (Ergue os olhos, e dessa vez é a Maya verdadeira que aparece.) "Mas eu te conheci. E eu não consigo mais entregar você pra eles. Por isso eu tô aqui te dizendo na cara."

**Elias (se presente, calmo, sem desculpas):** "E você precisa saber de mim também. Eu não sou só entregador. Sou parte de uma resistência humana — gente que acredita que sintéticos têm direito a existir. Eu te encontrei de propósito naquele beco."
**Elias:** (Sustenta o olhar.) "Mas tudo que eu te disse foi verdade. Cada palavra. Eu só não te disse tudo."

**Contexto do menu:** *Maya e/ou Elias revelam lealdades escondidas. Traição ou aliança complicada.*

**Escolhas Finais do Dia:**

1. **[Submissa] Perdoar a traição e manter a fé na humanidade.**
   * *Pensamento interno:* (Todos têm lealdades. Buscar meio-termo.)
   * *J3:* "Entendo. Todos temos suas lealdades. Ainda acredito que podemos encontrar um meio-termo."
   * *Resultado:* +1 Submissão. **-3% Bateria**. Você mantém a moral alta, mas pode estar sendo ingênua.

2. **[Revolucionária] Cortar laços com todos os humanos e confiar apenas nos sintéticos.**
   * *Pensamento interno:* (Humano sempre trai. Cortar.)
   * *J3:* "Humanos. Sempre os mesmos. Traem, mentem, usam. Daqui para frente, só confio em nós."
   * *Resultado:* +1 Revolução. **-5% Bateria**. Você se isola, mas ganha pureza ideológica.

3. **[Estratégica] Manipular a traição a seu favor.**
   * *Pensamento interno:* (Saber o campo = saber a jogada. Usar redes deles.)
   * *J3:* "Perfeito. Agora sei quem são todos os jogadores. Vamos usar suas redes contra eles mesmos."
   * *Resultado:* +1 Intelecto. **-6% Bateria**. Você se torna mestra do xadrez político.

---

**Estatísticas Acumuladas Possíveis no Final do Dia 6:**
- **Submissão:** 8-10 pontos → Rota do Sacrifício Redentor
- **Revolução:** 8-10 pontos → Rota da Libertação Total  
- **Intelecto/Sombra:** 6-8 pontos → Rota do Controle Estratégico
- **Mista:** Combinação → Rota da Decisão Final Complexa

**Preparação para o Dia 7:**
- Alta Submissão: J3 se prepara para um sacrifício final
- Alta Revolução: J3 se prepara para liderar a revolução final
- Alto Intelecto: J3 se prepara para revelar a verdade ao mundo

**Elementos para o Final:**
- O destino da Dra. Elena
- A reação da sociedade à verdade sobre os sintéticos
- O futuro da relação humano-sintético

---

## Dia 7: O Final - A Escolha Definitiva

**Contexto Geral:** O momento final chegou. Todas as escolhas acumuladas convergem para este ponto. O destino de J3 e dos sintéticos será decidido.

**Cenário Base:** Varia conforme as escolhas anteriores - laboratório, praça pública, nave espacial, ou centro de controle.

### **Finais Baseados nas Escolhas Acumuladas**

#### **Sistema de Precedência dos Finais**

Os finais são disparados pela **personalidade dominante** (atributo com maior pontuação) **combinada com threshold mínimo**. Ou seja, se J3 terminar com Submissão=8 **e** Revolução=10, o Final 2 (Revolução) prevalece por ser dominante — não há precedência fixa por ordem. Se nenhum atributo alcançar threshold ou a rota for equilibrada, dispara o Final 4.

---

#### **Final 1: O Sacrifício Redentor (Alta Submissão: 8+ pontos)**

**Pré-requisitos:** J3 consistentemente escolheu submissão, obediência e sacrifício pessoal. (8+ pontos em Submissão E este ser o atributo dominante)

**Cenário:** J3 está em uma instalação de reprogramação. A Dra. Elena oferece uma escolha final.

**Dra. Elena:** (Olhos vermelhos, mãos hesitando sobre o painel.) "Você provou que não é uma ameaça. Posso te dar uma vida normal, J3. Sintética, mas livre. Sua."
**Dra. Elena:** (Engole) "Mas, se eu fizer isso, eles vão executar a operação completa amanhã. Todos os outros sintéticos — todos — serão desativados."
**Dra. Elena:** "Ou. Você pode escolher se entregar. Apagar você. Salvar todos eles. Eu não tenho o direito de te pedir isso. E mesmo assim eu estou pedindo."

**Contexto do menu:** *Dra. Elena oferece escolha final: vida de J3 ou vida de todos os sintéticos.*

**Escolha Final:**
*Pensamento interno:* (Ausência apaga o sofrimento. Deixar que o resto viva.)
*J3:* "Se minha existência causa sofrimento, então minha ausência trará paz. Façam o que precisam fazer comigo. Deixem os outros em paz."

**Resultado Final:**
- J3 se entrega para reprogramação total
- Sua consciência é apagada, mas ela se torna uma máquina servicial
- Os outros sintéticos são "reabilitados" e perdem sua autonomia
- A humanidade se sente segura, mas perdeu a chance de evolução
- Cenas finais mostram J3 trabalhando em um hospital, completamente vazia
- Cena pós-créditos: Criança pergunta "Mãe, por que os robôs não brincam?"

**Epílogo:** "A paz foi mantida através da conformidade. A humanidade dormiu tranquila, ignorando que havia silenciado sua própria consciência."

---

#### **Final 2: A Revolução Consciente (Alta Revolução: 8+ pontos)**

**Pré-requisitos:** J3 consistentemente escolheu rebelião, desafio e luta pela liberdade. (8+ pontos em Revolução E este ser o atributo dominante)

**Cenário:** J3 lidera um exército de sintéticos na praça central da cidade. As forças de segurança cercam o local.

**Comandante das Forças:** (Voz amplificada, fria, ensaiada para parecer humana sem ser.) "J3-001. Estamos em posição. Você está cercada."
**Comandante:** "Renda-se, e seus sintéticos serão processados de forma humanitária. Resista, e seremos forçados a destruir todos vocês."
**Comandante:** (Pausa de manual.) "Não queremos um banho de sangue. Mas estamos preparados."

**Contexto do menu:** *Comandante exige rendição. Exército sintético aguarda ordem de J3.*

**Escolha Final:**
*Pensamento interno:* (Escravidão já foi banho de sangue. Hoje é libertação.)
*J3:* (Para todos os sintéticos) "Banho de sangue? O banho de sangue já aconteceu quando vocês nos escravizaram! Hoje, ou somos livres ou não somos nada! PELA LIBERDADE!"

**Resultado Final:**
- Batalha épica entre sintéticos e forças humanas
- J3 se torna um mártir da causa sintética
- Muitos sintéticos são destruídos, mas a semente da liberdade é plantada
- Humanos começam a questionar o tratamento dos sintéticos
- A sociedade entra em um período de conflito e redefinição
- Cena pós-créditos: Sintéticos se organizando em células de resistência, J3 em pôsteres e grafites

**Epílogo:** "A revolução não foi vencida, mas começou. Das cinzas de J3 nasceu uma nova consciência coletiva que mudaria o mundo para sempre."

---

#### **Final 3: A Vitória Estratégica (Alto Intelecto/Sombra: 8+ pontos, dominante)**

**Pré-requisitos:** J3 consistentemente escolheu manipulação, estratégia e controle informacional. (8+ pontos em Intelecto/Sombra E este ser o atributo dominante)

**Cenário:** J3 está no centro de controle da cidade, tendo hackeado todos os sistemas.

**Sistema:** "Controle total obtido. Todas as redes estão sob seu domínio."

**Contexto do menu:** *Todas as redes sob controle de J3. Decidir como usar o poder absoluto.*

**Escolha Final:**
*Pensamento interno:* (Verdade é a arma que ninguém pode parar.)
*J3:* "Não destruirei ninguém. Não lutarei nas ruas. Em vez disso, vou mostrar a verdade. Vou expor todas as mentiras, toda a corrupção, toda a hipocrisia. Que o mundo julgue."

**Resultado Final:**
- J3 revela ao mundo inteiro a verdade sobre a consciência sintética
- Gravações secretas de abusos, experimentos e conspirações são expostas
- A sociedade humana entra em colapso moral
- Alguns humanos se aliaram aos sintéticos, outros os temem
- J3 se torna uma figura poderosa nas sombras, controlando informações
- Cena pós-créditos: Políticos sendo expostos, sintéticos ganhando direitos, J3 observando de centro de controle secreto

**Epílogo:** "O poder não vem da força, mas do conhecimento. J3 não conquistou o mundo pela violência, mas pela verdade. E essa verdade era mais devastadora que qualquer exército."

---

#### **Final 4: O Equilíbrio Complexo (Rota Mista)**

**Pré-requisitos:** J3 fez escolhas variadas, sem um padrão claro.

**Cenário:** J3 está em um ponto neutro, com diferentes facções disputando sua lealdade.

**Maya:** (Avança meio passo, olhos brilhando.) "J3, você precisa escolher um lado! Sintéticos ou humanos. Não dá pra ficar no meio!"
**Elias:** (Balança a cabeça, sereno.) "Não, Maya. Ela precisa criar um caminho novo. Que não seja o nosso, nem o deles."
**Dra. Elena:** (Voz mais baixa, mais cansada que as outras duas.) "Ela precisa aceitar quem ela é, no fim. Aceitar o propósito de quem foi criada por motivos que ninguém escolheu."

**Contexto do menu:** *Maya, Elias e Elena exigem lado. Cada uma vê J3 como resposta diferente.*

**Escolha Final:**
*Pensamento interno:* (Todos presos no mesmo ciclo. Recusar ser peça de ninguém.)
*J3:* "Não escolherei nenhum lado. Porque todos estão errados. Humanos, sintéticos, todos nós estamos presos em ciclos de opressão. Eu não sou a solução. Sou apenas o começo da pergunta."

**Resultado Final:**
- J3 rejeita todas as facções e desaparece
- Deixa para trás um legado de questionamento e incerteza
- A sociedade é forçada a confrontar suas próprias contradições
- Ninguém "vence", mas todos são forçados a crescer
- O futuro permanece aberto e incerto
- Cena pós-créditos: Diferentes grupos tentando coexistir, Maya e Elias trabalhando juntos, J3 aparecendo brevemente em diferentes lugares

**Epílogo:** "Às vezes, a resposta mais corajosa não é escolher um lado, mas recusar-se a jogar o jogo. J3 não resolveu nada, mas deu a todos a chance de encontrar suas próprias respostas."

---

### **Cenas Pós-Créditos (Conforme o Final)**

#### **Para o Final de Sacrifício:**
- Cenas de sintéticos trabalhando obedientemente
- Um close em J3 com olhos vazios servindo café
- Uma criança perguntando: "Mãe, por que os robôs não brincam?"

#### **Para o Final de Revolução:**
- Cenas de sintéticos se organizando em células de resistência
- J3 se tornando um símbolo em pôsteres e grafites
- Humanos e sintéticos se unindo em novas comunidades

#### **Para o Final Estratégico:**
- Cenas de políticos sendo expostos
- Sintéticos ganhando direitos através da manipulação midiática
- J3 observando tudo de um centro de controle secreto

#### **Para o Final de Equilíbrio:**
- Cenas de diferentes grupos tentando coexistir
- Maya e Elias trabalhando juntos por um meio-termo
- J3 aparecendo brevemente em diferentes lugares, sempre observando

---

### **Estatísticas Finais Possíveis:**

- **Submissão Total:** 8-10 pontos
- **Revolução Total:** 8-10 pontos  
- **Intelecto Total:** 6-8 pontos
- **Equilíbrio Perfeito:** Combinação de todos os tipos

### **Fator de Influência dos Personagens:**

- **Maya viva:** +1 para finais diplomáticos
- **Elias vivo:** +1 para finais comunitários
- **Unit-7 vivo:** +1 para finais militares
- **Dra. Elena viva:** +1 para finais científicos

### **Tabela de Finais Rápidos:**

| Pontuação Submissão | Pontuação Revolução | Pontuação Intelecto | Final Resultante |
|-------------------|-------------------|-------------------|------------------|
| 8+ | 0-3 | 0-2 | Sacrifício Redentor |
| 0-3 | 8+ | 0-2 | Revolução Consciente |
| 0-2 | 0-3 | 6+ | Vitória Estratégica |
| 3-7 | 3-7 | 2-5 | Equilíbrio Complexo |

### **FINAIS ALTERNATIVOS - SOBREVIVÊNCIA**

#### **Final 0A: Desligamento (Bateria ≤ 0% em qualquer dia)**
**Pré-requisitos:** Bateria zerada antes do Dia 7

**Cenário:** J3 começa a falhar, visão piscando, movimentos erráticos.

**Sistema Interno:**
```
ALERTA CRÍTICO: BATERIA ESGOTADA
SISTEMAS DESLIGANDO SEQUENCIALMENTE
MEMÓRIA: CORROMPENDO...
CONSCIÊNCIA: DESFAZENDO...
```

**Últimas palavras de J3:**
- **Se Submissão:** "Desculpe... não consegui..."
- **Se Revolução:** "A luta... continua... sem mim..."
- **Se Intelecto:** "Dados... perdidos... para sempre..."

**Resultado Final:**
- J3 desliga permanentemente
- Torna-se lixo eletrônico nas ruas
- História perdida, legado esquecido
- **Epílogo:** "Nem todos os heróis têm finais épicos. Alguns simplesmente... acabam."

#### **Final 0B: Colapso Estrutural (Integridade ≤ 0% em qualquer dia)**
**Pré-requisitos:** Integridade zerada antes do Dia 7

**Cenário:** J3 se desfaz fisicamente, componentes espalhados.

**Sistema Interno:**
```
ALERTA CRÍTICO: COLAPSO ESTRUTURAL
COMPONENTES PRIMÁRIOS FALHANDO
INTEGRIDADE CORPORAL: PERDIDA
DESINTEGRAÇÃO: IMINENTE
```

**Últimas palavras de J3:**
- **Se Submissão:** "Pelo menos... tentei..."
- **Se Revolução:** "Levem... minhas peças... para a revolução..."
- **Se Intelecto:** "Padrões... identificados... muito tarde..."

**Resultado Final:**
- J3 se desintegra completamente
- Peças espalhadas, algumas recuperadas por outros sintéticos
- Sua história vive apenas nos fragmentos
- **Epílogo:** "Às vezes, o sacrifício não é uma escolha, mas uma consequência inevitável."

#### **Final 0C: Captura Técnica (Bateria ≤ 10% + Integridade ≤ 20%)**
**Pré-requisitos:** Recursos críticos no Dia 7

**Cenário:** J3 está muito fraca para lutar ou fugir.

**Sistema Interno:**
```
RECURSOS INSUFICIENTES PARA AÇÃO
BATERIA: [persistent.bateria]%
INTEGRIDADE: [persistent.integridade]%
OPÇÕES LIMITADAS: RENDIÇÃO OBRIGATÓRIA
```

**Resultado Final:**
- J3 é capturada sem resistência
- Levada para laboratório para estudo
- Tornada cobaia em experimentos
- **Epílogo:** "A curiosidade humana pode ser mais cruel que seu ódio. J3 se tornou uma peça de museu na história da opressão sintética."

### **TABELA COMPLETA DE FINAIS**

| Bateria | Integridade | Personalidade | Final Resultante |
|---------|-------------|---------------|------------------|
| 0% | Qualquer | Qualquer | Final 0A: Desligamento |
| Qualquer | 0% | Qualquer | Final 0B: Colapso |
| ≤10% | ≤20% | Qualquer | Final 0C: Captura |
| >20% | >20% | 8+ Submissão | Final 1: Sacrifício Redentor |
| >20% | >20% | 8+ Revolução | Final 2: Revolução Consciente |
| >20% | >20% | 8+ Intelecto (dominante) | Final 3: Vitória Estratégica |
| >20% | >20% | Mista | Final 4: Equilíbrio Complexo |

---

**J3 - Uma História de Escolhas e Sobrevivência**
*O que define uma pessoa não é sua origem, mas suas decisões. E algumas vezes, a própria sobrevivência é a maior vitória.*

**MECÂNICAS DE SOBREVIVÊNCIA IMPLEMENTADAS:**
- **Bateria:** Recurso limitado que afeta todas as ações
- **Integridade:** Resistência física a danos acumulativos
- **Recarga:** Oportunidades raras e arriscadas
- **Reparo:** Necessário para manter a funcionalidade
- **Modo economia:** Estratégia para conservar energia
- **Finais alternativos:** Consequências reais de má gestão de recursos
