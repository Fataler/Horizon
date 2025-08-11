image room_bg = "images/MiniGames/Kaban/Monitor2.png"
image screen_bg = im.Scale("images/MiniGames/Kaban/kaban_bg.jpeg", 1300, 650)
image coin = im.Scale("images/MiniGames/Kaban/coin.png", 64, 64)
image kaban = "images/MiniGames/Kaban/kaban.png"

init python:

    import random
  
    class ClickerGame:
        def __init__(self):
            self.score = 0
            self.target_score = 100
            self.is_completed = False
            self.message_shown = {10: False, 20: False, 30: False, 40: False, 50: False, 60: False, 70: False, 80: False, 90: False}
            self.current_message = ""
            self.message_timer = 0.0
            self.click_animations = []
            self.hp = 200
            self.max_hp = 200
            
        def click(self):
            if self.is_completed or self.hp <= 0:
                return
                
            self.score += 1
            self.hp -= 1
            
            self.add_click_animation()
            
            self.check_score_messages()
            
            if self.score >= self.target_score:
                self.is_completed = True
                
        def add_click_animation(self):
            x_offset = random.randint(-200, 200)
            y_offset = random.randint(-200, 200)
            
            animation = {
                'x': x_offset,
                'y': y_offset,
                'alpha': 1.0,
                'timer': 1.0
            }
            self.click_animations.append(animation)
            
        def update_animations(self, dt):
            for anim in self.click_animations[:]:
                anim['timer'] -= dt
                
                if anim['timer'] <= 0:
                    self.click_animations.remove(anim)
                else:
                    anim['alpha'] = anim['timer']
                    anim['y'] -= dt * 100
                
        def check_score_messages(self):
            if self.score == 10 and not self.message_shown[10]:
                self.show_message("Господин, расскажите правила этой игры.")
                self.message_shown[10] = True
            elif self.score == 20 and not self.message_shown[20]:
                self.show_message("Подождите, и это правда всё, что нужно делать?")
                self.message_shown[20] = True
            elif self.score == 30 and not self.message_shown[30]:
                self.show_message("Ваши развлечения весьма специфичны, господин Тайда.")
                self.message_shown[30] = True
            elif self.score == 40 and not self.message_shown[40]:
                self.show_message("Кажется, этот кабан так просто не сдастся.")
                self.message_shown[40] = True
            elif self.score == 50 and not self.message_shown[50]:
                self.show_message("Кабан опять хрюкнул. Это значит, вы побеждаете?")
                self.message_shown[50] = True
            elif self.score == 60 and not self.message_shown[60]:
                self.show_message("Он продолжает терпеть. Уважительно. Но неэффективно.")
                self.message_shown[60] = True
            elif self.score == 70 and not self.message_shown[70]:
                self.show_message("Наблюдаю снижение боевого духа кабана. Продолжайте атаку.")
                self.message_shown[70] = True
            elif self.score == 80 and not self.message_shown[80]:
                self.show_message("Отлично! Еще немного!")
                self.message_shown[80] = True
            elif self.score == 90 and not self.message_shown[90]:
                self.show_message("Кажется я ещё недостаточно понял, как нужно развлекаться по-настоящему.")
                self.message_shown[90] = True

        def show_message(self, text):
            self.current_message = text
            self.message_timer = 5.0
            
        def update_message_timer(self, dt):
            if self.message_timer > 0:
                self.message_timer -= dt
                if self.message_timer <= 0:
                    self.current_message = ""

screen clicker_game():
    modal True
    
    key "dismiss" action NullAction()
    
    default game = ClickerGame()
    default show_bounce_effect = False
    default bounce_timer_id = 0
    
    if True:
        timer 0.033 repeat True action Function(game.update_animations, 0.033)
        timer 0.033 repeat True action Function(game.update_message_timer, 0.033)
        timer 0.033 repeat True action If (game.is_completed, Return(True))
    
    add Parallax("screen_bg", 0.4):
        anchor (0.5, 0.5)
        xpos 0.5
        ypos 0.5
        zoom 1.2
        
    add "room_bg"
    
    if not game.is_completed:
        frame:
            background None
            xalign 0.5
            yalign 0.1
            
            text "[game.score]":
                size 70
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]
                anchor (0.0, 0.5)
                xpos 0.185
                ypos 0.155
                font gui.interface_text_font

            add "coin":
                anchor (0.5, 0.5)
                xpos 0.105
                ypos 0.155
                xoffset 100

        frame:
            background None
            xalign 0.5
            yalign 0.25
            
 
            frame:
                background None
                xsize 300
                ysize 20
                xalign 0.5
                yalign 0.25
                
                bar:
                    value AnimatedValue(game.hp, game.max_hp, 0.3)
                    xsize 296
                    ysize 16
                    xalign 0.5
                    yalign 0.5
                    left_bar "#ff4444"
                    right_bar "#444444"

            if not show_bounce_effect:
                imagebutton:
                    idle "kaban"
                    hover "kaban"
                    xalign 0.54
                    yalign 0.5
                    action [
                        Function(game.click),
                        SetScreenVariable("show_bounce_effect", True),
                        SetScreenVariable("bounce_timer_id", bounce_timer_id + 1)
                        # Function(renpy.play, "audio/click_sound.ogg", channel="sound")
                    ]
            
            if show_bounce_effect:
                add "kaban":
                    xalign 0.529
                    yalign 0.5
                    at bounce_effect
            
            for anim in game.click_animations:
                text "+1":
                    size 60
                    color "#00ff00"
                    bold True
                    xalign 0.5
                    yalign 0.5
                    xoffset anim['x']
                    yoffset anim['y']
                    outlines [(2, "#000000", 0, 0)]
                    at flying_text_with_alpha(anim['alpha'])
                
                add "coin":
                    xalign 0.5
                    yalign 0.5
                    xoffset anim['x'] + 60
                    yoffset anim['y']
                    at flying_text_with_alpha(anim['alpha'])
        
        if game.current_message:
            frame:
                background Frame("#000000aa", 20, 20)
                xalign 0.5
                yalign 0.90
                xpadding 30
                ypadding 45
                
                text game.current_message:
                    size 50
                    color "#ffffff"
                    xalign 0.5
                    at message_appear
    
    if not game.is_completed:
        textbutton "Выйти":
            text_size 40
            xalign 0.05
            yalign 0.05
            style "exit_button"
            action Return(False)
    
    if show_bounce_effect:
        $ current_timer_id = bounce_timer_id
        timer 0.13 action If(bounce_timer_id == current_timer_id, SetScreenVariable("show_bounce_effect", False))

transform screen_fade:
    alpha 1.0
    on show:
        alpha 0.0
        linear 0.35 alpha 1.0
    on hide:
        linear 0.35 alpha 0.0

transform bounce_effect:
    anchor (0.5, 0.5)
    
    zoom 1.0
    yoffset 0
    parallel:
        linear 0.08 zoom 1.1
        linear 0.08 zoom 1.0
    parallel:
        ease 0.1 yoffset -15
        ease 0.1 yoffset 0

transform flying_text_with_alpha(alpha_val):
    alpha alpha_val

transform message_appear:
    alpha 0.0 yoffset 20
    ease 0.3 alpha 1.0 yoffset 0

transform victory_text:
    zoom 0.5 alpha 0.0
    ease 0.5 zoom 1.2 alpha 1.0
    ease 0.2 zoom 1.0

transform victory_button:
    alpha 0.0 yoffset 30
    pause 0.5
    ease 0.3 alpha 1.0 yoffset 0

style exit_button_text:
    color "#ffffff"
    hover_color "#a7a6a6"
    outlines [(2, "#000000", 0, 0)]

label test_clicker_game:
    $ result = renpy.call_screen("clicker_game")
    if result:
        $ unlock_achievement(ACHIEVEMENT_PIG_SLAYER)
    return 