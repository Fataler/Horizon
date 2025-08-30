image scene_buket_mogila_fon = "CG/CG_Buket_mogila/fon.png"
image scene_buket_mogila_buket = "CG/CG_Buket_mogila/buket.png"

label scene_buket_mogila:
    play music music_sad fadein 1.0 loop
    show scene_buket_mogila_fon
    show scene_buket_mogila_buket at y_offset_appear(-100, 0.0, 1.0)
    with dissolve

    pause
    stop music fadeout 1.0
    return

