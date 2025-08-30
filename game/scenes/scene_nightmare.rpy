image menu_fon:
    "gui/menu/Menu_fon_red.png"

screen not_main_menu(from_game_menu=False):
    add "menu_fon" 
    add "iris_zlaya_cherkash" at soot_drift_bottom(2, 1.01, -10):
        zoom 1.05
        pos (0, -0.05)
    add "menu_nimb" at transform:
        pos (0.2, 0)
        alpha 1.0
        linear 2.0 alpha 0.5
        linear 2.0 alpha 1.0
        repeat

    add "menu_gg":
        pos (0.2, 0)

    add "hand_1" at hand_bob(up_time=6.0, down_time=5.0, distance=20, stretch=0.03, delay=0.0):
        pos (0.2, 0)
        zoom 1.02
    add "hand_2" at hand_bob(up_time=6.2, down_time=5.0, distance=22, stretch=0.03, delay=0.2):
        pos (0.2, 0)
        zoom 1.02
    add "hand_3" at hand_bob(up_time=6.5, down_time=5.2, distance=24, stretch=0.035, delay=0.4):
        pos (0.2, 0)
        zoom 1.02
    add "hand_4" at hand_bob(up_time=6.7, down_time=5.2, distance=26, stretch=0.035, delay=0.6):
        pos (0.2, 0)
        zoom 1.02
    add "hand_5" at hand_bob(up_time=7.0, down_time=5.4, distance=18, stretch=0.04, delay=0.8):
        pos (0.2, 0)
        zoom 1.02
    add "hand_6" at hand_bob(up_time=7.2, down_time=5.6, distance=25, stretch=0.04, delay=1.0):
        pos (0.2, 0)
        zoom 1.02
    add "hand_7" at hand_bob(up_time=7.5, down_time=5.8, distance=27, stretch=0.045, delay=1.2):
        pos (0.2, 0)
        zoom 1.02
    add "hand_8" at hand_bob(up_time=7.7, down_time=6.0, distance=20, stretch=0.045, delay=1.4):
        pos (0.2, 0)
        zoom 1.02
    add "hand_9" at hand_bob(up_time=8.0, down_time=6.2, distance=31, stretch=0.05, delay=1.6):
        pos (0.2, 0)
        zoom 1.02
    add "hand_10" at hand_bob(up_time=8.2, down_time=6.4, distance=38, stretch=0.05, delay=1.8):
        pos (0.2, 0)
        zoom 1.02
    add "hand_11" at hand_bob(up_time=8.5, down_time=6.6, distance=20, stretch=0.055, delay=2.0):
        pos (0.2, 0)
        zoom 1.02
#    add "hand_12" at hand_bob(up_time=8.8, down_time=6.8, distance=34, stretch=0.06, delay=2.2)

label scene_nightmare:
    show screen not_main_menu with dissolve
    pause
    return
