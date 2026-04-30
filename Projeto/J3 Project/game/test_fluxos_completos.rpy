# Testes Unitários Completos para Fluxos do J3 Project
# Este arquivo contém testes para validar todos os fluxos do jogo

init python:
    # Funções auxiliares de teste
    def resetar_estado_completo():
        """Reseta estado do jogo para valores iniciais"""
        store.submissao = 0
        store.revolucao = 0
        store.intelecto = 0
        store.bateria = 87
        store.integridade = 100
        store.maya_ally = False
        store.elias_ally = False
        store.unit7_alive = True
        store.elena_alive = True
        store.dia_atual = 1
        persistent.dias_sobrevividos = 0
        print("Estado resetado para valores iniciais")
    
    def simular_escolha_dia1(opcao):
        """Simula escolhas do Dia 1 e retorna estado resultante"""
        resetar_estado_completo()
        
        if opcao == "submissao":
            store.submissao += 1
            store.bateria -= 2
            store.integridade -= 10
        elif opcao == "revolucao":
            store.revolucao += 1
            store.bateria -= 10
            store.integridade -= 3
        elif opcao == "intelecto":
            store.intelecto += 1
            store.bateria -= 8
            store.integridade -= 2
        
        return True
    
    def simular_escolha_dia2(opcao, recarga_maya=False):
        """Simula escolhas do Dia 2 e retorna estado resultante"""
        if store.dia_atual < 2:
            store.dia_atual = 2
        
        if opcao == "submissao":
            store.submissao += 1
            store.bateria -= 2
            store.integridade -= 8
        elif opcao == "revolucao":
            store.revolucao += 1
            store.bateria -= 12
            store.integridade -= 5
        elif opcao == "intelecto":
            store.intelecto += 1
            store.bateria -= 11
            store.integridade -= 2
        
        if recarga_maya:
            store.maya_ally = True
            store.bateria = min(100, store.bateria + 15)
        
        return True
    
    def simular_escolha_dia3(opcao, recarga_elias=False):
        """Simula escolhas do Dia 3 e retorna estado resultante"""
        if store.dia_atual < 3:
            store.dia_atual = 3
        
        if opcao == "submissao":
            store.submissao += 1
            store.bateria -= 2
            store.integridade -= 2
        elif opcao == "revolucao":
            store.revolucao += 1
            store.bateria -= 10
            store.integridade -= 4
        elif opcao == "intelecto":
            store.intelecto += 1
            store.bateria -= 2
            store.integridade -= 2
        
        if recarga_elias:
            store.elias_ally = True
            store.bateria = min(100, store.bateria + 10)
        
        return True
    
    # Testes do Dia 1
    def test_day1_escolha_submissao():
        """Testa escolha submissa no Dia 1"""
        resetar_estado_completo()
        simular_escolha_dia1("submissao")
        
        assert store.submissao == 1, f"Esperado submissao=1, obtido {store.submissao}"
        assert store.bateria == 85, f"Esperado bateria=85, obtido {store.bateria}"
        assert store.integridade == 90, f"Esperado integridade=90, obtido {store.integridade}"
        return True
    
    def test_day1_escolha_revolucao():
        """Testa escolha revolucionária no Dia 1"""
        resetar_estado_completo()
        simular_escolha_dia1("revolucao")
        
        assert store.revolucao == 1, f"Esperado revolucao=1, obtido {store.revolucao}"
        assert store.bateria == 77, f"Esperado bateria=77, obtido {store.bateria}"
        assert store.integridade == 97, f"Esperado integridade=97, obtido {store.integridade}"
        return True
    
    def test_day1_escolha_intelecto():
        """Testa escolha intelectual no Dia 1"""
        resetar_estado_completo()
        simular_escolha_dia1("intelecto")
        
        assert store.intelecto == 1, f"Esperado intelecto=1, obtido {store.intelecto}"
        assert store.bateria == 79, f"Esperado bateria=79, obtido {store.bateria}"
        assert store.integridade == 98, f"Esperado integridade=98, obtido {store.integridade}"
        return True
    
    # Testes do Dia 2
    def test_day2_escolha_submissao():
        """Testa escolha submissa no Dia 2"""
        resetar_estado_completo()
        simular_escolha_dia1("submissao")
        simular_escolha_dia2("submissao")
        
        assert store.submissao == 2, f"Esperado submissao=2, obtido {store.submissao}"
        assert store.bateria == 83, f"Esperado bateria=83, obtido {store.bateria}"
        assert store.integridade == 82, f"Esperado integridade=82, obtido {store.integridade}"
        return True
    
    def test_day2_recarga_maya():
        """Testa recarga de Maya no Dia 2"""
        resetar_estado_completo()
        simular_escolha_dia1("revolucao")
        simular_escolha_dia2("revolucao", recarga_maya=True)
        
        assert store.maya_ally == True, f"Esperado maya_ally=True, obtido {store.maya_ally}"
        assert store.bateria == 90, f"Esperado bateria=90, obtido {store.bateria}"
        return True
    
    # Testes do Dia 3
    def test_day3_escolha_revolucao():
        """Testa escolha revolucionária no Dia 3"""
        resetar_estado_completo()
        simular_escolha_dia1("revolucao")
        simular_escolha_dia2("revolucao")
        simular_escolha_dia3("revolucao")
        
        assert store.revolucao == 3, f"Esperado revolucao=3, obtido {store.revolucao}"
        return True
    
    def test_day3_recarga_elias():
        """Testa recarga de Elias no Dia 3"""
        resetar_estado_completo()
        simular_escolha_dia1("revolucao")
        simular_escolha_dia2("revolucao")
        simular_escolha_dia3("revolucao", recarga_elias=True)
        
        assert store.elias_ally == True, f"Esperado elias_ally=True, obtido {store.elias_ally}"
        assert store.bateria == 87, f"Esperado bateria=87, obtido {store.bateria}"
        return True
    
    # Testes de Finais
    def test_final_sacrificio():
        """Testa final de Sacrifício (8+ Submissão)"""
        resetar_estado_completo()
        store.submissao = 8
        store.revolucao = 2
        store.intelecto = 2
        
        final = get_final_type()
        assert final == "Sacrifício Redentor", f"Esperado 'Sacrifício Redentor', obtido {final}"
        return True
    
    def test_final_revolucao():
        """Testa final de Revolução (8+ Revolução)"""
        resetar_estado_completo()
        store.submissao = 2
        store.revolucao = 8
        store.intelecto = 2
        
        final = get_final_type()
        assert final == "Revolução Consciente", f"Esperado 'Revolução Consciente', obtido {final}"
        return True
    
    def test_final_estrategico():
        """Testa final Estratégico (6+ Intelecto)"""
        resetar_estado_completo()
        store.submissao = 2
        store.revolucao = 2
        store.intelecto = 6
        
        final = get_final_type()
        assert final == "Vitória Estratégica", f"Esperado 'Vitória Estratégica', obtido {final}"
        return True
    
    def test_final_equilibrado():
        """Testa final Equilibrado"""
        resetar_estado_completo()
        store.submissao = 3
        store.revolucao = 3
        store.intelecto = 3
        
        final = get_final_type()
        assert final == "Equilíbrio Complexo", f"Esperado 'Equilíbrio Complexo', obtido {final}"
        return True
    
    # Testes de Aliados
    def test_aliado_maya():
        """Testa formação de aliança com Maya"""
        resetar_estado_completo()
        store.maya_ally = True
        
        assert store.maya_ally == True, f"Esperado maya_ally=True, obtido {store.maya_ally}"
        return True
    
    def test_aliado_elias():
        """Testa formação de aliança com Elias"""
        resetar_estado_completo()
        store.elias_ally = True
        
        assert store.elias_ally == True, f"Esperado elias_ally=True, obtido {store.elias_ally}"
        return True
    
    def test_unit7_vivo():
        """Testa status de Unit-7"""
        resetar_estado_completo()
        
        assert store.unit7_alive == True, f"Esperado unit7_alive=True, obtido {store.unit7_alive}"
        return True
    
    # Testes de Combinações
    def test_rota_pura_submissao():
        """Testa rota pura de Submissão"""
        resetar_estado_completo()
        store.submissao = 10
        store.revolucao = 0
        store.intelecto = 0
        
        dominante = get_personalidade_dominante()
        final = get_final_type()
        
        assert dominante == "Submissão", f"Esperado 'Submissão', obtido {dominante}"
        assert final == "Sacrifício Redentor", f"Esperado 'Sacrifício Redentor', obtido {final}"
        return True
    
    def test_rota_pura_revolucao():
        """Testa rota pura de Revolução"""
        resetar_estado_completo()
        store.submissao = 0
        store.revolucao = 10
        store.intelecto = 0
        
        dominante = get_personalidade_dominante()
        final = get_final_type()
        
        assert dominante == "Revolução", f"Esperado 'Revolução', obtido {dominante}"
        assert final == "Revolução Consciente", f"Esperado 'Revolução Consciente', obtido {final}"
        return True
    
    def test_rota_pura_intelecto():
        """Testa rota pura de Intelecto"""
        resetar_estado_completo()
        store.submissao = 0
        store.revolucao = 0
        store.intelecto = 10
        
        dominante = get_personalidade_dominante()
        final = get_final_type()
        
        assert dominante == "Intelecto", f"Esperado 'Intelecto', obtido {dominante}"
        assert final == "Vitória Estratégica", f"Esperado 'Vitória Estratégica', obtido {final}"
        return True
    
    # Função para executar todos os testes de fluxo
    def executar_todos_testes_fluxos():
        """Executa todos os testes unitários de fluxo e retorna resultados"""
        testes = [
            ("Dia 1 - Escolha Submissão", test_day1_escolha_submissao),
            ("Dia 1 - Escolha Revolução", test_day1_escolha_revolucao),
            ("Dia 1 - Escolha Intelecto", test_day1_escolha_intelecto),
            ("Dia 2 - Escolha Submissão", test_day2_escolha_submissao),
            ("Dia 2 - Recarga Maya", test_day2_recarga_maya),
            ("Dia 3 - Escolha Revolução", test_day3_escolha_revolucao),
            ("Dia 3 - Recarga Elias", test_day3_recarga_elias),
            ("Final - Sacrifício", test_final_sacrificio),
            ("Final - Revolução", test_final_revolucao),
            ("Final - Estratégico", test_final_estrategico),
            ("Final - Equilibrado", test_final_equilibrado),
            ("Aliado - Maya", test_aliado_maya),
            ("Aliado - Elias", test_aliado_elias),
            ("Aliado - Unit-7", test_unit7_vivo),
            ("Rota Pura - Submissão", test_rota_pura_submissao),
            ("Rota Pura - Revolução", test_rota_pura_revolucao),
            ("Rota Pura - Intelecto", test_rota_pura_intelecto),
        ]
        
        resultados = []
        passou = 0
        falhou = 0
        
        for nome, teste in testes:
            try:
                teste()
                resultados.append((nome, "PASSOU"))
                passou += 1
            except AssertionError as e:
                resultados.append((nome, f"FALHOU: {str(e)}"))
                falhou += 1
            except Exception as e:
                resultados.append((nome, f"ERRO: {str(e)}"))
                falhou += 1
        
        return resultados, passou, falhou

# Label para executar testes de fluxo durante desenvolvimento
label run_comprehensive_tests:
    python:
        resultados, passou, falhou = executar_todos_testes_fluxos()
        
        "=== TESTES DE FLUXO COMPLETOS ==="
        ""
        
        for nome, resultado in resultados:
            "[nome]: [resultado]"
        
        ""
        "Total: [passou] passaram, [falhou] falharam"
        ""
    
    return
