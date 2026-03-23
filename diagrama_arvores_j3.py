#!/usr/bin/env python3
"""
Gerador de Diagrama de Ramificações do J3 Project
Cria um fluxograma visual mostrando todas as escolhas e caminhos do jogo
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# Configuração do estilo cyberpunk
plt.style.use('dark_background')
fig, ax = plt.subplots(1, 1, figsize=(24, 32))
ax.set_xlim(0, 10)
ax.set_ylim(0, 40)
ax.axis('off')

# Cores cyberpunk
COR_SUBMISSAO = '#666666'  # Cinza
COR_REVOLUCAO = '#ff3366'  # Rosa rebelde
COR_INTELECTO = '#00ccff'  # Azul analítico
COR_MISTA = '#00ffcc'      # Ciano neon
COR_FUNDO = '#0a0a0a'      # Preto profundo
COR_TEXTO = '#ffffff'      # Branco

# Funções auxiliares
def criar_caixa(x, y, texto, cor=COR_TEXTO, bg_color='#1a1a2e', largura=1.8, altura=0.8):
    """Cria uma caixa de texto no diagrama"""
    caixa = FancyBboxPatch((x - largura/2, y - altura/2), largura, altura,
                           boxstyle="round,pad=0.1", 
                           facecolor=bg_color, 
                           edgecolor=cor, 
                           linewidth=2,
                           alpha=0.9)
    ax.add_patch(caixa)
    ax.text(x, y, texto, ha='center', va='center', color=cor, fontsize=10, weight='bold')
    return caixa

def criar_escolha(x, y, texto, cor):
    """Cria um nó de escolha"""
    circle = plt.Circle((x, y), 0.3, color=cor, alpha=0.8)
    ax.add_patch(circle)
    ax.text(x, y, texto, ha='center', va='center', color='white', fontsize=8, weight='bold')

def criar_conexao(x1, y1, x2, y2, cor=COR_TEXTO, estilo='-'):
    """Cria uma linha de conexão"""
    ax.plot([x1, x2], [y1, y2], color=cor, linewidth=2, linestyle=estilo, alpha=0.7)

def criar_seta(x1, y1, x2, y2, cor=COR_TEXTO, texto=''):
    """Cria uma seta com texto"""
    ax.annotate(texto, xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=cor, lw=2, alpha=0.7),
                color=cor, fontsize=8, ha='center')

# Título
ax.text(5, 39, 'J3 PROJECT - DIAGRAMA DE RAMIFICAÇÕES', 
        ha='center', va='center', color=COR_MISTA, fontsize=20, weight='bold')

# Subtítulo
ax.text(5, 38, 'Árvore de Escolhas e Consequências', 
        ha='center', va='center', color=COR_TEXTO, fontsize=14, alpha=0.8)

# Estrutura do jogo
criar_caixa(5, 36.5, 'INÍCIO', bg_color='#2a2a3e', cor=COR_MISTA)

# Dia 1 - A Avenida
criar_caixa(5, 35, 'DIA 1: A AVENIDA', bg_color='#1a1a2e', cor=COR_TEXTO)
criar_caixa(2, 33.5, 'Manifestante', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(5, 33.5, 'Criança Curiosa', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(8, 33.5, 'Policial', bg_color='#2a2a3e', cor=COR_TEXTO)

# Escolhas Dia 1
criar_escolha(1, 32, 'S', COR_SUBMISSAO)
criar_escolha(2, 32, 'R', COR_REVOLUCAO)
criar_escolha(3, 32, 'I', COR_INTELECTO)

criar_escolha(4, 32, 'S', COR_SUBMISSAO)
criar_escolha(5, 32, 'R', COR_REVOLUCAO)
criar_escolha(6, 32, 'I', COR_INTELECTO)

criar_escolha(7, 32, 'S', COR_SUBMISSAO)
criar_escolha(8, 32, 'R', COR_REVOLUCAO)
criar_escolha(9, 32, 'I', COR_INTELECTO)

# Conexões Dia 1
criar_conexao(5, 36, 5, 35)
criar_conexao(5, 35, 2, 33.5)
criar_conexao(5, 35, 5, 33.5)
criar_conexao(5, 35, 8, 33.5)

criar_conexao(2, 33.5, 1, 32)
criar_conexao(2, 33.5, 2, 32)
criar_conexao(2, 33.5, 3, 32)

criar_conexao(5, 33.5, 4, 32)
criar_conexao(5, 33.5, 5, 32)
criar_conexao(5, 33.5, 6, 32)

criar_conexao(8, 33.5, 7, 32)
criar_conexao(8, 33.5, 8, 32)
criar_conexao(8, 33.5, 9, 32)

# Dia 2 - O Fliperama
criar_caixa(5, 30, 'DIA 2: O FLIPERAMA', bg_color='#1a1a2e', cor=COR_TEXTO)
criar_caixa(3, 28.5, 'Intimidação', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(7, 28.5, 'Dono', bg_color='#2a2a3e', cor=COR_TEXTO)

# Escolhas Dia 2
criar_escolha(2, 27, 'S', COR_SUBMISSAO)
criar_escolha(3, 27, 'R', COR_REVOLUCAO)
criar_escolha(4, 27, 'I', COR_INTELECTO)

criar_escolha(6, 27, 'S', COR_SUBMISSAO)
criar_escolha(7, 27, 'R', COR_REVOLUCAO)
criar_escolha(8, 27, 'I', COR_INTELECTO)

# Conexões Dia 2
criar_seta(5, 31.5, 5, 30, COR_TEXTO, 'Consequências Dia 1')
criar_conexao(5, 30, 3, 28.5)
criar_conexao(5, 30, 7, 28.5)

criar_conexao(3, 28.5, 2, 27)
criar_conexao(3, 28.5, 3, 27)
criar_conexao(3, 28.5, 4, 27)

criar_conexao(7, 28.5, 6, 27)
criar_conexao(7, 28.5, 7, 27)
criar_conexao(7, 28.5, 8, 27)

# Dia 3 - O Beco
criar_caixa(5, 25, 'DIA 3: O BECO', bg_color='#1a1a2e', cor=COR_TEXTO)
criar_caixa(3, 23.5, 'Racismo', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(7, 23.5, 'Suborno', bg_color='#2a2a3e', cor=COR_TEXTO)

# Escolhas Dia 3
criar_escolha(2, 22, 'S', COR_SUBMISSAO)
criar_escolha(3, 22, 'R', COR_REVOLUCAO)
criar_escolha(4, 22, 'I', COR_INTELECTO)

criar_escolha(6, 22, 'S', COR_SUBMISSAO)
criar_escolha(7, 22, 'R', COR_REVOLUCAO)
criar_escolha(8, 22, 'I', COR_INTELECTO)

# Conexões Dia 3
criar_seta(5, 26.5, 5, 25, COR_TEXTO, 'Alianças Formadas')
criar_conexao(5, 25, 3, 23.5)
criar_conexao(5, 25, 7, 23.5)

criar_conexao(3, 23.5, 2, 22)
criar_conexao(3, 23.5, 3, 22)
criar_conexao(3, 23.5, 4, 22)

criar_conexao(7, 23.5, 6, 22)
criar_conexao(7, 23.5, 7, 22)
criar_conexao(7, 23.5, 8, 22)

# Dia 4 - O Refúgio
criar_caixa(5, 20, 'DIA 4: O REFÚGIO', bg_color='#1a1a2e', cor=COR_TEXTO)
criar_caixa(2, 18.5, 'Líder Unit-7', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(5, 18.5, 'Recursos', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(8, 18.5, 'Notícias', bg_color='#2a2a3e', cor=COR_TEXTO)

# Escolhas Dia 4
criar_escolha(1, 17, 'S', COR_SUBMISSAO)
criar_escolha(2, 17, 'R', COR_REVOLUCAO)
criar_escolha(3, 17, 'I', COR_INTELECTO)

criar_escolha(4, 17, 'S', COR_SUBMISSAO)
criar_escolha(5, 17, 'R', COR_REVOLUCAO)
criar_escolha(6, 17, 'I', COR_INTELECTO)

criar_escolha(7, 17, 'S', COR_SUBMISSAO)
criar_escolha(8, 17, 'R', COR_REVOLUCAO)
criar_escolha(9, 17, 'I', COR_INTELECTO)

# Conexões Dia 4
criar_seta(5, 21.5, 5, 20, COR_TEXTO, 'Consequências Acumuladas')
criar_conexao(5, 20, 2, 18.5)
criar_conexao(5, 20, 5, 18.5)
criar_conexao(5, 20, 8, 18.5)

criar_conexao(2, 18.5, 1, 17)
criar_conexao(2, 18.5, 2, 17)
criar_conexao(2, 18.5, 3, 17)

criar_conexao(5, 18.5, 4, 17)
criar_conexao(5, 18.5, 5, 17)
criar_conexao(5, 18.5, 6, 17)

criar_conexao(8, 18.5, 7, 17)
criar_conexao(8, 18.5, 8, 17)
criar_conexao(8, 18.5, 9, 17)

# Dia 5 - O Cerco
criar_caixa(5, 15, 'DIA 5: O CERCO', bg_color='#1a1a2e', cor=COR_TEXTO)
criar_caixa(2, 13.5, 'Invasão', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(5, 13.5, 'Sacrifício', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(8, 13.5, 'Fuga', bg_color='#2a2a3e', cor=COR_TEXTO)

# Escolhas Dia 5
criar_escolha(1, 12, 'S', COR_SUBMISSAO)
criar_escolha(2, 12, 'R', COR_REVOLUCAO)
criar_escolha(3, 12, 'I', COR_INTELECTO)

criar_escolha(4, 12, 'S', COR_SUBMISSAO)
criar_escolha(5, 12, 'R', COR_REVOLUCAO)
criar_escolha(6, 12, 'I', COR_INTELECTO)

criar_escolha(7, 12, 'S', COR_SUBMISSAO)
criar_escolha(8, 12, 'R', COR_REVOLUCAO)
criar_escolha(9, 12, 'I', COR_INTELECTO)

# Conexões Dia 5
criar_seta(5, 16.5, 5, 15, COR_TEXTO, 'Operação Limpeza Ética')
criar_conexao(5, 15, 2, 13.5)
criar_conexao(5, 15, 5, 13.5)
criar_conexao(5, 15, 8, 13.5)

criar_conexao(2, 13.5, 1, 12)
criar_conexao(2, 13.5, 2, 12)
criar_conexao(2, 13.5, 3, 12)

criar_conexao(5, 13.5, 4, 12)
criar_conexao(5, 13.5, 5, 12)
criar_conexao(5, 13.5, 6, 12)

criar_conexao(8, 13.5, 7, 12)
criar_conexao(8, 13.5, 8, 12)
criar_conexao(8, 13.5, 9, 12)

# Dia 6 - A Revelação
criar_caixa(5, 10, 'DIA 6: A REVELAÇÃO', bg_color='#1a1a2e', cor=COR_TEXTO)
criar_caixa(2, 8.5, 'Memória', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(5, 8.5, 'Dra. Elena', bg_color='#2a2a3e', cor=COR_TEXTO)
criar_caixa(8, 8.5, 'Traição', bg_color='#2a2a3e', cor=COR_TEXTO)

# Escolhas Dia 6
criar_escolha(1, 7, 'S', COR_SUBMISSAO)
criar_escolha(2, 7, 'R', COR_REVOLUCAO)
criar_escolha(3, 7, 'I', COR_INTELECTO)

criar_escolha(4, 7, 'S', COR_SUBMISSAO)
criar_escolha(5, 7, 'R', COR_REVOLUCAO)
criar_escolha(6, 7, 'I', COR_INTELECTO)

criar_escolha(7, 7, 'S', COR_SUBMISSAO)
criar_escolha(8, 7, 'R', COR_REVOLUCAO)
criar_escolha(9, 7, 'I', COR_INTELECTO)

# Conexões Dia 6
criar_seta(5, 11.5, 5, 10, COR_TEXTO, 'Verdade Sobre J3')
criar_conexao(5, 10, 2, 8.5)
criar_conexao(5, 10, 5, 8.5)
criar_conexao(5, 10, 8, 8.5)

criar_conexao(2, 8.5, 1, 7)
criar_conexao(2, 8.5, 2, 7)
criar_conexao(2, 8.5, 3, 7)

criar_conexao(5, 8.5, 4, 7)
criar_conexao(5, 8.5, 5, 7)
criar_conexao(5, 8.5, 6, 7)

criar_conexao(8, 8.5, 7, 7)
criar_conexao(8, 8.5, 8, 7)
criar_conexao(8, 8.5, 9, 7)

# Dia 7 - Finais
criar_caixa(5, 5, 'DIA 7: O FINAL', bg_color='#1a1a2e', cor=COR_TEXTO)

# Quais finais possíveis
criar_caixa(1.5, 3.5, 'SACRIFÍCIO\nREVENTOR', bg_color='#2a1a1a', cor=COR_SUBMISSAO, largura=2.5, altura=1.2)
criar_caixa(3.5, 3.5, 'REVOLUÇÃO\nCONSCIENTE', bg_color='#2a1a1a', cor=COR_REVOLUCAO, largura=2.5, altura=1.2)
criar_caixa(6.5, 3.5, 'VITÓRIA\nESTRATÉGICA', bg_color='#2a1a1a', cor=COR_INTELECTO, largura=2.5, altura=1.2)
criar_caixa(8.5, 3.5, 'EQUILÍBRIO\nCOMPLEXO', bg_color='#2a1a1a', cor=COR_MISTA, largura=2.5, altura=1.2)

# Conexões para os finais
criar_seta(5, 6, 1.5, 4.5, COR_SUBMISSAO, '8+ pts Submissão')
criar_seta(5, 6, 3.5, 4.5, COR_REVOLUCAO, '8+ pts Revolução')
criar_seta(5, 6, 6.5, 4.5, COR_INTELECTO, '6+ pts Intelecto')
criar_seta(5, 6, 8.5, 4.5, COR_MISTA, 'Rotas Mistas')

# Legendas
legend_x = 0.5
legend_y = 2

ax.text(legend_x, legend_y, 'LEGENDA:', ha='left', va='center', color=COR_MISTA, fontsize=12, weight='bold')
ax.text(legend_x, legend_y - 0.5, 'S = Submissão', ha='left', va='center', color=COR_SUBMISSAO, fontsize=10)
ax.text(legend_x, legend_y - 1, 'R = Revolução', ha='left', va='center', color=COR_REVOLUCAO, fontsize=10)
ax.text(legend_x, legend_y - 1.5, 'I = Intelecto/Sombra', ha='left', va='center', color=COR_INTELECTO, fontsize=10)

# Sistema de pontuação
ax.text(legend_x, legend_y - 2.5, 'SISTEMA DE PONTOS:', ha='left', va='center', color=COR_MISTA, fontsize=12, weight='bold')
ax.text(legend_x, legend_y - 3, '• Cada escolha afeta os atributos', ha='left', va='center', color=COR_TEXTO, fontsize=9)
ax.text(legend_x, legend_y - 3.5, '• Acúmulos determinam o final', ha='left', va='center', color=COR_TEXTO, fontsize=9)
ax.text(legend_x, legend_y - 4, '• Personagens influenciam o resultado', ha='left', va='center', color=COR_TEXTO, fontsize=9)

# Personagens importantes
ax.text(legend_x + 8, legend_y, 'PERSONAGENS-CHAVE:', ha='left', va='center', color=COR_MISTA, fontsize=12, weight='bold')
ax.text(legend_x + 8, legend_y - 0.5, '• Maya - Aliada humana', ha='left', va='center', color=COR_TEXTO, fontsize=9)
ax.text(legend_x + 8, legend_y - 1, '• Elias - Resistência', ha='left', va='center', color=COR_TEXTO, fontsize=9)
ax.text(legend_x + 8, legend_y - 1.5, '• Unit-7 - Líder militar', ha='left', va='center', color=COR_TEXTO, fontsize=9)
ax.text(legend_x + 8, legend_y - 2, '• Dra. Elena - Criadora', ha='left', va='center', color=COR_TEXTO, fontsize=9)

# Estatísticas do jogo
stats_text = """
ESTATÍSTICAS DO JOGO:
• 7 dias de gameplay
• 21+ escolhas principais
• 4 finais possíveis
• 3 atributos principais
• Múltiplas ramificações
"""

ax.text(9, 1, stats_text, ha='right', va='center', color=COR_TEXTO, fontsize=9, 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='#1a1a2e', alpha=0.8))

# Assinatura
ax.text(5, 0.5, 'J3 Project - Visual Novel Cyberpunk sobre Identidade e Livre-Arbítrio', 
        ha='center', va='center', color=COR_MISTA, fontsize=10, alpha=0.8, style='italic')

# Salvar o diagrama
plt.tight_layout()
plt.savefig('c:\\Users\\v\\Documents\\Projects\\J3 project\\diagrama_j3_completo.png', 
            dpi=300, bbox_inches='tight', facecolor=COR_FUNDO, edgecolor='none')
plt.close()

print("Diagrama de ramificações do J3 Project criado com sucesso!")
print("Arquivo salvo como: diagrama_j3_completo.png")
