# Mapeamento de imagens - definir aqui apenas as artes que ja existem no projeto.
# Sprites/backgrounds nao definidos aparecem como placeholder automatico do Ren'Py,
# facilitando identificar o que ainda falta produzir.

# --- Helpers: forca backgrounds a cobrirem toda a tela (1920x1080) ---
init python:
    def bg_fs(path):
        return Transform(path, xysize=(1920, 1080))

    # Enumera todas as variantes de atributo usadas no script mapeando para o PNG do personagem.
    # Assim 'show j3 neutral', 'show j3 damaged', etc. funcionam sem alterar os scripts.
    _char_map = {
        "j3":               ("characters/j3/J3.png",
                             ["neutral", "damaged", "confident", "rebel", "analytical"]),
        "j3_empty":         ("characters/j3/J3.png", []),
        "j3_revolutionary": ("characters/j3/J3.png", []),
        "j3_hacker":        ("characters/j3/J3.png", []),
        "j3_serving":       ("characters/j3/J3.png", []),
        "maya":             ("characters/maya/maya.png",
                             ["curious", "confident", "conflicted", "grateful"]),
        "elias":            ("characters/elias/Elias.png",
                             ["angry", "frustrated", "tired", "scared", "urgent", "determined"]),
        "elena":            ("characters/elena/elena.png", ["neutral"]),
        "elena_scientist":  ("characters/elena/elena.png", ["urgent"]),
        "unit7":            ("characters/unit7/unity 7.png",
                             ["stern", "leader", "suspicious", "determined"]),
        # --- Novos personagens (gerados via Gemini) ---
        "damaged_bot":      ("characters/damaged_bot/damaged_bot.png", []),
        "synth1":           ("characters/synth1/synth1.png", ["angry"]),
        "synth2":           ("characters/synth2/synth2.png", ["desperate"]),
        "child_curious":    ("characters/child_curious/child_curious.png", []),
        "synth_army":       ("characters/synth_army/synth_army.png", []),
        "drone_captor":     ("characters/drone_captor/drone_captor.png", []),
        "security":         ("characters/security/security.png", ["arrogant", "suspicious", "aggressive"]),
        "mother":           ("characters/mother/mother.png", []),
        "thug1":            ("characters/thug1/thug1.png", ["angry"]),
        "thug2":            ("characters/thug2/thug2.png", ["angry"]),
        "owner":            ("characters/owner/owner.png", ["angry"]),
        "homeless_woman":   ("characters/homeless_woman/homeless_woman.png", ["wise"]),
        "synth_fearful":    ("characters/synth_fearful/synth_fearful.png", []),
        "synth_angry":      ("characters/synth_angry/synth_angry.png", []),
        "commander":        ("characters/commander/commander.png", []),
        "synth_survivor":   ("characters/synth_survivor/synth_survivor.png", []),
        "protester":        ("characters/protester/protester.png", ["angry"]),
        "maria":            ("characters/maria/maria.png", ["curious"]),
        "patrol_drone":     ("characters/patrol_drone/patrol_drone.png", ["stern"]),
        "news_vendor":      ("characters/news_vendor/news_vendor.png", ["neutral"]),
    }
    for _tag, (_path, _attrs) in _char_map.items():
        renpy.image(_tag, _path)
        for _attr in _attrs:
            renpy.image(_tag + " " + _attr, _path)

# --- Backgrounds (fullscreen 1920x1080) ---
image bg avenue_night        = bg_fs("backgrounds/day1/avenue_night.png")
image bg arcade_night        = bg_fs("backgrounds/day2/arcade_night.png")
image bg alley_night         = bg_fs("backgrounds/day3/alley_night.png")
image bg refuge_underground  = bg_fs("backgrounds/day4/refuge_underground.png")
image bg refuge_siege        = bg_fs("backgrounds/day5/refuge_siege.png")
image bg reprogramming_cell  = bg_fs("backgrounds/day6/reprogramming_cell.png")
image bg underground_hideout = bg_fs("backgrounds/day6/underground_hideout.png")
image bg abandoned_lab       = bg_fs("backgrounds/day6/abandoned_lab.png")
image bg neutral_location    = bg_fs("backgrounds/day6/neutral_location.png")
image bg reprogramming_facility = bg_fs("backgrounds/day7/reprogramming_facility.png")
image bg city_plaza          = bg_fs("backgrounds/day7/city_plaza.png")
image bg control_center      = bg_fs("backgrounds/day7/control_center.png")
image bg hospital_service    = bg_fs("backgrounds/day7/hospital_service.png")
image bg neutral_crossroads  = bg_fs("backgrounds/day7/neutral_crossroads.png")
image bg resistance_poster   = bg_fs("backgrounds/day7/resistance_poster.png")
image bg shadow_control      = bg_fs("backgrounds/day7/shadow_control.png")
image bg coexistence_scene   = bg_fs("backgrounds/day7/coexistence_scene.png")
image bg coexistence_efforts = bg_fs("backgrounds/day7/coexistence_scene.png")
image bg synth_obedient      = bg_fs("backgrounds/day7/synth_obedient.png")
image bg resistance_cells    = bg_fs("backgrounds/day7/resistance_cells.png")
image bg political_exposure  = bg_fs("backgrounds/day7/political_exposure.png")
image bg dark_street         = bg_fs("backgrounds/finais/dark_street.png")
image bg laboratory          = bg_fs("backgrounds/finais/laboratory.png")

# =============================================================
# Posicionamento de personagens — resolve sobreposicao
# Os sprites estao em canvas 800x1080 ancorado no bottom.
# Sem esses transforms, "at left" e "at center" sobrepoem
# ~240px. Aqui redefinimos com zoom 0.85 + xcenter afastado:
#   left:   xcenter 15%  (canvas em x=288)
#   center: xcenter 50%  (canvas em x=960)
#   right:  xcenter 85%  (canvas em x=1632)
# Distancia suficiente para 2-3 personagens sem overlap.
# =============================================================
transform left:
    xcenter 0.15
    yalign 1.0
    zoom 0.85

transform center:
    xcenter 0.5
    yalign 1.0
    zoom 0.85

transform right:
    xcenter 0.85
    yalign 1.0
    zoom 0.85

# Variacoes para 4+ personagens em fila (Dia 4, finais do Dia 7)
transform far_left:
    xcenter 0.10
    yalign 1.0
    zoom 0.75

transform far_right:
    xcenter 0.90
    yalign 1.0
    zoom 0.75
