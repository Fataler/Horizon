image scene_photo_found_ryan = "CG/CG_Rayan_foto/1.png"
image scene_photo_found_tochk = "CG/CG_Rayan_foto/2.png"
image scene_photo_found_photo_full = "CG/CG_Rayan_foto/3.png"
image scene_photo_found_cherkash = "CG/CG_Rayan_foto/4.png"
image scene_photo_found_front_layer = "CG/CG_Rayan_foto/5.png"
image scene_photo_found_fon1 = "CG/CG_Rayan_foto/fon1.png"
image scene_photo_found_fon2 = "CG/CG_Rayan_foto/fon2.png"

layeredimage scene_photo_full:
    always:
        "CG/CG_Rayan_foto/fon1.png"
        #at appear()
    always:
        "CG/CG_Rayan_foto/fon2.png"
        at fade_in_out()
    

label scene_photo_found_cut:
    show scene_photo_full
    show scene_photo_found_ryan
    show scene_photo_found_tochk at soot_drift_bottom(zoom=1.05, speed=0.60, amplitude=-3, x_amplitude=-3, blink = True), truecenter:
        alpha 0.3
    show scene_photo_found_cherkash at soot_drift_bottom(zoom=1.05, speed=0.60, amplitude=3, x_amplitude=3, blink = True), truecenter
    with dissolve

    cutscene "Ч-что?.."
    cutscene "У меня в руке находилось фото моей девушки, оставшейся на Земле."
    cutscene "Это было единственное её фото, которое я взял с собой в полёт."
    play music2 music_nervous_ambient loop

    cutscene "В середине портрета красовалась приличная дыра."
    cutscene "Она была такой величины, что черты лица уже не удавалось разобрать."
    
    hide scene_photo_full
    with dissolve
    return

label scene_photo_found_full:
    show scene_photo_full
    show scene_photo_found_ryan
    show scene_photo_found_photo_full
    show scene_photo_found_tochk at soot_drift_bottom(zoom=1.05, speed=0.60, amplitude=3, x_amplitude=3, blink = True), truecenter:
        alpha 0.3
    show scene_photo_found_cherkash at soot_drift_bottom(zoom=1.05, speed=0.60, amplitude=-3, x_amplitude=-3, blink = True), truecenter
    with dissolve

    cutscene "Внутри не было никаких лекарств… Только фото. Это было фото… Моего близкого человека."
    cutscene "Как оно оказалось здесь. В сейфе Ирис?.."

    scene bg_black
    with dissolve
    return
