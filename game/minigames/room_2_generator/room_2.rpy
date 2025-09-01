default room2_data = {"system_hacked": False, "code_replaced": False, "pressure_locked": False}

image bg room2 = "minigames/room_2_generator/Generator_fon.png"

image generator_top = "minigames/room_2_generator/Generator_nothing_interest_2.png"
image monitor = "minigames/room_2_generator/Generator_minigame_1.png"
image generator = "minigames/room_2_generator/Generator_nothing_interest_1.png"
image terminal_left = "minigames/room_2_generator/Generator_terminal.png"
image pressure_left = "minigames/room_2_generator/Generator_minigame_2.png"

screen room2():
    sensitive (not inspect and not _menu) tag room
    layer "master"

    fixed:
        add "bg room2"

        imagebutton idle Null() hover "generator_top" action [SetVariable("inspect", "generator_top"), Jump("room_2")] focus_mask "generator_top" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "monitor" action [SetVariable("inspect", "monitor"), Jump("room_2")] focus_mask "monitor" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "generator" action [SetVariable("inspect", "generator"), Jump("room_2")] focus_mask "generator" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "terminal_left" action [SetVariable("inspect", "terminal_left"), Jump("room_2")] focus_mask "terminal_left" mouse "inspect" at hover_effect()
        imagebutton idle Null() hover "pressure_left" action [SetVariable("inspect", "pressure_left"), Jump("room_2")] focus_mask "pressure_left" mouse "inspect" at hover_effect()

label room_2:
    $ renpy.force_autosave()
    show screen room2 with dissolve
    $ renpy.block_rollback()

    if inspect == "generator_top":
        R beard_on "Вряд ли я смогу добраться дотуда. Не стоит терять время."

    elif inspect == "monitor":
        if not room2_data["system_hacked"]:
            R beard_on thinking suspicious "Кажется, здесь мне необходимо взломать систему."
            R beard_on "Выглядит несложно."
            R beard_on suspicious "Посмотрим…"
            call assemble_puzzle
            if _return:
                $ room2_data["system_hacked"] = True
                R beard_on ear smile "Отлично!"
                R ear neutral "Осталось совсем немного…"
            else:
                R beard_on "Хм, возможно стоит ещё тут осмотреться."
        else:
            R beard_on "Тут я всё сделал."

    elif inspect == "generator":
        "Просто щиток, ничего интересного."

    elif inspect == "terminal_left":
        if not room2_data["system_hacked"]:
            R beard_on "Перед этим я должен взломать систему."
        elif not room2_data["code_replaced"]:
            R beard_on "Нужно заменить часть кода на другой."
            R beard_on "Так, что там было на уроках информатики..."
            call hanoi_game(blocks_number=5)
            if _return:
                $ room2_data["code_replaced"] = True
                R beard_on thinking suspicious "Хмм…"
                R happy "У меня получилось!"
                R ear smile "Даже не верится."
                R "Осталось ещё немного..."
            else:
                R beard_on "Попробую позже."
        else:
            R beard_on "Тут я всё сделал."

    elif inspect == "pressure_left":
        if not room2_data["system_hacked"]:
            R beard_on "Перед этим я должен заменить исходный код."
        elif not room2_data["code_replaced"]:
            R beard_on "Перед этим я должен заменить исходный код."
        elif not room2_data["pressure_locked"]:
            R beard_on ear surprised "Так... Тут можно выровнять давление в поршнях двигателя."
            R beard_on "Знаю, что ничего сложного - просто пару раз щелкнуть переключателем, но..."
            R "Закрыто на замок."
            R "Придется взломать."
            R "Естественно, отмычек у меня нет."
            R "Пришлось импровизировать."
            R "Рядом с терминалом валяются куски пластика, попробую поковырять замок ими."
            call lockpick_start
            if _return:
                $ room2_data["pressure_locked"] = True
                R beard_on "Я сделал это!"
                return

    $ inspect = None
    $ renpy.block_rollback()
    call screen room2
    return
