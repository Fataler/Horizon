image scene_david_potracheno_fon = "CG/CG_David_potracheno/CG_David_potracheno_0001_fon.png"
image scene_david_potracheno_cherkash = "CG/CG_David_potracheno/CG_David_potracheno_0000_cherkash.png"

label scene_david_potracheno:
    show scene_david_potracheno_fon
    show scene_david_potracheno_cherkash at soot_drift_bottom(speed=1.0, amplitude=3, x_amplitude=2)
    with dissolve

    pause
    return
