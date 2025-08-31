default room1_data = {"safe_opened": False, "door_unlocked": False, "computer_hacked": False, "tried_ryan": False, "tried_iris": False, "tried_viktor": False, "tried_sofi": False}
default inspect = None

define check_color = Color("#0022ff")
define use_color = Color("#00ff2f")

image bg room1 = "minigames/room_1_lazaret/lazaret.png"

image safe = "minigames/room_1_lazaret/safe.png"
image computer = "minigames/room_1_lazaret/computer.png"
image door = "minigames/room_1_lazaret/door.png"
image monitor = "minigames/room_1_lazaret/monitor.png"
image ballon = "minigames/room_1_lazaret/ballon.png"
image closet = "minigames/room_1_lazaret/closet.png"
image screen_right = "minigames/room_1_lazaret/ekran.png"
image journal = "minigames/room_1_lazaret/journal.png"

screen room1():
    sensitive (not inspect and not _menu) tag room
    layer "master"

    fixed:
        add "bg room1"

        imagebutton idle Null() hover "door" action [SetVariable("inspect", "door"), Jump("room_1")] focus_mask "door" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "safe" action [SetVariable("inspect", "safe"), Jump("room_1")] focus_mask "safe" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "computer" action [SetVariable("inspect", "computer"), Jump("room_1")] focus_mask "computer" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "monitor" action [SetVariable("inspect", "monitor"), Jump("room_1")] focus_mask "monitor" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "screen_right" action [SetVariable("inspect", "screen_right"), Jump("room_1")] focus_mask "screen_right" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "closet" action [SetVariable("inspect", "closet"), Jump("room_1")] focus_mask "closet" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "ballon" action [SetVariable("inspect", "ballon"), Jump("room_1")] focus_mask "ballon" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "journal" action [SetVariable("inspect", "journal"), Jump("room_1")] focus_mask "journal" mouse "inspect" at hover_effect()

label room_1:
    $ renpy.force_autosave()
    $ room1_data.setdefault("safe_opened", False)
    $ room1_data.setdefault("computer_hacked", False)
    $ room1_data.setdefault("door_unlocked", False)
    $ room1_data.setdefault("tried_ryan", False)
    $ room1_data.setdefault("tried_iris", False)
    $ room1_data.setdefault("tried_viktor", False)
    $ room1_data.setdefault("tried_sofi", False)
    show screen room1
    $ renpy.block_rollback()

    if inspect == "safe":
        if not room1_data["safe_opened"]:
            $ expected_code = 1734
            $ result = renpy.call_screen("password_keypad", expected_code=expected_code, hints=["Число связано с Дэвидом."], title="СЕЙФ")
            if result:
                $ room1_data["safe_opened"] = True
                $ unlock_achievement(ACHIEVEMENT_SHERLOCK)
                "Внутри пусто… Но видно чистое место — тут что-то лежало недавно."
            else:
                "Код не подошёл. Нужна подсказка."
        else:
            "Здесь больше ничего нет."

    elif inspect == "computer":
        if not room1_data["computer_hacked"]:
            "Софи: Кажется, я могу попробовать взломать систему. Немного."
            $ result = renpy.call_screen("puzzle_grid_pure", image="minigames/puzzle/Puzzle.png", grid=5, size=1000)
            if result:
                $ room1_data["computer_hacked"] = True
                $ room1_data["door_unlocked"] = True
                $ unlock_achievement(ACHIEVEMENT_HACKER)
                "Есть! Система приняла изменения."
            else:
                "Ладно, поищем альтернативу."
        else:
            "Здесь больше ничего нет."

    elif inspect == "monitor":
        "Экран для отслеживания состояния пациента. Вряд ли он пригодится."

    elif inspect == "screen_right":
        if room1_data["tried_ryan"] and room1_data["tried_iris"] and room1_data["tried_viktor"] and room1_data["tried_sofi"]:
            "Тут больше нечего делать."
        else:
            "Экран требует приложить руку."
            menu:
                "Кому попробовать?"
                "Райан" if not room1_data["tried_ryan"]:
                    $ room1_data["tried_ryan"] = True
                    "Отпечаток не распознан."
                "Ирис" if not room1_data["tried_iris"]:
                    $ room1_data["tried_iris"] = True
                    "Отпечаток не распознан."
                "Виктор" if not room1_data["tried_viktor"]:
                    $ room1_data["tried_viktor"] = True
                    "Отпечаток не распознан."
                "Софи" if not room1_data["tried_sofi"]:
                    $ room1_data["tried_sofi"] = True
                    "Отпечаток не распознан."
            if not (room1_data["tried_ryan"] and room1_data["tried_iris"] and room1_data["tried_viktor"] and room1_data["tried_sofi"]):
                "Не получится. Требует отпечаток Дэвида."

    elif inspect == "closet":
        "Кажется, здесь только лекарства. Ничего, что нам поможет."

    elif inspect == "ballon":
        "Просто баллоны с сжатым воздухом, ничего интересного."

    elif inspect == "journal":
        "Может быть, здесь найдётся что-то полезное?"
        "Какой-то клочок бумаги."
        R "Ирис, ты в курсе, что это?"
        I "Понятия не имею…"

    elif inspect == "door":
        if not room1_data["door_unlocked"]:
            "Не поддаётся. Нужно придумать, как разблокировать её."
        else:
            play sfx sfx_door_open
            "Дверь с металлическим скрипом отворилась. Поспешим!"
            return

    $ inspect = None
    $ renpy.block_rollback()
    call screen room1
    return
