################################################################################
## Экран паузы
################################################################################

init -2:
    $_game_menu_screen = "pause_menu"

screen pause_menu(from_game_menu=False):
    tag menu

    $ elements_apperar_time = 2.0 if not from_game_menu else 1.0
    
    add "bg_black"
    
    frame:
        background None
        at menu_move_back(from_game_menu)
        
        add "bg_black"
        add Parallax("menu_fon", 0.5)
        add Parallax("menu_fon_2", 0.5)

        add Parallax("menu_nimb", 1)at transform:
            alpha 1.0
            linear 2.0 alpha 0.5
            linear 2.0 alpha 1.0
            repeat

        add Parallax("menu_gg", 0.5)

        add Parallax("hand_1", 0.55) at hand_bob(up_time=6.0, down_time=5.0, distance=20, stretch=0.03, delay=0.0)
        add Parallax("hand_2", 0.6) at hand_bob(up_time=6.2, down_time=5.0, distance=22, stretch=0.03, delay=0.2)
        add Parallax("hand_3", 0.65) at hand_bob(up_time=6.5, down_time=5.2, distance=24, stretch=0.035, delay=0.4)
        add Parallax("hand_4", 0.7) at hand_bob(up_time=6.7, down_time=5.2, distance=26, stretch=0.035, delay=0.6)
        add Parallax("hand_5", 0.75) at hand_bob(up_time=7.0, down_time=5.4, distance=18, stretch=0.04, delay=0.8)
        add Parallax("hand_6", 0.85) at hand_bob(up_time=7.2, down_time=5.6, distance=25, stretch=0.04, delay=1.0)
        add Parallax("hand_7", 0.95) at hand_bob(up_time=7.5, down_time=5.8, distance=27, stretch=0.045, delay=1.2)
        add Parallax("hand_8", 1.05) at hand_bob(up_time=7.7, down_time=6.0, distance=20, stretch=0.045, delay=1.4)
        add Parallax("hand_9", 1.15) at hand_bob(up_time=8.0, down_time=6.2, distance=31, stretch=0.05, delay=1.6)
        add Parallax("hand_10", 1.25) at hand_bob(up_time=8.2, down_time=6.4, distance=38, stretch=0.05, delay=1.8)
        add Parallax("hand_11", 1.35) at hand_bob(up_time=8.5, down_time=6.6, distance=20, stretch=0.055, delay=2.0)
        add Parallax("hand_12", 1.45) at hand_bob(up_time=8.8, down_time=6.8, distance=34, stretch=0.06, delay=2.2)

    frame:
        style_prefix "pause_menu"
        background None #"#00000080"
        xanchor 0.5
        xpos 0.83

        # Кнопки меню
        vbox at pause_menu_items_appear:
            spacing 30
            xalign 0.5
            yalign 0.5
            yfit True
            first_spacing 150

            text "ПАУЗА" size 120 xalign 0.5 color gui.accent_color style "pause_menu_button_text"
            
            textbutton _("Сохранить") action [SetVariable("came_from_pause_menu", True), Hide("pause_menu"), ShowMenu("save")]
            textbutton _("Загрузить") action [SetVariable("came_from_pause_menu", True), Hide("pause_menu"), ShowMenu("load")]
            textbutton _("История") action [SetVariable("came_from_pause_menu", True), Hide("pause_menu"), ShowMenu("history")]
            textbutton _("Настройки") action [SetVariable("came_from_pause_menu", True), Hide("pause_menu"), ShowMenu("preferences")]
            textbutton _("Главное меню") action MainMenu()
            textbutton _("Вернуться") action Return()

style pause_menu_button is main_menu_button:
    xalign 0.5
    yalign 0.5

style pause_menu_button_text is main_menu_button_text:
    xalign 0.5
    yalign 0.5
    size 55

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