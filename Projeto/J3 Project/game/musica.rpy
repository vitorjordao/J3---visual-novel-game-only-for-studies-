# Musica aleatoria de fundo
# Toca uma das faixas de audio/music a qualquer momento, e ao terminar
# escolhe outra aleatoriamente (sem repetir a mesma duas vezes seguidas).
# Persiste atraves de saves (Ren'Py salva o estado do canal music).

default _music_random_enabled = True

init python:
    import random as _music_random

    music_tracks = [
        "audio/music/After_the_Rainfall.mp3",
        "audio/music/Asphalt_Downpour.mp3",
        "audio/music/Late_Shift_at_Terminal_.mp3",
        "audio/music/Piston_Alignment.mp3",
        "audio/music/Sub_Level_View.mp3",
    ]

    # Container mutavel para guardar a ultima faixa escolhida (evita repetir).
    _music_last_track = [None]

    def _music_pick_next():
        candidates = [t for t in music_tracks if t != _music_last_track[0]]
        if not candidates:
            candidates = list(music_tracks)
        track = _music_random.choice(candidates)
        _music_last_track[0] = track
        return track

    def _music_queue_next():
        # Callback chamado pelo Ren'Py quando a fila do canal music esvazia.
        # Respeita flag global para permitir silenciar em cenas criticas (finais 0a/0b/0c).
        if not getattr(renpy.store, "_music_random_enabled", True):
            return
        renpy.music.queue(_music_pick_next(), channel="music", loop=False)

    renpy.music.set_queue_empty_callback(_music_queue_next, channel="music")

label iniciar_musica_aleatoria:
    $ _music_random_enabled = True
    if not renpy.music.is_playing(channel="music"):
        $ renpy.music.queue(_music_pick_next(), channel="music", loop=False)
    return

label parar_musica_aleatoria:
    # Desliga a aleatorizacao antes de "stop music" em finais criticos
    # para evitar que o callback re-enfileire faixa nova.
    $ _music_random_enabled = False
    stop music
    return
