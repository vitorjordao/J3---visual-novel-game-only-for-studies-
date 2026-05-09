"""
Test harness para o jogo J3 (Ren'Py).

Estrategia: extrai os blocos `init python:` de cada .rpy relevante e
executa em um namespace Python isolado com mocks de `store` e `renpy.*`.
Assim conseguimos testar as funcoes de jogo (consumir_bateria,
verificar_final_critico, get_personalidade_dominante, etc.) sem
precisar do runtime Ren'Py.
"""
from __future__ import annotations

import re
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
GAME_DIR = REPO_ROOT / "Projeto" / "J3 Project" / "game"


def extract_init_python(rpy_text: str) -> str:
    """
    Extrai o corpo de blocos `init python:` (com offset opcional, ex.
    `init -1 python:`) de um arquivo .rpy. Retorna fonte Python ja
    dedentado, pronto para exec.
    """
    lines = rpy_text.splitlines()
    out: list[str] = []
    in_block = False
    block_indent: int | None = None

    init_pattern = re.compile(r"^init(?:\s+-?\d+)?\s+python:\s*$")

    i = 0
    while i < len(lines):
        line = lines[i]
        if not in_block:
            if init_pattern.match(line):
                in_block = True
                block_indent = None
            i += 1
            continue

        if not line.strip():
            out.append("")
            i += 1
            continue

        leading = len(line) - len(line.lstrip(" "))
        if block_indent is None:
            block_indent = leading
        if leading < block_indent:
            # Saimos do bloco; reprocessa a mesma linha (pode ser inicio de outro init python).
            in_block = False
            block_indent = None
            continue
        out.append(line[block_indent:])
        i += 1

    return "\n".join(out)


def make_store(**overrides) -> SimpleNamespace:
    """Estado padrao do store antes de cada teste."""
    defaults = dict(
        bateria=100,
        integridade=100,
        submissao=0,
        revolucao=0,
        intelecto=0,
        dia_atual=1,
        memoria_recuperada=0,
        maya_ally=False,
        elias_ally=False,
        unit7_alive=True,
        elena_alive=True,
        escolha_feita=0,
        nvl_list=[],
    )
    defaults.update(overrides)
    return SimpleNamespace(**defaults)


def build_namespace(store: SimpleNamespace, jumps: list[str]) -> dict:
    """Namespace com mocks para exec do init python."""
    renpy_mock = MagicMock()
    renpy_mock.store = store

    def fake_jump(label: str) -> None:
        jumps.append(label)

    renpy_mock.jump = fake_jump
    # Ren'Py music API usado em musica.rpy
    renpy_mock.music = MagicMock()
    renpy_mock.music.queue = MagicMock()
    renpy_mock.music.is_playing = MagicMock(return_value=False)
    renpy_mock.music.set_queue_empty_callback = MagicMock()

    return {
        "store": store,
        "renpy": renpy_mock,
        "_jumps": jumps,
    }


@pytest.fixture
def sistema_j3_ns():
    """
    Carrega `sistema_j3.rpy`, executa os blocos init python em um namespace
    isolado e retorna (namespace, store, jumps). Cada teste recebe estado
    fresco.
    """
    rpy_text = (GAME_DIR / "sistema_j3.rpy").read_text(encoding="utf-8")
    py_source = extract_init_python(rpy_text)
    store = make_store()
    jumps: list[str] = []
    ns = build_namespace(store, jumps)
    exec(compile(py_source, "sistema_j3.rpy[init python]", "exec"), ns)
    return ns, store, jumps


@pytest.fixture
def musica_ns():
    """
    Carrega `musica.rpy` se existir (feature pode estar em branch separado).
    Marca skip se ausente.
    """
    musica_path = GAME_DIR / "musica.rpy"
    if not musica_path.exists():
        pytest.skip("musica.rpy nao presente neste branch")
    rpy_text = musica_path.read_text(encoding="utf-8")
    py_source = extract_init_python(rpy_text)
    store = make_store(_music_random_enabled=True)
    jumps: list[str] = []
    ns = build_namespace(store, jumps)
    exec(compile(py_source, "musica.rpy[init python]", "exec"), ns)
    return ns, store, jumps
