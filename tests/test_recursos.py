"""Testes de bateria, integridade e finais criticos."""
import pytest


class TestBateria:
    def test_consumir_normal(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.bateria = 50
        assert ns["consumir_bateria"](10) == "normal"
        assert store.bateria == 40

    def test_consumir_warning(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.bateria = 25
        store.integridade = 100  # alto, evita 0c
        assert ns["consumir_bateria"](5) == "low_battery"
        assert store.bateria == 20

    def test_consumir_critical_battery(self, sistema_j3_ns):
        ns, store, jumps = sistema_j3_ns
        store.bateria = 15
        store.integridade = 100
        ns["consumir_bateria"](5)
        # bateria=10 + integridade=100 nao dispara 0c (pede integridade<=20)
        # mas dispara warning_battery
        assert store.bateria == 10
        assert "final_0a_desligamento" not in jumps
        assert "final_0c_captura" not in jumps

    def test_consumir_zero_dispara_final_0a(self, sistema_j3_ns):
        ns, store, jumps = sistema_j3_ns
        store.bateria = 5
        ns["consumir_bateria"](10)
        assert store.bateria == 0
        assert "final_0a_desligamento" in jumps

    def test_consumir_nao_passa_de_zero(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.bateria = 3
        ns["consumir_bateria"](100)
        assert store.bateria == 0

    def test_recarregar_normal(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.bateria = 30
        ns["recarregar_bateria"](20)
        assert store.bateria == 50

    def test_recarregar_satura_em_100(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.bateria = 90
        ns["recarregar_bateria"](50)
        assert store.bateria == 100


class TestIntegridade:
    def test_consumir_normal(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.integridade = 60
        assert ns["consumir_integridade"](15) == "normal"
        assert store.integridade == 45

    def test_consumir_zero_dispara_final_0b(self, sistema_j3_ns):
        ns, store, jumps = sistema_j3_ns
        store.integridade = 5
        ns["consumir_integridade"](10)
        assert store.integridade == 0
        assert "final_0b_colapso" in jumps

    def test_reparar_normal(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.integridade = 40
        ns["reparar_integridade"](15)
        assert store.integridade == 55

    def test_reparar_satura_em_100(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.integridade = 95
        ns["reparar_integridade"](20)
        assert store.integridade == 100


class TestFinalCritico:
    def test_normal_retorna_normal(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.bateria = 50
        store.integridade = 60
        assert ns["verificar_final_critico"]() == "Normal"

    def test_bateria_zero_aciona_0a(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.bateria = 0
        store.integridade = 50
        assert ns["verificar_final_critico"]() == "final_0a_desligamento"

    def test_integridade_zero_aciona_0b(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.bateria = 50
        store.integridade = 0
        assert ns["verificar_final_critico"]() == "final_0b_colapso"

    def test_bateria_baixa_e_integridade_baixa_aciona_0c(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.bateria = 8
        store.integridade = 15
        assert ns["verificar_final_critico"]() == "final_0c_captura"

    def test_bateria_zero_tem_prioridade_sobre_integridade_zero(self, sistema_j3_ns):
        # 0a vem antes de 0b na ordem de checagem
        ns, store, _ = sistema_j3_ns
        store.bateria = 0
        store.integridade = 0
        assert ns["verificar_final_critico"]() == "final_0a_desligamento"


class TestStatusBateria:
    @pytest.mark.parametrize("valor,esperado", [
        (5, "CRÍTICA"),
        (10, "CRÍTICA"),
        (15, "BAIXA"),
        (20, "BAIXA"),
        (35, "MODERADA"),
        (50, "MODERADA"),
        (80, "BOA"),
        (100, "BOA"),
    ])
    def test_thresholds(self, sistema_j3_ns, valor, esperado):
        ns, store, _ = sistema_j3_ns
        store.bateria = valor
        assert ns["get_status_bateria"]() == esperado


class TestStatusIntegridade:
    @pytest.mark.parametrize("valor,esperado", [
        (10, "CRÍTICA"),
        (20, "CRÍTICA"),
        (25, "DANIFICADA"),
        (30, "DANIFICADA"),
        (50, "COMPROMETIDA"),
        (70, "COMPROMETIDA"),
        (90, "ESTÁVEL"),
        (100, "ESTÁVEL"),
    ])
    def test_thresholds(self, sistema_j3_ns, valor, esperado):
        ns, store, _ = sistema_j3_ns
        store.integridade = valor
        assert ns["get_status_integridade"]() == esperado


class TestStatusColor:
    def test_low(self, sistema_j3_ns):
        ns, _, _ = sistema_j3_ns
        assert ns["_status_color"](10, 20, 50) == "#ff3344"

    def test_mid(self, sistema_j3_ns):
        ns, _, _ = sistema_j3_ns
        assert ns["_status_color"](40, 20, 50) == "#ffaa22"

    def test_high(self, sistema_j3_ns):
        ns, _, _ = sistema_j3_ns
        assert ns["_status_color"](80, 20, 50) == "#22ff99"

    def test_borda_low(self, sistema_j3_ns):
        ns, _, _ = sistema_j3_ns
        # value <= low_threshold -> low
        assert ns["_status_color"](20, 20, 50) == "#ff3344"

    def test_borda_mid(self, sistema_j3_ns):
        ns, _, _ = sistema_j3_ns
        assert ns["_status_color"](50, 20, 50) == "#ffaa22"
