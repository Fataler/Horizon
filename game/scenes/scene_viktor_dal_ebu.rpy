image scene_viktor_dal_ebu_bez_nozha = "CG/CG_Victor_dal_eby/Bez_nozha.png"
image scene_viktor_dal_ebu_cherkashi = "CG/CG_Victor_dal_eby/Cherkashi_1.png"
image scene_viktor_dal_ebu_fon = "CG/CG_Victor_dal_eby/fon.png"
image scene_viktor_dal_ebu_nozh = "CG/CG_Victor_dal_eby/Nozh.png"
image scene_viktor_dal_ebu_zrachki = "CG/CG_Victor_dal_eby/zrachki.png"

label scene_viktor_dal_ebu:
    show scene_viktor_dal_ebu_fon
    show scene_viktor_dal_ebu_bez_nozha
    show scene_viktor_dal_ebu_zrachki at infinite_shake(frequency=0.5, x_amplitude=5, y_amplitude=1.0, jitter=1), truecenter
    show scene_viktor_dal_ebu_cherkashi at soot_drift_bottom(speed=1.0, amplitude=2, x_amplitude=2, zoom=1.01), truecenter
    with dissolve
    cutscene "Виктор сидел, сжавшись, у панели калибровки двигателя."
    
    show scene_viktor_dal_ebu_nozh at hand_appear_from_bottom
    with dissolve
    cutscene "Лицо его выражало полное безумие."
    cutscene "Одежда пропитана кровью."

    hide scene_viktor_dal_ebu_fon
    hide scene_viktor_dal_ebu_bez_nozha
    hide scene_viktor_dal_ebu_zrachki
    hide scene_viktor_dal_ebu_cherkashi
    hide scene_viktor_dal_ebu_nozh
    with dissolve
    return