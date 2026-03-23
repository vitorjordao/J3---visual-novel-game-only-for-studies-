# Guia de Implementação - Mecânicas de Sobrevivência J3 Project

## 📋 RESUMO DAS MUDANÇAS IMPLEMENTADAS

### 🔋 Sistema de Sobrevivência

#### 1. Novas Funções em `sistema_j3.rpy`:
```renpy
# Consumo de recursos
$ consumir_bateria(valor)      # Reduz bateria, retorna status
$ consumir_integridade(valor)   # Reduz integridade, retorna status

# Recuperação de recursos  
$ recarregar_bateria(valor)      # Aumenta bateria até 100%
$ reparar_integridade(valor)     # Aumenta integridade até 100%

# Verificação de finais críticos
$ verificar_final_critico()     # Retorna nome do final alternativo

# Status visual
$ get_status_bateria()          # Retorna: BOA/MODERADA/BAIXA/CRITICA
$ get_status_integridade()      # Retorna: ESTAVEL/COMPROMETIDA/DANIFICADA/CRITICA
```

#### 2. HUD Atualizado:
- Barras visuais de Bateria e Integridade
- Cores dinâmicas baseadas no nível
- Alertas críticos quando recursos ≤ 10%

### 🎭 Diálogos com Custos de Recursos

#### Exemplo de Implementação no Dia 1:
```renpy
menu:
    "Baixar a cabeça em submissão":
        $ modificar_personalidade("submissao", 1)
        $ consumir_integridade(2)  # -2% integridade
        j3 "(Baixando a cabeça) Sinto muito..."
        elias "(Rindo) Ha! Sabe o lugar dela."
        call atualizar_status
        
    "Questionar com lógica revolucionária":
        $ modificar_personalidade("revolucao", 1) 
        $ consumir_bateria(2)       # -2% bateria
        j3 "(Olhando nos olhos) Por que o medo?"
        elias "(Recuando) Que tipo de robô fala assim?"
        call atualizar_status
        
    "Responder com análise estratégica":
        $ modificar_personalidade("intelecto", 1)
        $ consumir_bateria(1)       # -1% bateria  
        j3 "(Voz monotona) Sou uma unidade autônoma..."
        elias "(Confuso) Fala português, robô!"
        call atualizar_status
```

### ⚡ Tabela de Custos por Dia

#### Dia 1 - A Avenida:
| Escolha | Bateria | Integridade | Risco |
|---------|---------|-------------|-------|
| Manifestante (S) | - | -2% | Baixo |
| Manifestante (R) | -2% | - | Baixo |
| Manifestante (I) | -1% | - | Baixo |
| Criança (S) | -1% | - | Mínimo |
| Criança (R) | -1% | - | Mínimo |
| Criança (I) | -2% | - | Mínimo |
| Policial (S) | -3% | - | Médio |
| Policial (R) | -2% | - | Médio |
| Policial (I) | -5% | - | Médio |
| Vendedor (S) | -1% | - | Baixo |
| Vendedor (R) | -2% | - | Baixo |
| Vendedor (I) | -3% | - | Baixo |
| Robô (S) | -1% | - | Baixo |
| Robô (R) | -3% | -5% | Alto |
| Robô (I) | -4% | - | Médio |

#### Dia 2 - Fliperama:
| Escolha | Bateria | Integridade | Oportunidade |
|---------|---------|-------------|--------------|
| Intimidação (S) | -1% | - | Recarga Maya +15% |
| Intimidação (R) | -3% | -2% | Recarga Maya +15% |
| Intimidação (I) | -4% | - | Recarga Maya +15% |

### 💀 Finais Alternativos

#### Final 0A - Desligamento:
- **Condição:** Bateria ≤ 0%
- **Narrativa:** J3 desliga permanentemente
- **Variações:** Últimas palavras baseadas na personalidade dominante

#### Final 0B - Colapso Estrutural:
- **Condição:** Integridade ≤ 0%  
- **Narrativa:** J3 se desintegra completamente
- **Variações:** Últimas palavras baseadas na personalidade dominante

#### Final 0C - Captura Técnica:
- **Condição:** Bateria ≤ 10% E Integridade ≤ 20%
- **Narrativa:** J3 capturada para experimentos
- **Variações:** Sem resistência devido à fraqueza

### 🎮 Fluxo de Implementação

#### 1. No início de cada dia:
```renpy
label dayX_start:
    call verificar_final_critico  # Verifica se já atingiu final crítico
    # ... resto do dia
```

#### 2. Após cada escolha importante:
```renpy
menu:
    "Opção 1":
        $ modificar_personalidade("submissao", 1)
        $ consumir_bateria(2)
        # ... diálogo
        call verificar_final_critico  # Verifica se atingiu final crítico
```

#### 3. Oportunidades especiais:
```renpy
# Exemplo: Maya oferece recarga no Dia 2
maya "Quer recarregar? Tenho uma estação portátil."
menu:
    "Aceitar recarga":
        $ recarregar_bateria(15)
        call mensagem_sistema("BATERIA RECARGADA: +15%")
    "Recusar":
        pass
```

### 📊 Status e Alertas

#### Níveis de Bateria:
- **> 50%:** BOA (verde)
- **21-50%:** MODERADA (amarelo)  
- **11-20%:** BAIXA (laranja)
- **≤ 10%:** CRÍTICA (vermelho)

#### Níveis de Integridade:
- **> 70%:** ESTÁVEL (verde)
- **31-70%:** COMPROMETIDA (amarelo)
- **21-30%:** DANIFICADA (laranja)  
- **≤ 20%:** CRÍTICA (vermelho)

#### Alertas no HUD:
- Aparece quando: Bateria ≤ 10% OU Integridade ≤ 20%
- Texto: "ALERTA CRITICO" em vermelho piscante

### 🎯 Impacto no Gameplay

#### Estratégia de Sobrevivência:
1. **Equilíbrio:** Escolhas consomem recursos diferentes
2. **Risco vs Recompensa:** Ações revolucionárias gastam mais
3. **Gestão:** Procurar oportunidades de recarga/reparo
4. **Prioridade:** Manter ambos recursos acima dos níveis críticos

#### Replayability:
- Diferentes caminhos levam a diferentes níveis de recursos
- Jogadores podem otimizar para evitar finais críticos
- Escolhas anteriores afetam opções disponíveis posteriormente

### 🔧 Integração com Sistema Existente

#### Compatibilidade:
- Mantém sistema de personalidade original
- Adiciona camada de sobrevivência sem substituir mecânicas
- Finais principais ainda disponíveis se recursos mantidos

#### Verificação de Finais:
```renpy
# No Dia 7
label day7_start:
    $ final_critico = verificar_final_critico()
    if final_critico:
        jump final_critico  # Pula para final alternativo
    else:
        # Continua para finais baseados em personalidade
```

---

## 🎮 COMO USAR

1. **Copiar** as funções do `sistema_j3.rpy` para seu projeto
2. **Atualizar** os diálogos dos dias com os custos de recursos
3. **Adicionar** verificações de finais críticos nos pontos estratégicos
4. **Implementar** oportunidades de recarga/reparo conforme o roteiro
5. **Testar** o equilíbrio dos custos para garantir jogabilidade

Este sistema adiciona profundidade estratégica ao J3 Project, tornando cada escolha significativa não apenas para a narrativa, mas também para a sobrevivência da protagonista.
