# Testes do J3 Project

## Estrutura

```
tests/
  conftest.py              fixtures pytest + extracao de init python
  test_recursos.py         bateria, integridade, finais criticos
  test_personalidade.py    submissao/revolucao/intelecto + dominante
  test_musica.py           shuffle aleatorio (skipa se musica.rpy ausente)
```

## Como funciona

Ren'Py mistura logica Python (`init python:`) com sintaxe propria de cena.
Nao da pra `import` um `.rpy` diretamente em pytest. Usamos um harness em
`conftest.py` que:

1. Le o arquivo `.rpy`.
2. Extrai todos os blocos `init python:` (com qualquer offset).
3. Dedenta e executa em um namespace isolado.
4. Mocka `store` (SimpleNamespace mutavel) e `renpy.*` (MagicMock).

As funcoes definidas no init python ficam acessiveis no dicionario
`namespace`. Cada teste recebe estado fresco via fixture.

## Rodar localmente

### WSL2 / Linux

```bash
python3 -m venv ~/j3-venv
~/j3-venv/bin/pip install -r requirements-test.txt
~/j3-venv/bin/pytest -v
```

### Windows nativo

```powershell
py -3 -m venv .venv
.venv\Scripts\pip install -r requirements-test.txt
.venv\Scripts\pytest -v
```

## CI

`.github/workflows/ci.yml` roda dois jobs em paralelo a cada push/PR:

- `pytest`: instala deps, roda toda a suite Python.
- `renpy-lint`: baixa o SDK Ren'Py 8.2.3 (cacheado), roda
  `renpy.sh "Projeto/J3 Project" lint`. Pega imagens faltando, labels
  mortos, sintaxe ruim.

## Cobertura atual (50 testes)

| Arquivo | Cobre |
|---------|-------|
| `test_recursos.py` | `consumir_bateria`, `consumir_integridade`, `recarregar_bateria`, `reparar_integridade`, `verificar_final_critico`, `get_status_bateria`, `get_status_integridade`, `_status_color` |
| `test_personalidade.py` | `modificar_personalidade` (clamp 0-10), `get_personalidade_dominante` |
| `test_musica.py` | `_music_pick_next` (no repeat imediato, distribuicao), `_music_queue_next` (callback respeita flag) |

## O que NAO esta coberto (ainda)

- **Fluxo narrativo end-to-end** (escolhas no menu -> final correto).
  Precisa do runtime Ren'Py com `testcase` blocks ou playthrough manual.
- **Renderizacao visual** (overlay de sprites, posicao de personagens,
  tamanho de texto). So pega via playtest ou screenshot diff.
- **Audio playback** (faixa toca de fato). Mocks nao validam `pygame`.

## Adicionar novos testes

1. Funcao nova em `init python:` no `.rpy` -> ja extraido pelo harness.
2. Criar `tests/test_<area>.py`. Importar via fixture (ex: `sistema_j3_ns`).
3. Rodar `pytest -v`.

Para arquivo `.rpy` novo, replicar o padrao `musica_ns` em
`conftest.py` (le, extrai, exec em namespace).

## Limitacoes do harness

- Nao executa codigo fora de `init python:` (labels, define, image).
  Logica de UI/cena nao e testavel via pytest.
- Mock de `renpy.jump` apenas grava o destino em `_jumps`; nao executa
  o label.
- `default X = Y` no .rpy nao e processado; cada teste deve setar
  manualmente os valores de `store` que precisar.
