image scene_pogrom_v_lazarete_fon = "CG/CG_pogrom_v_lazarete/CG_pogrom_v_lazarete_fon.png"
image scene_pogrom_v_lazarete_glaza = "CG/CG_pogrom_v_lazarete/CG_pogrom_v_lazarete_glaza.png"
image scene_pogrom_v_lazarete_cherkash = "CG/CG_pogrom_v_lazarete/CG_pogrom_v_lazarete_cherkash.png"

label scene_pogrom_v_lazarete:
    show scene_pogrom_v_lazarete_fon
    show scene_pogrom_v_lazarete_glaza at infinite_shake(x_amplitude=4, y_amplitude=4, frequency=0.9)
    show scene_pogrom_v_lazarete_cherkash at soot_drift_bottom(speed=0.2, zoom=1.001, amplitude=4, x_amplitude=3), truecenter
    with dissolve
    return
