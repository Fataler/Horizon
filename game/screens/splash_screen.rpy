################################################################################
## Сплешскрин
################################################################################
default show_main_menu_fade = False
default splash_duration = 5.0

init:
    image splash_gradient = "gui/splash/gradient.png"
    image splash_logo = "gui/splash/logo.png"
    image splash_bg = "gui/splash/bg.png"

screen logo_jam():
    add "splash_bg"

    add "splash_gradient" at delay_appear(0, 1)
        
    add "splash_logo":
        align (0.5, 0.5)
    
    
    add "bg_black" at delay_hide(0, 1)
    add "bg_paper" at delay_appear(4, 1)
        
label splashscreen:

    if not splash_enabled:
        return

    if not renpy.variant("pc"):
        return

    scene black
    with Dissolve(1.0)

    stop music

    show screen logo_jam

    if persistent.first_start:
        $renpy.pause(splash_duration, hard=True) # не скипабельно
    else:
        $renpy.pause(splash_duration)

    $renpy.music.stop(channel='video_ch', fadeout=None)
    hide screen logo_jam
    
    if persistent.first_start:
        $persistent.first_start = False
    
    $ show_main_menu_fade = True
    return
