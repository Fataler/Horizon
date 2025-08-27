image bg_coridor_fon = "CG/CG_koridor/CG_koridor_0004_fon.png"
image bg_coridor_cherkash = "CG/CG_koridor/CG_koridor_0000_cherkash.png"
image bg_coridor_teni_1 = "CG/CG_koridor/CG_koridor_0001_teni_1.png"

image bg_coridor_teni_2:
    "CG/CG_koridor/CG_koridor_0002_teni_2.png"
    anchor(0.5, 0.5)
    
image bg_coridor_figuri = "CG/CG_koridor/CG_koridor_0003_figuri.png"

label scene_coridor:
    scene bg_coridor_fon
    show bg_coridor_figuri
    
    show bg_coridor_teni_1
    show bg_coridor_teni_2 at move_by_circle(0.5, 0.5, 10, 2.0, 0.0, True):
        pos (0.53, 0.52)
    show bg_coridor_cherkash at soot_drift_bottom()
    pause
    return