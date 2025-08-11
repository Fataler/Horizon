default room1 = {"solved":[], "box_1":0, "box_2":0, "key":0, "door":0}
default inspect = None

define check_color = Color("#0022ff")
define use_color = Color("#00ff2f")

image bg room1 = "Room/Room.png"
image box_1_check = Transform("Room/ya_1_check.png", matrixcolor=TintMatrix(check_color))
    

image box_2_check = Transform("Room/ya_2_check.png", matrixcolor=TintMatrix(check_color))

image door_check = Transform("Room/Door_check.png", matrixcolor=TintMatrix(check_color))

image dook_open = Transform("Room/Door_check.png", matrixcolor=TintMatrix(use_color))

screen room1():
    sensitive (not inspect and not _menu) tag room
    layer "master"


    fixed:
        add "bg room1"

        if room1["key"] == 0:
            imagebutton idle Null() hover "door_check" action [SetVariable("inspect", "door"), Jump("room_1")] focus_mask "door_check" mouse "inspect" at hover_effect()
        else:
            imagebutton idle Null() hover "dook_open" action [SetVariable("inspect", "door"), Jump("room_1")] focus_mask "dook_open" mouse "inspect" at hover_effect()
        
        imagebutton idle Null() hover "box_1_check" action [SetVariable("inspect", "box_1"), Jump("room_1")] focus_mask "box_1_check" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "box_2_check" action [SetVariable("inspect", "box_2"), Jump("room_1")] focus_mask "box_2_check" mouse "inspect" at hover_effect()

label room_1:
    show screen room1
    $ renpy.block_rollback()

    if inspect == "box_1":
        if room1["box_1"] == 0:
            "Посмотрел в левый ящик впервые"
        elif room1["box_1"] == 1:
            "Посмотрел в левый во второй раз"
        else:
            "Тут точно ничего нет"
        $ room1["box_1"] += 1

    elif inspect == "box_2":
        if room1["box_2"] == 0:
            "Посмотрел в правый ящик впервые"
            "Опа! Нашел ключ!"
            $ room1["key"] = 1
        else:
            "Больше тут ничего нет..."
        $ room1["box_2"] += 1

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