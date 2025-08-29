label day_5_2_1_belive:
    scene bg_black with dissolve
    pause 2.0
    $ show_space_bg("bg_room_rayan_dark")
    with dissolve
    R_t beard_on serious think "Я снова вернулся на койку."
    R_t thinking neutral "Закрыл глаза и попытался сосредоточиться."
    scene bg_black with eye_off()
    pause 1.0
    R_t beard_on "Спустя некоторое время у меня получилось настроиться."
    show screen waveform_show()
    pause 1.0
    show scene_talk_in_end_17
    with Dissolve(2)
    play sfx sfx_hiss_with_voice1 fadein 0.5 fadeout 1.0 loop

    N "Ты вернулся!"
    N "Я думала, мы больше не сможем связаться с тобой…"
    R thinking not_sure "Почему?"
    N "Ресурсы твоего тела на исходе."
    N "По расчётам наших учёных, ты не протянешь больше, чем ещё несколько дней, если останешься в аномалии."
    N "Это вопрос нескольких дней…"
    R ne_ponyal "Но где остальные мои члены экипажа?"
    R "Ещё вчера всё было в порядке… Насколько это возможно."
    R ear dissatisfied "Ирис, Дэвид, Софи, Виктор… Без них я бы точно свихнулся."
    N "Райан. Эти люди… Мы поговорим об этом позже."
    N "Не переживай о них."
    N "С ними всё В ПОРЯДКЕ!"
    N "Если ты поступишь, как я скажу — ты спасёшь… всех."
    R thinking osharashen "Какого чёрта… И кто же ты?!"
    N "Ты забыл меня?"
    N "Что ж… Я не злюсь."
    N "Я рада, что мне удалось с тобой поговорить."
    R ear surprised "Я не понимаю…"
    N "Учёные пригласили меня, потому что тональность моего голоса тебе знакома."
    N "Технология не безупречна. Их голоса не пробивались через барьер в твой разум."
    N "А со мной была хоть какая-то вероятность успеха."
    R_t thinking osharashen "Наконец я узнал её…"
    R "Элис…"
    R "Ты ждала меня всё это время? Эти два года?"
    R "Я ведь планировал отправиться всего на месяц…"
    E "Да… Это были долгие месяцы: никто не знал, что с тобой и где ты…"
    E "Когда мы поняли, что ваш корабль попал в аномалию, и смогли подключиться к камерам, я снова обрела надежду!"
    E "На твоё возвращение."
    R ear hehe "Я так скучал…"
    R_t serious angry "Я крепко сжал кулаки. Я больше не имею права раскисать как тряпка."
    R_t "Я должен найти выход."
    R think "Хорошо. Я согласен."
    R "Что я должен сделать?"
    R_t thinking ne_ponyal "Ещё некоторое время она давала мне указания. Я записывал код, который должен был заменить часть программы двигателя."
    R_t suspicious "Мне было сложно принять, что моя жизнь на исходе."
    R_t "Действовать нужно было быстро и без права на ошибку."
    hide screen waveform_show with dissolve
    stop sfx fadeout 0.5
    scene bg_black with dissolve
    pause 1.0
    scene bg_generator_blue_screen
    with dissolve
    R beard_on serious think "Так…"
    R thinking not_sure "Что там нужно было сделать в первую очередь?"
    R_t "Подсказкой мне была бумажка, которую я прихватил из каюты."
    R_t "Там я записал все указания."

    call scene_zapiska

    R_t thinking suspicious "Мне необходимо взломать систему."
    #мини игра?
    R thinking not_sure "Это похоже на какой-то лабиринт?.."
    R "Я вижу, как слабо подсвечиваются нужные пути."
    R ear smile "Наконец-то! Дело сделано."
    R thinking ne_ponyal "Так, теперь…"
    #мини игра?
    R "Здесь нужно заменить часть кода на другой."
    R suspicious "Посмотрим…"
    R ear smile "Отлично!"
    R ear neutral "Осталось совсем немного…"
    #мини игра?
    R ear surprised "Кажется, тут придётся выровнять давление в поршнях двигателя."
    R thinking suspicious "Хмм…"
    R happy "У меня получилось!"
    R_t ear smile "Даже не верится."
    pause 1.0
    scene bg_generator_red
    play sfx3 sfx_alarm2 fadein 0.5 fadeout 0.5 loop
    call scene_earthquake 
    play sfx2 sfx_earthquake_boosted fadein 0.5 fadeout 0.5 loop
    R_t beard_on thinking osharashen "Пол под ногами задрожал."
    R_t ear sick "Гул двигателя так возрос, что пришлось прикрыть уши руками."
    R_t "Аварийная тревога то включалась, то затихала."
    R_t "Система не могла распознать, почему двигатель перешёл на дополнительные мощности."
    $ renpy.music.set_volume(0.5, delay=0.5, channel="sfx3")

    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    scene bg_black with dissolve
    pause 0.5
    scene bg_coridor2_red
    with dissolve
    stop sfx fadeout 0.5

    scene bg_black with dissolve
    call scene_earthquake
    pause 0.5
    $ show_space_bg("bg_commander_block_transparent_red")
    call scene_earthquake
    with dissolve
    R_t beard_on serious think "Наконец-то дело сделано."
    R_t thinking ne_ponyal "Весь корабль трясло, но я был уверен: всё идёт так, как должно быть."
    R_t "Она так сказала."
    R_t thinking ne_ponyal "Я до сих пор не мог понять, куда делась вся команда, но что-то внутри убеждало меня — всё будет хорошо."
    R_t ear neutral "Откинувшись в кресле, я пытался переварить новую реальность."
    R_t "И ждал, когда же я смогу снова вернуться на Землю…"
    R_t serious think "Внезапно моё внимание привлекла дверь в дальнем углу помещения."
    R_t "Она была завалена коробками и частично спрятана за шкафом."
    R_t "Так как мне больше ничего не оставалось, как ждать, я решил проверить, что там."
    R_t "Разобрав беспорядок у входа, я заглянул внутрь."

    scene bg_warehouse with dissolve
    call scene_earthquake 
    R_t beard_on ear dissatisfied "Здесь было темно и сыро."
    R_t ear sick "Едкий сладковатый запах ударил мне в ноздри."
    call scene_earthquake_hard
    R_t "Корабль набрал обороты и начал прорываться сквозь кокон аномалии с такой силой, что я едва держался на ногах."
    R_t "Включив фонарик, я смог осмотреть помещение."
    #цг трупиков
    play sfx sfx_drama
    call scene_corpses
    cutscene "Кто… Все эти люди?.."
    cutscene "Это не моя команда…"
    stop sfx2 fadeout 1.0
    stop sfx3 fadeout 1.0
    pause 1.0
    $ renpy.music.set_volume(1.0, delay=0.5, channel="sfx3")
    scene bg_black
    with fade
    pause 2.0
    jump epilogue