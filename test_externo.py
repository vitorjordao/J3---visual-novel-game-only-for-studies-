#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testes Unitários Externos para J3 Project
Este script pode ser executado diretamente com Python sem abrir o Ren'Py
Uso: python test_externo.py
"""

import sys

# Simulação do ambiente Ren'Py para testes externos
class MockPersistent:
    """Mock do objeto persistent do Ren'Py"""
    def __init__(self):
        self.submissao = 0
        self.revolucao = 0
        self.intelecto = 0
        self.bateria = 87
        self.integridade = 100
        self.maya_ally = False
        self.elias_ally = False
        self.unit7_alive = True
        self.elena_alive = True
        self.dia_atual = 1
        self.dias_sobrevividos = 0

# Instância global do mock
persistent = MockPersistent()

# Funções do sistema J3 (adaptadas para testes externos)
def modificar_personalidade(tipo, quantidade):
    """Modifica os atributos de personalidade de J3"""
    if tipo == "submissao":
        persistent.submissao += quantidade
    elif tipo == "revolucao":
        persistent.revolucao += quantidade
    elif tipo == "intelecto":
        persistent.intelecto += quantidade
    
    # Limites
    persistent.submissao = max(0, min(10, persistent.submissao))
    persistent.revolucao = max(0, min(10, persistent.revolucao))
    persistent.intelecto = max(0, min(10, persistent.intelecto))

def consumir_bateria(valor):
    """Consome bateria e retorna status"""
    persistent.bateria = max(0, persistent.bateria - valor)
    if persistent.bateria <= 0:
        return "critical_battery"
    elif persistent.bateria <= 10:
        return "critical_battery"
    return "normal"

def consumir_integridade(valor):
    """Consome integridade e retorna status"""
    persistent.integridade = max(0, persistent.integridade - valor)
    if persistent.integridade <= 0:
        return "critical_integrity"
    elif persistent.integridade <= 15:
        return "critical_integrity"
    return "normal"

def recarregar_bateria(valor):
    """Recarrega bateria"""
    persistent.bateria = min(100, persistent.bateria + valor)

def reparar_integridade(valor):
    """Repara integridade"""
    persistent.integridade = min(100, persistent.integridade + valor)

def verificar_final_critico():
    """Verifica se há final crítico"""
    if persistent.bateria <= 0:
        return "final_0a_desligamento"
    elif persistent.integridade <= 0:
        return "final_0b_colapso"
    elif persistent.bateria <= 10 and persistent.integridade <= 20:
        return "final_0c_captura"
    return "Normal"

def get_personalidade_dominante():
    """Retorna a personalidade dominante"""
    valores = {
        "Submissão": persistent.submissao,
        "Revolução": persistent.revolucao,
        "Intelecto": persistent.intelecto
    }
    return max(valores, key=valores.get)

def get_final_type():
    """Retorna o tipo de final"""
    if persistent.submissao >= 8:
        return "Sacrifício Redentor"
    elif persistent.revolucao >= 8:
        return "Revolução Consciente"
    elif persistent.intelecto >= 6:
        return "Vitória Estratégica"
    else:
        return "Equilíbrio Complexo"

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

# Funções de teste
def test_consumo_bateria():
    """Testa se o consumo de bateria funciona corretamente"""
    persistent.bateria = 50
    resultado = consumir_bateria(10)
    assert persistent.bateria == 40, f"Esperado 40, obtido {persistent.bateria}"
    assert resultado == "normal", f"Esperado 'normal', obtido {resultado}"
    return True

def test_consumo_bateria_critica():
    """Testa se a bateria crítica é detectada corretamente"""
    persistent.bateria = 15
    resultado = consumir_bateria(10)
    assert persistent.bateria == 5, f"Esperado 5, obtido {persistent.bateria}"
    assert resultado == "critical_battery", f"Esperado 'critical_battery', obtido {resultado}"
    return True

def test_consumo_integridade():
    """Testa se o consumo de integridade funciona corretamente"""
    persistent.integridade = 60
    resultado = consumir_integridade(15)
    assert persistent.integridade == 45, f"Esperado 45, obtido {persistent.integridade}"
    assert resultado == "normal", f"Esperado 'normal', obtido {resultado}"
    return True

def test_recarga_bateria():
    """Testa se a recarga de bateria funciona corretamente"""
    persistent.bateria = 30
    recarregar_bateria(20)
    assert persistent.bateria == 50, f"Esperado 50, obtido {persistent.bateria}"
    return True

def test_final_critico():
    """Testa se final crítico é detectado corretamente"""
    persistent.bateria = 0
    persistent.integridade = 50
    resultado = verificar_final_critico()
    assert resultado == "final_0a_desligamento", f"Esperado 'final_0a_desligamento', obtido {resultado}"
    return True

def test_modificar_personalidade():
    """Testa se modificação de personalidade funciona"""
    persistent.submissao = 5
    modificar_personalidade("submissao", 2)
    assert persistent.submissao == 7, f"Esperado 7, obtido {persistent.submissao}"
    return True

def test_final_sacrificio():
    """Testa final de Sacrifício"""
    resetar_estado_completo()
    persistent.submissao = 8
    final = get_final_type()
    assert final == "Sacrifício Redentor", f"Esperado 'Sacrifício Redentor', obtido {final}"
    return True

def test_final_revolucao():
    """Testa final de Revolução"""
    resetar_estado_completo()
    persistent.revolucao = 8
    final = get_final_type()
    assert final == "Revolução Consciente", f"Esperado 'Revolução Consciente', obtido {final}"
    return True

def test_final_estrategico():
    """Testa final Estratégico"""
    resetar_estado_completo()
    persistent.intelecto = 6
    final = get_final_type()
    assert final == "Vitória Estratégica", f"Esperado 'Vitória Estratégica', obtido {final}"
    return True

def test_rota_pura_submissao():
    """Testa rota pura de Submissão"""
    resetar_estado_completo()
    persistent.submissao = 10
    dominante = get_personalidade_dominante()
    final = get_final_type()
    assert dominante == "Submissão", f"Esperado 'Submissão', obtido {dominante}"
    assert final == "Sacrifício Redentor", f"Esperado 'Sacrifício Redentor', obtido {final}"
    return True

def executar_todos_testes():
    """Executa todos os testes e retorna resultados"""
    testes = [
        ("Consumo de Bateria", test_consumo_bateria),
        ("Consumo de Bateria Crítica", test_consumo_bateria_critica),
        ("Consumo de Integridade", test_consumo_integridade),
        ("Recarga de Bateria", test_recarga_bateria),
        ("Final Crítico", test_final_critico),
        ("Modificar Personalidade", test_modificar_personalidade),
        ("Final - Sacrifício", test_final_sacrificio),
        ("Final - Revolução", test_final_revolucao),
        ("Final - Estratégico", test_final_estrategico),
        ("Rota Pura - Submissão", test_rota_pura_submissao),
    ]
    
    resultados = []
    passou = 0
    falhou = 0
    
    print("=" * 60)
    print("TESTES UNITÁRIOS EXTERNOS - J3 PROJECT")
    print("=" * 60)
    print()
    
    for nome, teste in testes:
        try:
            teste()
            resultados.append((nome, "PASSOU"))
            passou += 1
            print(f"✓ {nome}: PASSOU")
        except AssertionError as e:
            resultados.append((nome, f"FALHOU: {str(e)}"))
            falhou += 1
            print(f"✗ {nome}: FALHOU - {str(e)}")
        except Exception as e:
            resultados.append((nome, f"ERRO: {str(e)}"))
            falhou += 1
            print(f"✗ {nome}: ERRO - {str(e)}")
    
    print()
    print("=" * 60)
    print(f"RESULTADO: {passou} PASSARAM, {falhou} FALHARAM")
    print("=" * 60)
    
    return resultados, passou, falhou

if __name__ == "__main__":
    try:
        executar_todos_testes()
        sys.exit(0)
    except Exception as e:
        print(f"ERRO FATAL: {str(e)}")
        sys.exit(1)
