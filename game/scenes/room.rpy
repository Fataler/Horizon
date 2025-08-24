default room1 = {"solved":[], "safe":0, "computer":0, "key":0, "door":0, "puzzle":0}
default inspect = None

define check_color = Color("#0022ff")
define use_color = Color("#00ff2f")

image bg room1 = "Room/EscapeRoomLazaret/lazaret.png"
# image box_1_check = Transform("Room/ya_1_check.png", matrixcolor=TintMatrix(check_color))

# image box_2_check = Transform("Room/ya_2_check.png", matrixcolor=TintMatrix(check_color))

# image door_check = Transform("Room/Door_check.png", matrixcolor=TintMatrix(check_color))

# image dook_open = Transform("Room/Door_check.png", matrixcolor=TintMatrix(use_color))

image safe = "Room/EscapeRoomLazaret/safe.png"
image computer = "Room/EscapeRoomLazaret/computer.png"
image door = "Room/EscapeRoomLazaret/door.png"
image monitor = "Room/EscapeRoomLazaret/monitor.png"

screen room1():
    sensitive (not inspect and not _menu) tag room
    layer "master"


    fixed:
        add "bg room1"

        if room1["key"] == 0:
            imagebutton idle Null() hover "door" action [SetVariable("inspect", "door"), Jump("room_1")] focus_mask "door" mouse "inspect" at hover_effect()
        else:
            imagebutton idle Null() hover "door" action [SetVariable("inspect", "door"), Jump("room_1")] focus_mask "door" mouse "inspect" at hover_effect()
        
        imagebutton idle Null() hover "safe" action [SetVariable("inspect", "safe"), Jump("room_1")] focus_mask "safe" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "computer" action [SetVariable("inspect", "computer"), Jump("room_1")] focus_mask "computer" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "monitor" action [SetVariable("inspect", "monitor"), Jump("room_1")] focus_mask "monitor" mouse "inspect" at hover_effect()

label room_1:
    show screen room1
    $ renpy.block_rollback()

    if inspect == "safe":
        if room1["safe"] == 0:
            "Я открыл сейф впервые"
            "Опа! Нашел ключ!"
            $ room1["key"] = 1
        else:
            "Тут больше ничего нет"
        $ room1["safe"] += 1

    elif inspect == "computer":
        if room1["puzzle"] == 0:
            call screen puzzle_grid_pure("images/test_puzzle_2.png", grid=5, size=1000)
            if _return:
                "Паззл собран!"
                $ room1["puzzle"] += 1
        else:
            "Тут больше ничего нет"

    elif inspect == "monitor":
        "Я посмотрел на монитор и увидел, что на нем написано: \"ХУЙ ПИЗДА ДЖИГУРДА\""

    elif inspect == "door":
        if room1["key"] == 0:
            "Дверь заперта"
        else:
            "Теперь, когда у меня есть ключ, я смогу открыть дверь"
            $ room1["door"] = 1
            "Я открыл дверь и вышел"
            return

    $ inspect = None
    $ renpy.block_rollback()
    call screen room1
    return