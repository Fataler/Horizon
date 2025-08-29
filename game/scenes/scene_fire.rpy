#region transforms
transform scene_fire_bg_heat:
    subpixel True
    parallel:
        block:
            easein 1.2 zoom 1.01
            easeout 1.2 zoom 1.00
            repeat
    parallel:
        block:
            linear 0.9 blur 0.8
            linear 0.9 blur 0.0
            repeat

transform scene_fire_flame_flicker:
    subpixel True
    parallel:
        block:
            linear 0.20 yoffset -3
            linear 0.18 yoffset 0
            repeat
    parallel:
        block:
            linear 0.22 alpha 0.95
            linear 0.18 alpha 1.00
            repeat

transform scene_fire_burn_wave:
    subpixel True
    parallel:
        block:
            easein 0.35 zoom 1.02
            easeout 0.30 zoom 1.00
            repeat
    parallel:
        block:
            linear 0.26 xoffset -2
            linear 0.22 xoffset 0
            repeat

transform soot_drift_bottom(speed=0.60, zoom=1.0, amplitude=6, x_amplitude=0, blink = True):
    subpixel True
    zoom zoom
    parallel:
        block:
            easein_cubic speed yoffset -amplitude
            easeout_cubic speed yoffset 0
            easein_cubic speed yoffset amplitude
            easeout_cubic speed yoffset 0
            repeat
    parallel:
        block:
            linear speed xoffset x_amplitude
            linear speed xoffset -x_amplitude
            linear speed xoffset 0
            repeat
    parallel:
        block:
            linear 0.40 alpha (0.90 if blink else 1.00)
            linear 0.60 alpha (1.00 if blink else 1.00)
            linear 0.30 alpha (0.95 if blink else 1.00)
            linear 0.40 alpha (1.00 if blink else 1.00)
            repeat

transform soot_drift_top:
    subpixel True
    parallel:
        block:
            linear 0.70 xoffset 4
            linear 0.70 xoffset 0
            repeat
    parallel:
        block:
            linear 0.45 alpha 0.90
            linear 0.45 alpha 1.00
            repeat
#endregion

layeredimage scene_fire_image:
    always:
        "CG/CG_fire/_0007_fon.png"  
        at scene_fire_bg_heat
    always:
        image:
            "CG/CG_fire/chely.png"
    always:
        image:
            "CG/CG_fire/fire_1.png"
            pause 0.2
            "CG/CG_fire/fire_2.png" 
            pause 0.2
            repeat
        at scene_fire_flame_flicker
    always:
        image:
            "CG/CG_fire/fire_burn_1.png"
            pause 0.2
            "CG/CG_fire/fire_burn_2.png" 
            pause 0.2
            repeat
        at scene_fire_burn_wave
    always:
        "CG/CG_fire/Cherkashi_nizhnie.png"
        at soot_drift_bottom
    always:
        "CG/CG_fire/Cherkashi_verhnie.png"
        at soot_drift_top

label scene_fire:
    show scene_fire_image:
        pos(0.0, 0.0)

    with dissolve
    pause
    return