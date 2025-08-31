image hanoi_bg = "minigames/hanoi/fon.png"

image block_1 = "minigames/hanoi/1.png"
image block_2 = "minigames/hanoi/2.png"
image block_3 = "minigames/hanoi/3.png"
image block_4 = "minigames/hanoi/4.png"
image block_5 = "minigames/hanoi/5.png"


define min_blocks_for_game = 1
define blocks_number = 5
define size_restrictions_enabled = True
define allow_same_tower_moves = False
define max_hints = 8
define hint_restore_time = 2.0
define no_tower_selected = -1
define control_panel_position = (0.02, 0.05)
define control_panel_spacing = 10
define moves_display_position = (0.5, 0.02)
define tower_anchor_point = (0.5, 1.0)
define blocks_vertical_offset = -20
define button_text_size = 55
define tower_label_size = 25
define moves_counter_size = 28
define block_frame_padding = 10
define block_width_multiplier = 2
define interactive_area_width = 390
define interactive_area_height = 580
define selected_tower_highlight = "#624c4c35"
define valid_move_highlight = "#00ff0022"
define transparent_background = "#ff000000"
define empty_tower_display_height = 1
define total_towers_in_game = 3
define base_block_size = 20
define tower_positions = [(660, 0.80), (1125, 0.80), (1583, 0.80)]
define hint_ready_color = "#00ff00"
define hint_used_color = "#ff0000"
define hint_size = (20, 20)

default reset_blocks_number = None

init python:
    def update_hint_timer():
        """Обновляет таймер подсказок и восстанавливает подсказки при необходимости"""
        global available_hints, last_hint_time, max_hints, hint_restore_time

        if available_hints < max_hints:
            current_time = renpy.get_game_runtime()
            time_since_last_hint = current_time - last_hint_time

            if time_since_last_hint >= hint_restore_time:
                available_hints = min(available_hints + 1, max_hints)
                last_hint_time = current_time

screen hanoi_game_screen(towers):
    timer 0.06 action [Function(update_hint_timer), renpy.restart_interaction] repeat True
    layer "master"
    add "hanoi_bg"

    hbox:
        align (0.02, 0.02)
        spacing 5

        for i in range(max_hints):
            if i < available_hints:
                add Solid(hint_ready_color, xysize=hint_size)
            else:
                add Solid(hint_used_color, xysize=hint_size)

        if available_hints < max_hints:
            python:
                current_time = renpy.get_game_runtime()
                time_since_last_hint = current_time - last_hint_time
                time_remaining = max(0, hint_restore_time - time_since_last_hint)
            text "[int(time_remaining)]с" size 16 color "#ffffff"

    vbox:
        align control_panel_position
        spacing control_panel_spacing

        textbutton "Подсказка" action [Play("ui", sfx_click_put_down), Return("hint")] text_size button_text_size
        textbutton "Сброс" action [Play("ui", sfx_click_pick_up), Return("reset")] text_size button_text_size
        textbutton "Сдаться" action [Play("ui", sfx_click_pick_up), Jump("give_up")] text_size button_text_size
        textbutton "Правила" action [Play("ui", sfx_click_pick_up), Function(renpy.call_in_new_context, "hanoi_rules_explanation")] text_size button_text_size

        if config.developer:
            textbutton "SKIP" action Jump("win") text_size button_text_size

    text "Ходы: [player_moves]" size moves_counter_size align moves_display_position font gui.interface_text_font
    
    for i, each_tower in enumerate(towers):
        # vbox:
        #     pos each_tower["tower_pos"]
        #     anchor tower_anchor_point

        #     # if each_tower["mark"] == "start":
        #     #     text "Старт" size 25 xalign 0.5
        #     #     null height (block_size*1)
        #     # elif each_tower["mark"] == "finish":
        #     #     text "Цель" size 25 xalign 0.5
        #     #     null height (block_size*1)
        #     # else:
        #     #     text "" size 25 xalign 0.5
        #     #     null height (block_size*1)

        vbox:
            pos each_tower["tower_pos"]
            anchor tower_anchor_point
            yoffset blocks_vertical_offset
            spacing 10
            
            for each_block in each_tower["blocks"]:
                add each_block["image"] xalign 0.5
                        
        if can_click:
            button:
                xminimum interactive_area_width xmaximum interactive_area_width
                yminimum interactive_area_height ymaximum interactive_area_height
                pos each_tower["tower_pos"] anchor tower_anchor_point

                if start_from_tower == i:
                    background selected_tower_highlight
                elif start_from_tower >= 0 and check_move_with_rules(start_from_tower, i):
                    background valid_move_highlight
                else:
                    background transparent_background

                if start_from_tower < 0 and can_select_tower(each_tower["blocks"]):
                    action [Play("ui", sfx_click_pick_up), 
                    SetVariable("start_from_tower", i)]
                    tooltip "Выбрать башню для взятия блока"

                elif start_from_tower == i:
                    action [Play("ui", sfx_click_deselect),
                    SetVariable("start_from_tower", no_tower_selected)]
                    tooltip "Отменить выбор"

                elif start_from_tower >= 0 and check_move_with_rules(start_from_tower, i):
                    action [Play("ui", sfx_click_put_down),
                    SetVariable("finish_to_tower", i), 
                    Return("move_done")]
                    tooltip "Поместить блок сюда"

                else:
                    action [Play("ui", sfx_error2)]
                    tooltip "Недопустимый ход"

        else:
            button:
                xminimum interactive_area_width xmaximum interactive_area_width
                yminimum interactive_area_height ymaximum interactive_area_height
                pos each_tower["tower_pos"] anchor tower_anchor_point
                background transparent_background
                action []
                tooltip "Взаимодействие отключено"


init python:
    def check_game_state():
        global towers, finish_tower, blocks_number
        return len(towers[finish_tower]["blocks"]) == blocks_number

    def can_select_tower(tower_blocks):
        return len(tower_blocks) > 0

    def hanoi_can_place_block(selected_tower, target_tower_index, has_size_restrictions=False):
        if has_size_restrictions:
            if len(towers[target_tower_index]["blocks"]) == 0:
                return True
            return selected_tower["size"] < towers[target_tower_index]["blocks"][0]["size"]
        return True

    def is_valid_move(selected_tower, target_tower_index, allow_same_tower=False, has_size_restrictions=False):
        if not allow_same_tower and selected_tower == target_tower_index:
            return False

        if has_size_restrictions:
            selected_block = towers[selected_tower]["blocks"][0]
            target_blocks = towers[target_tower_index]["blocks"]

            if len(target_blocks) == 0:
                return True

            return selected_block["size"] < target_blocks[0]["size"]

        return True

    def get_game_rules():
        return allow_same_tower_moves, size_restrictions_enabled

    def check_move_with_rules(selected_tower, target_tower_index):
        allow_same, size_restricted = get_game_rules()
        return is_valid_move(selected_tower, target_tower_index, allow_same, size_restricted)



    def get_hint(towers, finish_tower, has_size_restrictions=False):
        global allow_same_tower_moves, player_moves

        total_blocks = sum(len(t["blocks"]) for t in towers)
        if len(towers[finish_tower]["blocks"]) == total_blocks and total_blocks > 0:
            return None

        start_tower = None
        for i, t in enumerate(towers):
            if t.get("mark") == "start":
                start_tower = i
                break
        if start_tower is None:
            return None

        aux_tower = next((i for i in range(total_towers_in_game) if i not in (start_tower, finish_tower)), None)
        if aux_tower is None:
            return None

        smallest_pos = None
        for i in range(total_towers_in_game):
            if towers[i]["blocks"] and towers[i]["blocks"][0]["size"] == 1:
                smallest_pos = i
                break
        if smallest_pos is None:
            return None

        should_move_smallest = (player_moves % 2 == 0)

        order = [start_tower, finish_tower, aux_tower] if (total_blocks % 2 == 1) else [start_tower, aux_tower, finish_tower]

        if should_move_smallest:
            try:
                idx = order.index(smallest_pos)
            except ValueError:
                idx = 0
            target = order[(idx + 1) % 3]

            if is_valid_move(smallest_pos, target, allow_same_tower_moves, has_size_restrictions):
                return (smallest_pos, target)

            for candidate in [t for t in range(total_towers_in_game) if t != smallest_pos]:
                if is_valid_move(smallest_pos, candidate, allow_same_tower_moves, has_size_restrictions):
                    return (smallest_pos, candidate)

            return None
        else:
            other_towers = [t for t in range(total_towers_in_game) if t != smallest_pos]
            t1, t2 = other_towers[0], other_towers[1]

            top1 = towers[t1]["blocks"][0] if towers[t1]["blocks"] else None
            top2 = towers[t2]["blocks"][0] if towers[t2]["blocks"] else None

            if top1 is None and top2 is None:
                for candidate in [t for t in range(total_towers_in_game) if t != smallest_pos]:
                    if is_valid_move(smallest_pos, candidate, allow_same_tower_moves, has_size_restrictions):
                        return (smallest_pos, candidate)
                return None

            if top1 is None and top2 is not None:
                if is_valid_move(t2, t1, allow_same_tower_moves, has_size_restrictions):
                    return (t2, t1)
            elif top2 is None and top1 is not None:
                if is_valid_move(t1, t2, allow_same_tower_moves, has_size_restrictions):
                    return (t1, t2)
            else:
                if top1["size"] < top2["size"]:
                    if is_valid_move(t1, t2, allow_same_tower_moves, has_size_restrictions):
                        return (t1, t2)
                else:
                    if is_valid_move(t2, t1, allow_same_tower_moves, has_size_restrictions):
                        return (t2, t1)

            if is_valid_move(t1, t2, allow_same_tower_moves, has_size_restrictions):
                return (t1, t2)
            if is_valid_move(t2, t1, allow_same_tower_moves, has_size_restrictions):
                return (t2, t1)

            return None


    def hanoi_moves_count(x):
        if x == 1:
            return 1
        elif x > 1:
            return 1 + hanoi_moves_count(x-1) * 2
        else:
            return 0

label hanoi_game(blocks_number=5):
    play ui sfx_connect3
    if hasattr(renpy.store, 'reset_blocks_number') and reset_blocks_number is not None:
        $ blocks_number = reset_blocks_number
        $ reset_blocks_number = None
    $ blocks_number = min(blocks_number, 5)
    $ blocks_set = []
    python:
        for b in range(1, blocks_number+1):
            blocks_set.append({"size": b, "image": "block_%d" % b})

    $ start_tower = 0
    $ finish_tower = 2

    $ block_size = base_block_size
    $ towers_pos = tower_positions

    $ towers = [ {"tower_pos":towers_pos[0],"blocks":[], "mark":None},
        {"tower_pos":towers_pos[1],"blocks":[], "mark":None},
        {"tower_pos":towers_pos[2],"blocks":[], "mark":None}
        ]

    $ towers[start_tower]["blocks"] = blocks_set
    $ towers[start_tower]["mark"] = "start"
    $ towers[finish_tower]["mark"] = "finish"

    $ player_moves = 0
    $ minimal_moves = hanoi_moves_count(blocks_number)

    $ available_hints = max_hints
    $ hint_restore_timer = 0.0
    $ last_hint_time = renpy.get_game_runtime()

    show screen hanoi_game_screen(towers=towers)

label hanoi_loop:
    $ start_from_tower = no_tower_selected
    $ finish_to_tower = -1

    $ can_click = True
    $ result = ui.interact()

    if result == "hint":
        python:
            if available_hints > 0:
                hint = get_hint(towers, finish_tower, size_restrictions_enabled)
                if hint:
                    start_from_tower, finish_to_tower = hint
                    available_hints -= 1
                    last_hint_time = renpy.get_game_runtime()
                else:
                    result = None
            else:
                result = None

    if result == "reset":
        jump hanoi_game

    $ can_click = False

    if start_from_tower == no_tower_selected or finish_to_tower < 0 or not towers[start_from_tower]["blocks"]:
        jump hanoi_loop

    $ block_to_move = towers[start_from_tower]["blocks"][0]
    $ towers[start_from_tower]["blocks"] = towers[start_from_tower]["blocks"][1:]
    $ towers[finish_to_tower]["blocks"].insert(0, block_to_move)

    $ player_moves += 1

    if check_game_state():
        jump win

    jump hanoi_loop
label win:
    $ can_click = False
    play ui sfx_win
    if player_moves > minimal_moves:
        "Победа!\nЗатрачено ходов: [player_moves]"
    else:
        "Идеальная победа!\nЗатрачено ходов: [player_moves]"

    hide screen hanoi_game_screen
    return True

label give_up:
    play ui sfx_disconnect
    $ can_click = False
    "Удачи в следующий раз!"
    hide screen hanoi_game_screen
    return False

label hanoi_rules_explanation:

    R_t thinking neutral "Хорошо, нужно сосредоточиться и вспомнить, что я должен сделать."
    R_t "Видимо, на этом экране я смогу переписать код для взлома системы, как сказала Элис."
    R_t "Передо мной три файла (MAIN.EXE, BUFFER.EXE, PATCH.EXE). В левом находятся данные разных размеров."

    R_t thinking not_sure "Цель - переместить все данные с MAIN.EXE на PATCH.EXE."
    R_t "Но есть важное правило, которое нельзя нарушать..."

    R_t thinking suspicious "Блок данных можно класть только на данные большего размера или на пустое место."
    R_t "Запомнить: больший блок не может лежать на меньшем!"

    R_t "Я смогу взломать систему, когда все блоки окажутся в файле PATCH.EXE."

    return