image scene_shelk = "CG/CG_schelk/CG_schelk.png"
image scene_shelk_cherk_chelik = "CG/CG_schelk/CG_schelk_cherk_chelik.png"
image scene_shelk_hand = "CG/CG_schelk/CG_schelk_hand.png"

transform shelk_hand(speed=0.18, repeat_time=1):
    subpixel True
    xoffset 0
    yoffset 0
    parallel:
        easein_cubic speed yoffset 50
        pause speed*0.5
        easeout_cubic speed yoffset 0
        ease speed*0.08 yoffset 7
        ease speed*0.08 yoffset 0
        repeat repeat_time

label scene_shelk:
    show scene_shelk
    show scene_shelk_cherk_chelik
    show scene_shelk_hand at shelk_hand
    with dissolve

    pause

    show scene_shelk_hand at shelk_hand(repeat_time=2)

    pause
    return