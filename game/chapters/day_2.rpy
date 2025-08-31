label day_2:
    # "День 2"
    pause 1.0
    scene bg_black
    with dissolve
    play sfx sfx_crunch_whoosh
    call test_clock(start_time="22/43/00")
    scene bg_black
    with dissolve
    $ renpy.force_autosave()
    pause 1.0
    $ show_space_bg("bg_room_rayan_dark")
    pause 1.0

    #music
    play music music_quite_ambient fadein 1.0 loop

    R_t ear sick "По ощущениям я проснулся довольно рано."
    R_t "С трудом разлепил глаза — получилось лишь после нескольких попыток протереть веки пальцами."

    play sfx click2
    pause 0.2
    play sfx click2

    R_t surprised "Ночник не работал."
    R_t serious think "Я сел на кровати и уставился на стену, с которой на меня в ответ смотрели многочисленные плакаты."
    R "Музыка, которую я слушал в прошлой жизни."

    play sfx sfx_steps_short fadeout 2.0

    R_t "Со стороны коридора то и дело были слышны шаги коллег, которые тоже проснулись и спешили на кухню."
    R_t ear sick "Почему-то я не мог собраться с мыслями."
    R_t "Всю ночь мне снились странные сновидения."
    R_t surprised "Диверсия, тотемы, убийство капитана…"
    R_t thinking suspicious "Какие тотемы на космическом корабле? Это больше про крипипасты с форумов."
    R_t ear hehe "Я усмехнулся."
    R_t "Напугать меня таким — всё ещё за гранью возможного. Это же полный абсурд."
    R_t dissatisfied "Но всё же я чувствую себя немного не в своей колее."
    R_t "Возможно, мне просто не хватает сегодняшней дозы кофе."
    R_t thinking neutral "Я прикрыл глаза и улыбнулся."
    R_t "Тот сублимированный кофе, что у нас есть на корабле, никогда не сравнится с моим домашним."
    R_t "Когда-то давно я просыпался от запаха обжаренных зёрен с лёгким привкусом гари от конфорки старой газовой плиты."
    R_t ear hehe "Это был своеобразный знак: пора надевать тёплые тапки, набрасывать плед и выползать на небольшую веранду."
    R_t "Это значило, что мой старший брат сварил свой фирменный напиток."
    R_t "До школы оставалось немного времени — я садился на влажную после ночного ливня скамейку у выхода из дома."
    R_t "И просто смотрел на океан."
    R_t "Дедушка, как обычно, раскуривал свою трубку, забитую доверху ароматным табаком."
    R_t "Этот запах всегда щекотал мне нос, но был, по-своему, родным."
    R_t thinking ne_ponyal "Что ж, когда-нибудь, может быть, я вернусь туда."
    R_t suspicious "Ну а пока с домом меня разделяет бесконечная космическая пустота."
    R_t serious think "Пора приниматься за работу."
    R_t "В комнате было довольно душно — нужно было немного освежиться."

    call scene_mirror_dark

    cutscene "Поэтому, как обычно, я решил начать утро с созерцания своего хмурого лица."
    play sfx click2
    cutscene "Но лампа у зеркала с умывальником не работала."
    play sfx click2
    pause 0.2
    play sfx click2
    cutscene "Я проверил остальные приборы — никаких признаков жизни."
    cutscene "Опять выбило генератор."
    cutscene "Бывает."

    scene black with dissolve
    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    pause 1.0
    scene bg_coridor1_dark
    show expression Solid("#000000") as overlay_light at alpha_mask_fade_inverse1(0.6)

    R_t serious think "Толком не умывшись, не причёсываясь и собравшись впотьмах, я вышел в коридор."
    R_t ear sick "Если бы не фонарь, который я ношу с собой, пришлось бы двигаться, перебирая руками по стене."
    R_t neutral "Благо, вдалеке был виден лёгкий свет на кухне."
    R_t "Значит, ребята уже собрались."
    R_t hehe "Об этом говорил и запах разогретой пищи."

    stop sfx fadeout 2.0
    scene black with dissolve
    pause 0.5
    #music не сильно тревожная
    stop music fadeout 1.0

    play music2 music_kitchen_daily fadein 0.5 loop
    scene bg_dinner_block_dark with dissolve
    show i profile neutral right at left
    show v profile neutral left at right
    play sfx2 sfx_talk_people fadein 0.5 fadeout 0.5 loop
    R_t neutral "За столом сидели Виктор и Ирис."
    R_t "Дэвида и Софи нигде не было видно."
    R_t "Между коллегами уже завязался разговор."

    show v smile

    R_t "Радист увлечённо что-то рассказывал, тыкая пальцем в экран планшета, а врач внимательно слушала и кивала."
    
    show i tricky at giggle
    show v at fear
    play sfx sfx_laugh_people
    R_t "Периодически они смеялись."
    play sfx3 sfx_steps_two
    R_t serious think "Я подошёл к столу."
    stop sfx2 fadeout 0.5
    show i pen nervous_laughter

    R_t "Ирис обратила на меня внимание."
    I "Ну привет, засоня!"
    I "Проспал свою очередь включать генератор."
    R ear hehe "Доброго утречка."

    show v pockets dream

    R_t "Виктор был в хорошем настроении и широко улыбнулся:"
    V think "Дэв повёл Софи устранять поломку и теперь стоит там у неё над душой!"
    I normal ridicule "Наконец-то никто не воняет здесь своими спиртовыми растворами."
    R_t thinking neutral "Мне даже показалось, что я почувствовал этот щекочущий ноздри запах, но это было лишь наваждение."
    
    show i pen neutral
    
    V happy "Ладно тебе, расслабься!"
    V "Скоро мы выйдем из темноты на свет, нужно всего лишь немного подождать."

    show v ruki tricky with dissolve

    R_t "Он завёл руки за голову и расслабленно откинулся назад."

    scene bg_dinner_block
    show i pen ozadachen right at left
    show v ruki puzzled left at right
    play sfx sfx_light_on
    #$ renpy.music.set_volume(0.5, delay=0, channel="sfx2")
    play sfx2 sfx_fon_generator2 fadein 0.5 fadeout 1.0 loop
    pause 1.0

    R_t not_sure "В этот момент появилось электричество, и в помещении снова стало приятно находиться."
    
    show i normal neutral_happy
    V tricky "Вот видишь?"
    pause 1.5

    $ renpy.music.set_volume(0, delay=0.5, channel="music2")
    scene bg_dinner_block_dark
    show i profile ahui right at left
    show v ruki osharashen left at right
    stop sfx2
    #$ renpy.music.set_volume(1.0, delay=0, channel="sfx2")
    play sfx sfx_electrisity1
    pause 1.5
    play sfx2 sfx_power_down fadein 0.5

    pause 1.0

    R_t thinking osharashen "Не успел Виктор победно оскалиться, как энергия снова пропала."
    R_t "С громким, страшным треском."
    I osharashen "Кажется, там что-то бахнуло внизу."
    I "Может, стоит глянуть?"
    V pockets nedovolen "Думаю, они смогут разобраться сами."

    show i normal neutral

    V ruki puzzled "Нам тоже необходимо заниматься своими делами."
    #sfx водичька
    #music 
    $ renpy.music.set_volume(1.0, delay=0.5, channel="music2")
    R_t serious think "Я налил себе невкусного пресного кофе и потягивал его маленькими глотками."
    V pockets dream "Райан, представляешь, я сегодня поймал сигнал."
    V "Правда, не уверен, что он действительно что-то значит — очень уж похоже на обычный космический шум."
    
    show v at giggle
    play sfx sfx_laugh_men1
    pause 0.5

    R_t "Радист рассмеялся:"
    V think "Мне даже на секунду показалось, что в записи был чей-то зов."


    I ridicule "Ты и вчера слышал, что «кто-то звал». Это был холодильник."

    show v ruki tricky at giggle
    show i neutral_happy at fear
    play sfx sfx_laugh_people
    #r smile
    R_t "Коллеги заулыбались."
    R serious think "Не забивай этим голову, я уверен, мы найдём базу и без точных координат."
    R ear hehe "Ведь с вами я."

    show i profile neutral

    V pockets sorry "Да, естественно. Тем более, я пока не могу его проанализировать."
    R_t thinking ne_ponyal "Виктор показал пальцем на чёрный экран планшета:"
    V "Он разряжен, и подключать его к аварийному питанию нельзя: оно только для критических модулей."
    R_t serious think "Мне оставалось только пожать плечами."
    R "Уверен, скоро всё починят."
    V ruki puzzled "Ах да, я должен передать новости."
    V sad "Основного сигнала я так и не смог поймать. Всё ещё движемся по изначальным координатам."
    R thinking suspicious "Правильно ли понимаю, что с аварийным питанием мы можем двигаться только на автопилоте?"
    I pen sad "Да, командир сказал, что на данный момент мы ничего не можем сделать."
    R neutral "Что ж… Схожу, навещу Дэвида и Софи."
    R_t serious think "Я попрощался с коллегами, взял свою чашку с кофе и направился в сторону генераторной."
    
    play sfx steps
    #фон бокового коридора
    stop music2 fadeout 1.0
    scene black with dissolve
    pause 1.0

    scene bg_coridor3_red_cylinders with dissolve
    play sfx2 sfx_metal_hits_grinding fadein 0.5 fadeout 0.5
    stop sfx fadeout 1.0

    R_t serious neutral "Ещё на подходе к отсеку с генератором я услышал стук металла, скрежет и тихие разговоры."

    #music
    play music music_Xtonicheskoe_fon loop
    scene bg_generator_red
    show s ruki ozadachen left at right
    show d serious neutral right at Transform(xalign=0.5, yalign=1.0)
    with dissolve
    stop sfx2 fadeout 1.0
    play sfx3 sfx_alarm3 fadein 0.5 fadeout 0.5 loop

    R_t "Внутри, при красном свете аварийной лампочки, находились механик и командир."
    #R_t "Всё помещение было заставлено разного вида баллонами, банками, бутылками с разными жидкостями, а рядом с членами экипажа на полу лежали инструменты."
    show d serious calm left at move_on_scene(1.5, 0)
    play sfx sfx_steps_two
    R_t "Софи перебирала бутыли с очень озадаченным видом, а Дэвид ходил из стороны в сторону, сердито хмурясь."
    show d right at move_on_scene(1.5, 0.5)
    play sfx sfx_steps_two
    R_t "Они ещё не заметили моего присутствия."
    show d neutral left at move_on_scene(1.5, 0)
    play sfx sfx_steps_two
    D "Ну как же так получилось, что мы до сих пор не определили, в чём неисправность?"
    show d right at move_on_scene(1.5, 0.5)
    play sfx sfx_steps_two
    S shy worried "Судя по показателям, генератор перегревается и переходит в режим минимальной аварийной поддержки, но почему…"
    show d serious calm left at move_on_scene(1.5, 0)
    play sfx sfx_steps_two
    D "Я всё проверил: вентиляция работает исправно, охлаждающей жидкости достаточно."
    show d fear right at move_on_scene(1.5, 0.5)
    play sfx sfx_steps_two
    D "Если мы не исправим это в ближайшее время, можем не долететь до точки назначения. Это очень важно."
    show d calm left at move_on_scene(1.5, 0)
    play sfx sfx_steps_two
    D "Единственная странность, которую я заметил, — жидкость слишком быстро испаряется."
    show d right at move_on_scene(1.5, 0.5)
    play sfx sfx_steps_two
    R_t "К тому моменту, как он это сказал, я уже подошёл к ним вплотную."
    show d left at move_on_scene(0.75, 0.25)
    play sfx sfx_steps_two
    pause 0.5
    show d serious osharashen at fear
    pause 1.0
    D serious osharashen "Тьфу ты, в этой темноте ничего не разглядишь."
    D fist smug "Привет, Райан."
    R_t ear hehe "Я забавно помахал ему рукой."
    R "Здравствуй, кэп."
    R thinking ne_ponyal "Вижу, у вас здесь какие-то трудности?"

    show s ruki calm with dissolve

    R_t "Софи горько вздохнула."
    show d right
    D angry "Кто бы мог дать мне ответ, почему испарение жидкости в камере охлаждения происходит так быстро?"
    R "Давайте проверим."
    R_t suspicious "Я взглянул на прозрачный люк рядом с местом, где стояла Софи."
    R_t "Где-то внизу, в слегка освещённой камере, плескалась вода."
    R_t "Конечно же, это была не обычная H2O, а состав, поддерживающий правильный температурный режим у самого главного элемента нашего корабля — генератора."
    R_t neutral "Люк выглядел вполне заполненным, но даже сквозь обувь я чувствовал, как пол обжигает ступни."
    R not_sure "Думаю, нам необходимо открыть люк и взять пробу для проверки."

    stop music fadeout 1.0
    play music2 music_Xtonicheskoe_creepy loop
    show s shy nedovolen at fear
    show d serious osharashen

    S "Ни в коем случае!"
    S "Нельзя часто открывать люк, иначе нарушатся условия эксплуатации жидкости."

    show s shy nedovolen

    S "Только я могу открывать его — и только для дозаполнения."
    
    show d serious calm
    
    R_t thinking osharashen "Дэв нахмурился, но промолчал."

    show s shy worried

    R serious think "Хорошо. В таком случае скажи, чем я могу тебе помочь?"
    R "Пока нет основного источника энергии, я, как навигатор, бесполезен."
    R_t "Софи покачала головой."
    S ruki calm "Увы, сейчас мне нужно просто немного времени."

    show s profile neutral

    R_t "Она взяла тряпку, окунула её в небольшой баллон и принялась протирать внешний корпус генератора."
    R_t thinking ne_ponyal "Я потянулся к баллону, чтобы посмотреть его состав, но девушка внезапно вспылила."

    show s ruki crazy at angry
    show d serious osharashen

    S "Перестаньте следить за мной! Я просто делаю свою работу."
    R_t "Лицо её выражало ярость."
    R_t thinking osharashen "Я опешил от такой реакции."
    R_t "Возможно, некоторые люди не любят, когда наблюдают за их действиями — это можно понять."

    show d calm with dissolve
    pause 0.5
    stop music2 fadeout 2.0

    show d left at exit_left

    play sfx sfx_steps_short

    R_t serious think "Пожав плечами, я пошёл на выход. Дэвид догнал меня."
    R_t "Мы ничего не сказали друг другу, но обменялись многозначительными взглядами."

    stop sfx3 fadeout 0.5
    scene black with dissolve
    pause 0.5
    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    #music
    play music music_daily fadein 0.5 loop
    scene bg_coridor3_dark_cylinders 
    show d serious neutral right at left
    with dissolve

    R_t serious think "Уже двигаясь по коридору, кэп нарушил тишину."
    D calm "Я немного припугнул её этим «не долетим»."
    D neutral "Долетим, конечно, запас пока есть. Если проблема только в нём, конечно."
    R_t "Я кивнул."
    R thinking suspicious "Тебе не кажется странным её поведение?"
    R "Я не склонен обвинять людей, но она выглядит совершенно некомпетентной."
    R "Если бы это была не космическая миссия, а, скажем, обычная работа, я бы предположил, что она дочка начальника, устроенная по блату."
    show d calm with dissolve
    pause 0.5
    R_t "Дэв вздохнул."
    D "По досье у неё всё в порядке. Она механик с очень большим стажем."
    D neutral "Предполагаю, проблема в характере — с этим ничего не поделать."
    stop sfx fadeout 0.5
    R_t serious think "Мы дошли до развилки."
    D "Я пойду в командный отсек, мне нужно заполнить бортовой журнал."
    R thinking not_sure "А у меня снова разыгрался аппетит. Не отказался бы от большого прожаренного стейка… ну или хотя бы пасты с его вкусом."
    
    play sfx2 sfx_laugh_men1
    show d happy at giggle
    
    R_t "Дэвид рассмеялся."
    D "Шагом марш на кухню!"
    R_t "Я решил подыграть и вскинул руку к виску."
    R ear hehe "Есть, сэр!"
    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop
    R_t "На этом моменте каждый пошёл своим путём."
    
    stop sfx fadeout 0.5
    scene black with dissolve
    pause 0.5
    scene bg_dinner_block_dark
    show i smoke calm right at left
    show v profile smile left at right
    with dissolve

    R_t serious think "На кухне всё ещё сидели Ирис и Виктор."
    R_t "Это было неожиданно, но они играли в карты."
    R_t thinking ne_ponyal "Предметом их азартного спора стал единственный оставшийся тюбик со вкусом оливье."
    R_t "Ещё некоторое время я наблюдал за их игрой, затем долил себе кофе и вернулся на своё рабочее место."

    stop music fadeout 0.5
    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    scene black with dissolve
    stop sfx fadeout 0.5
    pause 1.0
    $ show_space_bg("bg_commander_block_transparent_dark")
    pause 1.0
    play sfx sfx_power_up fadeout 2.0
    $ show_space_bg("bg_commander_block_transparent_default")
    pause 0.2
    $ show_space_bg("bg_commander_block_transparent_dark")
    pause 0.2
    $ show_space_bg("bg_commander_block_transparent_default")
    pause 0.2

    R_t thinking ne_ponyal "Свет в кабине пару раз моргнул и наконец устаканился. Похоже, Софи справилась."
    R_t suspicious "Сверив показания приборов с картами, я убедился, что мы движемся в верном направлении."
    R_t "Никаких видимых препятствий на пути я не обнаружил."
    R_t serious think "Это значило, что я мог расслабиться, откинуться в кресле и любоваться красотой."

    #фон космос
    show cosmos_fon
    with dissolve
    stop sfx
    stop sfx2 fadeout 2.0

    #music Anxious space ambient
    play music music_waves fadein 1.0 fadeout 0.5 loop
    play music2 music_theme_cosmos fadein 1.0 fadeout 0.5 loop

    cutscene "Сегодня космическая гладь особенно завораживала: она переливалась цветами, и чем дольше я вглядывался, тем отчётливее видел за иллюминатором волны."
    
    $ renpy.music.set_volume(1.0, delay=0.5, channel="sfx")

    #цг 11 начало
    $ show_scene_cosmos("11")
    cutscene "Большие волны, полные пены и морской соли."
    cutscene "Свежий лёгкий запах тины и мокрого песка."
    cutscene "Сделав очередной глоток разбавленного ароматного кофе, я вспомнил брата."
    $ hide_scene_cosmos()
    #цг 11 конец
    #цг 4 начало
    $ show_scene_cosmos("4")
    cutscene "Он всегда был для меня эдакой отцовской фигурой."
    cutscene "Большей частью своего воспитания я обязан ему."
    cutscene "Отец и мать часто были заняты на работе. На матери также лежали все хлопоты по дому и забота о моей болезненной младшей сестре."
    cutscene "Им было совсем не до маленького меня — я был предоставлен самому себе."
    $ hide_scene_cosmos()
    #цг 4 конец
    #цг 3 начало
    $ show_scene_cosmos("3")
    cutscene "Первая поездка на велосипеде, первая пойманная рыба, первая двойка в школе, первый морской узел…"
    cutscene "Он всегда был рядом и помогал, чем мог."
    cutscene "До определённого момента."
    cutscene "Я зажмурился и потер рукой переносицу."
    cutscene "Мне неприятно вспоминать этот этап жизни нашей семьи."
    cutscene "Но слов из песни не выкинешь."
    $ hide_scene_cosmos()
    #цг 3 конец 
    #цг 2 начало
    $ show_scene_cosmos("2")
    cutscene "Когда брату исполнилось девятнадцать, он попал под дурное влияние."
    cutscene "Так же, как и я, он нуждался в наставнике — крепком мужском плече, которое вовремя наставит на путь истинный."
    cutscene "Такой человек нашёлся, но верным этот путь назвать сложно."
    cutscene "Брат с головой ушёл в оккультизм."
    cutscene "Всё чаще мы находили у себя дома странные предметы: кости животных, клочки волос."
    cutscene "На все вопросы брат лишь раздражённо отнекивался."
    $ hide_scene_cosmos()
    #цг 2 конец 
    #цг 1 начало
    $ show_scene_cosmos("1")
    cutscene "Всё чаще он стал пропадать вне дома, и всё чаще я замечал, как он прячет руки."
    cutscene "Однажды, подглядев за ним в щель двери его комнаты, я увидел, что его тело покрыто ранами и ссадинами."
    cutscene "Он словно превратился в совсем другого человека."
    cutscene "Глаза глубоко запали и начали нездорово блестеть, руки стали дрожать."
    cutscene "Из открытого и добродушного человека он превратился в нервную, суеверную тень прошлого себя."
    cutscene "На несколько лет мы потеряли его из виду."
    cutscene "Я тяжело переживал этот период: неизвестность давит больше всего."
    cutscene "Лишь спустя несколько месяцев после его исчезновения мы получили письмо."
    cutscene "Он просил нас не беспокоиться о нём: работает при общине."
    cutscene "На благо их собственной веры."
    $ hide_scene_cosmos()
    #цг 1 конец
    #цг 10 начало
    $ show_scene_cosmos("10")
    cutscene "Она захлестнула его с головой, как волны, что разбивались о берег у нашего дома и тащили всё, до чего могли дотянуться, в тёмные глубины океана."
    cutscene "Как и эти звёзды, зовущие меня окунуться и плыть в просторах космоса."
    $ hide_scene_cosmos()
    #цг 10 конец

    scene bg_commander_block_default
    $ show_space_bg("bg_commander_block_transparent_default")
    stop music fadeout 1.0
    stop music2 fadeout 1.0

    R_t thinking ne_ponyal "За всеми этими размышлениями я не заметил, как в помещении стало очень жарко."
    R_t "По ощущениям, воздух нагрелся градусов на десять."
    R_t "Становилось трудно дышать."
    R_t "Необходимо было проверить, что происходит."

    $ show_space_bg("bg_commander_block_red")
    play sound sfx_alarm2 fadein 0.5 fadeout 0.5 loop
    play music music_nervous_ambient loop

    R_t thinking osharashen "Только я встал со своего кресла, как включилась аварийная тревога."

    play sfx2 sfx_steps_fast fadein 0.5 fadeout 2.0 loop

    R_t "Ускорив шаг, я выбежал в коридор."

    $ hide_space_bg
    scene black 
    with dissolve
    $ renpy.music.set_volume(0.3, delay=0.5, channel="sound")
    stop sfx2 fadeout 1.0
    pause 0.5
    #анимация аварийной тревоги coridor1
    #music
    scene bg_coridor1_red with dissolve
    show i profile ahui right with dissolve
    R_t serious angry "Сразу на выходе я заметил Ирис."
    show i at center, shaky
    pause 2.0
    play sfx sfx_fall_body
    show i oooops at down_little with dissolve
    R_t "Лицо её покраснело, девушка держалась рукой за стену, ноги подкосились."
    R thinking osharashen "Ирис!.. Всё в порядке?"

    show i at center
    show i normal bychit at move_vertically(yalign1=1.1) with dissolve

    R_t serious angry "Я подхватил её под локоть, стараясь удержать, но она уже не стояла на ногах."
    
    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop
    show i profile oooops with dissolve
    R_t "Перекинув её руку через своё плечо, я потащил её к ближайшему аварийному пункту."
    R_t very_angry "Некоторое время мы передвигались так. Я старался реже вдыхать раскалённый воздух, чтобы не обжечь гортань и лёгкие."
    
    stop sfx
    
    R_t think "Лишь добравшись до ближайшего пункта, я смог раздобыть для себя и Ирис по маске с баллонами с более-менее прохладным воздухом."
    
    play sfx sfx_steps_fast fadein 0.5 fadeout 0.5 loop
    
    R_t "После этого я побежал в сторону генератора."

    R_t "Ирис, пришедшая в сознание, медленно двинулась за мной."

    hide i with dissolve

    #фон генераторная анимация тревоги
    stop sfx fadeout 0.5
    scene bg_generator_red
    show s shy angry right at center
    show d serious angry left at Transform(xalign=1.0, yalign=1.0)
    show v profile angry right at Transform(xalign=0.15, yalign=1.0)
    with dissolve
    $ renpy.music.set_volume(1.0, delay=0.5, channel="sound")
    show i profile osharashen right at Transform(xalign=-0.2, yalign=1.0) with dissolve

    R_t serious think "Здесь уже находились остальные члены экипажа."

    show s ruki crazy at angry
    show d at fear

    R_t angry "В середине помещения происходила жаркая перепалка."
    R_t "Из-за громкого звука аварийной тревоги я едва мог расслышать слова."
    R_t "Вокруг стояли пустые баллоны с охлаждающей жидкостью, а люк в полу был открыт."
    R_t "Судя по гаечному ключу в руках командира, он распахнул его сам, вопреки недавнему предупреждению механика."
    
    show s shy angry at angry
    
    R_t "Софи кричала на Дэвида и активно жестикулировала."

    show d at angry

    R_t "Он же грубо пытался схватить девушку и показывал пальцем в сторону генератора."
    R_t "До меня доносились обрывки их речи:"
    S ruki crazy "Грязный… {w=1.0} Обезвредить… {w=1.0} Вирус… {w=1.0} Очистить…"
    R_t "Виктор тоже был здесь."

    show v pockets suspects

    R_t think "Жестами радист подозвал меня поближе и показал пальцем на баллон."
    R_t "На нём красовалась надпись «Спирт»."
    R_t thinking osharashen "Я округлил глаза и в ошеломлении наблюдал за перепалкой механика и командира."
    R_t "На кой чёрт добавлять спирт в уже запатентованный рабочий охлаждающий состав?.."
    R_t "Немудрено, что он мгновенно испарялся."

    show d fist angry at angry, move_step(-100, 0.2)
    pause 0.15
    play sfx sfx_steps_fast_two
    show s shy surprised at fear, move_step(-50, 0.2)

    R_t "В какой-то момент командир замахнулся рукой, чтобы ударить Софи, та попыталась уклониться."

    show v nedovolen
    R_t serious fainting "От жара становилось плохо, маска не помогала."

    play sfx sfx_steps_two
    show d annoyed right at move_step(50, 0.3)

    R_t "Дэвид развернулся и попытался пойти в сторону генератора."

    play sfx sfx_steps_fast_two
    show s nedovolen at move_step(250, 0.3, 1)
    pause 1.0
    play sfx sfx_steps_two
    show s at Transform(xalign=0.7, yalign=1.0), move_step(-30)
    show d at move_step(-30)

    R_t think "Софи вцепилась в его руку и старалась тащить назад."

    play sfx sfx_steps_fast_two
    show d angry left at move_step(50), angry
    show s ruki hurt at move_step(-50), fear

    R_t "Разъярённый капитан резко отмахнулся от неё."

    play sfx sfx_steps_two
    show d at move_step(-50)
    show s shy surprised at Transform(xalign=0.65, yalign=1.0), move_step(-50), fear

    R_t "Шаг. Ещё шаг."

    play sfx sfx_steps_two
    show d angry at move_step(-50)
    show s ruki hurt at Transform(xalign=0.6, yalign=1.0), move_step(-50), fear
    pause 1.5
    stop music fadeout 1.0
    show s shy surprised at jump(height=1000)
    play sfx2 sfx_scream_women_ah
    pause 0.5
    play sfx sfx_water_splash
    hide s with dissolve
    show v ruki osharashen
    
    show d serious osharashen
    R_t angry "И девушка упала в открытый люк."

    play sfx sfx_steps_fast_two
    show v profile angry at move_step(300), fear

    R_t "Медлить было нельзя. Мы с Виктором бросились к люку."

    $ renpy.music.set_volume(0.3, delay=0.5, channel="sound")

    #music
    play music music_anxiety loop
    call scene_sofi_tonet

    scene bg_generator_red 
    show i profile ahui right at Transform(xalign=-0.15, yalign=1.0)
    show v profile crazy right at Transform(xalign=0.4, yalign=1.0)
    show d serious osharashen left at Transform(xalign=0.9, yalign=1.0)
    with dissolve
    pause 1.0
    play sfx sfx_steps_fast_two
    show d fist angry at move_step(-200), angry
    show v pockets angry at move_step(-100), fear
    pause 1.0
    play sfx sfx_heat_metal

    R_t think "Дэвид резко откинул нас с Виктором от люка и запер крышку."
    #music стресс
    show v at fear
    R angry "Что ты делаешь?"

    show d at Transform(xalign=0.9, yalign=1.0), angry

    D serious fear "Мы не можем терять время! Иначе мы все погибнем! Забудь про неё!"
    V ruki osharashen "Что?.."

    show d at Transform(xalign=0.9, yalign=1.0), angry

    D "Генератор! Помогите мне, нам нужно его охладить!"
    play sfx sfx_evaporating_water
    show d fist angry at move_step(50)
    R_t "Он вскрыл баллон с составом и попытался вылить его прямо на огромную, пышущую жаром машину."
    V pockets nedovolen "Ты уверен, что это поможет?!"
    D serious calm "Я… Я уже ни в чём не уверен!"

    play sfx sfx_evaporating_water

    R_t "Я вскрыл второй баллон и вылил его с другой стороны генератора."
    R_t think "На мгновение показалось, что это помогло."
    R_t "Возможно, мы хотели, чтобы это было так."
    R_t ear dissatisfied "Температура в помещении всё росла и росла."

    play sfx sfx_alarm3 fadein 0.5 fadeout 0.5 loop

    R_t "На датчике генератора она достигла критической отметки."

    stop music fadeout 0.5
    show v ruki osharashen
    show d osharashen
    R_t thinking osharashen "Не сразу, но мы почувствовали запах гари."
    R_t "Огонь?.."
    R_t "Секунда{w}, две."

    R_t "И генератор вспыхнул ярким огнём."
    
    stop sound fadeout 1.0
    show expression Solid("#b12300") as overlay_light at alpha_mask_fade(1.0)
    play sfx sfx_explosion
    pause 2.5
    play sfx2 sfx_burning_fire fadein 0.5 fadeout 1.0 loop

    #цг огонь взрыв
    call scene_fire

    R_t serious fainting_blood "Жаркий воздух и вентиляция мгновенно разнесли искры по помещению."
    play sfx3 sfx_cough_man2
    R_t "Я больше не мог сдерживаться и зашелся в удушающем кашле."
    R_t "Кажется, мы не успели…"
    R_t serious fainting_blood "Я потерял сознание."

    play sfx sfx_fall_body
    stop sfx2 fadeout 1.0
    scene bg_red with dissolve
    pause 1.0
    show scene_talk_in_end_18
    with Dissolve(2)
    pause 2.0

    show screen waveform_show()
    with dissolve

    play sfx sfx_hiss_with_voice1 fadein 0.5 fadeout 1.0
    
    R_t serious fainting_blood "И снова этот уже знакомый голос:"

    N "Опять… Ну что же ты, давай, давай… Ты же слышишь меня?.."
    hide screen waveform_show
    scene bg_black with dissolve
    stop sfx fadeout 1.0
    $ renpy.pause(0.5, hard=True)
    $ unlock_achievement(ACHIEVEMENT_ELECTRIC)
    $ renpy.pause(1.0, hard=True)
    with dissolve
    $ renpy.force_autosave()
    jump day_3
