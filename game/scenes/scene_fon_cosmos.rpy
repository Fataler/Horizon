image scene_fon_cosmos_1 = "CG/CG_fon_cosmos/CG_fon_cosmos_0000s_0000_1_1.png"
image scene_fon_cosmos_2 = "CG/CG_fon_cosmos/CG_fon_cosmos_0000s_0001_1_2.png"
image scene_fon_cosmos_3 = "CG/CG_fon_cosmos/CG_fon_cosmos_0001s_0000_2_1.png"
image scene_fon_cosmos_4 = "CG/CG_fon_cosmos/CG_fon_cosmos_0001s_0001_2_2.png"
image scene_fon_cosmos_5 = "CG/CG_fon_cosmos/CG_fon_cosmos_0002s_0000_3_1.png"
image scene_fon_cosmos_6 = "CG/CG_fon_cosmos/CG_fon_cosmos_0002s_0001_3_2.png"
image scene_fon_cosmos_cosmos1 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0000_cosmos1.png"
image scene_fon_cosmos_cosmos2 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0001_cosmos2.png"
image scene_fon_cosmos_cosmos3 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0002_cosmos3.png"
image scene_fon_cosmos_cosmos4 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0003_cosmos4.png"
image scene_fon_cosmos_cosmos5 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0004_cosmos5.png"
image scene_fon_cosmos_cosmos6 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0005_cosmos6.png"
image scene_fon_cosmos_cosmos7 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0006_cosmos7.png"
image scene_fon_cosmos_cosmos8 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0007_cosmos8.png"
image scene_fon_cosmos_cosmos9 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0008_cosmos9.png"
image scene_fon_cosmos_cosmos10 = "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0009_cosmos10.png"

transform stars_twinkle:
    subpixel True
    parallel:
        block:
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            repeat
    parallel:
        block:
            linear 0.3 zoom 1.05
            linear 0.3 zoom 1.0
            repeat

transform nebula_drift:
    subpixel True
    parallel:
        block:
            easein 4.0 xoffset 10
            easeout 4.0 xoffset -10
            repeat
    parallel:
        block:
            linear 0.8 alpha 0.6
            linear 0.8 alpha 1.0
            repeat

transform deep_space_move:
    subpixel True
    parallel:
        block:
            linear 6.0 yoffset 5
            linear 6.0 yoffset -5
            repeat
    parallel:
        block:
            linear 0.4 alpha 0.8
            linear 0.4 alpha 1.0
            repeat

layeredimage scene_fon_cosmos_image:
    always:
        "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0010_cosmos11.png"
        at deep_space_move
    always:
        image:
            "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0011_cosmos12.png"
            pause 0.1
            "CG/CG_fon_cosmos/CG_fon_cosmos_0012s_0010_cosmos11.png"
            pause 0.1
            repeat
        at stars_twinkle
    always:
        "CG/CG_fon_cosmos/CG_fon_cosmos_0003s_0000_4_1.png"
        at nebula_drift
    always:
        "CG/CG_fon_cosmos/CG_fon_cosmos_0003s_0001_4_2.png"
        at nebula_drift
    always:
        "CG/CG_fon_cosmos/CG_fon_cosmos_0004s_0000_5_1.png"
        at deep_space_move
    always:
        "CG/CG_fon_cosmos/CG_fon_cosmos_0004s_0001_5_2.png"
        at stars_twinkle
    always:
        "CG/CG_fon_cosmos/CG_fon_cosmos_0005s_0000_6_1.png"
        at nebula_drift
    always:
        "CG/CG_fon_cosmos/CG_fon_cosmos_0005s_0001_6_2.png"
        at nebula_drift

label scene_fon_cosmos:
    show scene_fon_cosmos_image:
        pos(0.0, 0.0)

    with dissolve
    pause
    return
