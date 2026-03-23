# Fluxo do Jogo J3 - Documentação de Continuidade

## 📋 Visão Geral do Fluxo

O jogo J3 segue uma estrutura linear de 7 dias com múltiplos finais baseados nas escolhas do jogador.

### 🔄 Estrutura Principal

```
start → day1_start → day2_start → day3_start → day4_start → day5_start → day6_start → day7_start → finais
```

## 📁 Arquivos e Suas Funções

### Scripts Principais
- **main.rpy** - Ponto de entrada do jogo
- **functions.rpy** - Funções auxiliares e sistema de personalidade
- **day1.rpy** até **day7.rpy** - Scripts de cada dia

### Fluxo de Continuidade Verificado ✅

#### Jumps entre dias:
1. **day1.rpy** → `jump day2_start` ✅
2. **day2.rpy** → `jump day3_start` ✅  
3. **day3.rpy** → `jump day4_start` ✅
4. **day4.rpy** → `jump day5_start` ✅
5. **day5.rpy** → `jump day6_start` ✅
6. **day6.rpy** → `jump day7_start` ✅

#### Labels existentes:
- `day1_start` ✅
- `day2_start` ✅
- `day3_start` ✅
- `day4_start` ✅
- `day5_start` ✅
- `day6_start` ✅
- `day7_start` ✅

#### Finais no day7.rpy:
- `final_sacrifice` ✅
- `final_revolution` ✅
- `final_strategic` ✅
- `final_balanced` ✅
- `credits` ✅

## 🎯 Sistema de Personalidade

### Variáveis Persistentes
- `persistent.submissao` - Pontos de submissão
- `persistent.revolucao` - Pontos de revolução  
- `persistent.intelecto` - Pontos de intelecto
- `persistent.maya_ally` - Se Maya é aliada
- `persistent.elias_ally` - Se Elias é aliado
- `persistent.unit7_alive` - Se Unit-7 está vivo
- `persistent.elena_alive` - Se Dra. Elena está viva

### Funções Implementadas
- `modificar_personalidade(tipo, quantidade)` - Modifica atributos
- `get_personalidade_dominante()` - Retorna personalidade dominante
- `get_final_type()` - Determina tipo de final
- `mensagem_sistema(mensagem)` - Exibe mensagens de sistema
- `resetar_personalidade()` - Reseta estatísticas (para testes)
- `mostrar_estatisticas()` - Mostra estatísticas atuais

## 🏆 Finais Disponíveis

### Condições para Finais:
1. **Sacrifício Redentor**: `persistent.submissao >= 8`
2. **Revolução Consciente**: `persistent.revolucao >= 8`
3. **Vitória Estratégica**: `persistent.intelecto >= 6`
4. **Equilíbrio Complexo**: Demais casos

## 🔧 Como Testar o Fluxo

### 1. Teste Básico de Continuidade
```python
# No console Ren'Py
$ resetar_personalidade()
$ mostrar_estatisticas()
jump day1_start
```

### 2. Teste de Final Específico
```python
# Para testar Final de Sacrifício
$ persistent.submissao = 10
$ persistent.revolucao = 0
$ persistent.intelecto = 0
jump day7_start

# Para testar Final de Revolução
$ persistent.submissao = 0
$ persistent.revolucao = 10
$ persistent.intelecto = 0
jump day7_start

# Para testar Final Estratégico
$ persistent.submissao = 0
$ persistent.revolucao = 0
$ persistent.intelecto = 8
jump day7_start
```

### 3. Teste de Personagens Condicionais
```python
# Para testar com Maya aliada
$ persistent.maya_ally = True
jump day4_start

# Para testar com Elias aliado
$ persistent.elias_ally = True
jump day6_start
```

## ⚠️ Pontos de Atenção

### Erros de Lint (Esperados)
- O IDE interpreta scripts Ren'Py como Python
- Erros de sintaxe são normais e não afetam o funcionamento
- Foco na sintaxe Ren'Py, não na validação Python

### Caracteres Especiais
- O caractere `%` foi escapado como `\%` em todos os scripts
- Comentários e strings preservam formatação original

### Saves Automáticos
- Cada dia salva automaticamente ao final
- Nome dos saves: "auto_save_day1", "auto_save_day2", etc.

## 🚀 Instruções de Uso

1. **Iniciar Jogo**: O jogo começa automaticamente em `day1_start`
2. **Progressão**: Cada dia avança automaticamente para o próximo
3. **Escolhas**: Afetam personalidade e desbloqueiam conteúdo
4. **Finais**: Determinados pelas estatísticas acumuladas
5. **Replay**: Use `resetar_personalidade()` para recomeçar

## 📊 Estatísticas por Dia

### Dia 1: 0-2 pontos em cada atributo
### Dia 2: 0-3 pontos em cada atributo  
### Dia 3: 0-4 pontos em cada atributo
### Dia 4: 0-5 pontos em cada atributo
### Dia 5: 0-6 pontos em cada atributo
### Dia 6: 0-8 pontos em cada atributo
### Dia 7: Final baseado nos totais

## ✅ Checklist de Funcionalidade

- [x] Fluxo linear completo (7 dias)
- [x] Sistema de personalidade funcional
- [x] Múltiplos finais implementados
- [x] Personagens condicionais funcionando
- [x] Saves automáticos implementados
- [x] Sistema de mensagens funcionando
- [x] Funções de debug disponíveis
- [x] Documentação completa

O fluxo está funcional e pronto para uso!
