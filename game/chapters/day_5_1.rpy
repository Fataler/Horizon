label day_5:
    # День 5 — перебивка
    scene bg_black
    with dissolve
    pause 2.0
    scene bg_room_rayan_default
    with dissolve

    R_t thinking osharashen "Я резко открыл глаза и сел на кровати."
    R_t ear surprised "Огляделся."
    R_t "Снова она, моя каюта."
    R_t neutral "И никаких следов газа в воздухе."

    scene mirror_default
    with dissolve

    R_t "Казалось, всё в порядке."
    R_t thinking ne_ponyal "Немного посиневшее лицо быстро приобрело здоровый вид."
    R_t suspicious "С этой экспедицией явно было что-то не так, и я должен это выяснить."
    R_t "Глупо скрывать, необходимо обсудить это с экипажем."
    R_t serious think "Пусть они лучше примут меня за сумасшедшего, но мы все вместе найдём решение."

    scene bg_room_rayan_default
    with dissolve

    R_t serious think "Впопыхах набросив на себя форму, полный решимости, я направился навстречу нелёгкому разговору с командой."

    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop
    scene bg_black
    with dissolve
    pause 0.5
    scene bg_coridor1_default
    with dissolve

    R_t ear sick "Шум вентиляции давил на меня, мешая сосредоточиться."
    R_t "Что я им скажу?"
    R_t surprised "Как объясню весь этот бред, что случился со мной?"
    R_t "В этот раз у меня не было сомнений, что это всё — не просто сны."

    stop sfx fadeout 0.5
    scene bg_black
    with dissolve
    pause 0.5
    scene bg_dinner_block
    with dissolve

    R_t serious think "Сегодня на кухне было на удивление тихо. Если быть точнее — никого."
    R_t ear surprised "Неужели я проспал завтрак, и все уже разошлись?"
    R_t "Почему не разбудили меня?"

    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop
    scene bg_coridor2_default
    with dissolve
    pause 2.0

    stop sfx fadeout 0.5

    scene bg_med_block
    with dissolve
    R_t ear neutral "Ирис нет."
    R_t "Может быть, она с Софи?"

    scene bg_generator_blue_screen
    with dissolve
    R_t ear neutral "Пусто…"

    play sfx3 sfx_fon_generator2 fadein 0.5 fadeout 0.5 loop
    scene bg_engine
    with dissolve
    R_t serious think "Я вошёл в помещение с двигателем, вход не был заблокирован."
    R_t "Та же тишина и пустота встретили меня."
    R_t thinking ne_ponyal "Во всём корабле как будто не было ни души."

    stop sfx3 fadeout 1.0
    scene bg_coridor1_default
    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop
    with dissolve
    R_t ear dissatisfied "Члены экипажа словно сквозь землю провалились."
    R_t thinking osharashen "Точно! Дэвид наверняка созвал собрание в командном центре."

    scene bg_coridor2_default
    with dissolve
    R_t serious think "От сердца немного отлегло, и я поспешил туда."
    R_t ear hehe "А я ведь уже успел не на шутку взволноваться."

    stop sfx fadeout 1.0
    scene bg_commander_block_transparent_default
    with dissolve
    R_t serious think "Но… И здесь я никого не застал."
    R_t "Медленным шагом я подошёл к своему рабочему месту."
    R_t thinking suspicious "Координаты те же."
    R_t "Мы стоим на месте."
    R_t neutral "Все эти дни стояли."
    R_t "Цифры менялись на такие незначительные величины, будто мы двигались вперёд-назад на крошечное, по космическим меркам, расстояние."
    R_t ne_ponyal "Вид за огромным окном… Тот же."

    play sfx sfx_heart_beat1 fadein 0.5 fadeout 0.5 loop
    show pulse_mask at alpha_mask_fade

    R_t serious fainting "Усталость сразу навалилась на меня, словно придавливая к полу."
    R_t "Сердце начало колотиться как бешеное."
    R_t ear sick "Куда они делись… И что мне теперь делать?"
    R_t "У меня оставался единственный план. Камеры видеонаблюдения."

    stop sfx fadeout 1.0
    play sfx2 sfx_steps fadein 0.5 fadeout 0.5 loop
    scene bg_black
    with dissolve
    pause 0.5
    scene bg_coridor1_default
    with dissolve
    R_t ear dissatisfied "Но что-то внутри подсказывало мне, что я не увижу там ничего хорошего."

    stop sfx2 fadeout 0.5   
    scene bg_black
    with dissolve
    pause 0.5
    scene bg_monitors_block
    show expression Solid("#fff") as overlay_light at light_hurt
    pause 2.0
    show expression Solid("#fff") as overlay_light at alpha_mask_fade_inverse
    pause 1.0
    stop sfx3 fadeout 2.0
    show expression Solid("#000000") as overlay_light at alpha_mask_fade
    pause 1.0

    R_t ear sick "Резкий свет мониторов в тёмной комнате на мгновение ослепил меня."
    R_t "Их было так много."
    R_t thinking ne_ponyal "Я бросил взгляд на один, другой, третий, в надежде увидеть хоть какое-то движение."
    R_t "Но ни на одном из них не было видно признаков жизни."
    R_t serious think "Я присел на стул в полном бессилии."
    R_t "Как взять себя в руки, когда ты один, без связи, и миллионы световых лет отделяют тебя от человечества?"
    R_t thinking neutral "Нужно проанализировать ситуацию."
    R_t not_sure "Что происходило во сне? Или — «вчера»?"
    R_t "Дэвид слетел с катушек."
    R_t ear dissatisfied "Говорил, что все мы — бесполезные неразумные дети, не способные выполнять указания."
    R_t hehe "Я усмехнулся про себя."
    #цг 18 начало
    show screen cosmos_background_screen("18")
    with dissolve
    cutscene "Это пробудило во мне воспоминания о моём дедушке."
    cutscene "В солидном возрасте с ним случилось то, чего мы все так боимся."
    cutscene "Разум начал ослабевать, деменция взяла своё."
    hide screen cosmos_background_screen
    #цг 18 конец
    #цг 17 начало
    show screen cosmos_background_screen("17")
    with dissolve
    cutscene "В периоды обострения своего недуга он начинал видеть в каждом человече своего врага."
    cutscene "Подозревал нас во всех смертных грехах."
    hide screen cosmos_background_screen
    #цг 17 конец
    #цг 14 начало
    show screen cosmos_background_screen("14")
    with dissolve
    cutscene "Одним из его любимых занятий было найти особенный повод для того, чтобы лишить нас того, что мы любим."
    cutscene "Трудно спорить с человеком, не контролирующим ход своих мыслей и не обладающим критическим мышлением."
    cutscene "Итак. Как мне помогла эта информация?"
    cutscene "Думаю, вряд ли в этом есть хоть какой-то смысл."
    hide screen cosmos_background_screen
    with dissolve
    #цг 14 конец

    play sfx sfx_morse fadein 0.5 fadeout 0.5 loop

    R_t thinking osharashen "Внезапно ход моих мыслей прервал писк."
    R_t "Это было пищание приборной панели видеонаблюдения."
    R_t "Писк не был цикличным или бездумным."
    R_t serious angry "Это… Точно было послание!"
    R_t thinking suspicious "Я взял со стола ручку и принялся настукивать в такт."
    R_t "Так… Короткий… Длинный… Короткий, короткий…"
    R_t not_sure "Это азбука Морзе."
    R_t ".-- --- - / - . -... . / -.. . .-.. .- - -..- / -. . .... ..- .--- --..-- / -.. .- ..--.. / .-- --- - / - . -... . / -.. . .-.. .- - -..- / -. . .... ..- .--- --..-- / -.. .- ..--.."
    R_t ne_ponyal "Некоторое время мне пришлось потратить, чтобы расшифровать послание."
    R_t "Кто-то пытался связаться со мной."
    stop sfx fadeout 0.5
    play sfx2 sfx_steps fadein 0.5 fadeout 0.5 loop
    scene bg_black
    with dissolve
    pause 0.5
    scene bg_coridor2_default
    with dissolve
    R_t "В послании говорилось, что мне необходимо принять сигнал. Довольно специфическим образом."
    R_t thinking ne_ponyal "И правда, я вспомнил, что слышал голос тогда, когда умирал или засыпал."
    R_t "Когда не чувствовал больше ничего."
    R_t ear dissatisfied "Нужно было рискнуть."

    stop sfx2 fadeout 0.5
    scene bg_black
    with dissolve
    pause 0.5
    scene bg_room_rayan_dark
    with dissolve
    R_t thinking neutral "Я всё думал о том, кто же мог пытаться связаться со мной."
    R_t "Это не похоже на наше обычное общение с диспетчерской на Земле."
    R_t not_sure "Или они решили сменить тактику, потому что не смогли иным образом выйти на контакт?"
    R_t ear neutral "Всё, что мне оставалось, это лежать и смотреть в потолок."
    R_t "Ждать, когда некий мифический голос свяжется со мной."
    R_t "Каким вообще образом это происходит?"
    R_t surprised "Транс? Телепатия? Моя галлюцинация?"
    R_t thinking happy "Я рассмеялся. Ну конечно же нет."
    #голос
    R_t ne_ponyal "И тут я начал слышать…"
    R_t "Далёкий… Очень тихий голос."
    R_t ear dissatisfied "Знакомый, но непонятный."
    R_t sick "Мне пришлось буквально силой разогнать все свои мысли, чтобы я мог прислушаться."

    scene bg_black
    with dissolve
    #голос
    N "Райан, приём! Ты меня слышишь?"
    N "Райан?"
    R thinking neutral "Я слышу. Кто со мной говорит?"
    N "Господи. Наконец-то."
    N "Послушай."
    N "Слушай меня внимательно."
    N "Мы уже долгое время пытаемся связаться с тобой."
    R ear surprised "Кто вы? Это диспетчер?"
    R "Как у вас это удалось? Я… Буквально разговариваю сам с собой."
    N "Сейчас это не важно."
    N "Ты застрял."
    N "Эта аномалия не даёт тебе выбраться."
    R thinking osharashen "Аномалия?"
    N "В неё невозможно зайти, и выйти из неё тоже."
    N "Всё, что сейчас находится в ней, остаётся в том же состоянии."
    N "Ничего не может измениться."
    N "Поэтому раз за разом ты… Ты умираешь…"
    R "Каким образом?!"
    N "Имея доступ к навигационному компьютеру, мы вели корабль максимально близко к краю аномалии."
    N "Тем самым запуская процесс отмотки времени назад, чтобы сохранить тебе жизнь."
    N "Мы делали это уже много… Очень много раз."
    R "А как же все остальные?"
    R "Они тоже проходят этот… цикл вместе со мной."
    R not_sure "Это длится уже… Дней пять, наверное?"
    R "Но сегодня я не смог никого найти."
    N "…"
    N "Это последствия."
    N "Нельзя слишком долго находиться там."
    N "Но мы ничего не могли сделать до этого дня."
    N "Мы были за пределами горизонта событий этой аномалии."
    N "Мы долго добивались устойчивой связи, а затем ты не мог — или не хотел — выходить на контакт."
    R osharashen "Но почему я? Вы пробовали связаться с капитаном?"
    N "…"
    N "Я расскажу тебе, как разорвать этот круг."
    R "Но…"
    N "Не перебивай."
    N "Корабль находится внутри большого кокона."
    N "Аномалия обволакивает его словно плёнка."
    N "Он пытается двигаться, но мягко бьётся об эту оболочку. Не может её преодолеть."
    N "Ускорь генератор и выведи двигатель на максимум, внедрив фрагмент кода, который я продиктую."
    N "К сожалению, у нас нет возможности прислать его тебе файлом."
    N "Это чудо, что вообще удалось связаться с тобой."
    R serious angry "Всё это звучит как какой-то бред. Я должен обсудить это с Дэвидом."
    N "…"
    N "О каком Дэвиде ты вообще говоришь?"
    N "Уже два года мы наблюдаем за тобой по камерам."
    N "В твоей экспедиции не числилось никого с именем Дэвид."

    scene bg_room_rayan_dark
    play sfx sfx_heart_beat1 fadein 0.5 fadeout 0.5 loop
    
    R_t serious angry "Я резко открыл глаза. Сердце яростно застучало, словно хотело вырваться из груди."
    R_t think "Сигнал был потерян."


    R_t serious fainting "На дрожащих ногах я подошёл к зеркалу."
    #цг бородатого
    scene mirror_dark
    with dissolve
    R_t beard ear surprised "Оттуда на меня смотрел уставший мужчина, обзаведшийся некоторыми морщинами, парой шрамов и щетиной."
    R_t serious angry "Неужели это всё правда…"
    stop sfx fadeout 0.5
    menu:
        "Поверить спасителю и возобновить контакт":
            jump day_5_2_1_belive

        "Не идти на поводу у подозрительного голоса":
            jump day_5_2_2_dont_belive
