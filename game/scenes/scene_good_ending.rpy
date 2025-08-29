image scene_good_ending_chely = "CG/CG_good_ending/CG_good_ending_chely.png"
image scene_good_ending_dom = "CG/CG_good_ending/CG_good_ending_dom.png"
image scene_good_ending_doroga = "CG/CG_good_ending/CG_good_ending_doroga.png"
image scene_good_ending_effecty = "CG/CG_good_ending/CG_good_ending_effecty.png"
image scene_good_ending_mogoly = "CG/CG_good_ending/CG_good_ending_mogoly.png"
image scene_good_ending_ramka = "CG/CG_good_ending/CG_good_ending_ramka.png"
image scene_good_ending_trava = "CG/CG_good_ending/CG_good_ending_0006_trava.png"

transform gentle_wind:
    subpixel True
    parallel:
        block:
            easein 3.0 xoffset 5
            easeout 3.0 xoffset 0
            repeat

transform cloud_move:
    subpixel True
    parallel:
        block:
            linear 8.0 xoffset 20
            linear 8.0 xoffset -20
            repeat
    parallel:
        block:
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            repeat

label scene_good_ending:
    show scene_good_ending_mogoly at soot_drift_bottom(speed=0.3, amplitude=1, x_amplitude=0), truecenter zorder 7
    show scene_good_ending_chely at gentle_wind zorder 8
    show scene_good_ending_effecty at soot_drift_bottom() zorder 9:
        alpha 0.5
    show scene_good_ending_ramka zorder 10
    with dissolve
    pause

    
    hide scene_good_ending_mogoly
    show scene_good_ending_doroga at soot_drift_bottom(speed=0.3, amplitude=1, x_amplitude=0), truecenter
    with dissolve
    pause
    hide scene_good_ending_doroga
    show scene_good_ending_trava at gentle_wind, soot_drift_bottom(speed=0.3, amplitude=1, x_amplitude=0), truecenter
    with dissolve
    pause
    hide scene_good_ending_trava
    show scene_good_ending_dom at soot_drift_bottom(speed=0.3, amplitude=1, x_amplitude=0), truecenter
    with dissolve
    pause

    return

label scene_good_ending_doroga:
    show scene_good_ending_chely at gentle_wind zorder 8
    show scene_good_ending_effecty at soot_drift_bottom() zorder 9:
        alpha 0.5
    show scene_good_ending_ramka zorder 10
    show scene_good_ending_doroga at soot_drift_bottom(speed=0.3, amplitude=1, x_amplitude=0), truecenter
    with dissolve
    pause

    return
