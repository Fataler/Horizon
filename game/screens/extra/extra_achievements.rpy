screen extra_achievements_tab(content_width=1330):
    vbox:
        spacing 15
        xfill True
        yfill True

        text "Достижения экипажа" style "extra_panel_title"

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            side_yfill True
            xfill True
            yfill True

            vbox:
                xfill True
                use achievements_content(content_width=content_width)
