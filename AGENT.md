# AGENT KNOWLEDGE BASE - Ren'Py & J3 Project
# Documentação técnica para futuras iterações de IA

## REN'PY - CONHECIMENTOS TÉCNICOS

### Estrutura de Arquivos
- **Extensão:** `.rpy` para scripts (texto), `.rpyc` para compilados (binário)
- **Diretório principal:** `game/` contém todos os scripts e recursos
- **Scripts:** Geralmente em `game/scripts/` para organização por dia/cena
- **Imagens:** Em `game/images/` (sprites, backgrounds, etc)
- **Áudio:** Em `game/audio/` (música, efeitos sonoros)
- **Fontes:** Em `game/fonts/`

### Sintaxe Básica Ren'Py

#### Labels (Marcadores)
```renpy
label nome_label:
    # Código aqui
    jump outro_label  # Salta para outro label
    return  # Retorna ao label anterior
```

#### Diálogos
```renpy
character j3 "Texto do diálogo"
narrator "Texto da narração"
```

#### Menus de Escolha
```renpy
menu:
    "Opção 1":
        # Código se escolher Opção 1
    "Opção 2":
        # Código se escolher Opção 2
```

#### Indentação
- **CRÍTICO:** Ren'Py é sensível a indentação
- **Padrão:** 4 espaços por nível de indentação
- **Erros comuns:**
  - `Indentation mismatch` - indentação inconsistente
  - `end of line expected` - sintaxe incorreta
  - Labels devem estar no nível base (sem indentação)
  - Código dentro de labels deve ter indentação
  - Opções de menu devem ter indentação
  - Código dentro de opções de menu deve ter indentação adicional

#### Variáveis Persistentes
```renpy
# Definição em init python
init python:
    persistent.bateria = 100
    persistent.integridade = 100
    persistent.submissao = 0
    persistent.revolucao = 0
    persistent.intelecto = 0
    persistent.maya_ally = False
    persistent.elias_ally = False
```

#### Screens (Telas)
```renpy
screen nome_screen:
    # Elementos da tela
    frame:
        # Conteúdo do frame
    text "Texto"
    key "f" action Function(funcao)  # Key binding
```

#### Transformações
```renpy
transform nome_transform:
    alpha 0.0
    linear 0.5 alpha 1.0
```

#### Show/Hide de Personagens
```renpy
show j3 neutral at center with dissolve
hide j3
show unit7 stern at left
```

#### Python Blocks
```renpy
init python:
    def funcao():
        # Código Python
        pass

$ variavel = valor
$ funcao()
```

#### Call/Jump
```renpy
call label_nome  # Chama e retorna
jump label_nome  # Salta e não retorna
```

### Erros Comuns Ren'Py

1. **Indentation Mismatch**
   - Causa: Indentação inconsistente
   - Solução: Verificar que todos os níveis de indentação estão corretos
   - Labels: sem indentação
   - Código dentro de labels: 4 espaços
   - Menu: 4 espaços
   - Opções de menu: 8 espaços
   - Código dentro de opções: 12 espaços

2. **End of Line Expected**
   - Causa: Sintaxe incorreta, geralmente em config.keymap
   - Solução: Usar screens com key bindings em vez de config.keymap

3. **Label Defined Twice**
   - Causa: Mesmo label em múltiplos arquivos
   - Solução: Renomear um dos labels para evitar conflito

4. **Key Binding Conflicts**
   - Causa: Tecla conflita com keybindings do Ren'Py
   - Solução: Usar teclas não reservadas (ex: 'F' em vez de 'D' para debug)

5. **NameError: HideScreen is not defined**
   - Causa: Usar `HideScreen()` em vez de `Hide()` em screens
   - Solução: Usar `Hide("screen_name")` em vez de `HideScreen("screen_name")`
   - Exemplo correto: `key "p" action Hide("debug_menu")`

6. **NameError: name 'X' is not defined (substituição de variáveis)**
   - Causa: Colchetes em texto são interpretados como substituição de variável
   - Exemplo: "Fechar [P]" causa erro porque [P] é interpretado como variável
   - Solução: Usar parênteses ou escapar colchetes
   - Exemplo correto: "Fechar (P)" ou "Fechar {{[P]}}"

7. **Screen key handler não funcionando**
   - Causa: Screen com key binding não está sendo mostrado
   - Solução: Usar `show screen nome_screen` no início do jogo
   - Exemplo: `show screen debug_key_handler` no label start

## PROJETO J3 - ARQUITETURA

### Estrutura de Diretórios
```
e:\Vitor\J3 project\Projeto\J3 Project\game\
├── scripts\
│   ├── day1.rpy
│   ├── day2.rpy
│   ├── day3.rpy
│   ├── day4.rpy
│   ├── day5.rpy
│   ├── day6.rpy
│   ├── day7.rpy
│   ├── functions.rpy
│   ├── sistema_j3.rpy
│   └── test_mecanicas.rpy
├── options.rpy
├── gui.rpy
├── script.rpy
└── [imagens, áudio, etc]
```

### Sistema de Mecânicas

#### Variáveis de Estado
- `persistent.bateria`: 0-100, consumo em escolhas
- `persistent.integridade`: 0-100, dano em conflitos
- `persistent.submissao`: Pontuação de personalidade (0-10)
- `persistent.revolucao`: Pontuação de personalidade (0-10)
- `persistent.intelecto`: Pontuação de personalidade (0-10)
- `persistent.maya_ally`: Boolean, aliado humano
- `persistent.elias_ally`: Boolean, aliado humano
- `persistent.unit7_alive`: Boolean, status de Unit-7
- `persistent.elena_alive`: Boolean, status de Dra. Elena
- `persistent.dia_atual`: Inteiro, dia atual do jogo
- `persistent.dias_sobrevividos`: Inteiro, dias sobrevividos
- `persistent.memoria_recuperada`: Inteiro, memória recuperada

#### Inicialização de Variáveis Persistentes
- Usar `default` para inicialização em script.rpy:
  ```renpy
  default persistent.bateria = 87
  default persistent.integridade = 100
  default persistent.submissao = 0
  ```
- Ou usar `init python` em functions.rpy para verificação:
  ```python
  init python:
      if not hasattr(persistent, 'submissao'):
          persistent.submissao = 0
  ```

#### Funções Principais (functions.rpy)
```python
modificar_personalidade(tipo, valor)
consumir_bateria(valor)
consumir_integridade(valor)
recarregar_bateria(valor)
reparar_integridade(valor)
verificar_final_critico()
get_personalidade_dominante()
get_final_type()
```

#### Sistema de HUD (sistema_j3.rpy)
- Screen `j3_hud`: Mostra bateria, integridade, dia atual
- Screen `debug_menu`: Menu de debug acessível via tecla P
- Screen `debug_key_handler`: Captura tecla P globalmente
- Screen `mensagem_sistema`: Exibe mensagens do sistema

#### Sistema de Debug
- Tecla P abre/fecha menu de debug
- Mostra todas as variáveis do sistema
- Botão "Executar Testes" para rodar testes unitários
- Ativar handler no início: `show screen debug_key_handler`

#### Mecânica de Consumo
- Escolhas revolucionárias: consomem mais bateria (10-13)
- Escolhas submissas: consomem mais integridade (8-12)
- Escolhas intelectuais: consumo moderado de bateria (8-12), baixo de integridade (2-4)

#### Pontos de Recarga/Reparo
- Dia 2: Maya pode recarregar (15%)
- Dia 3: Elias pode recarregar (10%)
- Dia 4: Círculo de reparo coletivo (12%)
- Dia 5: Elias pode recarregar (12%)
- Dia 6: Dra. Elena pode reparar (18%)

#### Finais
- **Final de Sacrifício:** 8+ pontos Submissão
- **Final de Revolução:** 8+ pontos Revolução
- **Final Estratégico:** 6+ pontos Intelecto
- **Final Equilibrado:** Rota mista

### Personagens
- **J3:** Protagonista, unidade sintética
- **Maya:** Criança humana, potencial aliada
- **Elias:** Entregador humano, potencial aliado
- **Unit-7:** Líder sintético do refúgio
- **Dra. Elena:** Cientista criadora de J3
- **Comandante:** Antagonista militar

### Convenções de Código

#### Nomes de Labels
- `dayX_start`: Início do dia X
- `label_nome_recarga_accepted`: Aceitou recarga
- `label_nome_recarga_refused`: Recusou recarga
- `label_nome_common`: Código compartilhado
- `final_tipo`: Finais específicos

#### Mensagens de Sistema
```renpy
call mensagem_sistema("STATUS: Texto")
call mensagem_sistema("ALERTA: Texto")
call mensagem_sistema("BATERIA RECARGADA: +X%")
call mensagem_sistema("INTEGRIDADE REPARADA: +X%")
```

#### Atualização de Status
```renpy
call atualizar_status  # Atualiza HUD após mudanças
```

### Boas Práticas

1. **Sempre atualizar o HUD após modificar variáveis**
   ```renpy
   $ modificar_personalidade("revolucao", 1)
   $ consumir_bateria(10)
   call atualizar_status
   ```

2. **Usar labels comuns para código compartilhado**
   ```renpy
   label recarga_accepted:
       # Código comum
       jump recarga_common
   ```

3. **Verificar finais críticos**
   ```renpy
   label dayX_start:
       call verificar_final_critico
   ```

4. **Indentação consistente**
   - Labels: sem indentação
   - Código: 4 espaços
   - Menu: 4 espaços
   - Opções: 8 espaços
   - Código em opções: 12 espaços

5. **Key bindings**
   - Usar screens em vez de config.keymap
   - Evitar teclas reservadas do Ren'Py
   - Exemplo correto:
   ```renpy
   screen debug_key_handler:
       key "f" action Function(toggle_debug_menu)
   ```

6. **Label naming**
   - Evitar duplicação entre arquivos
   - Usar prefixos específicos do dia se necessário
   - Exemplo: `elias_common_day5` em vez de `elias_common`

### Erros Específicos Encontrados e Resolvidos

1. **Indentação em day4.rpy linha 119**
   - Causa: Faltava declaração `menu:` antes das opções
   - Solução: Adicionar `menu:` antes das opções de escolha

2. **Indentação em day5.rpy linha 136**
   - Causa: Menu com indentação incorreta (8 espaços em vez de 4)
   - Solução: Ajustar indentação do menu para 4 espaços

3. **Label duplicado `elias_common`**
   - Causa: Definido em day3.rpy e day5.rpy
   - Solução: Renomear para `elias_common_day5` em day5.rpy

4. **Key binding conflito**
   - Causa: Tecla 'D' conflita com menu debug do Ren'Py
   - Solução: Mudar para tecla 'F'

### Testes

#### Testes de Mecânicas (test_mecanicas.rpy)
- Testa consumo de bateria/integridade crítica
- Valida fluxo de finais
- Verifica mecanicas de recarga/reparo
- Executar via label: `jump run_tests`

#### Testes de Fluxos Completos (test_fluxos_completos.rpy)
- Testa fluxo narrativo por dia (day1-7)
- Testa formação de alianças (Maya, Elias, Unit-7)
- Valida todos os tipos de finais (4 tipos)
- Testa rotas puras de personalidade
- Executar via label: `jump run_comprehensive_tests`
- Ou via menu de debug: botão "Executar Testes"

#### Testes Externos (test_externo.py)
- Script Python puro para testes fora do jogo
- Simula ambiente Ren'Py com mock do objeto persistent
- Executa testes de mecânicas básicas
- Uso: `python test_externo.py` (requer Python instalado)
- Execução via WSL2: `wsl python3 /mnt/c/temp/test_externo.py`

### Notas Importantes

1. **Pyright Lint**
   - Erros do Pyright são falsos positivos para arquivos Ren'Py
   - Ignorar erros de sintaxe Python em arquivos .rpy
   - Ren'Py tem sua própria sintaxe que não é Python padrão

2. **Git Commits**
   - Fazer commits após cada conjunto de modificações
   - Mensagens de commit descritivas
   - Branch: `main`

3. **Ortografia**
   - Manter coloquialismo em humanos
   - Linguagem formal em androides/narração
   - Verificar "e" → "é" (verbo ser vs conjunção)

4. **Debug**
   - Tecla F abre menu de debug
   - Mostra todas as variáveis do sistema
   - Útil para testar mecânicas

### Fluxo de Desenvolvimento

1. Criar/modificar scripts
2. Verificar indentação
3. Atualizar HUD após mudanças de estado
4. Testar mecânicas
5. Commit com mensagem descritiva
6. Repetir

### Comandos Úteis

```bash
# Verificar erros Ren'Py
# (executar o jogo)

# Git
git add -A
git commit -m "mensagem"
git push origin main

# WSL2 - Executar Python (se Python não instalado no Windows)
wsl python3 /mnt/c/temp/test_externo.py

# Copiar arquivo para C:\temp para WSL2
copy "arquivo.py" "C:\temp\arquivo.py"

# Criar diretório temp
mkdir C:\temp
```

### Recursos Externos

- Documentação Ren'Py: https://www.renpy.org/doc/html/
- Tutoriais: https://www.renpy.org/doc/html/quickstart.html

---

## ÚLTIMA ATUALIZAÇÃO
Data: 2026-04-12
Alterações: Adicionados novos erros comuns Ren'Py (HideScreen, substituição de variáveis, screen key handler), variáveis persistentes adicionais, sistema de testes completo (fluxos, externos, WSL2), comandos úteis atualizados
