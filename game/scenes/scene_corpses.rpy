image corpses_cherkash = "CG/CG_ending_bad_ekipaj/CG_ending_bad_ekipaj_cherkash.png"

image corpses = "CG/CG_ending_bad_ekipaj/CG_ending_bad_ekipaj_Ekipaj.png"

label scene_corpses:
    show corpses
    show corpses_cherkash at soot_drift_bottom(2, 1.01, -10)
    pause
    return