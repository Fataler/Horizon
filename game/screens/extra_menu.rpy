screen extra_menu():
    tag menu
    add "bg_black"
    default entries = [
        ("Пазл 1", Function(renpy.call, "igroteka_puzzle", 1, 2)),
        ("Пазл 2", Function(renpy.call, "igroteka_puzzle", 2, 3)),
        ("Пазл 3", Function(renpy.call, "igroteka_puzzle", 3, 4)),
        ("Ханой 1", Function(renpy.call, "igroteka_hanoi", 4, 3)),
        ("Ханой 2", Function(renpy.call, "igroteka_hanoi", 5, 4)),
        ("Ханой 3", Function(renpy.call, "igroteka_hanoi", 6, 5)),
        ("Игра 7", Function(renpy.call, "igroteka_placeholder", 7)),
        ("Игра 8", Function(renpy.call, "igroteka_placeholder", 8)),
        ("Игра 9", Function(renpy.call, "igroteka_placeholder", 9)),
    ]

    grid 3 3:
        xalign 0.5
        yalign 0.5
        spacing 20
        for i, (name, act) in enumerate(entries, start=1):
            frame:
                xsize 300
                ysize 200
                background Solid("#6a6565")

                button:
                    xsize 300
                    ysize 200
                    align (0.5, 0.5)
                    background None
                    hover_background Solid("#333333")
                    action act

                    if persistent.igroteka_progress and persistent.igroteka_progress.get(i):
                        add Transform("gui/achievements/done.png", alpha=0.8):
                            pos (1.0, 1.0)
                            anchor(1.0, 1.0)

                    # Фон с галочкой для пройденных игр
                    

                    text name align (0.5, 0.5)


    textbutton _("Назад") action ShowMenu("main_menu") align (0.98, 0.95)


