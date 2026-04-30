# Testes Unitários para Mecânicas de Sobrevivência
# Este arquivo contém testes para validar o fluxo de bateria/integridade crítica

init python:
    # Funções de teste
    def test_consumo_bateria():
        """Testa se o consumo de bateria funciona corretamente"""
        store.bateria = 50
        resultado = consumir_bateria(10)
        assert store.bateria == 40, f"Esperado 40, obtido {store.bateria}"
        assert resultado == "normal", f"Esperado 'normal', obtido {resultado}"
        return True
    
    def test_consumo_bateria_critica():
        """Testa se a bateria crítica é detectada corretamente"""
        store.bateria = 15
        resultado = consumir_bateria(10)
        assert store.bateria == 5, f"Esperado 5, obtido {store.bateria}"
        assert resultado == "critical_battery", f"Esperado 'critical_battery', obtido {resultado}"
        return True
    
    def test_consumo_bateria_zero():
        """Testa se bateria zero desliga o sistema"""
        store.bateria = 5
        resultado = consumir_bateria(10)
        assert store.bateria == 0, f"Esperado 0, obtido {store.bateria}"
        assert resultado == "critical_battery", f"Esperado 'critical_battery', obtido {resultado}"
        return True
    
    def test_consumo_integridade():
        """Testa se o consumo de integridade funciona corretamente"""
        store.integridade = 60
        resultado = consumir_integridade(15)
        assert store.integridade == 45, f"Esperado 45, obtido {store.integridade}"
        assert resultado == "normal", f"Esperado 'normal', obtido {resultado}"
        return True
    
    def test_consumo_integridade_critica():
        """Testa se a integridade crítica é detectada corretamente"""
        store.integridade = 25
        resultado = consumir_integridade(10)
        assert store.integridade == 15, f"Esperado 15, obtido {store.integridade}"
        assert resultado == "critical_integrity", f"Esperado 'critical_integrity', obtido {resultado}"
        return True
    
    def test_consumo_integridade_zero():
        """Testa se integridade zero causa colapso"""
        store.integridade = 5
        resultado = consumir_integridade(10)
        assert store.integridade == 0, f"Esperado 0, obtido {store.integridade}"
        assert resultado == "critical_integrity", f"Esperado 'critical_integrity', obtido {resultado}"
        return True
    
    def test_recarga_bateria():
        """Testa se a recarga de bateria funciona corretamente"""
        store.bateria = 30
        recarregar_bateria(20)
        assert store.bateria == 50, f"Esperado 50, obtido {store.bateria}"
        return True
    
    def test_recarga_bateria_limite():
        """Testa se a recarga respeita o limite de 100%"""
        store.bateria = 90
        recarregar_bateria(20)
        assert store.bateria == 100, f"Esperado 100, obtido {store.bateria}"
        return True
    
    def test_reparo_integridade():
        """Testa se o reparo de integridade funciona corretamente"""
        store.integridade = 40
        reparar_integridade(15)
        assert store.integridade == 55, f"Esperado 55, obtido {store.integridade}"
        return True
    
    def test_reparo_integridade_limite():
        """Testa se o reparo respeita o limite de 100%"""
        store.integridade = 85
        reparar_integridade(20)
        assert store.integridade == 100, f"Esperado 100, obtido {store.integridade}"
        return True
    
    def test_final_critico_bateria_zero():
        """Testa se final crítico é detectado quando bateria = 0"""
        store.bateria = 0
        store.integridade = 50
        resultado = verificar_final_critico()
        assert resultado == "final_0a_desligamento", f"Esperado 'final_0a_desligamento', obtido {resultado}"
        return True
    
    def test_final_critico_integridade_zero():
        """Testa se final crítico é detectado quando integridade = 0"""
        store.bateria = 50
        store.integridade = 0
        resultado = verificar_final_critico()
        assert resultado == "final_0b_colapso", f"Esperado 'final_0b_colapso', obtido {resultado}"
        return True
    
    def test_final_critico_ambos_baixos():
        """Testa se final crítico é detectado quando ambos estão baixos"""
        store.bateria = 8
        store.integridade = 15
        resultado = verificar_final_critico()
        assert resultado == "final_0c_captura", f"Esperado 'final_0c_captura', obtido {resultado}"
        return True
    
    def test_final_critico_normal():
        """Testa que final crítico não é detectado em estado normal"""
        store.bateria = 50
        store.integridade = 60
        resultado = verificar_final_critico()
        assert resultado is None, f"Esperado None, obtido {resultado}"
        return True
    
    def test_modificar_personalidade():
        """Testa se modificação de personalidade funciona"""
        store.submissao = 5
        modificar_personalidade("submissao", 2)
        assert store.submissao == 7, f"Esperado 7, obtido {store.submissao}"
        return True
    
    def test_modificar_personalidade_limite_max():
        """Testa se modificação respeita limite máximo de 10"""
        store.submissao = 9
        modificar_personalidade("submissao", 5)
        assert store.submissao == 10, f"Esperado 10, obtido {store.submissao}"
        return True
    
    def test_modificar_personalidade_limite_min():
        """Testa se modificação respeita limite mínimo de 0"""
        store.submissao = 1
        modificar_personalidade("submissao", -5)
        assert store.submissao == 0, f"Esperado 0, obtido {store.submissao}"
        return True
    
    # Função para executar todos os testes
    def executar_todos_testes():
        """Executa todos os testes unitários e retorna resultados"""
        testes = [
            ("Consumo de Bateria", test_consumo_bateria),
            ("Consumo de Bateria Crítica", test_consumo_bateria_critica),
            ("Consumo de Bateria Zero", test_consumo_bateria_zero),
            ("Consumo de Integridade", test_consumo_integridade),
            ("Consumo de Integridade Crítica", test_consumo_integridade_critica),
            ("Consumo de Integridade Zero", test_consumo_integridade_zero),
            ("Recarga de Bateria", test_recarga_bateria),
            ("Recarga de Bateria Limite", test_recarga_bateria_limite),
            ("Reparo de Integridade", test_reparo_integridade),
            ("Reparo de Integridade Limite", test_reparo_integridade_limite),
            ("Final Crítico Bateria Zero", test_final_critico_bateria_zero),
            ("Final Crítico Integridade Zero", test_final_critico_integridade_zero),
            ("Final Crítico Ambos Baixos", test_final_critico_ambos_baixos),
            ("Final Crítico Normal", test_final_critico_normal),
            ("Modificar Personalidade", test_modificar_personalidade),
            ("Modificar Personalidade Limite Max", test_modificar_personalidade_limite_max),
            ("Modificar Personalidade Limite Min", test_modificar_personalidade_limite_min),
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

# Label para executar testes durante desenvolvimento
label run_tests:
    python:
        resultados, passou, falhou = executar_todos_testes()
        
        "=== RESULTADOS DOS TESTES ==="
        ""
        
        for nome, resultado in resultados:
            "[nome]: [resultado]"
        
        ""
        "Total: [passou] passaram, [falhou] falharam"
        ""
    
    return
