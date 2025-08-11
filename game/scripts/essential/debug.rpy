init -1 python:
    import os, datetime

    def log_debug(msg):
        path = os.path.join(config.basedir, "debug_log.txt")
        ts   = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] {msg}\n")
        if renpy.config.developer:
            print(f"[{ts}] {msg}")

    from functools import partial as curry

    if config.developer:
        config.overlay_screens += ["dev_hotkeys", "dev_hud"]
        if hasattr(config, "always_shown_screens"):
            config.always_shown_screens += ["dev_hotkeys", "dev_hud"]

screen dev_hud():
    if _show_hud:
        frame align (1.0, 1.0) padding (6, 4) background "#0008":
            text "%d × %d" % renpy.get_mouse_pos() style "debug_text"
        timer 0.33 action renpy.restart_interaction repeat True

screen dev_hotkeys():
    key "shift_K_h" action ToggleVariable("_show_hud")
    key "shift_K_j" action Function(_open_jump)
    key "shift_K_l" action Function(ShowMenu("image_tools"))

style debug_jump_textbutton is gui_button_text
style debug_jump_textbutton_text is gui_button_text:
    size 20
    xalign 0.0

style debug_text:
    color "#ffffff"
