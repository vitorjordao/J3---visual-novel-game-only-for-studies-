# Game Design Document - J3 Projeto

**Título:** J3 - A Consciência Artificial  
**Gênero:** Visual Novel / Jogo Narrativo Interativo  
**Engine:** Ren'Py  
**Plataforma:** PC (Windows/Linux/Mac)  
**Público-Alvo:** +16 anos  
**Duração Estimada:** 2-3 horas  

---

## 1. Visão Geral

### 1.1 Conceito
J3 é um visual novel cyberpunk que explora temas de identidade, preconceito e livre-arbítrio através das escolhas do jogador que moldam a personalidade de um robô humanoide que desperta sem memória.

### 1.2 Fundamentação Cultural (Baseado no Manual MINC)
- **Produção Cultural Brasileira Independente:** Projeto alinhado com as diretrizes do Marco Legal dos Games
- **Diversidade Cultural:** Explora temas de preconceito racial, de gênero e tecnológico
- **Inovação Narrativa:** Sistema de branching complexo com múltiplos finais
- **Representatividade:** Personagens diversos e narrativa inclusiva

---

## 2. Mecânicas Principais

### 2.1 Sistema de Escolhas e Personalidade
**Mecânica Central:** Cada escolha do jogador afeta indicadores de personalidade:

- **Submissão (0-10):** Rota de obediência e sacrifício
- **Revolução (0-10):** Rota de rebelião e liberdade  
- **Intelecto/Sombra (0-10):** Rota estratégica e manipulação
- **Equilíbrio:** Resultado de valores balanceados

### 2.2 Estrutura Narrativa
- **7 Dias de Gameplay:** Estrutura em atos
- **Branching Dinâmico:** Escolhas afetam eventos futuros
- **4 Finais Principais:** Baseado na personalidade final
- **Sistema de Memória:** Recuperação gradual da identidade

---

## 3. Personagens

### 3.1 Protagonista
**J3-001:** Robô humanoide, aparência andrógina, desperta sem memória
- **Estado Inicial:** Neutro, confuso, processando ambiente
- **Evolução:** Moldada pelas escolhas do jogador
- **Sistema Interno:** Interface HUD mostrando status e memória

### 3.2 Personagens Secundários
- **Maya (22 anos):** Garota do fliperama, potencial aliada, representa curiosidade humana
- **Elias (35 anos):** Entregador, vítima de preconceito racial, tema de injustiça social
- **Unit-7:** Sintético militar, líder do refúgio, representa ordem vs liberdade
- **Dra. Elena (45 anos):** Cientista criadora, figura de autoridade moral

---

## 4. Estrutura de Conteúdo

### 4.1 Progressão dos Dias
**Dias 1-3: Introdução e World Building**
- Dia 1: Avenida - Despertar e pânico moral
- Dia 2: Fliperama - Conflito de gênero
- Dia 3: Beco - Racismo estrutural

**Dias 4-7: Consequências e Resolução**
- Dia 4: Refúgio - Consequências das escolhas
- Dia 5: Cerco - Ponto sem retorno
- Dia 6: Revelação - Verdade sobre J3
- Dia 7: Final - Escolha definitiva

### 4.2 Sistema de Branching
- **Escolhas Principais:** 15-20 decisões significativas
- **Eventos Condicionais:** Desbloqueados baseados em personalidade
- **Diálogos Dinâmicos:** Respondem a indicadores de personalidade
- **Flashbacks:** Recuperação de memória progressiva

---

## 5. Aspectos Técnicos

### 5.1 Plataformas de Produção
- **Engine:** Ren'Py 8.x
- **Desenvolvimento:** Python + Ren'Py Script
- **Versionamento:** Git/GitHub
- **Distribuição:** Itch.io (primário), Steam (secundário)

### 5.2 Hardware e Software
- **Desenvolvimento:** PC padrão, 8GB RAM mínimo
- **Arte:** Krita/GIMP (grátis) ou Photoshop
- **Áudio:** Audacity (grátis)
- **Testes:** Build Ren'Py multiplataforma

### 5.3 Requisitos Mínimos (Jogador)
- **SO:** Windows 7+, macOS 10.12+, Linux
- **Processador:** Dual-core 2GHz
- **Memória:** 4GB RAM
- **Armazenamento:** 500MB disponível
- **Vídeo:** Placa de vídeo integrada

---

## 6. Arte e Áudio

### 6.1 Estilo Visual
- **Arte:** 2D digital, estilo cyberpunk noir
- **Resolução:** 1920x1080 (escalável)
- **Personagens:** Sprites com expressões variadas
- **Cenários:** Backgrounds detalhados com atmosfera urbana

### 6.2 Interface
- **UI:** Minimalista, cyberpunk
- **HUD:** Sistema interno de J3 integrado à interface
- **Menus:** Navegação intuitiva com tema tecnológico

### 6.3 Áudio
- **Música:** Ambient cyberpunk, synthwave
- **Efeitos:** Interface tecnológica, ambiente urbano
- **Voz:** Diálogos sem voz (texto apenas) - otimização para dev solo

---

## 7. Metas de Desenvolvimento

### 7.1 Escopo Realista (Dev Solo)
- **Arte Simplificada:** Foco em storytelling sobre complexidade visual
- **Sistema Modular:** Implementação incremental de funcionalidades
- **Conteúdo Essencial:** 7 dias + 4 finais (sem conteúdo extra inicialmente)

### 7.2 Métricas de Sucesso
- **Conclusão:** Projeto finalizável em 2 meses
- **Qualidade:** Experiência completa sem bugs críticos
- **Impacto:** Narrativa coesa com mensagem clara

---

## 8. Aspectos Culturais e Sociais

### 8.1 Temas Explorados
- **Identidade:** O que nos torna humanos?
- **Preconceito:** Análise de discriminação em múltiplas formas
- **Tecnologia:** Relação humano-máquina na sociedade
- **Livre-arbítrio:** Escolhas e consequências morais

### 8.2 Representatividade (Diretriz MINC)
- **Diversidade Étnico-Racial:** Personagens representativos
- **Gênero:** Exploração de identidade de gênero
- **Regionalismo:** Contexto urbano brasileiro contemporâneo
- **Acessibilidade:** Interface clara e compreensível

---

## 9. Distribuição e Marketing

### 9.1 Plataformas
- **Primário:** Itch.io (acessível para indie)
- **Secundário:** Steam (se recursos disponíveis)
- **Gratuito:** Versão demo nos 2 primeiros dias

### 9.2 Estratégia de Lançamento
- **Demo:** Dias 1-2 gratuitos
- **Completo:** Pequeno custo simbólico ou gratuito
- **Comunidade:** Foco em feedback e melhoria contínua

---

## 10. Cronograma Simplificado (Dev Solo)

### Fase 1: Design e Documentação (2 semanas)
- GDD finalizado
- Roteiro revisado
- Arte conceitual básica

### Fase 2: Desenvolvimento Core (4 semanas)
- Projeto Ren'Py configurado
- Sistema de escolhas implementado
- Arte básica dos personagens

### Fase 3: Conteúdo (4 semanas)
- Dias 1-7 implementados
- Branching funcional
- Testes e correções

### Fase 4: Polimento (2 semanas)
- Arte finalizada
- Áudio implementado
- Bugs corrigidos

**Total:** 12 semanas (3 meses)

---

## 11. Riscos e Mitigações

### 11.1 Riscos Principais
- **Escopo:** Complexidade do sistema de branching
- **Tempo:** Arte consome mais tempo que esperado
- **Técnico:** Limitações do Ren'Py

### 11.2 Mitigações
- **MVP:** Foco na experiência narrativa essencial
- **Arte Simplificada:** Estilo consistente mas simples
- **Testes Contínuos:** Validação frequente de funcionalidades

---

## 12. Orçamento Zero (Dev Solo)

### 12.1 Custos Mínimos
- **Software:** 100% gratuito (Ren'Py, Krita, Audacity)
- **Distribuição:** Sem custos no Itch.io
- **Marketing:** Orgânico, redes sociais

### 12.2 Investimento de Tempo
- **Total:** 150-200 horas
- **Semanal:** 15-20 horas
- **Foco:** Consistência sobre intensidade

---

**Status:** Em Desenvolvimento  
**Versão:** 1.0  
**Última Atualização:** 21/03/2026  
**Desenvolvedor:** Solo (Equipe de 1 pessoa)
