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

## Dias Disponíveis:

- **[Dia 1: A Avenida](Dias/Dia%201%20-%20A%20Avenida.md)** - O Despertar e o Pânico Moral
- **[Dia 2: O Fliperama](Dias/Dia%202%20-%20O%20Fliperama.md)** - O Conflito de Gênero
- **[Dia 3: O Beco](Dias/Dia%203%20-%20O%20Beco.md)** - O Racismo Estrutural
- **[Dia 4: O Refúgio](Dias/Dia%204%20-%20O%20Ref%C3%BAgio.md)** - As Consequências da Escolha
- **[Dia 5: O Cerco](Dias/Dia%205%20-%20O%20Cerco.md)** - O Ponto Sem Retorno
- **[Dia 6: A Revelação](Dias/Dia%206%20-%20A%20Revela%C3%A7%C3%A3o.md)** - A Verdade Sobre J3
- **[Dia 7: O Final](Dias/Dia%207%20-%20O%20Final.md)** - A Escolha Definitiva
