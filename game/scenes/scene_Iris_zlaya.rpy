image iris_zlaya_cherkash = "CG/CG_Iris_zlaya/Cherkash_3.png"

image iris_zlaya_cherkash_2 = "CG/CG_Iris_zlaya/Cherkash_4.png"

image iris_zlaya_glaza:
    "CG/CG_Iris_zlaya/Glaza_2.png"
    pos (0.5, 0.5)
    anchor (0.5, 0.5)

image iris_zlaya_iris = "CG/CG_Iris_zlaya/Iris_1.png"

transform crazy_shake(speed=0.2):
    zoom 1.0
    parallel:
        linear speed xoffset 0 yoffset 0
        linear speed xoffset -7 yoffset 4
        repeat
    parallel:
        pause 0.5
        linear speed*2 zoom 1.015
        linear speed*2 zoom 1.00
        repeat
            

label scene_Iris_zlaya:
    show iris_zlaya_iris
    show iris_zlaya_glaza at crazy_shake
    show iris_zlaya_cherkash at soot_drift_bottom(2, 1.01, -10)
    show iris_zlaya_cherkash_2 at soot_drift_bottom(2.0, 1.01, 10)
    pause
    return