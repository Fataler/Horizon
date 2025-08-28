image scene_photo_found_ryan = "CG/CG_Rayan_foto/1.png"
image scene_photo_found_cherk = "CG/CG_Rayan_foto/2.png"
image scene_photo_found_photo_full = "CG/CG_Rayan_foto/3.png"
image scene_photo_found_pre_front_layer = "CG/CG_Rayan_foto/4.png"
image scene_photo_found_front_layer = "CG/CG_Rayan_foto/5.png"
image scene_photo_found_fon1 = "CG/CG_Rayan_foto/fon1.png"
image scene_photo_found_fon2 = "CG/CG_Rayan_foto/fon2.png"

layeredimage scene_photo_full:
    always:
        "CG/CG_Rayan_foto/1.png"
        at appear()
    always:
        "CG/CG_Rayan_foto/fon2.png"
        at fade_in_out()
    

label scene_photo_found_cut:
    show scene_photo_full
    with dissolve

    cutscene "Ч-что?.."
    cutscene "У меня в руке находилось фото моей девушки, оставшейся на Земле."
    cutscene "Это было единственное её фото, которое я взял с собой в полёт."
    cutscene "В середине портрета красовалась приличная дыра."
    cutscene "Она была такой величины, что черты лица по краям уже не удавалось разобрать."
    
    hide scene_photo_full
    with dissolve
    return

label scene_photo_found_full:
    show scene_photo_full
    with dissolve

    pause
    return
