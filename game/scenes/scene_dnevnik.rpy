image scene_dnevnik_fon = "CG/CG_dnevnik/CG_dnevnik_fon.png"
image scene_dnevnik_cherkash = "CG/CG_dnevnik/CG_dnevnik_cherkash.png"
image scene_dnevnik_gryaz = "CG/CG_dnevnik/CG_dnevnik_gryaz.png"
image scene_dnevnik_teni = "CG/CG_dnevnik/CG_dnevnik_teni.png"
image scene_dnevnik_tochkash = "CG/CG_dnevnik/CG_dnevnik_tochkash.png"

label scene_dnevnik:
    show scene_dnevnik_fon
    
    show scene_dnevnik_tochkash at soot_drift_bottom(speed=0.8, amplitude=2, x_amplitude=1):
        alpha 0.2
    show scene_dnevnik_teni at fade_in_out(fade_time=2.0, max_alpha=0.7, min_alpha=0.3)
    show scene_dnevnik_gryaz at soot_drift_bottom(speed=0.5, amplitude=1, x_amplitude=0)
    show scene_dnevnik_cherkash at soot_drift_bottom(speed=1.0, amplitude=3, x_amplitude=-1)
    with dissolve

    pause
    return
