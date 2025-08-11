init python:
    def get_taida_sprite(path):
        return Transform(path, zoom=0.8)

    def get_dzinzo_sprite(path):
        return Transform(path, zoom=0.7, xzoom=-1)

#region images
image bg_battle = "images/MiniGames/Battle/Battle Scene.jpg"

#endregion

define MSG_TAIDA_DEFAULT = "Что сделает Тайда?"
define MSG_TAIDA_DEFEATED = "Тайда повержен! Бой окончен."
define MSG_ESCAPE_FAILED = "Побег невозможен!"

define BAG_MESSAGES = [
    "Тайда шарится в сумке и находит пару игрушек из игровых автоматов. Они наполняют его решимостью.",
    "В сумке завалялся вчерашний обед. Тайде это не поможет.",
    "Тайда шарится в сумке, но больше ничего не может найти."]

define MAGIC_MESSAGES = [
    "Тайда начинает носиться по комнате. Дзиндзо недоумевает и теряет {b}2 HP{/b}.",
    "Тайда слишком устал и не может двигаться. Дзиндзо начинает опаздывать и теряет {b}2 HP{/b}.",
    "Чтобы отдохнуть, Тайда притворился спящим. Дзиндзо теряет {b}20 секунд времени{/b} и {b}2 HP{/b}.",
    "У Тайды закончились идеи. Больше это не сработает."]

define TAIDA_BATTLE_MESSAGES = [
    "Собрав все свои силы, Тайда ударяет Дзиндзо. Снято {b}2 HP{/b}.",
    "Тайда снова наносит удар! Критический промах. Снятно {b}2 HP{/b}.",
    "Тайда решает применить свой особый удар. Удар оказывается неэффективным. Снято {b}2 HP{/b}.",
    "Тайда: \n'Нет! Мы ещё не закончили!'"]

define DZINZO_BATTLE_MESSAGES = [
    "Дзиндзо не понимает что проиходит и пропускает ход.",
    "Дзиндзо пропускает ход и говорит: \n'Господин, что происходит? Это какая-то тренировка ваших физических способностей?'",
    "Дзиндзо: \n'Простите, меня ждет ваша мама в саду. Позвольте мне откланяться.'",]

define MSG_DZINZO_ATTACK = "Дзиндзо: 'Хорошо, давайте я проверю ваши показатели защиты.' \nДзиндзо наносит удар. Снято {b}999 HP{/b}."

default player_hp = 100
default mishanya_hp = 100
default battle_state = ACTIONS.SELECT_ACTION #"select_action"  # select_action, attacking, enemy_turn, defeated, kostyan_defeated, message_show
default battle_message = ""
default show_battle_buttons = True
default magic_used = False
default bag_message_index = 0
default magic_message_index = 0
default taida_battle_index = 0
default dzinzo_battle_index = 0
default escape_attempted = False

init python:
    class ACTIONS:
            ESCAPE = "escape_action"
            BAG = "bag_action"
            MAGIC = "magic_action"
            ATTACK = "attack_action"
            ATTACKING = "attacking_action"
            SELECT_ACTION = "select_action"
            ENEMY_TURN = "enemy_turn_action"
            ENEMY_SKIP = "enemy_skip_action"
            DEFEATED = "defeated"

transform pokemon_attack_left:
    xoffset 0
    linear 0.1 xoffset -40
    linear 0.1 xoffset 40
    linear 0.1 xoffset -40
    linear 0.1 xoffset 40
    linear 0.1 xoffset 0

transform pokemon_attack_right:
    xoffset 0
    linear 0.1 xoffset 40
    linear 0.1 xoffset -40
    linear 0.1 xoffset 40
    linear 0.1 xoffset -40
    linear 0.1 xoffset 0

transform hit_effect:
    matrixcolor TintMatrix("#ff0000") * BrightnessMatrix(0.3)
    linear 0.2 matrixcolor TintMatrix("#ff0000") * BrightnessMatrix(0.8)
    linear 0.2 matrixcolor TintMatrix("#ff0000") * BrightnessMatrix(0.3)
    linear 0.3 matrixcolor IdentityMatrix()

transform battle_entrance_left:
    xoffset -400
    alpha 0.0
    ease 1 xoffset 0 alpha 1.0

transform battle_entrance_right:
    xoffset 400
    alpha 0.0
    ease 1 xoffset 0 alpha 1.0

transform defeat_shake:
    xoffset 0
    linear 0.1 xoffset -10
    linear 0.1 xoffset 10
    linear 0.1 xoffset -10
    linear 0.1 xoffset 10
    linear 0.1 xoffset -5
    linear 0.1 xoffset 5
    linear 0.1 xoffset 0
    ease 2.0 alpha 0.0

style message_text:
    color "#000000"
    size 45
    xalign 0.0
    yalign 0.5

transform taida_pos:
    pos (-50, -198)
    anchor (0.0, 0.5)

transform dzinzo_pos:
    pos (-20, -178)
    anchor (0.0, 0.5)

transform ui_fade_in:
    alpha 0.0
    pause 0.5
    ease 0.5 alpha 1.0

screen pokemon_battle():
    tag battle
    modal True
    
    add "bg_battle"

    frame:
        pos (750, 1000)
        
        xysize (380, 130)
        background "#FFFFFF"
        anchor (0.5, 0.5)
        padding (15, 15)
        at battle_entrance_left
        
        vbox:
            spacing 8
            xalign 0.0
            yalign 0.5
            
            text "Тайда" size 28 color "#000000" xalign 0.0
            hbox:
                text "Ур.17" size 25 color "#000000" xalign 1.0
            
            hbox:
                spacing 10
                text "HP" size 18 color "#000000"
                bar:
                    value AnimatedValue(player_hp, 100, 1.0)
                    range 100
                    ysize 18
                    left_bar "#00FF00"
                    right_bar "#808080"
            
            text "[player_hp]/100" size 20 color "#000000" xalign 1.0

        if battle_state == ACTIONS.ESCAPE:
            add get_taida_sprite("side t ear summer_norm angry") at taida_pos
        elif battle_state == ACTIONS.BAG:
            add get_taida_sprite("side t ear summer_norm crazy") at taida_pos
        elif battle_state == ACTIONS.MAGIC:
            add get_taida_sprite("side t ear summer_norm asharashen") at taida_pos
        elif battle_state == ACTIONS.SELECT_ACTION:
            add get_taida_sprite("side t ear summer_norm") at taida_pos
        elif battle_state == ACTIONS.ATTACKING:
            add get_taida_sprite("side t ear summer_norm angry") at pokemon_attack_left, taida_pos
        elif battle_state == ACTIONS.ENEMY_TURN:
            add get_taida_sprite("side t ear summer_norm angry") at defeat_shake, hit_effect, taida_pos
        elif battle_state == ACTIONS.DEFEATED:
            pass
        else:
            add get_taida_sprite("side t ear summer_norm") at taida_pos
    
    frame:
        pos (1500, 680)
        xysize (380, 130)
        background "#FFFFFF"
        anchor (0.5, 0.5)
        padding (15, 15)
        at battle_entrance_right
        
        vbox:
            spacing 8
            xalign 0.0
            yalign 0.5
            
            text "Дзиндзо" size 28 color "#000000" xalign 0.0
            hbox:
                text "Ур.???" size 25 color "#000000" xalign 1.0
            
            hbox:
                spacing 10
                text "HP" size 18 color "#000000"
                bar:
                    value AnimatedValue(mishanya_hp, 100, 1.0)
                    range 100
                    ysize 18
                    left_bar "#00FF00"
                    right_bar "#808080"

            text "???/???" size 20 color "#000000" xalign 1.0

        if battle_state == ACTIONS.ENEMY_TURN:
            add get_dzinzo_sprite("side d thinking") at pokemon_attack_right, dzinzo_pos
        elif battle_state == ACTIONS.ENEMY_SKIP:
            add get_dzinzo_sprite("side d thinking") at hit_effect, dzinzo_pos
        elif battle_state == ACTIONS.SELECT_ACTION:
            add get_dzinzo_sprite("side d neutral") at dzinzo_pos
        elif battle_state == ACTIONS.MAGIC:
            add get_dzinzo_sprite("side d surprised") at dzinzo_pos
        elif battle_state == ACTIONS.BAG:
            add get_dzinzo_sprite("side d cunning") at dzinzo_pos
        else:
            add get_dzinzo_sprite("side d neutral") at dzinzo_pos
    

    frame:
        xpos 0.5
        ypos 0.15
        xysize (1200, 200)
        background "#FFFFFF"
        anchor (0.5, 0.5)
        padding (20, 20)
        at ui_fade_in
        
        vbox:
            xalign 0.5
            yalign 0.5
            
            if battle_message:
                text battle_message style "message_text"
            elif battle_state == ACTIONS.SELECT_ACTION:
                text MSG_TAIDA_DEFAULT style "message_text"
            else:
                text " " style "message_text"
    
    if show_battle_buttons and battle_state == ACTIONS.SELECT_ACTION:
        frame:
            xpos 0.95
            ypos 0.95
            xysize (500, 180)
            background "#FFFFFF"
            anchor (1.0, 1.0)
            padding (15, 15)
            at ui_fade_in
            
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                
                hbox:
                    spacing 15
                    xalign 0.5
                    
                    textbutton "УДАР":
                        xysize (220, 70)
                        text_size 26
                        text_color "#FFFFFF"
                        background "#FF6347"
                        hover_background "#FF4500"
                        text_outlines [(1, "#000000", 0, 0)]
                        action Function(start_attack)
                    
                    textbutton "СУМКА":
                        xysize (220, 70)
                        text_size 26
                        text_color "#FFFFFF"
                        background "#4169E1"
                        hover_background "#1E90FF"
                        text_outlines [(1, "#000000", 0, 0)]
                        action Function(try_bag)
                
                hbox:
                    spacing 15
                    xalign 0.5
                    
                    textbutton "МАГИЯ":
                        xysize (220, 70)
                        text_size 26
                        text_color "#FFFFFF"
                        background "#32CD32"
                        hover_background "#00FF00"
                        text_outlines [(1, "#000000", 0, 0)]
                        action Function(try_magic)
                    
                    textbutton "БЕЖАТЬ":
                        xysize (220, 70)
                        text_size 26
                        text_color "#FFFFFF"
                        background "#FFD700"
                        hover_background "#FFA500"
                        text_outlines [(1, "#000000", 0, 0)]
                        action Function(try_escape)

    if battle_state == ACTIONS.ATTACKING:
        timer get_message_time(battle_message) - 1 action Function(enemy_attack)
    elif battle_state == ACTIONS.ENEMY_TURN:
        timer get_message_time(battle_message) + 2 action Function(enemy_attack_final)
    elif battle_state == ACTIONS.DEFEATED:
        timer get_message_time(battle_message) action Return()
    elif battle_state == ACTIONS.ESCAPE:
        timer get_message_time(battle_message) action [Function(set_battle_state, ACTIONS.SELECT_ACTION)]
    elif battle_state == ACTIONS.BAG:
        timer get_message_time(battle_message) action [Function(set_battle_state, ACTIONS.SELECT_ACTION)]
    elif battle_state == ACTIONS.MAGIC:
        timer get_message_time(battle_message) action [Function(set_battle_state, ACTIONS.SELECT_ACTION)]
    elif battle_state == ACTIONS.ENEMY_SKIP:
        timer get_message_time(battle_message) action [Function(set_battle_state, ACTIONS.SELECT_ACTION)]

init python:
    def set_battle_state(state):
        global battle_state, show_battle_buttons, battle_message
        battle_state = state
        show_battle_buttons = True
        battle_message = ""
        renpy.restart_interaction()

    def get_message_time(message):
        if not message:
            return 2.0
        
        time = 2.0 + len(message) * 0.03
        return max(2.0, min(10.0, time))

    def start_attack():
        global battle_state, battle_message, show_battle_buttons, mishanya_hp, taida_battle_index

        renpy.play(sfx_hit)

        battle_state = ACTIONS.ATTACKING
        show_battle_buttons = False
        
        battle_message = TAIDA_BATTLE_MESSAGES[taida_battle_index]
        mishanya_hp -= 2
        taida_battle_index = min(taida_battle_index + 1, len(TAIDA_BATTLE_MESSAGES) - 1)
        
        renpy.restart_interaction()
    
    def try_escape():
        global battle_message, show_battle_buttons, battle_state, escape_attempted
        
        unlock_achievement(ACHIEVEMENT_STRATEGIST)
        
        show_battle_buttons = False
        battle_message = MSG_ESCAPE_FAILED
        battle_state = ACTIONS.ESCAPE
        escape_attempted = True
        renpy.restart_interaction()

    def try_bag():
        global battle_message, show_battle_buttons, bag_message_index, battle_state
        
        show_battle_buttons = False
        battle_state = ACTIONS.BAG
        battle_message = BAG_MESSAGES[bag_message_index]
        
        bag_message_index = min(bag_message_index + 1, len(BAG_MESSAGES) - 1)
        
        renpy.restart_interaction()
    
    def try_magic():
        global battle_message, show_battle_buttons, magic_message_index, mishanya_hp, battle_state
        
        show_battle_buttons = False
        battle_state = ACTIONS.MAGIC
        battle_message = MAGIC_MESSAGES[magic_message_index]
        
        if magic_message_index < len(MAGIC_MESSAGES) - 1:
            mishanya_hp -= 2
        
        magic_message_index = min(magic_message_index + 1, len(MAGIC_MESSAGES) - 1)
        
        renpy.restart_interaction()
        
    def enemy_attack():
        global player_hp, battle_message, battle_state, dzinzo_battle_index
        
        if dzinzo_battle_index < len(DZINZO_BATTLE_MESSAGES):
            battle_state = ACTIONS.ENEMY_SKIP
            battle_message = DZINZO_BATTLE_MESSAGES[dzinzo_battle_index]
            dzinzo_battle_index += 1
        else:
            battle_state = ACTIONS.ENEMY_TURN
            battle_message = MSG_DZINZO_ATTACK
            player_hp -= 999

        if player_hp <= 0:
            player_hp = 0
            
        renpy.restart_interaction()
    
    def enemy_attack_final():
        global battle_message, battle_state, show_battle_buttons, escape_attempted, magic_message_index, bag_message_index
        
        renpy.play(sfx_hit)

        if (escape_attempted and magic_message_index == len(MAGIC_MESSAGES) - 1 and bag_message_index == len(BAG_MESSAGES) - 1):
            unlock_achievement(ACHIEVEMENT_MAX_DAMAGE)
        
        if player_hp <= 0:
            battle_message = MSG_TAIDA_DEFEATED
            battle_state = ACTIONS.DEFEATED
        else:
            battle_message = ""
            battle_state = ACTIONS.SELECT_ACTION
            show_battle_buttons = True
        
        renpy.restart_interaction()
    
    def reset_battle():
        global player_hp, mishanya_hp, battle_state, battle_message, show_battle_buttons
        global bag_message_index, magic_message_index, taida_battle_index, dzinzo_battle_index, magic_used
        
        player_hp = 100
        mishanya_hp = 100
        battle_state = ACTIONS.SELECT_ACTION
        battle_message = ""
        show_battle_buttons = True
        bag_message_index = 0
        magic_message_index = 0
        taida_battle_index = 0
        dzinzo_battle_index = 0
        magic_used = False
        
        renpy.restart_interaction()