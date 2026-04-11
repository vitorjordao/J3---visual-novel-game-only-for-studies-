# J3 - A Consciência Artificial

## Sobre o Projeto

J3 é um visual novel cyberpunk desenvolvido em Ren'Py que explora temas de identidade, preconceito e livre-arbítrio. O jogador controla J3-001, um robô humanoide que desperta sem memória e cuja personalidade é moldada pelas escolhas do jogador.

## Estrutura do Projeto

### 📁 Pastas Principais

```
J3 Project/
├── game/
│   ├── script.rpy              # Script principal
│   ├── options.rpy             # Configurações do jogo
│   ├── gui.rpy                 # Interface gráfica
│   ├── sistema_j3.rpy          # Sistema personalizado do J3
│   ├── screens.rpy             # Telas personalizadas
│   ├── 
│   ├── characters/             # Sprites dos personagens
│   │   ├── j3/                # J3-001 protagonista
│   │   ├── maya/              # Maya - aliada humana
│   │   ├── elias/             # Elias - entregador
│   │   ├── unit7/             # Unit-7 - sintético militar
│   │   └── elena/             # Dra. Elena - cientista
│   │
│   ├── backgrounds/            # Cenários do jogo
│   │   ├── day1/              # Dia 1 - A Avenida
│   │   ├── day2/              # Dia 2 - O Fliperama
│   │   └── ...                # Dias 3-7
│   │
│   ├── scripts/                # Scripts organizados
│   │   ├── day1.rpy           # Dia 1 completo
│   │   └── ...                # Dias 2-7
│   │
│   ├── audio/                  # Arquivos de áudio
│   │   ├── music/             # Músicas temáticas
│   │   ├── sfx/               # Efeitos sonoros
│   │   └── voice/             # Dublagens (futuro)
│   │
│   ├── fonts/                  # Fontes personalizadas
│   ├── gui/                    # Elementos de interface
│   └── images/                 # Imagens gerais
│
└── Documentação/               # Documentos do projeto
    ├── GDD - J3 Projeto.md
    ├── Cronograma/
    └── Resumo MINC - J3 Projeto.md
```

## 🎮 Sistema de Jogo

### Mecânicas Principais

- **Sistema de Personalidade:** Três atributos principais:
  - **Submissão (0-10):** Rota de obediência e sacrifício
  - **Revolução (0-10):** Rota de rebelião e liberdade
  - **Intelecto (0-10):** Rota estratégica e manipulação

- **HUD do Sistema J3:** Interface em tempo real mostrando:
  - Status da bateria e integridade
  - Níveis de personalidade
  - Memória recuperada
  - Dia atual

- **Escolhas Significativas:** Cada decisão afeta:
  - Atributos de personalidade
  - Eventos futuros
  - Diálogos disponíveis
  - Final do jogo

### Estrutura Narrativa

- **7 Dias de Gameplay:** Progressão em atos
- **4 Finais Diferentes:** Baseados na personalidade dominante
- **Branching Dinâmico:** Escolhas afetam eventos subsequentes
- **Sistema de Memória:** Recuperação gradual da identidade

## 🎨 Tema Visual

### Estilo Cyberpunk

- **Cores Principais:**
  - Ciano neon (#00ffcc) - Cor principal do J3
  - Azul escuro (#1a1a2e) - Fundos e interfaces
  - Rosa suave (#ff6b9d) - Personagens humanos
  - Laranja (#ff9f1c) - Autoridade militar

- **Interface:** Minimalista tecnológica com HUD integrado
- **Arte:** 2D digital com atmosfera urbana sombria
- **Tipografia:** Fontes cyberpunk personalizadas

## 🔧 Configuração Técnica

### Requisitos

- **Engine:** Ren'Py 8.x
- **Resolução:** 1920x1080 (escalável)
- **Plataformas:** Windows, macOS, Linux
- **Idioma:** Português Brasileiro

### Desenvolvimento

- **Ferramentas:** Krita/GIMP (arte), Audacity (áudio), VS Code (código)
- **Versionamento:** Git/GitHub
- **Distribuição:** Itch.io (primário)

## 📋 Status Atual

### ✅ Concluído

- [x] Estrutura de pastas organizada
- [x] Sistema de personalidade implementado
- [x] HUD do sistema J3 funcional
- [x] Interface cyberpunk configurada
- [x] Script do Dia 1 implementado
- [x] Sistema de escolhas funcionando

### 🚧 Em Progresso

- [ ] Assets visuais (sprites, backgrounds)
- [ ] Música e efeitos sonoros
- [ ] Scripts dos Dias 2-7
- [ ] Telas de menu personalizadas
- [ ] Sistema de save/load

### 📅 Planejado

- [ ] Testes e balanceamento
- [ ] Polimento visual
- [ ] Build final
- [ ] Lançamento (Junho 2026)

## 🎯 Como Executar

1. **Instale o Ren'Py SDK** (versão 8.x ou superior)
2. **Abra o projeto** no Ren'Py
3. **Execute** o projeto (F5 ou "Launch Project")
4. **Teste** o sistema de escolhas e HUD

## 📝 Notas de Desenvolvimento

### Próximos Passos Imediatos

1. **Criar sprites básicos** dos personagens
2. **Desenvolver backgrounds** para o Dia 1
3. **Implementar áudio** básico
4. **Testar sistema** de save/load
5. **Desenvolver Dia 2** completo

### Dicas para Desenvolvimento

- Use o sistema `escolha_j3()` para escolhas que afetam personalidade
- O HUD pode ser ativado/desativado com `show/hide screen j3_hud`
- Use `call mensagem_sistema()` para mensagens do sistema J3
- O sistema de personalidade está em `sistema_j3.rpy`

## 📞 Contato

**Desenvolvedor:** Vitor Jordão 
**Projeto:** J3 - A Consciência Artificial  
**Motor:** Ren'Py  

---

*"O que nos torna humanos não é nossa origem, mas nossas escolhas."*
