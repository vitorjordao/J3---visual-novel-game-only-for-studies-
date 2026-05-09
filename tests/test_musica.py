"""
Testes do shuffle aleatorio de trilha sonora.

Skipa se musica.rpy nao estiver presente (feature pode estar em branch
separado nao-merged).
"""
from collections import Counter


class TestPickNext:
    def test_retorna_uma_das_faixas(self, musica_ns):
        ns, _, _ = musica_ns
        track = ns["_music_pick_next"]()
        assert track in ns["music_tracks"]

    def test_nao_repete_imediato(self, musica_ns):
        ns, _, _ = musica_ns
        primeira = ns["_music_pick_next"]()
        segunda = ns["_music_pick_next"]()
        assert primeira != segunda

    def test_sequencia_longa_nao_tem_repeat_imediato(self, musica_ns):
        ns, _, _ = musica_ns
        tracks = [ns["_music_pick_next"]() for _ in range(200)]
        for i in range(1, len(tracks)):
            assert tracks[i] != tracks[i - 1], (
                f"Repeat imediato em i={i}: {tracks[i-1]!r} -> {tracks[i]!r}"
            )

    def test_eventualmente_toca_todas(self, musica_ns):
        ns, _, _ = musica_ns
        tracks = [ns["_music_pick_next"]() for _ in range(500)]
        cont = Counter(tracks)
        # Cada faixa deve ter sido tocada ao menos uma vez em 500 picks.
        assert set(cont.keys()) == set(ns["music_tracks"])


class TestQueueNextCallback:
    def test_chama_renpy_music_queue(self, musica_ns):
        ns, _, _ = musica_ns
        ns["_music_queue_next"]()
        renpy = ns["renpy"]
        assert renpy.music.queue.called

    def test_respeita_flag_disabled(self, musica_ns):
        ns, store, _ = musica_ns
        store._music_random_enabled = False
        ns["renpy"].music.queue.reset_mock()
        ns["_music_queue_next"]()
        assert not ns["renpy"].music.queue.called

    def test_volta_a_funcionar_quando_flag_reativada(self, musica_ns):
        ns, store, _ = musica_ns
        store._music_random_enabled = False
        ns["_music_queue_next"]()
        ns["renpy"].music.queue.reset_mock()
        store._music_random_enabled = True
        ns["_music_queue_next"]()
        assert ns["renpy"].music.queue.called
