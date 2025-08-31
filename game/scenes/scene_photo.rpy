image scene_photo_tear_1 = Transform("CG/CG_foto/_0000_Tear_1.png", zoom=1.1)
image scene_photo_tear_2 = Transform("CG/CG_foto/_0001_Tear_2.png", zoom=1.1)
image scene_photo_tear_3 = Transform("CG/CG_foto/_0002_Tear_3.png", zoom=1.1)
image scene_photo_tear_4 = Transform("CG/CG_foto/_0003_Tear_4.png", zoom=1.1)
image scene_photo_tear_5 = Transform("CG/CG_foto/_0004_Tear_5.png", zoom=1.1)
image scene_photo_tear_6 = Transform("CG/CG_foto/_0005_Tear_6.png", zoom=1.1)

image scene_photo_fon = "CG/CG_foto/_0010_fon.png"
image scene_photo_hand_1 ="CG/CG_foto/_0006_Hand_1.png"
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
        linear 0.1 xoffset -1
        linear 0.1 xoffset 1
        repeat

transform tear_shake():
    linear 0.1 xoffset -1
    linear 0.1 xoffset 1
    repeat

transform r_hand_shake:
    linear 0.1 xoffset 1
    linear 0.1 xoffset -1
    repeat

label scene_photo:

    show scene_photo_fon
    show scene_photo_cherkashi at soot_drift_bottom(2, 1.1), truecenter
    show scene_photo_light_for_scale at fade_in_out(1.0)

    show scene_photo_hand_2 at hand_appear_from_bottom

    pause 0.5
    
    
    show scene_photo_hand_1 at hand_appear_from_bottom
    
    cutscene "Фото моей семьи."


    show scene_photo_tear_2 at tear_shake
    with dissolve

    pause 0.5
    show scene_photo_tear_1 at tear_shake
    hide scene_photo_tear_2
    with dissolve

    
    cutscene "Дедушка, брат, тётя. Сестрёнка…"

    
    show scene_photo_tear_4 at tear_shake
    with dissolve

    pause 0.5
    show scene_photo_tear_3 at tear_shake
    hide scene_photo_tear_4
    with dissolve

    cutscene "Теперь я понимаю."
    
    show scene_photo_tear_6 at tear_shake
    with dissolve

    pause 0.5
    show scene_photo_tear_5 at tear_shake
    hide scene_photo_tear_6
    with dissolve

    cutscene "Они все остались на Земле."
    cutscene "У моей смерти было много лиц, но все они были мои."
    
    scene bg_black with dissolve
    return