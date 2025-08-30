image corpses_cherkash = "CG/CG_ending_bad_ekipaj/CG_ending_bad_ekipaj_cherkash.png"

image corpses = "CG/CG_ending_bad_ekipaj/CG_ending_bad_ekipaj_Ekipaj.png"

label scene_corpses:
    play music music_theme_bad_ending_cosmos fadein 1.0 loop
    show corpses
    show corpses_cherkash at soot_drift_bottom(2, 1.01, -10)
    pause
    stop music fadeout 1.0
    return
