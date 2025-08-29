image scene_hand_needle_cherkash = At("CG/CG_ruka_igla/Cherkash.png", soot_drift_bottom(zoom=1.02, amplitude=-6, x_amplitude=3))
    
image scene_hand_needle_tochkash = At("CG/CG_ruka_igla/tochkash.png", soot_drift_bottom(zoom=1.02, amplitude=6, x_amplitude=-3))

image scene_hand_needle_ruka_krov = "CG/CG_ruka_igla/ruka_krov.png"
image scene_hand_needle_ruka_s_igloi = "CG/CG_ruka_igla/ruka_s_igloi.png"

transform infinite_shake(frequency=0.3, x_amplitude=10, y_amplitude=10, jitter=2):
    subpixel True
    parallel:
        block:
            easein_cubic frequency xoffset -x_amplitude
            easeout_cubic frequency xoffset x_amplitude
            repeat
    parallel:
        block:
            easein_cubic frequency yoffset -y_amplitude
            easeout_cubic frequency yoffset y_amplitude
            repeat
    parallel:
        block:
            pause frequency * 0.25
            linear 0.01 xoffset (renpy.random.randint(-jitter, jitter))
            linear 0.01 yoffset (renpy.random.randint(-jitter, jitter))
            linear 0.01 xoffset 0
            linear 0.01 yoffset 0
            repeat

label scene_hand_needle:
    show scene_hand_needle_ruka_krov
    show scene_hand_needle_ruka_s_igloi at infinite_shake(frequency=0.24, x_amplitude=0, y_amplitude=5, jitter=3):
        zoom 1.003
    show scene_hand_needle_tochkash:
        anchor(0.5, 0.5)
        pos(0.5, 0.5)
        alpha 0.3
    show scene_hand_needle_cherkash:
        anchor(0.5, 0.5)
        pos(0.5, 0.5)
    with dissolve

    cutscene "Я поднял руку к лицу и увидел, как кровь стекает по моей ладони."
    cutscene "В глазах потемнело."

    scene bg_black
    with dissolve
    return