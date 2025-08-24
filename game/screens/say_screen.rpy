## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"
        style "say_window"
                
        fixed:
            xfill True
            yfit True

            vbox:
                spacing 6
                frame:
                    style "say_textframe"
                    text what id "what"

            if who:
                window:
                    style "namebox"
                    text who id "who"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0 zoom 0.9

    # if not (config.developer):
    #     key "mouseup_4" action ShowMenu("history")
    #     key "K_PAGEUP" action ShowMenu("history")


## Делает namebox доступным для стилизации через объект Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label

style say_window:
    subpixel True
    xalign 0.5
    xsize 1280
    align (0.5, 0.98)
    xpadding 30
    ypadding 20
    background Frame(textbox_style, Borders(0,0, 0, 0), tile=False)
    yminimum gui.textbox_height
    xfill False
    yfill False

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    adjust_spacing True
    outlines [(2, "000000AA", 0, 0)]

style say_textframe:
    background None
    xfill True
    padding (140, 50, 140, 20)