#region images
image safe_open_with_dust = "minigames/password_keyboard/Safe_open_with_dust.jpg"
image safe_fon = "minigames/password_keyboard/Safe_fon.png"

image safe_enter = "minigames/password_keyboard/Safe_enter_dark.png"
image safe_num_0 = "minigames/password_keyboard/Safe_0_dark.png"
image safe_num_0_hover = "minigames/password_keyboard/Safe_0.png"
image safe_num_1 = "minigames/password_keyboard/Safe_1_dark.png"
image safe_num_1_hover = "minigames/password_keyboard/Safe_1.png"
image safe_num_2 = "minigames/password_keyboard/Safe_2_dark.png"
image safe_num_2_hover = "minigames/password_keyboard/Safe_2.png"
image safe_num_3 = "minigames/password_keyboard/Safe_3_dark.png"
image safe_num_3_hover = "minigames/password_keyboard/Safe_3.png"
image safe_num_4 = "minigames/password_keyboard/Safe_4_dark.png"
image safe_num_4_hover = "minigames/password_keyboard/Safe_4.png"
image safe_num_5 = "minigames/password_keyboard/Safe_5_dark.png"
image safe_num_5_hover = "minigames/password_keyboard/Safe_5.png"
image safe_num_6 = "minigames/password_keyboard/Safe_6_dark.png"
image safe_num_6_hover = "minigames/password_keyboard/Safe_6.png"
image safe_num_7 = "minigames/password_keyboard/Safe_7_dark.png"
image safe_num_7_hover = "minigames/password_keyboard/Safe_7.png"
image safe_num_8 = "minigames/password_keyboard/Safe_8_dark.png"
image safe_num_8_hover = "minigames/password_keyboard/Safe_8.png"
image safe_num_9 = "minigames/password_keyboard/Safe_9_dark.png"
image safe_num_9_hover = "minigames/password_keyboard/Safe_9.png"
image safe_backspace = "minigames/password_keyboard/Safe_reset_dark.png"
image safe_backspace_hover = "minigames/password_keyboard/Safe_reset.png"
image safe_enter_hover = "minigames/password_keyboard/Safe_enter.png"
#endregion
#region logic
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

    def keypad_digit_action(digit):
        """Действие для цифровых кнопок"""
        if renpy.get_screen_variable("locked"):
            return
        entered = renpy.get_screen_variable("entered") or ""
        expected_code = renpy.get_screen_variable("expected_code")
        max_len = len(str(expected_code)) if expected_code is not None else 32
        if len(entered) < max_len:
            _ui_play_click()
            renpy.set_screen_variable("entered", entered + digit)

    def keypad_backspace_action():
        """Действие для кнопки backspace"""
        if renpy.get_screen_variable("locked"):
            return
        entered = renpy.get_screen_variable("entered") or ""
        if len(entered) > 0:
            _ui_play_click()
            renpy.set_screen_variable("entered", entered[:-1])

    def keypad_enter_action():
        """Действие для кнопки enter"""
        if renpy.get_screen_variable("locked"):
            return
        entered = renpy.get_screen_variable("entered") or ""
        expected_code = renpy.get_screen_variable("expected_code")
        code_str = str(expected_code) if expected_code is not None else ""
        if entered == code_str:
            _ui_play_ok()
            renpy.set_screen_variable("status", "ok")
            renpy.set_screen_variable("locked", True)
        else:
            _ui_play_error()
            renpy.set_screen_variable("status", "error")
            renpy.set_screen_variable("locked", True)


#endregion
#region transforms
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
#endregion
#region default variables
default keypad_key_size = (50, 50)  # Size for positioning keypad buttons
default keypad_font = "gui/fonts/PixeloidSans.ttf"
default keypad_hint_button_size = (220, 64)
default keypad_close_button_size = (170, 64)
default keypad_hint_button_color = "#4169E1"
default keypad_hint_button_hover_color = "#1E90FF"
default keypad_close_button_color = "#555555"
default keypad_close_button_hover_color = "#ff0000"
default keypad_screen_font_size = 55
#endregion

label scene_password_keypad:
    $ renpy.force_autosave()
    "Тест экрана ввода пароля"
    $ expected = "1008"
    $ result = renpy.call_screen("password_keypad", expected_code=expected, mask_input=False)
    if result:
        "Код верный. Продолжаем."
    else:
        "Отмена ввода кода."
    return

screen password_keypad(expected_code, hints=[], title=None, mask_input=False, auto_close_delay=1.2):
    layer "master"
    modal True
    add "safe_fon"

    default entered = ""
    default status = None   # None | "error" | "ok"
    default locked = False
    default current_hint = ""
    default hint_index = 0

    $ code_str = str(expected_code)
    $ max_len = len(code_str) if expected_code is not None else 32

    key "K_1" action Function(keypad_digit_action, "1")
    key "K_2" action Function(keypad_digit_action, "2")
    key "K_3" action Function(keypad_digit_action, "3")
    key "K_4" action Function(keypad_digit_action, "4")
    key "K_5" action Function(keypad_digit_action, "5")
    key "K_6" action Function(keypad_digit_action, "6")
    key "K_7" action Function(keypad_digit_action, "7")
    key "K_8" action Function(keypad_digit_action, "8")
    key "K_9" action Function(keypad_digit_action, "9")
    key "K_0" action Function(keypad_digit_action, "0")
    key "K_BACKSPACE" action Function(keypad_backspace_action)
    key "K_RETURN" action Function(keypad_enter_action)

    if title:
        text title:
            align (0.5, 0.0)
            size 55
            color gui.interface_text_color
            font gui.interface_text_font

    frame:
        align (0.64, 0.4)
        xsize 280
        ysize 100
        background None #Frame("#0B0F14", 20, 20)
        xpadding 24
        ypadding 16

        if status == "error":
            text "ERROR!":
                size keypad_screen_font_size
                color "#ff6565"
                font keypad_font
                xalign 0.5
                at display_shake
        elif status == "ok":
            text "OK!":
                size keypad_screen_font_size
                color "#7CFC00"
                font keypad_font
                xalign 0.5
        else:
            $ shown_value = entered if not mask_input else ("*" * len(entered))
            text shown_value:
                size keypad_screen_font_size
                color "#ECECEC"
                font keypad_font
                xalign 0.5

    imagebutton:
        idle "safe_num_1"
        hover "safe_num_1_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "1")
    imagebutton:
        idle "safe_num_2"
        hover "safe_num_2_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "2")
    imagebutton:
        idle "safe_num_3"
        hover "safe_num_3_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "3")

    imagebutton:
        idle "safe_num_4"
        hover "safe_num_4_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "4")
    imagebutton:
        idle "safe_num_5"
        hover "safe_num_5_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "5")
    imagebutton:
        idle "safe_num_6"
        hover "safe_num_6_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "6")

    imagebutton:
        idle "safe_num_7"
        hover "safe_num_7_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "7")
    imagebutton:
        idle "safe_num_8"
        hover "safe_num_8_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "8")
    imagebutton:
        idle "safe_num_9"
        hover "safe_num_9_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "9")

    imagebutton:
        idle "safe_backspace"
        hover "safe_backspace_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_backspace_action)
    imagebutton:
        idle "safe_num_0"
        hover "safe_num_0_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_digit_action, "0")
    imagebutton:
        idle "safe_enter"
        hover "safe_enter_hover"
        sensitive not locked
        focus_mask True
        action Function(keypad_enter_action)

    hbox:
        spacing 14
        pos (0.5, 0.95)

        if hints:
            textbutton "Подсказка":
                xysize keypad_hint_button_size
                text_size 30
                text_color "#FFFFFF"
                background keypad_hint_button_color
                hover_background keypad_hint_button_hover_color
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

        textbutton "Уйти" style "keypad_close_button":
            anchor (0.5, 0.5)
            text_size 55
            
            action Return(False)

    if status == "error":
        timer 0.9 action [SetScreenVariable("entered", ""), SetScreenVariable("status", None), SetScreenVariable("locked", False)]
    elif status == "ok":
        timer auto_close_delay action Return(True)

style keypad_close_button is gui_button


