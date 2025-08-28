image bg_coridor_fon = "CG/CG_koridor/CG_koridor_0004_fon.png"
image bg_coridor_cherkash = "CG/CG_koridor/CG_koridor_0000_cherkash.png"
image bg_coridor_teni_1 = "CG/CG_koridor/CG_koridor_0001_teni_1.png"

image bg_coridor_teni_2:
    "CG/CG_koridor/CG_koridor_0002_teni_2.png"
    anchor(0.5, 0.5)
    
image bg_coridor_figuri = "CG/CG_koridor/CG_koridor_0003_figuri.png"

label scene_coridor:
    scene bg_coridor_fon
    with dissolve
    show bg_coridor_figuri
    show bg_coridor_teni_1
    show bg_coridor_teni_2 at move_by_circle(0.5, 0.5, 10, 2.0, 0.0, True):
        pos (0.53, 0.52)
        alpha 0.5
    show bg_coridor_cherkash at soot_drift_bottom(zoom=1.01), truecenter
    with dissolve
    cutscene "Судя по широкой спине и уверенной походке, это был капитан."
    cutscene "Ирис убеждала не посвящать капитана, пока мы не поговорим с Виктором и не поймём, кто устроил этот кошмар."
    cutscene "И двигался он прямо в нашу сторону."
    cutscene "Мне необходимо было срочно принять решение."
    cutscene "Неизвестно, свернёт ли он куда-либо до того, как увидит нас, или пойдёт прямо."
    cutscene "Рисковать было нельзя: преждевременная встреча могла сорвать наш план."
    cutscene "Я проскочил в первое попавшееся помещение: дверь была рядом."
    cutscene "Врач и механик забежали следом."
    return