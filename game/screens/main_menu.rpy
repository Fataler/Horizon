## Экран главного меню
init:
    default hand_zoom = 1.03

    image logo_anim:
        choice 6:
            "gui/menu/Logo 1.png"
            pause 0.5
        choice 4:
            "gui/menu/Logo 1.png"
            pause 0.3
        choice 2:
            "gui/menu/Logo 1_2.png"
            pause 0.04
            "gui/menu/Logo 1.png"
            pause 0.18
        choice 2:
            "gui/menu/Logo 1_3.png"
            pause 0.03
            "gui/menu/Logo 1_2.png"
            pause 0.03
            "gui/menu/Logo 1.png"
            pause 0.2
        choice 1:
            "gui/menu/Logo 1_4.png"
            pause 0.02
            "gui/menu/Logo 1_2.png"
            pause 0.02
            "gui/menu/Logo 1_3.png"
            pause 0.02
            "gui/menu/Logo 1.png"
            pause 0.25
        repeat

    image bg_white = Solid("#ffffff")
    image menu_fon:
        "gui/menu/Menu_fon_prozrachni.png"
        zoom 1.05
    
    image menu_fon_2:
        "gui/menu/menu_black.png"
        zoom hand_zoom
    
    image hand_1:
        "gui/menu/_0004_Hand-1.png"
        zoom hand_zoom

    image hand_2:
        "gui/menu/_0005_Hand-2.png"
        zoom hand_zoom

    image hand_3:
        "gui/menu/_0006_Hand-3.png"
        zoom hand_zoom

    image hand_4:
        "gui/menu/_0007_Hand-4.png"
        zoom hand_zoom

    image hand_5:
        "gui/menu/_0008_Hand-5.png"
        zoom hand_zoom

    image hand_6:
        "gui/menu/_0009_Hand-6.png"
        zoom hand_zoom

    image hand_7:
        "gui/menu/_0010_Hand-7.png"
        zoom hand_zoom

    image hand_8:
        "gui/menu/_0011_Hand-8.png"
        zoom hand_zoom

    image hand_9:
        "gui/menu/_0012_Hand-9.png"
        zoom hand_zoom

    image hand_10:
        "gui/menu/_0013_Hand-10.png"
        zoom hand_zoom

    image hand_11:
        "gui/menu/_0014_Hand-11.png"
        zoom hand_zoom

    image hand_12:
        "gui/menu/_0015_Hand-12.png"
        zoom hand_zoom

    image menu_gg:
        "gui/menu/menu_gg.png"
        zoom hand_zoom

    image menu_nimb:
        "gui/menu/menu_nimb.png"
        zoom hand_zoom
        
transform hue_cycle:
        matrixcolor HueMatrix(0)
        linear 10.0 matrixcolor HueMatrix(360)
        repeat

screen main_menu():
    tag menu

    add Parallax("menu_fon", 0.5)
    add Parallax("menu_fon_2", 0.5)

    add Parallax("menu_nimb", 1) at transform:
        alpha 1.0
        linear 2.0 alpha 0.5
        linear 2.0 alpha 1.0
        repeat

    add Parallax("menu_gg", 0.5)

    add Parallax("hand_1", 0.55)
    add Parallax("hand_2", 0.6)
    add Parallax("hand_3", 0.65)
    add Parallax("hand_4", 0.7)
    add Parallax("hand_5", 0.75)
    add Parallax("hand_6", 0.85)
    add Parallax("hand_7", 0.95)
    add Parallax("hand_8", 1.05)
    add Parallax("hand_9", 1.15)
    add Parallax("hand_10", 1.25)
    add Parallax("hand_11", 1.35)
    add Parallax("hand_12", 1.45)

    add Parallax("logo_anim", 0):
        pos (1400, 570)
        anchor (0.5, 0.5)

    # imagebutton:
    #     idle Transform("avatar_circle", size=(160, 160))
    #     action OpenURL('https://t.me/viendesu_official')
    #     anchor (0.5, 0.5)
    #     xpos 0.09
    #     ypos 0.87
    #     at hover_scale

    style_prefix "main_menu"

    vbox at delay_appear(0):
        spacing 10
        anchor (0.5, 1.3)
        xpos 2150
    
        textbutton _("Начать") action Start():
            text_size 90

        textbutton _("Загрузить") action ShowMenu("load"):
            text_size 55
            
        
        textbutton _("Достижения") action ShowMenu("achievements_screen"):
            text_size 55

        textbutton _("Настройки") action ShowMenu("preferences"):
            text_size 55

        textbutton _("Об игре") action [ShowMenu("about")]: #Function(unlock_achievement, THANK_YOU),
            text_size 55

        if renpy.variant("pc"):
            textbutton _("Выход") action Quit(confirm=not main_menu):
                text_size 50

    if show_main_menu_fade:
        add "bg_black" at menu_alpha_out(1)
        timer 1 action SetVariable("show_main_menu_fade", False)

style main_menu_button:
    xfill True
    properties gui.button_properties("main_menu")

style main_menu_button_text is gui_button_text

style main_menu_button_text:
    properties gui.text_properties("main_menu")
    color gui.interface_text_color
    hover_color gui.hover_color
    text_align 0.0
    xalign 0.0
    font gui.interface_text_font

style main_menu_vbox is vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text is gui_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title is main_menu_text:
    properties gui.text_properties("title")

style main_menu_version is main_menu_text:
    properties gui.text_properties("version")

transform hover_scale:
    anchor (0.5, 0.5)
    rotate 0
    on idle:    
        parallel:
            linear 0.1 xzoom 1.0 yzoom 1.0
    on hover:
        parallel:
            linear 0.1 xzoom 1.1 yzoom 1.1

transform menu_alpha_out(time=0.5):
    alpha 1
    linear time alpha 0

transform alpha_in(time=0.5):
    alpha 0
    linear time alpha 1

transform alpha_out(time=0.5):
    alpha 1
    linear time alpha 0
