image scene_dom_fon = "CG/CG_dom/CG_dom_fon.png"
image scene_dom_fleks = "CG/CG_dom/CG_dom_fleks.png"
image scene_dom_shmeks = "CG/CG_dom/CG_dom_shmeks.png"

label scene_dom:
    show scene_dom_fon
    show scene_dom_fleks at soot_drift_bottom(speed=0.7, zoom=1.001, amplitude=1, x_amplitude=1), truecenter
    show scene_dom_shmeks at soot_drift_bottom(speed=0.9, zoom=1.001, amplitude=2, x_amplitude=-1), truecenter
    with dissolve

    pause
    return
