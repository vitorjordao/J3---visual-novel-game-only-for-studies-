# Funções auxiliares para o sistema J3
# Este arquivo contém as funções necessárias para o funcionamento dos scripts.
# Estado de gameplay (submissao, revolucao, intelecto, maya_ally, elias_ally,
# unit7_alive, elena_alive) é variável de store — definida via `default` em
# script.rpy — para que o rollback do Ren'Py restaure os valores corretamente.

# Função para obter personalidade dominante
init python:
    def get_personalidade_dominante():
        """Retorna a personalidade dominante atual"""
        valores = {
            "Submissão": store.submissao,
            "Revolução": store.revolucao,
            "Intelecto": store.intelecto
        }

        dominante = max(valores, key=valores.get)
        return dominante

# Função para obter tipo de final
init python:
    def get_final_type():
        """Retorna o tipo de final baseado nas estatísticas"""
        if store.submissao >= 8:
            return "Sacrifício Redentor"
        elif store.revolucao >= 8:
            return "Revolução Consciente"
        elif store.intelecto >= 6:
            return "Vitória Estratégica"
        else:
            return "Equilíbrio Complexo"

# Helpers para marcar custo/ganho de recursos em escolhas do menu.
# Uso nos labels: "[custo(bat=2, integ=10)] Texto da escolha"
init python:
    def custo(bat=0, integ=0):
        parts = []
        if bat:
            parts.append("{color=#ff5566}-%d BAT{/color}" % bat)
        if integ:
            parts.append("{color=#ff5566}-%d INT{/color}" % integ)
        return ("[" + " / ".join(parts) + "]  ") if parts else ""

    def ganho(bat=0, integ=0):
        parts = []
        if bat:
            parts.append("{color=#55ff99}+%d BAT{/color}" % bat)
        if integ:
            parts.append("{color=#55ff99}+%d INT{/color}" % integ)
        return ("[" + " / ".join(parts) + "]  ") if parts else ""

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
        store.submissao = 0
        store.revolucao = 0
        store.intelecto = 0
        store.maya_ally = False
        store.elias_ally = False
        store.unit7_alive = True
        store.elena_alive = True
        print("Personalidade resetada para valores iniciais")

# Função para mostrar estatísticas atuais (para debug)
init python:
    def mostrar_estatisticas():
        """Mostra todas as estatísticas atuais"""
        print("=== ESTATÍSTICAS ATUAIS ===")
        print(f"Submissão: {store.submissao}")
        print(f"Revolução: {store.revolucao}")
        print(f"Intelecto: {store.intelecto}")
        print(f"Maya Aliada: {store.maya_ally}")
        print(f"Elias Aliado: {store.elias_ally}")
        print(f"Unit-7 Vivo: {store.unit7_alive}")
        print(f"Dra. Elena Viva: {store.elena_alive}")
        print(f"Personalidade Dominante: {get_personalidade_dominante()}")
        print(f"Tipo de Final: {get_final_type()}")
        print("========================")
