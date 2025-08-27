image scene_mogily_herk = "CG/CG_mogily/CG_mogily_herk.png"
image scene_mogily_amka = "CG/CG_mogily/CG_mogily_amka.png"
image scene_mogily_fon = "CG/CG_mogily/CG_mogily_fon.png"

label scene_mogily:
    show scene_mogily_fon
    show scene_mogily_amka at soot_drift_bottom(speed=1.0, zoom=1.005, amplitude= -1, x_amplitude=1), truecenter
    show scene_mogily_herk at soot_drift_bottom(speed=0.5, zoom=1.005, amplitude= 1, x_amplitude=-1), truecenter
    with dissolve

    pause