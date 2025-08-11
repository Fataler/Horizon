define FONT_NAME = "gui/fonts/dehinted-DarumadropOne.ttf"

#region: transforms
transform diagonal_line_left:
    rotate -45
    subpixel True
    pause 1
    linear 8.0 rotate -30
    linear 8.0 rotate -45
    repeat

transform diagonal_line_right:
    rotate -5
    subpixel True
    pause 1
    linear 7.0 rotate -25
    linear 7.0 rotate -5
    repeat

transform shadow_move:
    xoffset 0
    linear 2.0 xoffset -30
    linear 2.0 xoffset 0
    repeat

transform profile_card_appear:
    alpha 0.0
    ease 1.0 alpha 1.0

transform character_appear:
    alpha 0.0
    xoffset 100
    zoom 1.1
    pause 0.5
    parallel:
        ease 1.2 alpha 1.0
    parallel:
        easeout 1.2 xoffset 0
    parallel:
        easeout 1.2 zoom 1.0

transform text_appear:
    alpha 0.0
    rotate -10
    zoom 0.8
    parallel:
        ease 1.0 alpha 1.0
    parallel:
        easeout 1.5 rotate 0
    parallel:
        easeout 1.0 zoom 1.0

transform name_appear:
    alpha 0.0
    xoffset -500
    yoffset -200
    rotate 5
    zoom 1.5
    pause 1.0
    
    parallel:
        ease 1.0 alpha 1.0
    parallel:
        easeout 1.2 xoffset 0
    parallel:
        easeout 1.0 yoffset 0
    parallel:
        easeout 1.0 zoom 1.0
    
    block:
        linear 3.0 zoom 1.06
        linear 3.0 zoom 1.0
        repeat

transform stats_appear:
    rotate 6
    alpha 0.0
    pause 1.8
    ease 0.5 alpha 1.0

transform character_float:
    yoffset 0
    ease 2.0 yoffset -8
    ease 2.0 yoffset 0
    repeat
#endregion

#region: images
init:
    image bg = Solid("#FFFFFF")
    image video_katsumi = Movie(channel='video_ch', play="video/katsumi.webm", loops=0, stop_music=True, loop=False)
    image video_hikaru = Movie(channel='video_ch', play="video/hikaru.webm", loops=0, stop_music=True, loop=False)
    image video_den = Movie(channel='video_ch', play="video/den.webm", loops=0, stop_music=True, loop=False)
    image video_umi = Movie(channel='video_ch', play="video/umi.webm", loops=0, stop_music=True, loop=False)
    image video_izumi = Movie(channel='video_ch', play="video/izumi.webm", loops=0, stop_music=True, loop=False)

init python:
    def diagonal_line_left_element(color):
        return At(
            Solid(color, xysize=(60, 3000)), 
            Transform(anchor=(0.5, 0.5), xpos=200, ypos=650),
            diagonal_line_left
        )

    def diagonal_line_right_element(color):
        return At(
            Solid(color, xysize=(60, 3000)), 
            Transform(anchor=(0.5, 0.5), xpos=1500, ypos=650),
            diagonal_line_right
        )
        
#endregion


screen student_profile(character_name="КАЦУМИ", character_sprite="images/test.png", character_stats=None):
    tag profile

    $ main_color = "#F58B7A"
    $ secondary_color = "#EAC1BA"

    if (character_name == "Хикару"):
        $ main_color = "#204DDB"
        $ secondary_color = "#97D4FF"
    
    add "bg"
    
    add diagonal_line_left_element(secondary_color)
    
    add diagonal_line_right_element(secondary_color)
    
    frame:
        xysize (1920, 1080)
        background None
        
        fixed:
            xysize (800, 600)
            at text_appear
            
            text character_name:
                xpos 150
                ypos -400
                size 180
                color main_color
                font FONT_NAME
                #outlines [(4, secondary_color, 0, 0)]
                at name_appear
                
            fixed:
                add Solid(main_color):
                    xysize (400, 6000)
                    anchor (0.5, 0.5)
                    xpos 0.5
                    ypos 300
                    rotate -85
                
                if character_stats:
                    vbox:
                        xpos 250
                        ypos -100
                        spacing 30
                        at stats_appear
                        
                        for info_name, info_value in character_stats.items():
                            text f"{info_name.upper()}{str(info_value).upper()}":
                                size 50
                                color "#FFFFFF"
                                font FONT_NAME
                                outlines [(2, "#000000", 0, 0)]
                                text_align 0.5
                                ysize 2000
                                #xsize 2500
        
        vbox:
            xpos 1100
            at character_appear
            
            #shadow
            add Transform(character_sprite, matrixcolor=BrightnessMatrix(-1.0)):
                xalign 0.8
                yalign 1.0
                alpha 0.3
                at shadow_move
            
            #character
            add character_sprite:
                yoffset -1080
                xalign 0.9
                yalign 1.0
                at character_float

label hide_student_profile:
    hide screen student_profile with Dissolve(0.5)
    window show
    return

init python:
    def close_student_profile():
        renpy.hide_screen("student_profile")
        renpy.return_statement()

label show_student_profile(character_name="КАЦУМИ", character_sprite="images/test.png", character_stats=None):
    
    window hide
    
    show screen student_profile(character_name, character_sprite, character_stats) with Dissolve(0.8)
    
    return

screen profile_katsumi():
    add "video_katsumi":
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

screen profile_hikaru():
    add "video_hikaru":
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

screen profile_den():
    add "video_den":
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

screen profile_umi():
    add "video_umi":
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

screen profile_izumi():
    add "video_izumi":
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

label test_video:
    window hide

    show screen profile_katsumi

    k "Хэй, Тайда! Ты чего такой кислый? Опять отчитали? Ожидаемо, для такого дурачка вроде тебя."

    hide screen profile_katsumi with Dissolve(0.5)
    return

label test_student_profile:
    
    call show_student_profile("Кацуми","images/k_test.png",{"": "КЛАСС 2-B Академии Ссыкай", "специальность: ": "программист", "характер: ": "Цундере"}) from _call_show_student_profile

    k "Хэй, Тайда! Ты чего такой кислый? Опять отчитали? Ожидаемо, для такого дурачка вроде тебя."

    call hide_student_profile from _call_hide_student_profile

    jump test_another_profile

    
    return

label test_another_profile:    
    call show_student_profile("Хикару", 
        "images/f_test.png",
        {"": "КЛАСС 2-B Академии Ссыкай", "специальность: ": "Создание чертежей", "характер: ": "Кудере"}) from _call_show_student_profile_1    
    h "Если понадобится помощь, обратись ко мне, я одолжу тебе свои конспекты."
    
    return 