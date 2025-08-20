# Password keypad screen with dynamic code and hints

init python:
    def _ui_play_click():
        try:
            renpy.play(sfx_ui_click, channel="ui")
        except Exception:
            pass

    def _ui_play_error():
        try:
            renpy.play(sfx_ui_over, channel="ui")
        except Exception:
            pass

    def _ui_play_ok():
        try:
            renpy.play(sfx_ui_achieve, channel="ui")
        except Exception:
            pass

transform keypad_appear:
    alpha 0.0
    zoom 0.95
    ease 0.20 alpha 1.0 zoom 1.0

transform dim_fade:
    alpha 0.0
    ease 0.20 alpha 1.0

transform display_shake:
    xoffset 0
    linear 0.05 xoffset -12
    linear 0.05 xoffset 12
    linear 0.05 xoffset -8
    linear 0.05 xoffset 8
    linear 0.05 xoffset 0

label test_password_keypad:
    "Тест экрана ввода пароля"
    $ expected = "1008"
    $ hints = [
        "Подсказка 1: В дневнике что-то было про свадьбу 10.08",
        "Подсказка 2: Интересно, какой пароль, если не 10.08",
        "Подсказка 3: Вероятнее всего, пароль это {b}1008{/b}."
    ]
    $ result = renpy.call_screen("password_keypad", expected_code=expected, hints=hints, title="Введите код", mask_input=False)
    if result:
        "Код верный. Продолжаем."
    else:
        "Отмена ввода кода."
    return

screen password_keypad(expected_code, hints=[], title=None, mask_input=False, auto_close_delay=1.2):

    modal True
    key "dismiss" action NullAction()

    default entered = ""
    default status = None   # None | "error" | "ok"
    default locked = False
    default current_hint = ""
    default hint_index = 0

    $ code_str = str(expected_code)
    $ max_len = len(code_str) if expected_code is not None else 32

    key "K_1" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "1")], NullAction()))
    key "K_2" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "2")], NullAction()))
    key "K_3" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "3")], NullAction()))
    key "K_4" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "4")], NullAction()))
    key "K_5" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "5")], NullAction()))
    key "K_6" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "6")], NullAction()))
    key "K_7" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "7")], NullAction()))
    key "K_8" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "8")], NullAction()))
    key "K_9" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "9")], NullAction()))
    key "K_0" action If(locked, NullAction(), If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "0")], NullAction()))
    key "K_BACKSPACE" action If(locked, NullAction(), If(len(entered) > 0, [_ui_play_click, SetScreenVariable("entered", entered[:-1])], NullAction()))
    key "K_RETURN" action If(locked, NullAction(), If(entered == code_str, [_ui_play_ok, SetScreenVariable("status", "ok"), SetScreenVariable("locked", True)], [_ui_play_error, SetScreenVariable("status", "error"), SetScreenVariable("locked", True)]))

    $ font_to_use = "gui/fonts/PixeloidSans.ttf"

    add Solid("#00000088") at dim_fade

    frame:
        at keypad_appear
        xalign 0.5
        yalign 0.5
        background Frame("#11141AEE", 40, 40)
        xpadding 36
        ypadding 32

        vbox:
            spacing 22
            xalign 0.5

            if title:
                text title:
                    size 44
                    color gui.interface_text_color
                    xalign 0.5

            frame:
                xsize 620
                ysize 120
                xalign 0.5
                background Frame("#0B0F14", 20, 20)
                xpadding 24
                ypadding 16

                if status == "error":
                    text "ERROR!":
                        size 66
                        color "#ff6565"
                        font font_to_use
                        xalign 0.5
                        at display_shake
                elif status == "ok":
                    text "OK!":
                        size 66
                        color "#7CFC00"
                        font font_to_use
                        xalign 0.5
                else:
                    $ shown_value = entered if not mask_input else ("*" * len(entered))
                    text shown_value:
                        size 66
                        color "#E5E5E5"
                        font font_to_use
                        xalign 0.5

            grid 3 4:
                spacing 12
                xalign 0.5

                textbutton "1":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "1")], NullAction())
                textbutton "2":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "2")], NullAction())
                textbutton "3":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "3")], NullAction())

                textbutton "4":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "4")], NullAction())
                textbutton "5":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "5")], NullAction())
                textbutton "6":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "6")], NullAction())

                textbutton "7":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "7")], NullAction())
                textbutton "8":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "8")], NullAction())
                textbutton "9":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "9")], NullAction())

                textbutton "←":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#2B2B31"
                    hover_background "#3A3A40"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) > 0, [_ui_play_click, SetScreenVariable("entered", entered[:-1])], NullAction())
                textbutton "0":
                    xysize (190, 90)
                    text_size 40
                    text_color "#FFFFFF"
                    background "#1F1F26"
                    hover_background "#2C2C33"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(len(entered) < max_len, [_ui_play_click, SetScreenVariable("entered", entered + "0")], NullAction())
                textbutton "Enter":
                    xysize (190, 90)
                    text_size 36
                    text_color "#FFFFFF"
                    background "#b33b6b"
                    hover_background "#8f2f55"
                    text_insensitive_color "#777777"
                    sensitive not locked
                    action If(entered == code_str, [_ui_play_ok, SetScreenVariable("status", "ok"), SetScreenVariable("locked", True)], [_ui_play_error, SetScreenVariable("status", "error"), SetScreenVariable("locked", True)])

            hbox:
                spacing 14
                xalign 0.5

                textbutton "Подсказка":
                    xysize (220, 64)
                    text_size 30
                    text_color "#FFFFFF"
                    background "#4169E1"
                    hover_background "#1E90FF"
                    action [
                        _ui_play_click,
                        SetScreenVariable("current_hint", (hints[hint_index] if hint_index < len(hints) else "Подсказки закончились.")),
                        SetScreenVariable("hint_index", (hint_index + 1 if hint_index < len(hints) else hint_index))
                    ]

                text current_hint:
                    size 30
                    color "#FFFFFF"
                    outlines [(1, "#000000", 0, 0)]
                    xmaximum 700
                    min_width 700

                textbutton "Закрыть":
                    xysize (170, 64)
                    text_size 28
                    text_color "#FFFFFF"
                    background "#555555"
                    hover_background "#777777"
                    action Return(False)

    if status == "error":
        timer 0.9 action [SetScreenVariable("entered", ""), SetScreenVariable("status", None), SetScreenVariable("locked", False)]
    elif status == "ok":
        timer auto_close_delay action Return(True)


