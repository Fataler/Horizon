image scene_viktor_dal_ebu_bez_nozha = "CG/CG_Victor_dal_eby/Bez_nozha.png"
image scene_viktor_dal_ebu_cherkashi = "CG/CG_Victor_dal_eby/Cherkashi_1.png"
image scene_viktor_dal_ebu_fon = "CG/CG_Victor_dal_eby/fon.png"
image scene_viktor_dal_ebu_nozh = "CG/CG_Victor_dal_eby/Nozh.png"
image scene_viktor_dal_ebu_zrachki = "CG/CG_Victor_dal_eby/zrachki.png"

label scene_viktor_dal_ebu:
    show scene_viktor_dal_ebu_fon
    show scene_viktor_dal_ebu_bez_nozha
    show scene_viktor_dal_ebu_zrachki at soot_drift_bottom(0.5, 1), hand_shake(2)
    show scene_viktor_dal_ebu_cherkashi at soot_drift_bottom(1, 1.01)
    show scene_viktor_dal_ebu_nozh at hand_appear_from_bottom
    pause
    return