# Funções auxiliares para o sistema J3
# Este arquivo contém as funções necessárias para o funcionamento dos scripts

# Inicialização das variáveis de personalidade
init python:
    # Variáveis persistentes para rastrear personalidade
    if not hasattr(persistent, 'submissao'):
        persistent.submissao = 0
    if not hasattr(persistent, 'revolucao'):
        persistent.revolucao = 0
    if not hasattr(persistent, 'intelecto'):
        persistent.intelecto = 0
    if not hasattr(persistent, 'maya_ally'):
        persistent.maya_ally = False
    if not hasattr(persistent, 'elias_ally'):
        persistent.elias_ally = False
    if not hasattr(persistent, 'unit7_alive'):
        persistent.unit7_alive = True
    if not hasattr(persistent, 'elena_alive'):
        persistent.elena_alive = True

# Função para modificar personalidade
init python:
    def modificar_personalidade(tipo, quantidade):
        """Modifica os atributos de personalidade de J3"""
        global persistent
        
        if tipo == "submissao":
            persistent.submissao += quantidade
        elif tipo == "revolucao":
            persistent.revolucao += quantidade
        elif tipo == "intelecto":
            persistent.intelecto += quantidade
        
        # Debug
        print(f"Personalidade atualizada: {tipo} +{quantidade}")
        print(f"Status: Sub={persistent.submissao}, Rev={persistent.revolucao}, Int={persistent.intelecto}")

# Função para obter personalidade dominante
init python:
    def get_personalidade_dominante():
        """Retorna a personalidade dominante atual"""
        valores = {
            "Submissão": persistent.submissao,
            "Revolução": persistent.revolucao,
            "Intelecto": persistent.intelecto
        }
        
        dominante = max(valores, key=valores.get)
        return dominante

# Função para obter tipo de final
init python:
    def get_final_type():
        """Retorna o tipo de final baseado nas estatísticas"""
        if persistent.submissao >= 8:
            return "Sacrifício Redentor"
        elif persistent.revolucao >= 8:
            return "Revolução Consciente"
        elif persistent.intelecto >= 6:
            return "Vitória Estratégica"
        else:
            return "Equilíbrio Complexo"

# Função de sistema para mensagens
init python:
    def mensagem_sistema(mensagem):
        """Exibe uma mensagem de sistema no HUD"""
        # Esta função pode ser expandida para mostrar mensagens na tela
        print(f"SISTEMA: {mensagem}")
        # Aqui você pode adicionar código para mostrar na tela se necessário

# Função para resetar personalidade (para testes)
init python:
    def resetar_personalidade():
        """Reseta todas as estatísticas de personalidade"""
        global persistent
        persistent.submissao = 0
        persistent.revolucao = 0
        persistent.intelecto = 0
        persistent.maya_ally = False
        persistent.elias_ally = False
        persistent.unit7_alive = True
        persistent.elena_alive = True
        print("Personalidade resetada para valores iniciais")

# Função para mostrar estatísticas atuais (para debug)
init python:
    def mostrar_estatisticas():
        """Mostra todas as estatísticas atuais"""
        print("=== ESTATÍSTICAS ATUAIS ===")
        print(f"Submissão: {persistent.submissao}")
        print(f"Revolução: {persistent.revolucao}")
        print(f"Intelecto: {persistent.intelecto}")
        print(f"Maya Aliada: {persistent.maya_ally}")
        print(f"Elias Aliado: {persistent.elias_ally}")
        print(f"Unit-7 Vivo: {persistent.unit7_alive}")
        print(f"Dra. Elena Viva: {persistent.elena_alive}")
        print(f"Personalidade Dominante: {get_personalidade_dominante()}")
        print(f"Tipo de Final: {get_final_type()}")
        print("========================")
