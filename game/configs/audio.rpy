# Музыка
define music_assembling = "audio/bg/Assembling.ogg"
define music_rock = "audio/bg/Rock.ogg"
define music_comedy_v2 = "audio/bg/Comedy V2.ogg"
define music_comedy_loop = "audio/bg/Comedy(loop).ogg"
define music_comedy = "audio/bg/Comedy.ogg"
#басы
define music_main_theme_2_v3 = "audio/bg/Main Theme 2 V3.ogg"
define music_main_theme_2 = "audio/bg/Main Theme 2.ogg"
#стардювеллей
define music_main_theme_3_v2 = "audio/bg/Main Theme 3 V2.ogg"
define music_main_theme_3 = "audio/bg/Main Theme 3.ogg"
define music_main_theme = "audio/bg/Main Theme.ogg"
define music_melancholy = "audio/bg/Melancholy.ogg"
define music_meatball_parade = "audio/bg/Meatball-Parade.mp3"
define music_gratification = "audio/bg/Gratification.ogg"
define fluffing_a_duck = "audio/bg/Fluffing-a-Duck.mp3"
define music_yay = "audio/bg/Sakura-Girl-Yay-chosic.com_.mp3"

# Игра
define sfx_hit = "audio/sfx/01 Hit.wav"
define sfx_bell = "audio/sfx/02 Bell.ogg"
define sfx_birds_v2 = "audio/sfx/03 Birds V2.ogg"
define sfx_birds = "audio/sfx/03 Birds.ogg"
define sfx_knock = "audio/sfx/04 Knock.ogg"
define sfx_bushes_v2 = "audio/sfx/05 Bushes V2.ogg"
define sfx_bushes = "audio/sfx/05 Bushes.ogg"
define sfx_giggles_v2 = "audio/sfx/06 Giggles v2.ogg"
define sfx_giggles = "audio/sfx/06 Giggles.ogg"
define sfx_crowd = "audio/sfx/07 Crowd.ogg"
define sfx_furniture = "audio/sfx/08 Furniture.ogg"
define sfx_throwing_things_around = "audio/sfx/09 Throwing things around.ogg"
define sfx_pressure = "audio/sfx/Pressure.ogg"
define sfx_open_door = "audio/sfx/Door-Close-SFX.ogg"
define sfx_slap = "audio/sfx/Slap.mp3"
define sfx_steps_on_road = "audio/sfx/Steps_on_road.mp3"
define sfx_steps_on_floor = "audio/sfx/Steps_on_floor.mp3"
define sfx_vshooh = "audio/sfx/vshooh.ogg"
define sfx_door_lock = "audio/sfx/door-lock.mp3"
define sfx_scream = "audio/sfx/scream.ogg"
define sfx_tiktak = "audio/sfx/tiktak.ogg"

# Интерфейс
define sfx_ui_achieve = "audio/sfx/UI 01 Achive.ogg"
define sfx_ui_click = "audio/sfx/UI 02 Click.ogg"
define sfx_ui_over = "audio/sfx/UI 03 Over.ogg"

# каналы
init python:
    renpy.music.register_channel("ui", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx2", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)