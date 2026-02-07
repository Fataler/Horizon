default extra_menu_tab = "music"

screen extra_menu():
    tag menu
    style_prefix "extra"

    on "show" action Function(extra_update_background_duck)
    on "hide" action [Function(extra_stop_music, False), Function(extra_restore_background_music)]
    on "replaced" action [Function(extra_stop_music, False), Function(extra_restore_background_music)]

    $ extra_outer_x = 20
    $ extra_outer_w = max(1200, config.screen_width - (extra_outer_x * 2))
    $ extra_content_w = max(900, extra_outer_w - 120)
    $ extra_modules_w = max(860, extra_content_w - 410)
    $ extra_achievements_w = max(760, extra_modules_w)

    use game_menu(
        _("Экстра"),
        outer_width=extra_outer_w,
        content_width=extra_content_w,
        content_left_margin=20,
        outer_xpos=extra_outer_x,
    ):
        hbox:
            spacing 20
            xfill True
            yfill True

            frame:
                style "extra_section_frame"
                xsize 320
                yfill True

                vbox:
                    spacing 24
                    xfill True

                    text "ЭКСТРА" style "extra_section_title"

                    textbutton _("Муз. плеер"):
                        style "extra_tab_button"
                        action SetVariable("extra_menu_tab", "music")
                        selected extra_menu_tab == "music"

                    textbutton _("Галерея"):
                        style "extra_tab_button"
                        action [SetVariable("extra_menu_tab", "gallery"), SetVariable("extra_gallery_index", 0)]
                        selected extra_menu_tab == "gallery"

                    textbutton _("Достижения"):
                        style "extra_tab_button"
                        action SetVariable("extra_menu_tab", "achievements")
                        selected extra_menu_tab == "achievements"

                    null height 28

                    text "Control Hub" style "extra_hint_title"
                    text "Независимые модули: аудио, галерея, прогресс." style "extra_hint_text"

            frame:
                style "extra_content_frame"
                xfill True
                yfill True

                if extra_menu_tab == "achievements":
                    use extra_achievements_tab(content_width=extra_achievements_w)
                elif extra_menu_tab == "gallery":
                    use extra_gallery_tab(content_width=extra_modules_w)
                else:
                    use extra_music_player_tab(content_width=extra_modules_w)


style extra_section_frame:
    background "#101419D9"
    padding (26, 24)

style extra_content_frame:
    background "#0a0f14C8"
    padding (22, 22)

style extra_section_title is gui_text:
    color gui.accent_color
    size 62

style extra_tab_button is button:
    background "#8ec9ff10"
    hover_background "#8ec9ff24"
    selected_background "#ff7a1855"
    outlines [(1, "#8ec9ff40", 0, 0)]
    padding (16, 13)
    xfill True

style extra_tab_button_text is button_text:
    font gui.interface_text_font
    size 46
    color gui.interface_text_color
    hover_color gui.hover_color
    selected_color gui.accent_color

style extra_hint_text is gui_text:
    color "#D4E8FFAA"
    size 25

style extra_hint_title is gui_text:
    color "#8EC9FF"
    size 31

style extra_panel_title is gui_text:
    color gui.accent_color
    size 52
