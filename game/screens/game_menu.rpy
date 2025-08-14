## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None или один из "viewport" или "vpgrid". Этот
## экран предназначен для использования с одним или несколькими дочерними
## элементами, которые трансклюдируются (помещаются) внутрь него.

transform menu_move:
    pause 0.3
    parallel:
        ease 0.5 xoffset -390

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    
    style_prefix "game_menu"

    frame:
        at menu_move
        
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

    # add "gui/menu/frame_bg.png": 
    # #at menu_board_drop:
    #     anchor (0.5, 0.5)
    #     xpos 678
    #     ypos 560

    frame at menu_items_appear:
        top_margin 15
        xsize 1390
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    #use navigation

    textbutton _("Назад"):
        style "return_button"
        action ShowMenu(MAIN_MENU_SCREEN, from_game_menu=True)

    if main_menu:
        key "game_menu" action ShowMenu(MAIN_MENU_SCREEN, from_game_menu=True)


style game_menu_outer_frame is empty:
    #background "#90909085"
    xpos 0.37
    yoffset -10
    
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

# style return_button is gui_button
# style return_button_text is main_menu_button_text

style game_menu_content_frame:
    #background "#90909085"
    left_margin 220
    #right_margin 50
    top_margin 120
    bottom_margin 80
    xsize 1200

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 190

style game_menu_label_text:
    size gui.title_text_size
    color gui.interface_text_color
    yalign 0.5

style return_button:
    anchor (1.0, 0.5)
    xpos gui.navigation_xpos
    hover_color gui.hover_color
    yalign 1.0
    yoffset -45