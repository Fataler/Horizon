layeredimage viktor_scene:
    always:
        "images/CG/CG Victor shooting/2.png"
    always:
        "images/CG/CG Victor shooting/1.png"
        at fade_in_out(0.5)

label scene_viktor:
    show viktor_scene
    with dissolve
    #Выбор:
    menu:
        "Побежать и обезвредить Виктора":
            hide viktor_scene
            with dissolve

            show layer master at screen_step_zoom(zoom1=1.0)
            R_t serious angry "Я резко двинулся в сторону безумца."

            show v crazy_down

        "Выстрелить":
            hide viktor_scene
            with dissolve

            R_t serious angry "Я резко достал пистолет из кобуры."
            R_t "Пистолет Дэвида."

            #цг CG Victor shooting
            R_t "Наставив дуло на радиста, я процедил:"
            R serious very_angry "Сложи руки за головой, иначе я буду вынужден выстрелить!"
            R serious angry "Я не хочу этого, но не позволю тебе сорвать нашу экспедицию."

            show v at giggle
            play sfx sfx_laugh_men2
            pause 0.5

            R_t "Виктор лишь рассмеялся и продолжил бормотать какие-то несвязные вещи."
            
            show layer master at screen_step_zoom(zoom1=1.0)
            play sfx sfx_steps_two

            R_t very_angry "Я начал медленно приближаться к нему." 

            show layer master at screen_step_zoom(zoom1=1.025)
            play sfx sfx_steps_two

            R_t "Шаг за шагом."

            show layer master at screen_step_zoom(zoom1=1.05)
            play sfx sfx_steps_two

            R_t angry "Он не проявлял агрессии. Уже на подходе я выдохнул и ослабил внимание."

            show v crazy_down

            R_t "Радист сидел на полу, растирая кровь по рукам."
            R_t "Он поднял голову."

            show v crazy

            R_t "Казалось, я никогда не забуду этот взгляд."
            R_t "Взгляд, полный отчаяния."
            R_t angry "Рука дрогнула — разбираться не было времени: так или иначе, передо мной был убийца."
            R_t "Я снова направил на него оружие."
            R_t "Но Виктор был быстрее."

    show layer master at screen_shake
    R_t very_angry "Лезвие блеснуло во мраке. Инстинктивно я уклонился, но это было ошибкой."
    R_t "Он не целился в меня."
    
    play sfx sfx_hit
    show v at angry

    R_t "С размаху Виктор ударил ножом в открытый отсек двигателя с множеством разноцветных проводов."
    
    stop sfx3 fadeout 0.5
    play sfx sfx_electrisity1 fadeout 0.5
    pause 1.0
    play sfx sfx_explosion
    pause 1.0
    scene bg_white with dissolve
    pause 1.0

    R_t serious fainting_blood "Я успел услышать лишь жуткий треск и увидеть яркую вспышку, как в глазах потемнело."

    scene bg_black
    with fade
    #возможно цг

    show screen waveform_show()
    R_t serious fainting_blood "Сквозь темноту я услышал тихий женский голос:"

    play sfx sfx_hiss_with_voice1 fadein 0.5 fadeout 1.0
    

    N "Нет, так не должно быть… Необходимо вернуть в исходную точку…"
    hide screen waveform_show

    stop sfx fadeout 1.0

    return
