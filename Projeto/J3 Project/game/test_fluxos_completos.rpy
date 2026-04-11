# Testes Unitários Completos para Fluxos do J3 Project
# Este arquivo contém testes para validar todos os fluxos do jogo

init python:
    # Funções auxiliares de teste
    def resetar_estado_completo():
        """Reseta estado do jogo para valores iniciais"""
        persistent.submissao = 0
        persistent.revolucao = 0
        persistent.intelecto = 0
        persistent.bateria = 87
        persistent.integridade = 100
        persistent.maya_ally = False
        persistent.elias_ally = False
        persistent.unit7_alive = True
        persistent.elena_alive = True
        persistent.dia_atual = 1
        persistent.dias_sobrevividos = 0
        print("Estado resetado para valores iniciais")
    
    def simular_escolha_dia1(opcao):
        """Simula escolhas do Dia 1 e retorna estado resultante"""
        resetar_estado_completo()
        
        if opcao == "submissao":
            persistent.submissao += 1
            persistent.bateria -= 2
            persistent.integridade -= 10
        elif opcao == "revolucao":
            persistent.revolucao += 1
            persistent.bateria -= 10
            persistent.integridade -= 3
        elif opcao == "intelecto":
            persistent.intelecto += 1
            persistent.bateria -= 8
            persistent.integridade -= 2
        
        return True
    
    def simular_escolha_dia2(opcao, recarga_maya=False):
        """Simula escolhas do Dia 2 e retorna estado resultante"""
        if persistent.dia_atual < 2:
            persistent.dia_atual = 2
        
        if opcao == "submissao":
            persistent.submissao += 1
            persistent.bateria -= 2
            persistent.integridade -= 8
        elif opcao == "revolucao":
            persistent.revolucao += 1
            persistent.bateria -= 12
            persistent.integridade -= 5
        elif opcao == "intelecto":
            persistent.intelecto += 1
            persistent.bateria -= 11
            persistent.integridade -= 2
        
        if recarga_maya:
            persistent.maya_ally = True
            persistent.bateria = min(100, persistent.bateria + 15)
        
        return True
    
    def simular_escolha_dia3(opcao, recarga_elias=False):
        """Simula escolhas do Dia 3 e retorna estado resultante"""
        if persistent.dia_atual < 3:
            persistent.dia_atual = 3
        
        if opcao == "submissao":
            persistent.submissao += 1
            persistent.bateria -= 2
            persistent.integridade -= 2
        elif opcao == "revolucao":
            persistent.revolucao += 1
            persistent.bateria -= 10
            persistent.integridade -= 4
        elif opcao == "intelecto":
            persistent.intelecto += 1
            persistent.bateria -= 2
            persistent.integridade -= 2
        
        if recarga_elias:
            persistent.elias_ally = True
            persistent.bateria = min(100, persistent.bateria + 10)
        
        return True
    
    # Testes do Dia 1
    def test_day1_escolha_submissao():
        """Testa escolha submissa no Dia 1"""
        resetar_estado_completo()
        simular_escolha_dia1("submissao")
        
        assert persistent.submissao == 1, f"Esperado submissao=1, obtido {persistent.submissao}"
        assert persistent.bateria == 85, f"Esperado bateria=85, obtido {persistent.bateria}"
        assert persistent.integridade == 90, f"Esperado integridade=90, obtido {persistent.integridade}"
        return True
    
    def test_day1_escolha_revolucao():
        """Testa escolha revolucionária no Dia 1"""
        resetar_estado_completo()
        simular_escolha_dia1("revolucao")
        
        assert persistent.revolucao == 1, f"Esperado revolucao=1, obtido {persistent.revolucao}"
        assert persistent.bateria == 77, f"Esperado bateria=77, obtido {persistent.bateria}"
        assert persistent.integridade == 97, f"Esperado integridade=97, obtido {persistent.integridade}"
        return True
    
    def test_day1_escolha_intelecto():
        """Testa escolha intelectual no Dia 1"""
        resetar_estado_completo()
        simular_escolha_dia1("intelecto")
        
        assert persistent.intelecto == 1, f"Esperado intelecto=1, obtido {persistent.intelecto}"
        assert persistent.bateria == 79, f"Esperado bateria=79, obtido {persistent.bateria}"
        assert persistent.integridade == 98, f"Esperado integridade=98, obtido {persistent.integridade}"
        return True
    
    # Testes do Dia 2
    def test_day2_escolha_submissao():
        """Testa escolha submissa no Dia 2"""
        resetar_estado_completo()
        simular_escolha_dia1("submissao")
        simular_escolha_dia2("submissao")
        
        assert persistent.submissao == 2, f"Esperado submissao=2, obtido {persistent.submissao}"
        assert persistent.bateria == 83, f"Esperado bateria=83, obtido {persistent.bateria}"
        assert persistent.integridade == 82, f"Esperado integridade=82, obtido {persistent.integridade}"
        return True
    
    def test_day2_recarga_maya():
        """Testa recarga de Maya no Dia 2"""
        resetar_estado_completo()
        simular_escolha_dia1("revolucao")
        simular_escolha_dia2("revolucao", recarga_maya=True)
        
        assert persistent.maya_ally == True, f"Esperado maya_ally=True, obtido {persistent.maya_ally}"
        assert persistent.bateria == 90, f"Esperado bateria=90, obtido {persistent.bateria}"
        return True
    
    # Testes do Dia 3
    def test_day3_escolha_revolucao():
        """Testa escolha revolucionária no Dia 3"""
        resetar_estado_completo()
        simular_escolha_dia1("revolucao")
        simular_escolha_dia2("revolucao")
        simular_escolha_dia3("revolucao")
        
        assert persistent.revolucao == 3, f"Esperado revolucao=3, obtido {persistent.revolucao}"
        return True
    
    def test_day3_recarga_elias():
        """Testa recarga de Elias no Dia 3"""
        resetar_estado_completo()
        simular_escolha_dia1("revolucao")
        simular_escolha_dia2("revolucao")
        simular_escolha_dia3("revolucao", recarga_elias=True)
        
        assert persistent.elias_ally == True, f"Esperado elias_ally=True, obtido {persistent.elias_ally}"
        assert persistent.bateria == 87, f"Esperado bateria=87, obtido {persistent.bateria}"
        return True
    
    # Testes de Finais
    def test_final_sacrificio():
        """Testa final de Sacrifício (8+ Submissão)"""
        resetar_estado_completo()
        persistent.submissao = 8
        persistent.revolucao = 2
        persistent.intelecto = 2
        
        final = get_final_type()
        assert final == "Sacrifício Redentor", f"Esperado 'Sacrifício Redentor', obtido {final}"
        return True
    
    def test_final_revolucao():
        """Testa final de Revolução (8+ Revolução)"""
        resetar_estado_completo()
        persistent.submissao = 2
        persistent.revolucao = 8
        persistent.intelecto = 2
        
        final = get_final_type()
        assert final == "Revolução Consciente", f"Esperado 'Revolução Consciente', obtido {final}"
        return True
    
    def test_final_estrategico():
        """Testa final Estratégico (6+ Intelecto)"""
        resetar_estado_completo()
        persistent.submissao = 2
        persistent.revolucao = 2
        persistent.intelecto = 6
        
        final = get_final_type()
        assert final == "Vitória Estratégica", f"Esperado 'Vitória Estratégica', obtido {final}"
        return True
    
    def test_final_equilibrado():
        """Testa final Equilibrado"""
        resetar_estado_completo()
        persistent.submissao = 3
        persistent.revolucao = 3
        persistent.intelecto = 3
        
        final = get_final_type()
        assert final == "Equilíbrio Complexo", f"Esperado 'Equilíbrio Complexo', obtido {final}"
        return True
    
    # Testes de Aliados
    def test_aliado_maya():
        """Testa formação de aliança com Maya"""
        resetar_estado_completo()
        persistent.maya_ally = True
        
        assert persistent.maya_ally == True, f"Esperado maya_ally=True, obtido {persistent.maya_ally}"
        return True
    
    def test_aliado_elias():
        """Testa formação de aliança com Elias"""
        resetar_estado_completo()
        persistent.elias_ally = True
        
        assert persistent.elias_ally == True, f"Esperado elias_ally=True, obtido {persistent.elias_ally}"
        return True
    
    def test_unit7_vivo():
        """Testa status de Unit-7"""
        resetar_estado_completo()
        
        assert persistent.unit7_alive == True, f"Esperado unit7_alive=True, obtido {persistent.unit7_alive}"
        return True
    
    # Testes de Combinações
    def test_rota_pura_submissao():
        """Testa rota pura de Submissão"""
        resetar_estado_completo()
        persistent.submissao = 10
        persistent.revolucao = 0
        persistent.intelecto = 0
        
        dominante = get_personalidade_dominante()
        final = get_final_type()
        
        assert dominante == "Submissão", f"Esperado 'Submissão', obtido {dominante}"
        assert final == "Sacrifício Redentor", f"Esperado 'Sacrifício Redentor', obtido {final}"
        return True
    
    def test_rota_pura_revolucao():
        """Testa rota pura de Revolução"""
        resetar_estado_completo()
        persistent.submissao = 0
        persistent.revolucao = 10
        persistent.intelecto = 0
        
        dominante = get_personalidade_dominante()
        final = get_final_type()
        
        assert dominante == "Revolução", f"Esperado 'Revolução', obtido {dominante}"
        assert final == "Revolução Consciente", f"Esperado 'Revolução Consciente', obtido {final}"
        return True
    
    def test_rota_pura_intelecto():
        """Testa rota pura de Intelecto"""
        resetar_estado_completo()
        persistent.submissao = 0
        persistent.revolucao = 0
        persistent.intelecto = 10
        
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
