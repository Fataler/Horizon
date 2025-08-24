image scene_photo_tear_1 = "CG/CG_foto/_0000_Tear_1.png"
image scene_photo_tear_2 = "CG/CG_foto/_0001_Tear_2.png"
image scene_photo_tear_3 = "CG/CG_foto/_0002_Tear_3.png"
image scene_photo_tear_4 = "CG/CG_foto/_0003_Tear_4.png"
image scene_photo_tear_5 = "CG/CG_foto/_0004_Tear_5.png"
image scene_photo_tear_6 = "CG/CG_foto/_0005_Tear_6.png"

image scene_photo_fon = "CG/CG_foto/_0010_fon.png"
image scene_photo_hand_1 = "CG/CG_foto/_0006_Hand_1.png"
image scene_photo_hand_2 = "CG/CG_foto/_0007_Hand_2.png"
image scene_photo_light_for_scale = "CG/CG_foto/_0008_light_for_scale.png"
image scene_photo_cherkashi = "CG/CG_foto/_0009_cherkashi.png"

transform hand_appear_from_bottom:
    subpixel True
    zoom 1.1
    ypos 500
    alpha 0.0
    
    parallel:
        easein 1.0 ypos 0 alpha 1.0
        
    parallel:
        linear 0.1 xoffset - 1
        linear 0.1 xoffset 1
        repeat

transform hand_shake(amplitude=1):
    linear 0.1 xoffset - amplitude
    linear 0.1 xoffset amplitude
    repeat

transform r_hand_shake:
    linear 0.1 xoffset 1
    linear 0.1 xoffset -1
    repeat

label scene_photo:
    show scene_photo_fon
    show scene_photo_cherkashi at soot_drift_bottom(2, 1.1)
    show scene_photo_light_for_scale at fade_in_out(1.0)
    show scene_photo_hand_2 at hand_appear_from_bottom

    "Так же, там было её фото"
    show scene_photo_hand_1 at hand_appear_from_bottom

    show scene_photo_tear_1 at hand_shake
    with dissolve
    "Плак"
    
    show scene_photo_tear_2 at hand_shake
    hide scene_photo_tear_1
    with dissolve
    "Плак"
    show scene_photo_tear_3 at hand_shake
    with dissolve
    "Плак"
    show scene_photo_tear_4 at hand_shake
    hide scene_photo_tear_3
    with dissolve
    "Плак"
    show scene_photo_tear_5 at hand_shake
    with dissolve
    "Плак"
    show scene_photo_tear_6 at hand_shake
    hide scene_photo_tear_5
    with dissolve
    "Плак"
    pause
    return