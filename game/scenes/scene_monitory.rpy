image monitory_cherkash = "CG/CG_monitory_GG/CG_monitory_GG_0001_cherkashi.png"

image monitory_glaza:
    "CG/CG_monitory_GG/CG_monitory_GG_0000_glaza.png"
    pos (0.5, 0.5)
    anchor (0.5, 0.5)

image monitory_GG1 = "CG/CG_monitory_GG/CG_monitory_GG_0002_fon1.png"
image monitory_GG2 = "CG/CG_monitory_GG/CG_monitory_GG_0003_fon2.png"

transform crazy_shake(speed=0.2):
    zoom 1.0
    parallel:
        linear speed xoffset 0 yoffset 0
        linear speed xoffset -7 yoffset 4
        repeat
    parallel:
        pause 0.5
        linear speed*2 zoom 1.015
        linear speed*2 zoom 1.00
        repeat
            
image monitor_flicker:
    "monitory_GG1"
    0.08
    "monitory_GG2"
    0.06
    repeat

label scene_monitory:
    show monitor_flicker
    show monitory_glaza at crazy_shake
    show monitory_cherkash at soot_drift_bottom(2, 1.01, -10)
    pause
    return