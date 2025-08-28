define credits_duration = 70.0

init python:    
    class Credits(renpy.Displayable):
        def __init__(self, content, duration=credits_duration):
            super(Credits, self).__init__()
            self.content = content
            self.duration = duration
            self.height = 0
            self.time = 0
            self.finished = False
            
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            
            text = Text(self.content, text_align=0.5, size=35)
            text_render = renpy.render(text, width, height, st, at)
            
            self.height = text_render.height + height
            
            speed = (self.height + height) / (self.duration * 1.5)
            
            y = height - (st * speed)

            if y < -text_render.height:
                self.finished = True
                y = -text_render.height 
                
            render.blit(text_render, (width//2 - text_render.width//2, y))
            
            if not self.finished:
                renpy.redraw(self, 0)
            return render

label label_credits:
    call screen credits
    return

screen credits():
    modal True
    default credits_obj = Credits(
"""{color=#393185}
{image=gui/menu/logo.png}

{size=65}{b}Команда:{/b}{/size}


{size=45}{b}Featharine{/b}{/size}
лидер
сценарий
персонажи
CG


{size=45}{b}Remi Prochet{/b}{/size}
музыка
звуки


{size=45}{b}Fataler{/b}{/size}
оригинальная идея
код
мини игры
верстка
анимации


{size=45}{b}Kapushishin{/b}{/size}
дизайн UI
фоны
сборка эпизодов
тестирование
режиссура
референсы


{size=65}Отдельная 
благодарность:{/size}

{size=45}{b}Коты Тигр и Лиса{/b}{/size}

катание по клавиатуре
моральная поддержка




Продолжение следует…
""")
    
    fixed:
        xfill True
        yfill True
        at show_screen_transform
        
        add "bg_menu_main"
        
        # Картинки
        timer (credits_duration * 0.33) action Show("credits_image", img_name="credits_img_1", is_left=True)
        timer (credits_duration * 0.40) action Hide("credits_image")

        timer (credits_duration * 0.42) action Show("credits_image", img_name="credits_img_2", is_left=False)
        timer (credits_duration * 0.50) action Hide("credits_image")

        timer (credits_duration * 0.52) action Show("credits_image", img_name="credits_img_3", is_left=True)
        timer (credits_duration * 0.60) action Hide("credits_image")

        timer (credits_duration * 0.62) action Show("credits_image", img_name="credits_img_4", is_left=False)
        timer (credits_duration * 0.70) action Hide("credits_image")

        timer (credits_duration * 0.72) action Show("credits_image", img_name="credits_img_5", is_left=True)
        timer (credits_duration * 0.80) action Hide("credits_image")

        timer (credits_duration * 0.82) action Show("credits_image", img_name="credits_img_6", is_left=False)
        timer (credits_duration * 0.88) action Hide("credits_image")

        timer (credits_duration * 0.89) action Show("credits_image", img_name="credits_img_7", is_left=True)
        timer (credits_duration * 1.05) action Hide("credits_image")
        
        add credits_obj xalign 0.5

        timer credits_duration + 5 action Show("credits_end")
        
        textbutton "Пропустить" action Return() xalign 0.95 yalign 0.05 at delay_appear(15.0)

screen credits_end():
    $ unlock_achievement(ACHIEVEMENT_THANK_YOU)
    text "Спасибо за игру!":
        size 95 
        align (0.5, 0.5)
        color "#393185"
        at credits_thanks

    timer 8.0 action Return()

transform credits_thanks:
    subpixel True
    alpha 0.0
    ease 1.0 alpha 1.0

screen credits_image(img_name=None, is_left=True):
    fixed:
        xfill True
        yfill True
        at show_screen_transform
            
        if img_name:
            $ xpos = 0.01 if is_left else 0.99
            $ trans = credits_left_appear if is_left else credits_right_appear
            add img_name at trans xalign xpos yalign 0.5 xsize 640 ysize 360

transform credits_left_appear:
    alpha 0.0 xoffset -50
    ease 3 alpha 1.0 xoffset 0

transform credits_right_appear:
    alpha 0.0 xoffset 50
    ease 3 alpha 1.0 xoffset 0
