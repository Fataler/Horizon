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
    
    window hide
    show scene_shelk
    show scene_shelk_cherk_chelik
    show scene_shelk_hand at shelk_hand
    with dissolve

    cutscene "Щёлк."
    show scene_shelk_hand at shelk_hand

    play sfx sfx_click2
    pause 0.2
    play sfx sfx_click2

    cutscene "Щёлк-щёлк."
    
    #show scene_shelk_hand at shelk_hand(repeat_time=2)

    #цг гг лицом в экран

    cutscene "Фух, вроде работает."
    cutscene "Ну и ну."
    cutscene "Запишу в следующем докладе, что у нас неполадки с основным генератором."
    return