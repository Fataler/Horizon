################################################################################
## Экран паузы
################################################################################

init -2:
    $_game_menu_screen = "pause_menu"

default pause_character_counter = 0

init python:
    def next_pause_character():
        global pause_character_counter
        pause_character_counter = pause_character_counter % 5 + 1

screen pause_menu():
    on "show" action Function(next_pause_character)

    modal True

    add "bg_menu_main" at menu_board_drop

    add Parallax("gui/menu/logo.png", 0.1):
        anchor (0.5, 0.5)
        xpos 400
        ypos 500
        zoom 0.8

    frame:
        style_prefix "pause_menu"
        background None #"#00000080"
        at menu_board_drop
        xanchor 0.5
        xpos 0.5

        # Кнопки меню
        vbox at pause_menu_items_appear:
            spacing 30
            #xpos 0
            #ypos 210
            xalign 0.5
            yalign 0.5

            text "ПАУЗА" size 60 xalign 0.5 color gui.accent_color style "pause_menu_button_text"
            
            textbutton _("Сохранить") action [Hide("pause_menu"), ShowMenu("save")]
            textbutton _("Загрузить") action [Hide("pause_menu"), ShowMenu("load")]
            textbutton _("История") action [Hide("pause_menu"), ShowMenu("history")]
            textbutton _("Настройки") action [Hide("pause_menu"), ShowMenu("preferences")]
            textbutton _("Главное меню") action MainMenu()
            textbutton _("Вернуться") action Return()
           
    if pause_character_counter == 1:
        add "gg_shadow":
            anchor (0.5, 0.5)   
            pos (1555, 565)
            at delay_appear(0.3)
        
        add Parallax("gg", 0.2):
            anchor (0.5, 0.5)
            at move_appear(1370, 695, 1558)

        add "gg_chirkash":
            anchor (0.5, 0.5)  
            pos (1565, 535)
            at delay_appear(0.3)
    elif pause_character_counter == 2:
        add "den_shadow":
            anchor (0.5, 0.5)   
            pos (1590, 530)
            at delay_appear(0.3)

        add Parallax("denis", 0.2):
            anchor (0.5, 0.5)
            at move_appear(1370,762, 1548)

        add "den_chirkash":
            anchor (0.5, 0.5)  
            pos (1590, 530)
            at delay_appear(0.3)
    elif pause_character_counter == 3:
        add "hikaru_shadow":
            anchor (0.5, 0.5)   
            pos (1600, 535)
            at delay_appear(0.3)

        add Parallax("hikaru", 0.2):
            anchor (0.5, 0.5)
            at move_appear(1380, 700)

        add "hikaru_chirkash":
            anchor (0.5, 0.5)  
            pos (1600, 535)
            at delay_appear(0.3)
    elif pause_character_counter == 4:
        add "kazumi_shadow":
            anchor (0.5, 0.5)   
            pos (1605, 540)
            at delay_appear(0.3)

        add Parallax("kazumi", 0.2):
            anchor (0.5, 0.5)
            at move_appear(1375, 690)

        add "kazumi_chirkash":
            anchor (0.5, 0.5)  
            pos (1605, 540)
            at delay_appear(0.3)
    elif pause_character_counter == 5:
        add "umi_shadow":
            anchor (0.5, 0.5)   
            pos (1610, 540)
            at delay_appear(0.3)

        add Parallax("umi", 0.2):
            anchor (0.5, 0.5)        
            at move_appear(1368, 688)

        add "umi_chirkash":
            anchor (0.5, 0.5)  
            pos (1610, 540)
            at delay_appear(0.3)

style pause_menu_button is main_menu_button:
    xalign 0.5
    yalign 0.5

style pause_menu_button_text is main_menu_button_text:
    xalign 0.5
    yalign 0.5
    size 50

transform pause_menu_board_drop(start_pos = -900):
    ypos start_pos
    easein 0.5 ypos 0
    easeout 0.2 ypos -50
    easein 0.15 ypos 0

transform pause_menu_board_hide(height = -900):
    ypos 0
    easeout 0.15 ypos -50
    easein 0.2 ypos 0
    easeout 0.5 ypos height

transform pause_menu_items_appear:
    alpha 0.0
    pause 0.5
    easein 0.3 alpha 1.0