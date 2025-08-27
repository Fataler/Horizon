image scene_zapiska_fon = "CG/CG_zapiska/CG_zapiska_fon.png"
image scene_zapiska_cherkash = "CG/CG_zapiska/CG_zapiska_cherkash.png"
image scene_zapiska_list_and_text = "CG/CG_zapiska/CG_zapiska_list_and_text.png"
image scene_zapiska_ruka = "CG/CG_zapiska/CG_zapiska_ruka.png"

transform hand_move:
    subpixel True
    parallel:
        block:
            easein 1.5 yoffset -10
            easeout 1.5 yoffset 0
            repeat
    parallel:
        block:
            linear 0.1 xoffset -1
            linear 0.1 xoffset 1
            repeat

label scene_zapiska:
    show scene_zapiska_fon
    show scene_zapiska_list_and_text at soot_drift_bottom(speed=0.5, amplitude=1, x_amplitude=0)
    show scene_zapiska_ruka at hand_move
    show scene_zapiska_cherkash at soot_drift_bottom(speed=0.8, amplitude=2, x_amplitude=1)
    with dissolve

    pause
    return
