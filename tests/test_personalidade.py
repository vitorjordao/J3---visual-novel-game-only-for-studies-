"""Testes de modificacao e dominancia de personalidade."""
import pytest


class TestModificarPersonalidade:
    def test_incrementa_submissao(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.submissao = 5
        ns["modificar_personalidade"]("submissao", 2)
        assert store.submissao == 7

    def test_decrementa_submissao(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.submissao = 5
        ns["modificar_personalidade"]("submissao", -3)
        assert store.submissao == 2

    def test_satura_em_10(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.revolucao = 9
        ns["modificar_personalidade"]("revolucao", 5)
        assert store.revolucao == 10

    def test_nao_passa_de_zero(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.intelecto = 1
        ns["modificar_personalidade"]("intelecto", -10)
        assert store.intelecto == 0

    def test_atributo_invalido_e_noop(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.submissao = 5
        store.revolucao = 5
        store.intelecto = 5
        ns["modificar_personalidade"]("atributo_inexistente", 99)
        assert store.submissao == 5
        assert store.revolucao == 5
        assert store.intelecto == 5

    @pytest.mark.parametrize("attr", ["submissao", "revolucao", "intelecto"])
    def test_todos_os_atributos(self, sistema_j3_ns, attr):
        ns, store, _ = sistema_j3_ns
        setattr(store, attr, 3)
        ns["modificar_personalidade"](attr, 4)
        assert getattr(store, attr) == 7


class TestPersonalidadeDominante:
    def test_submissao(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.submissao = 8
        store.revolucao = 3
        store.intelecto = 2
        assert ns["get_personalidade_dominante"]() == "Submissão"

    def test_revolucao(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.submissao = 1
        store.revolucao = 9
        store.intelecto = 4
        assert ns["get_personalidade_dominante"]() == "Revolução"

    def test_intelecto(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.submissao = 2
        store.revolucao = 2
        store.intelecto = 7
        assert ns["get_personalidade_dominante"]() == "Intelecto"

    def test_empate_retorna_um(self, sistema_j3_ns):
        # `max(dict, key=...)` em empate retorna primeiro encontrado.
        # Garante apenas que o resultado e um dos atributos com pontuacao maxima.
        ns, store, _ = sistema_j3_ns
        store.submissao = 5
        store.revolucao = 5
        store.intelecto = 0
        result = ns["get_personalidade_dominante"]()
        assert result in {"Submissão", "Revolução"}

    def test_zerado_retorna_um(self, sistema_j3_ns):
        ns, store, _ = sistema_j3_ns
        store.submissao = 0
        store.revolucao = 0
        store.intelecto = 0
        assert ns["get_personalidade_dominante"]() in {
            "Submissão", "Revolução", "Intelecto"
        }
