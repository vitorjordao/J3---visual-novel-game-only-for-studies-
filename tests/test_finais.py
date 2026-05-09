"""
Testes dos 4 finais principais (functions.rpy::get_final_type) +
helpers de custo/ganho usados nas escolhas.
"""
import pytest


class TestGetFinalType:
    def test_sacrificio_submissao_alta(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 8
        store.revolucao = 0
        store.intelecto = 0
        assert ns["get_final_type"]() == "Sacrifício Redentor"

    def test_revolucao_alta(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 0
        store.revolucao = 9
        store.intelecto = 0
        assert ns["get_final_type"]() == "Revolução Consciente"

    def test_vitoria_estrategica_intelecto(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 2
        store.revolucao = 2
        store.intelecto = 6
        assert ns["get_final_type"]() == "Vitória Estratégica"

    def test_equilibrio_complexo_default(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 3
        store.revolucao = 3
        store.intelecto = 3
        assert ns["get_final_type"]() == "Equilíbrio Complexo"

    def test_zero_e_equilibrio(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 0
        store.revolucao = 0
        store.intelecto = 0
        assert ns["get_final_type"]() == "Equilíbrio Complexo"

    def test_threshold_submissao_exato_8(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 8
        assert ns["get_final_type"]() == "Sacrifício Redentor"

    def test_submissao_7_cai_em_equilibrio(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 7
        store.revolucao = 5
        store.intelecto = 5
        # Sub<8, Rev<8, Int<6 -> equilibrio
        assert ns["get_final_type"]() == "Equilíbrio Complexo"

    def test_threshold_intelecto_exato_6(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 0
        store.revolucao = 0
        store.intelecto = 6
        assert ns["get_final_type"]() == "Vitória Estratégica"

    def test_intelecto_5_cai_em_equilibrio(self, functions_ns):
        ns, store, _ = functions_ns
        store.intelecto = 5
        assert ns["get_final_type"]() == "Equilíbrio Complexo"

    def test_prioridade_submissao_sobre_revolucao(self, functions_ns):
        # Quando ambos >= 8, get_final_type prioriza Submissao por
        # ordem de checagem. Documenta comportamento atual.
        ns, store, _ = functions_ns
        store.submissao = 9
        store.revolucao = 10
        assert ns["get_final_type"]() == "Sacrifício Redentor"


class TestPersonalidadeDominanteFunctions:
    """get_personalidade_dominante existe em functions.rpy E sistema_j3.rpy.
    Aqui validamos a copia em functions.rpy para garantir paridade."""

    def test_submissao(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 7
        store.revolucao = 2
        store.intelecto = 1
        assert ns["get_personalidade_dominante"]() == "Submissão"

    def test_revolucao(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 1
        store.revolucao = 8
        store.intelecto = 3
        assert ns["get_personalidade_dominante"]() == "Revolução"

    def test_intelecto(self, functions_ns):
        ns, store, _ = functions_ns
        store.submissao = 1
        store.revolucao = 2
        store.intelecto = 9
        assert ns["get_personalidade_dominante"]() == "Intelecto"


class TestCustoGanho:
    """Helpers que renderizam tags de custo/ganho de recursos no menu."""

    def test_custo_bateria_e_integridade(self, functions_ns):
        ns, _, _ = functions_ns
        result = ns["custo"](bat=2, integ=10)
        assert "-2 BAT" in result
        assert "-10 INT" in result
        assert result.startswith("[")
        assert result.rstrip().endswith("]")

    def test_custo_so_bateria(self, functions_ns):
        ns, _, _ = functions_ns
        result = ns["custo"](bat=5)
        assert "-5 BAT" in result
        assert "INT" not in result

    def test_custo_so_integridade(self, functions_ns):
        ns, _, _ = functions_ns
        result = ns["custo"](integ=15)
        assert "-15 INT" in result
        assert "BAT" not in result

    def test_custo_zerado_retorna_vazio(self, functions_ns):
        ns, _, _ = functions_ns
        assert ns["custo"]() == ""
        assert ns["custo"](bat=0, integ=0) == ""

    def test_ganho_inverte_cor(self, functions_ns):
        ns, _, _ = functions_ns
        result = ns["ganho"](bat=10, integ=5)
        assert "+10 BAT" in result
        assert "+5 INT" in result
        # Cores diferentes entre custo (vermelho) e ganho (verde)
        custo = ns["custo"](bat=10)
        assert "#ff5566" in custo
        ganho = ns["ganho"](bat=10)
        assert "#55ff99" in ganho


class TestDispatcherDay7VsGetFinalType:
    """
    day7.rpy tem dispatcher proprio (dominante + threshold) que pode
    divergir de get_final_type() (so threshold). Documenta divergencia.

    Cenario: submissao=8, revolucao=10
    - Dispatcher day7: dominante=Revolução, revolucao>=8 -> final_revolution
    - get_final_type(): submissao>=8 (1a condicao) -> Sacrifício Redentor

    Esses testes provam que a divergencia EXISTE no codigo. Se algum dia
    forem unificados, esses testes falham e indicam que o invariante
    mudou — momento de revisar a UI que mostra get_final_type().
    """

    def test_divergencia_quando_submissao_e_revolucao_ambos_altos(
        self, functions_ns
    ):
        ns, store, _ = functions_ns
        store.submissao = 8
        store.revolucao = 10
        store.intelecto = 0
        # functions.rpy retorna pela ordem de checagem
        assert ns["get_final_type"]() == "Sacrifício Redentor"
        # mas dominante seria Revolução
        assert ns["get_personalidade_dominante"]() == "Revolução"

    def test_divergencia_intelecto_perdedor_para_equilibrio(self, functions_ns):
        # Se int=6 mas sub=7, get_final_type retorna Estrategica.
        # Mas dominante sempre seria Submissao.
        ns, store, _ = functions_ns
        store.submissao = 7
        store.revolucao = 0
        store.intelecto = 6
        assert ns["get_final_type"]() == "Vitória Estratégica"
        assert ns["get_personalidade_dominante"]() == "Submissão"
