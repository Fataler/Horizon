transform scene_good_ending_effecty_transform(alpha_val=1):
    alpha alpha_val
    soot_drift_bottom(speed=1.0, amplitude=4, x_amplitude=2)
    
image scene_good_ending_chely = At("CG/CG_good_ending/CG_good_ending_chely.png", gentle_wind())
image scene_good_ending_dom = "CG/CG_good_ending/CG_good_ending_dom.png"
image scene_good_ending_doroga = At("CG/CG_good_ending/CG_good_ending_doroga.png", scene_good_ending_effecty_transform(1))

image scene_good_ending_effecty = At("CG/CG_good_ending/CG_good_ending_effecty.png", scene_good_ending_effecty_transform(0.5))
image scene_good_ending_mogoly = "CG/CG_good_ending/CG_good_ending_mogoly.png"
image scene_good_ending_ramka = "CG/CG_good_ending/CG_good_ending_ramka.png"
image scene_good_ending_trava = "CG/CG_good_ending/CG_good_ending_0006_trava.png"

#сцена могила с букетом
image scene_mogila_fon = "CG/CG_Buket_mogila/fon.png"
image scene_mogila_fon_buket = "CG/CG_mogily/CG_mogily_fon_buket.png"
image scene_mogila_buket = "CG/CG_Buket_mogila/buket.png"

#сцена дом внутри
image scene_dom_fon = "CG/CG_dom/CG_dom_fon.png"
image scene_dom_fleks = "CG/CG_dom/CG_dom_fleks.png"
image scene_dom_shmeks = "CG/CG_dom/CG_dom_shmeks.png"


init python:
    define_numbered_animation("scene_good_ending_mayak_mult", "CG/CG_lighthouse", start=1, end=13, delay=0.27)

transform gentle_wind:
    subpixel True
    parallel:
        block:
            easein 3.0 xoffset 5
            easeout 3.0 xoffset 0
            repeat

transform cloud_move:
    subpixel True
    parallel:
        block:
            linear 8.0 xoffset 20
            linear 8.0 xoffset -20
            repeat
    parallel:
        block:
            linear 0.5 alpha 0.7
            linear 0.5 alpha 1.0
            repeat

transform soft_drop(distance=100, duration=1.8):
    subpixel True
    yoffset -distance
    alpha 0
    easein duration*0.5 yoffset 5 alpha 1.0
    ease duration*0.5 yoffset 0

transform focus_and_zoom_out(start_zoom=2.0, end_zoom=1.0, focus_x=0.5, focus_y=0.5, duration=2.0, delay=0.0):
    subpixel True
    align (0.5, 0.5)
    anchor (focus_x, focus_y)
    zoom start_zoom
    pause delay
    # block:
    #     linear duration * 0.5 zoom end_zoom * 2 anchor (0.6, 0.6)
    block:
        linear duration zoom end_zoom * 1 anchor (0.5, 0.5)

label scene_good_ending:
    
    # Дорога старт
    play sfx music_waves fadein 0.5 fadeout 1.0 loop
    play music music_quite_ambient2 fadein 0.5 fadeout 1.0 loop

    show scene_good_ending_doroga at truecenter zorder 7
    show scene_good_ending_chely at gentle_wind zorder 8
    show scene_good_ending_effecty
    show scene_good_ending_ramka zorder 10
    with dissolve
    cutscene "Я прищурил глаза от яркого солнца."
    cutscene "Ноздри щекотал лёгкий солоноватый запах."
    cutscene "Свежий и ударяющий в голову."
    cutscene "Мы шли по просёлочной дороге."
    cutscene "Гравий шуршал под ногами."
    cutscene "Вокруг не было ни души."
    cutscene "Мы шли молча."
    cutscene "Я держал Элис за руку."
    
    scene bg_white
    with dissolve
    $ renpy.pause(0.5, hard=True)
    # Дорога конец
        
    # маяк старт

    show scene_good_ending_mayak_mult
    with dissolve
    cutscene "Некоторое время после прорыва оболочки аномалии я летел к базе один."
    cutscene "Мне удалось посадить корабль на базу N117, где меня уже ждали."
    cutscene "Около двух недель я лежал в лазарете, а затем отправился с другой экспедицией на Землю."
    cutscene "Многое прояснилось в моей голове за это время."
    cutscene "Долгое пребывание в аномалии сильно ударило по психике."
    cutscene "Но мне повезло намного больше, чем остальному экипажу нашей миссии."
    cutscene "Они умерли мгновенно при столкновении с аномалией."
    cutscene "Как позже выяснили ученые, импульс аномалии вызывает катастрофическую перегрузку нейронов в бодрствующей коре."
    cutscene "Я выжил лишь потому, что проспал момент столкновения и был без сознания."
    cutscene "Мой разум заблокировал воспоминания о том, как я нашёл их: мёртвыми на своих местах."
    cutscene "Как я спрятал их в отсеке рядом с командным центром."
    cutscene "Как я заменил их на личины своих близких."
    hide scene_good_ending_mayak_mult
    with dissolve
    # маяк конец

    scene bg_white
    with dissolve
    $ renpy.pause(0.5, hard=True)

    # трава старт
    show scene_good_ending_trava at gentle_wind, soot_drift_bottom(speed=0.3, amplitude=1, x_amplitude=0), truecenter
    show scene_good_ending_chely
    show scene_good_ending_effecty
    show scene_good_ending_ramka
    with dissolve
    cutscene "Я смотрел на Элис, которая шагала рядом."
    cutscene "Я обязан ей своей жизнью."
    cutscene "Нет, сотней своих жизней."
    cutscene "Спустя два года она так и не потеряла надежду вернуть меня на Землю."
    cutscene "Элис вместе с учёными провела долгие дни и ночи в диспетчерской и лаборатории — и вместе они смогли создать инновационную технологию."
    cutscene "Технологию, позволяющую передавать сигнал и общаться сквозь столь далёкие расстояния."
    cutscene "Это был настоящий научный прорыв, проверенный в реальных условиях."
    cutscene "Но для меня было удивительно другое."
    cutscene "Она могла просто забыть обо мне."
    cutscene "Как о страшном сне. О человеке, навсегда потерянном вдали от дома."
    cutscene "Я сжал её руку. Элис улыбнулась мне."
    hide scene_good_ending_trava
    # трава конец

    scene bg_white
    with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)

    # дом старт
    show scene_good_ending_dom at soot_drift_bottom(speed=0.3, amplitude=1, x_amplitude=0), truecenter
    show scene_good_ending_chely
    show scene_good_ending_effecty
    show scene_good_ending_ramka
    with Dissolve(1.0)

    cutscene "Мы подошли к нашей цели. Впереди уже был виден маяк."
    cutscene "Берег сужался, дорога всё чаще уходила в песок и россыпь мелких цветных камней."
    cutscene "На верхушке маяка не горел свет."
    cutscene "Под ним располагался старый деревянный дом."
    cutscene "Некогда украшавшая его цветастая краска облупилась."
    cutscene "Я подошёл к входу."
    cutscene "Покосившаяся дверь, разрушившаяся крыша."
    cutscene "Потрескавшееся каменное крыльцо."
    cutscene "В моём кармане лежал ключ."
    cutscene "Старый заржавевший ключ, болтающийся на коричневой плотной верёвочке."
    cutscene "Удивительно, но он легко вошёл в замочную скважину, и замок провернулся."
    cutscene "Со скрипом дверь отворилась."
    cutscene "Я не спешил заходить."
    cutscene "Сквозь отверстие в крыше комната была хорошо освещена."
    cutscene "Пыль летала в воздухе, подсвеченная лучами солнца."
    cutscene "Элис посмотрела на меня и зашла первой."
    $ renpy.music.set_volume(0.1, delay=0.5, channel="sfx")
    hide scene_good_ending_dom
    # дом конец

    scene bg_black
    with dissolve
    $ renpy.pause(0.5, hard=True)

    # дом внутри старт
    show scene_dom_fon
    show scene_good_ending_effecty 
    show scene_good_ending_ramka
    with dissolve
    cutscene "Спустя некоторое время я последовал за ней."
    cutscene "Здесь всё было как прежде."
    cutscene "Большой платяной шкаф в углу."
    cutscene "Обувница с несколькими парами тапок."
    cutscene "Широкий деревянный стул был задвинут под небольшой стол с масляной лампой."
    cutscene "С кухни слышалось тихое чириканье — скорее всего, какая-то птица свила там гнездо."
    cutscene "Пол скрипел под ногами."
    cutscene "Я присел на стул и поставил под ноги рюкзак."
    cutscene "Закрыл глаза и прислушался."
    $ renpy.music.set_volume(1.0, delay=1.0, channel="sfx")
    cutscene "Шум моря. Волна за волной накатывала воспоминания о моём родном доме, словно оживляя картинки в памяти."
    cutscene "Я зажёг масляную лампу своей зажигалкой и раскрыл рюкзак."
    cutscene "В нём лежал букет цветов."
    cutscene "Элис подошла и молча положила руку мне на плечо."
    cutscene "Наши взгляды встретились. Пора."
    # дом внутри конец
    stop sfx fadeout 1.0
    scene bg_black
    with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)

    show scene_good_ending_mogoly at gentle_wind, truecenter
    show scene_good_ending_effecty 
    show scene_good_ending_ramka
    with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)

    cutscene "На заднем дворе больше не было огорода."
    cutscene "Земля растрескалась, выжили только редкие сорняки."
    hide scene_good_ending_mogoly
    hide scene_good_ending_effecty 
    hide scene_good_ending_ramka
    with dissolve
    $ renpy.pause(0.5, hard=True)

    # цг могилы с челами
        
    show scene_mogily_fon
    show scene_good_ending_chely
    show scene_good_ending_effecty 
    show scene_good_ending_ramka
    with dissolve
    $ renpy.pause(0.5, hard=True)
    cutscene "Мы подошли к четырём каменным плитам."
    cutscene "У моей смерти было много лиц, но все они были мои."
    
    # цг с букетом
    show scene_mogila_fon
    with dissolve
    $ renpy.pause(0.5, hard=True)

    show scene_mogila_buket at soft_drop(distance=200)
    cutscene "Я положил букет в середину."

    scene bg_white
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)

    # цг могилы
    show scene_mogila_fon_buket at focus_and_zoom_out(start_zoom=3.5, end_zoom=1.0, focus_x=0.38, focus_y=0.85, duration=5.0, delay=0.0)
    show scene_good_ending_effecty 
    show scene_good_ending_ramka
    with dissolve

    $ renpy.pause(5.0, hard=True)
    cutscene "Ирис,{w=0.5} Виктор,{w=0.5} Софи,{w=0.5} Дэвид."
    cutscene "Вы навсегда будете в нашей памяти."
    $ renpy.pause(1.0, hard=True)
    
    scene bg_black
    with Dissolve(3.0)

    $ renpy.pause(3.0, hard=True)
    $ unlock_achievement(ACHIEVEMENT_COMPLETE)
    $ persistent.game_completed = True
    $ renpy.save_persistent()

    call label_credits
