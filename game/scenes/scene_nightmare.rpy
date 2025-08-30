image bg_white = Solid("#ffffff")
image menu_fon:
    "gui/menu/Menu_fon_red.png"

image menu_fon_2:
    "gui/menu/menu_black.png"
    zoom hand_zoom

image hand_1:
    "gui/menu/_0004_Hand-1.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_2:
    "gui/menu/_0005_Hand-2.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_3:
    "gui/menu/_0006_Hand-3.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_4:
    "gui/menu/_0007_Hand-4.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_5:
    "gui/menu/_0008_Hand-5.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_6:
    "gui/menu/_0009_Hand-6.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_7:
    "gui/menu/_0010_Hand-7.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_8:
    "gui/menu/_0011_Hand-8.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_9:
    "gui/menu/_0012_Hand-9.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_10:
    "gui/menu/_0013_Hand-10.png"
    zoom hand_zoom
    pos (0.2, 0)

image hand_11:
    "gui/menu/_0014_Hand-11.png"
    zoom hand_zoom
    pos (0.2, 0)

#image hand_12:
#    "gui/menu/_0015_Hand-12.png"
#    zoom hand_zoom
#    pos (0.2, 0)

image menu_gg:
    "gui/menu/menu_gg.png"
    pos (0.2, 0)

image menu_nimb:
    "gui/menu/menu_nimb.png"
    pos (0.2, 0)

transform hand_bob(up_time=6.0, down_time=5.0, distance=30, stretch=0.04, delay=0.0):
    yoffset -distance
    pause delay
    yzoom 1.0
    block:
        parallel:
            linear down_time / 3 yoffset -10
            linear up_time / 2 yoffset -distance
        parallel:
            linear down_time yzoom 1.0
            easeout_quad (up_time * 0.6) yzoom (1.0 + stretch)
            easein_quad (up_time * 0.4) yzoom 1.0
        repeat

screen not_main_menu(from_game_menu=False):
    add "menu_fon"

    add "menu_nimb" at transform:
        alpha 1.0
        linear 2.0 alpha 0.5
        linear 2.0 alpha 1.0
        repeat

    add "menu_gg"

    add "hand_1" at hand_bob(up_time=6.0, down_time=5.0, distance=20, stretch=0.03, delay=0.0)
    add "hand_2" at hand_bob(up_time=6.2, down_time=5.0, distance=22, stretch=0.03, delay=0.2)
    add "hand_3" at hand_bob(up_time=6.5, down_time=5.2, distance=24, stretch=0.035, delay=0.4)
    add "hand_4" at hand_bob(up_time=6.7, down_time=5.2, distance=26, stretch=0.035, delay=0.6)
    add "hand_5" at hand_bob(up_time=7.0, down_time=5.4, distance=18, stretch=0.04, delay=0.8)
    add "hand_6" at hand_bob(up_time=7.2, down_time=5.6, distance=25, stretch=0.04, delay=1.0)
    add "hand_7" at hand_bob(up_time=7.5, down_time=5.8, distance=27, stretch=0.045, delay=1.2)
    add "hand_8" at hand_bob(up_time=7.7, down_time=6.0, distance=20, stretch=0.045, delay=1.4)
    add "hand_9" at hand_bob(up_time=8.0, down_time=6.2, distance=31, stretch=0.05, delay=1.6)
    add "hand_10" at hand_bob(up_time=8.2, down_time=6.4, distance=38, stretch=0.05, delay=1.8)
    add "hand_11" at hand_bob(up_time=8.5, down_time=6.6, distance=20, stretch=0.055, delay=2.0)
#    add "hand_12" at hand_bob(up_time=8.8, down_time=6.8, distance=34, stretch=0.06, delay=2.2)

label scene_nightmare:
    show screen not_main_menu with dissolve
    pause
    return
