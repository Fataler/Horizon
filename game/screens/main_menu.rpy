## Экран главного меню
init:
    image bg_white = Solid("#ffffff")

    image guys_shadow:
        "gui/menu/guys_shadow.png"

    image gg:
        "gui/menu/gg.png"
    
    image umi:
        "gui/menu/umi.png"

    image hikaru:
        "gui/menu/hikaru.png"
    
    image kazumi:
        "gui/menu/kazumi.png"

    image denis:
        "gui/menu/den.png"

    image gg_shadow:
        "gui/menu/Shadow_Taida_Dzindzo.png"

    image umi_shadow:
        "gui/menu/Shadow_Umi.png"

    image hikaru_shadow:
        "gui/menu/Shadow_Hikaru.png"
    
    image kazumi_shadow:
        "gui/menu/Shadow_Kazumi.png"

    image den_shadow:
        "gui/menu/Shadow_Den.png"

    image gg_chirkash:
        "gui/menu/Chirkash_Taida_Dzindzo_1.png"
        pause 0.1
        "gui/menu/Chirkash_Taida_Dzindzo_2.png"
        pause 0.1
        "gui/menu/Chirkash_Taida_Dzindzo_3.png"
        repeat
    
    image umi_chirkash:
        "gui/menu/Chirkash_Umi_1.png"
        pause 0.1
        "gui/menu/Chirkash_Umi_2.png"
        pause 0.1
        "gui/menu/Chirkash_Umi_3.png"
        repeat

    image hikaru_chirkash:
        "gui/menu/Chirkash_Hikaru_1.png"
        pause 0.1
        "gui/menu/Chirkash_Hikaru_2.png"
        pause 0.1
        "gui/menu/Chirkash_Hikaru_3.png"
        repeat
    
    image kazumi_chirkash:
        "gui/menu/Chirkash_Kazumi_1.png"
        pause 0.1
        "gui/menu/Chirkash_Kazumi_2.png"
        pause 0.1
        "gui/menu/Chirkash_Kazumi_3.png"
        repeat

    image den_chirkash:
        "gui/menu/Chirkashi_Den_1.png"
        pause 0.1
        "gui/menu/Chirkashi_Den_2.png"
        pause 0.1
        "gui/menu/Chirkashi_Den_3.png"
        repeat

transform hue_cycle:
        matrixcolor HueMatrix(0)
        linear 10.0 matrixcolor HueMatrix(360)
        repeat

transform parametric_appear(delay=0.5):
    alpha 0
    pause delay
    linear 0.3 alpha 1

screen main_menu():
    tag menu

    add "bg_menu_main"

    add Parallax("gui/menu/logo.png", 0.1):
        anchor (0.5, 0.5)
        xpos 450
        ypos 310

    add Parallax("guys_shadow", 0.5) at hue_cycle:
        anchor (0.5, 0.5)
        xpos 1140
        ypos 590
    
    add Parallax("umi", 0.6):
        anchor (0.5, 0.5)
        xpos 1368
        ypos 688
    
    add Parallax("hikaru", 0.6):
        anchor (0.5, 0.5)
        xpos 959
        ypos 641
    
    add Parallax("gg", 0.9):
        anchor (0.5, 0.5)
        xpos 1168
        ypos 599

    add Parallax("kazumi", 1.1):
        anchor (0.5, 0.5)
        xpos 840
        ypos 804
    
    add Parallax("denis", 1.2):
        anchor (0.5, 0.5)
        xpos 1370
        ypos 762

    imagebutton:
        idle Transform("avatar_circle", size=(160, 160))
        action OpenURL('https://t.me/viendesu_official')
        anchor (0.5, 0.5)
        xpos 0.09
        ypos 0.87
        at hover_scale

    #vbox at menu_items_appear:
    style_prefix "main_menu"

    #spacing gui.navigation_spacing
    
    textbutton _("Начать") action Start():
        xpos 1209
        ypos 173
        text_size 90

    textbutton _("Загрузить") action ShowMenu("load"):
        xpos 646
        ypos 559
        text_size 55
        
    
    textbutton _("Достижения") action ShowMenu("achievements_screen"):
        xpos 537
        ypos 749
        text_size 55

    textbutton _("Настройки") action ShowMenu("preferences"):
        xpos 1666
        ypos 344
        text_size 55

    textbutton _("Об игре") action [ShowMenu("about")]: #Function(unlock_achievement, THANK_YOU),
        xpos 1702
        ypos 699
        text_size 55

    if renpy.variant("pc"):
        textbutton _("Выход") action Quit(confirm=not main_menu):
            xpos 440
            ypos 999
            text_size 50

    if show_main_menu_fade:
        add "bg_paper" at menu_alpha_out(1)
        timer 1 action SetVariable("show_main_menu_fade", False)

style main_menu_button:
    anchor (0.5, 0.5)
    properties gui.button_properties("main_menu")

style main_menu_button_text is gui_button_text

style main_menu_button_text:
    properties gui.text_properties("main_menu")
    color gui.interface_text_color
    hover_color gui.hover_color
    size 80
    xalign 0.5
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
