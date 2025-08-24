label day_2:
    # "День 2"
    scene bg_black
    with dissolve
    pause 1.0
    scene bg_room_rayan_dark
    with dissolve
    pause 1.0

    R_t ear sick "По ощущениям я проснулся довольно рано."
    R_t "С трудом разлепил глаза — получилось лишь после нескольких попыток протереть веки пальцами."

    play sfx click2
    pause 0.2
    play sfx click2

    R_t surprised "Ночник не работал."
    R_t serious think "Я сел на кровати и уставился на стену, с которой на меня в ответ смотрели многочисленные плакаты."
    R "Музыка, которую я слушал в прошлой жизни."

    play sfx sfx_steps

    R_t "Со стороны коридора то и дело были слышны шаги коллег, которые тоже проснулись и спешили на кухню."
    
    stop sfx fadeout 1.0

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
    R_t ear hehe "Это был своеобразный знак: пора надевать тёплые тапки, набрасывать на себя плед и выползать в сторону небольшой веранды."
    R_t "Это значило, что мой старший брат сварил свой фирменный напиток, и оставалось ещё немного времени перед школой, чтобы сесть на влажной после ночного ливня деревянной скамейке у выхода из дома и полюбоваться океаном."
    R_t "Дедушка, как обычно, раскуривал свою трубку, забитую доверху ароматным табаком."
    R_t "Этот запах всегда щекотал мне нос, но был, по-своему, родным."
    R_t thinking ne_ponyal "Что ж, когда-нибудь, может быть, я вернусь туда."
    R_t suspicious "Ну а пока с домом меня разделяет бесконечная космическая пустота."
    R_t serious think "Пора приниматься за работу."
    R_t "В комнате было довольно душно — нужно было немного освежиться."

    #цг гг смотрит в зеркало
    R_t ear neutral "Поэтому, как обычно, я решил начать утро с созерцания своего хмурого лица."
    play sfx click2
    R_t "Но лампа у зеркала с умывальником не работала."
    play sfx click2
    pause 0.2
    play sfx click2
    R_t thinking suspicious "Я проверил остальные приборы — никаких признаков жизни."
    R_t ne_ponyal "Опять выбило генератор."
    R_t neutral "Бывает."

    scene black with dissolve
    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop
    pause 1.0
    scene bg_coridor1_dark with dissolve

    R_t serious think "Толком не умывшись, не причёсываясь и собравшись впотьмах, я вышел в коридор."
    R_t ear sick "Если бы не фонарь, который я ношу с собой, пришлось бы двигаться, перебирая руками по стене."
    R_t neutral "Благо, вдалеке уже был виден лёгкий свет на кухне."
    R_t "Значит, ребята уже собрались."
    R_t hehe "Об этом также говорил и запах разогретой пищи."

    stop sfx fadeout 2.0
    scene black with dissolve
    pause 0.5
    scene bg_dinner_block_dark with dissolve
    show i profile neutral right at left
    show v profile neutral left at right

    R_t neutral "За столом уже сидели Виктор и Ирис."
    R_t "Дэвида и Софи нигде не было видно."
    R_t "Между коллегами уже завязался разговор."

    show v smile

    R_t "Радист увлечённо что-то рассказывал, тыкая пальцем в экран планшета, а врач внимательно слушала и кивала."
    
    show i tricky at giggle
    show v at fear
    play sfx sfx_laugh_people
    R_t "Периодически они смеялись."
    R_t serious think "Я подошёл к столу."

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

    R_t "Он закинул руки на затылок и откинулся на стуле."

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

    V pockets sorry "Да, естественно. Тем более я пока не могу его проанализировать."
    R_t thinking ne_ponyal "Виктор показал пальцем на чёрный экран планшета:"
    V "Он разряжен, и я не могу заряжать с резервного источника энергии нежизненно важные устройства."
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
    scene black with dissolve
    pause 1.0

    #"…"
    "…"

    scene bg_coridor3_red_cylinders with dissolve
    play sfx2 sfx_metal_hits_grinding fadein 0.5 fadeout 0.5

    R_t serious neutral "Ещё на подходе к отсеку с генератором я услышал стук металла, скрежет и тихие разговоры."

    scene bg_generator_dark
    show s ruki ozadachen left at right
    #d serious
    show d right at left
    with dissolve
    stop sfx fadeout 1.0
    stop sfx2 fadeout 1.0

    R_t "Внутри, при красном свете аварийной лампочки, находились механик и командир."
    #R_t "Всё помещение было заставлено разного вида баллонами, банками, бутылками с разными жидкостями, а рядом с членами экипажа на полу лежали инструменты."
    #show d left at move_on_scene()
    R_t "Софи перебирала бутыли с очень озадаченным видом, а Дэвид ходил из стороны в сторону, сердито хмурясь."
    #show d right at move_on_scene()
    R_t "Они ещё не заметили моего присутствия."
    #show d angry left at move_on_scene()
    D "Ну как же так получилось, что мы до сих пор не определили, в чём неисправность?"
    #show d right at move_on_scene()
    S shy worried "Судя по показателям, генератор перегревается и переходит в режим минимальной аварийной поддержки, но почему…"
    #show d serious left at move_on_scene()
    D "Я всё проверил: вентиляция работает исправно, охлаждающей жидкости достаточно."
    #show d right at move_on_scene()
    D "Если мы не исправим это в ближайшее время, можем не долететь до точки назначения. Это очень важно."
    #show d think left at move_on_scene()
    D "Единственная странность, которую я заметил, — жидкость слишком быстро испаряется."
    #show d right at move_on_scene()
    R_t "К тому моменту, как он это сказал, я уже подошёл к ним вплотную."
    #show d surprised left at move_on_scene(не до конца), fear
    D "Тьфу ты, в этой темноте ничего не разглядишь."
    #d neutral
    D "Привет, Райан."
    R_t ear hehe "Я забавно помахал ему рукой."
    R "Здравствуй, кэп."
    R thinking ne_ponyal "Вижу, у вас здесь какие-то трудности?"

    show s ruki calm with dissolve

    R_t "Софи горько вздохнула."
    #d serious
    D "Кто бы мог дать мне ответ, почему испарение жидкости в камере охлаждения происходит так быстро?"
    R "Давайте проверим."
    R_t suspicious "Я взглянул на прозрачный люк рядом с местом, где стояла Софи."
    R_t "Где-то внизу, в слегка освещённой камере, плескалась вода."
    R_t "Конечно же, это была не обычная H2O, а состав, поддерживающий правильный температурный режим у самого главного элемента нашего корабля — генератора."
    R_t neutral "Люк выглядел вполне заполненным, но даже сквозь обувь я чувствовал, как пол обжигает ступни."
    R not_sure "Думаю, нам необходимо открыть люк и взять пробу для проверки."

    show s shy nedovolen
    #show d osharashen

    S "Ни в коем случае!"
    S "Нельзя часто открывать люк, иначе нарушатся условия эксплуатации жидкости."

    show s shy nedovolen

    S "Только я могу открывать его — и только для дозаполнения."
    
    #show d serious
    
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
    #show d osharashen

    S "Перестаньте следить за мной! Я просто делаю свою работу."
    R_t "Лицо её выражало ярость."
    R_t thinking osharashen "Я опешил от такой реакции."
    R_t "Возможно, некоторые люди не любят, когда наблюдают за их действиями — это можно понять."

    #show d right at exit_right(time=2.0)

    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop

    R_t serious think "Пожав плечами, я пошёл на выход. Дэвид догнал меня."
    R_t "Мы ничего не сказали друг другу, но обменялись многозначительными взглядами."

    #"…"
    #"…"
    scene black with dissolve
    pause 0.5
    #show d right
    scene bg_coridor3_dark_cylinders 
    with dissolve

    R_t serious think "Уже двигаясь по коридору, кэп нарушил тишину."
    #d neutral
    D "Я немного припугнул её этим «не долетим»."
    D "Долетим, конечно, запас пока есть. Если проблема только в нём, конечно."
    R_t "Я кивнул."
    R thinking suspicious "Тебе не кажется странным её поведение?"
    R "Я не склонен обвинять людей, но она выглядит совершенно некомпетентной."
    R "Если бы это была не космическая миссия, а, скажем, обычная работа, я бы предположил, что она дочка начальника, принятая по блату."
    
    #show d sad
    
    R_t "Дэв вздохнул."
    #d serious
    D "По досье у неё всё в порядке. Она механик с очень большим стажем."
    D "Предполагаю, проблема в характере — с этим ничего не поделать."
    stop sfx
    R_t serious think "Мы дошли до развилки."
    #d neutral
    D "Я пойду в командный отсек, мне нужно заполнить бортовой журнал."
    R thinking not_sure "А у меня снова разыгрался аппетит. Не отказался бы от большого прожаренного стейка… ну или хотя бы пасты со вкусом стейка."
    
    #show d happy at giggle
    
    R_t "Дэвид рассмеялся."
    D "Шагом марш на кухню!"
    R_t "Я решил подыграть и вскинул руку к виску."
    R ear hehe "Есть, сэр!"
    R_t "На этом моменте каждый пошёл своим путём."
    
    scene black with dissolve
    pause 0.5
    scene bg_dinner_block
    show i profile neutral right at left
    show v profile smile left at right
    with dissolve

    R_t serious think "На кухне всё ещё сидели Ирис и Виктор."
    R_t "Это было неожиданно, но они играли в карты."
    R_t thinking ne_ponyal "Предметом их азартного спора стал единственный оставшийся тюбик со вкусом оливье."
    R_t "Ещё некоторое время я наблюдал за их игрой, затем долил себе кофе и вернулся на своё рабочее место."

    scene black with dissolve
    pause 1.0
    scene bg_commander_block_transparent_dark with dissolve
    pause 1.0
    play sfx sfx_power_up fadeout 2.0
    scene bg_commander_block_transparent_default
    pause 0.3
    scene bg_commander_block_transparent_dark
    pause 0.3
    play sfx2 fon_generator2 fadein 0.5 fadeout 0.5 loop
    scene bg_commander_block_transparent_default
    pause 0.3

    R_t thinking ne_ponyal "Свет в кабине пару раз моргнул и наконец устаканился. Похоже, Софи справилась."
    R_t suspicious "Сверив показания приборов с картами, я убедился, что мы движемся в верном направлении."
    R_t "Никаких видимых препятствий на пути я не обнаружил."
    R_t serious think "Это значило, что я мог расслабиться, откинуться в кресле и любоваться красотой."

    #фон космос
    scene bg_black_t_90
    with dissolve
    stop sfx
    stop sfx2 fadeout 2.0

    #музыка Anxious space ambient
    $ renpy.music.set_volume(0.3, delay=0.5, channel="sfx")
    play sfx music_waves fadein 1.0 fadeout 0.5 loop

    R_t "Сегодня космическая гладь была особенно завораживающей. Она переливалась из одного цвета в другой, и чем больше я вглядывался в неё, тем чаще казалось, что за окном кабины видно волны."
    
    $ renpy.music.set_volume(1.0, delay=0.5, channel="sfx")

    R_t thinking ne_ponyal "Большие волны, полные пены и морской соли."
    R_t "Свежий лёгкий запах тины и мокрого песка."
    R_t neutral "Сделав очередной глоток разбавленного ароматного кофе, я вспомнил брата."
    R_t "Он всегда был для меня эдакой отцовской фигурой."
    R_t "Большей частью своего воспитания я обязан ему."
    R_t suspicious "Отец и мать часто были заняты на работе. На матери также лежали все хлопоты по дому и забота о моей болезненной младшей сестре."
    R_t "Им было совсем не до маленького меня — я был предоставлен самому себе."
    R_t ne_ponyal "Первая поездка на велосипеде, первая пойманная рыба, первая двойка в школе, первый морской узел…"
    R_t "Он всегда был рядом и помогал, чем мог."
    R_t ear sick "До определённого момента."
    R_t "Я зажмурился и потер рукой переносицу."
    R_t surprised "Мне неприятно вспоминать этот этап жизни нашей семьи."
    R_t "Но слов из песни не выкинешь."
    R_t thinking suspicious "Когда брату исполнилось девятнадцать, он попал под дурное влияние."
    R_t "Так же, как и я, он нуждался в наставнике — крепком мужском плече, что вовремя наставит на путь истинный."
    R_t "Такой человек нашёлся, но верным этот путь назвать сложно."
    R_t neutral "Брат с головой ушёл в оккультизм."
    R_t "Всё чаще мы находили у себя дома странные предметы: кости животных, клочки волос."
    R_t suspicious "На все вопросы брат лишь раздражённо отнекивался."
    R_t "Всё чаще он стал пропадать вне дома, и всё чаще я замечал, как он прячет руки."
    R_t not_sure "Однажды, подглядев за ним в щель двери его комнаты, я увидел, что его тело покрыто ранами и ссадинами."
    R_t "Он словно превратился в совсем другого человека."
    R_t suspicious "Глаза глубоко запали и начали нездорово блестеть, руки стали дрожать."
    R_t "Из открытого и добродушного человека он превратился в нервную, суеверную тень прошлого себя."
    R_t neutral "На несколько лет мы потеряли его из виду."
    R_t "Я тяжело переживал этот период: неизвестность давит больше всего."
    R_t not_sure "Лишь спустя несколько месяцев после его исчезновения мы получили письмо."
    R_t "Он просил нас не беспокоиться о нём: работает при общине."
    R_t suspicious "На благо их собственной веры."
    R_t "Она захлестнула его с головой, как волны, что разбивались о берег у нашего дома и тащили всё, до чего могли дотянуться, в тёмные глубины океана."
    R_t "Как и эти звёзды, зовущие меня окунуться и плыть в просторах космоса."

    scene bg_commander_block_transparent_default with dissolve
    stop sfx fadeout 1.0

    R_t thinking ne_ponyal "За всеми этими размышлениями я не заметил, как в помещении стало очень жарко."
    R_t "По ощущениям, воздух нагрелся градусов на десять."
    R_t "Становилось трудно дышать."
    R_t "Необходимо было проверить, что происходит."

    #анимация аварийной тревоги commander_block
    scene bg_commander_block_red
    play sound sfx_alarm2 fadein 0.5 fadeout 0.5 loop

    R_t thinking osharashen "Только я встал со своего кресла, как включилась аварийная тревога."

    play sfx2 sfx_steps_fast fadein 0.5 fadeout 2.0 loop

    R_t "Ускорив шаг, я выбежал в коридор."

    scene black with dissolve
    $ renpy.music.set_volume(0.3, delay=0.5, channel="sound")
    stop sfx2 fadeout 1.0
    pause 0.5
    #анимация аварийной тревоги coridor1
    scene bg_coridor1_red with dissolve
    show i profile ahui right with dissolve
    R_t serious angry "Сразу на выходе я заметил Ирис."
    show i at center, shaky
    pause 2.0
    show i oooops at down_little with dissolve
    R_t "Лицо её покраснело, девушка держалась рукой за стену, ноги подкосились."
    R thinking osharashen "Ирис!.. Всё в порядке?"

    show i at center
    show i normal bychit at move_vertically(yalign1=1.1) with dissolve

    R_t serious angry "Я подхватил её под локоть, стараясь удержать, но она уже не стояла на ногах."
    
    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop

    R_t "Перекинув её руку через своё плечо, я потащил её к ближайшему аварийному пункту."
    R_t very_angry "Некоторое время мы передвигались так. Я старался реже вдыхать раскалённый воздух, чтобы не обжечь гортань и лёгкие."
    
    stop sfx
    
    R_t think "Лишь добравшись до ближайшего пункта, я смог раздобыть для себя и Ирис по маске с баллонами с более-менее прохладным воздухом."
    
    play sfx sfx_steps_fast fadein 0.5 fadeout 0.5 loop
    
    R_t "После этого я побежал в сторону генератора."

    R_t "Ирис, пришедшая в сознание, медленно двинулась за мной."

    hide i with dissolve

    #фон генераторная анимация тревоги
    scene bg_generator_red
    show s shy angry right at center
    #d
    show i angry left at right
    show v profile angry right at Transform(xalign=-0.1, yalign=1.0)
    with dissolve
    stop sfx
    $ renpy.music.set_volume(1.0, delay=0.5, channel="sound")
    #show i normal neutral right at quad_left with dissolve

    R_t serious think "Здесь уже находились остальные члены экипажа."

    show s ruki crazy at angry
    #show d at fear
    show i at fear

    R_t angry "В середине помещения происходила жаркая перепалка."
    R_t "Из-за громкого звука аварийной тревоги я едва мог расслышать слова."
    R_t "Вокруг стояли пустые баллоны с охлаждающей жидкостью, а люк в полу был открыт."
    R_t "Судя по гаечному ключу в руках командира, он распахнул его сам, вопреки недавнему предупреждению механика."
    
    show s shy angry at angry
    
    R_t "Софи кричала на Дэвида и активно жестикулировала."

    #show d at angry
    show i at move_step(-50, 0.15)
    pause 0.15
    show i at angry

    R_t "Он же грубо пытался схватить девушку и показывал пальцем в сторону генератора."
    R_t "До меня доносились обрывки их речи:"

    show s nedovolen at angry

    S shy angry "Грязный… Обезвредить… Вирус… Очистить…"
    R_t "Виктор тоже был здесь."

    show v pockets suspects

    R_t think "Жестами радист подозвал меня поближе и показал пальцем на баллон."
    R_t "На нём красовалась надпись «Спирт»."
    R_t thinking osharashen "Я округлил глаза и в ошеломлении наблюдал за перепалкой механика и командира."
    R_t "На кой чёрт добавлять спирт в уже запатентованный, рабочий охлаждающий состав?.."
    R_t "Немудрено, что он мгновенно испарялся."

    #show d at angry, step_up
    show i at angry, move_step(-100, 0.2)
    pause 0.15
    show s surprised at fear, move_step(-50, 0.2)

    R_t "В какой-то момент командир замахнулся рукой, чтобы ударить Софи, та попыталась уклониться."

    show v nedovolen
    R_t serious fainting "От жара становилось плохо, маска не помогала."

    #show d right at step_up
    show i right at move_step(50, 0.3)

    R_t "Дэвид развернулся и попытался пойти в сторону генератора."

    show s nedovolen at move_step(250, 0.3, 1)
    pause 1.0
    show s at Transform(xalign=0.7, yalign=1.0), move_step(-30)
    #show d at step_left
    show i at move_step(-30)

    R_t think "Софи вцепилась в его руку и старалась тащить назад."

    #show d angry at step_left
    show i angry left at move_step(50), angry
    show s ruki hurt at move_step(-50), fear

    R_t "Разъярённый капитан резко отмахнулся от неё."

    #show d angry at step_left
    show i at move_step(-50)
    show s shy surprised at Transform(xalign=0.65, yalign=1.0), move_step(-50), fear

    R_t "Шаг. Ещё шаг."

    show i angry at move_step(-50)
    show s ruki hurt at Transform(xalign=0.6, yalign=1.0), move_step(-50), fear
    pause 1.0
    #У МЕНЯ НЕ РАБОТАЕТ НИКАКАЯ ВЕРТИКАЛЬНАЯ АНИМАЦИЯ, НАДОЕЛО
    show s shy surprised at move_vertically(yalign1=1.0, yalign2=2.0)
    pause 0.5
    play sfx sfx_water_splash
    hide s with dissolve
    show v ruki osharashen
    
    R_t angry "И девушка упала в открытый люк."

    show v profile angry at move_step(300), fear

    R_t "Медлить было нельзя. Мы с Виктором бросились к люку."

    $ renpy.music.set_volume(0.3, delay=0.5, channel="sound")
    #цг Софи в люке

    R_t serious angry "Внутри было темно, но мы видели, как девушка пытается держаться на плаву."
    R_t very_angry "В нос ударил резкий запах спирта — настолько сильный, что туман в голове рассеялся."
    R_t "Софи барахталась в воде, пытаясь удержаться на поверхности."
    R_t "Но люк был настолько глубок, что ей не удавалось ухватиться за край."
    R_t "Перчатка с левой руки девушки ушла ко дну резервуара, правой рукой она пыталась удерживать при себе сумку с важными инструментами."
    R_t angry "Я мгновенно перегнулся через край люка, чтобы подать ей руку."
    R_t "Она несколько раз пыталась схватиться за неё, но сделать этого не удавалось."

    show v profile crazy at Transform(xalign=-0.1, yalign=1.0), joy

    R_t very_angry "Виктор схватился за меня, чтобы помочь удержаться."
    R_t "Я опускал руку всё ниже и ниже."
    R_t angry "И вот наши руки почти соприкоснулись."
    R_t "Но в этот момент я увидел брезгливость на её лице."
    R_t "Почти коснувшись моей кисти, она резко одёрнула руку."
    R_t very_angry "Она потеряла самообладание и мгновенно начала задыхаться."
    R_t "Я видел, как жидкость попадает ей в рот и ноздри, как она то всплывала, то вновь пропадала в толще воды."
    
    show i at move_step(-400), angry
    show v pockets angry at Transform(xalign=0.1, yalign=1.0), move_step(-100), fear
    pause 0.5
    play sfx sfx_heat_metal

    R_t think "Дэвид резко откинул нас с Виктором от люка и запер крышку."
    R angry "Что ты делаешь?"

    show i at Transform(xalign=1.0, yalign=1.0), angry

    D "Она нас всех убьёт!"
    V ruki osharashen "Что?.."

    show i at Transform(xalign=1.0, yalign=1.0), angry

    D "Генератор! Помогите мне, нам нужно его охладить!"
    play sfx sfx_evaporating_water

    R_t "Он вскрыл баллон с составом и попытался вылить его прямо на огромную, пышущую жаром машину."
    V pockets nedovolen "Ты уверен, что это поможет?!"
    D "Я… Я уже ни в чём не уверен!"

    play sfx sfx_evaporating_water

    R_t "Я вскрыл второй баллон и вылил его с другой стороны генератора."
    R_t think "На мгновение показалось, что это помогло."
    R_t "Возможно, мы хотели, чтобы это было так."
    R_t ear dissatisfied "Температура в помещении всё росла и росла."

    play sfx sfx_alarm3 fadein 0.5 fadeout 0.5 loop

    R_t "На датчике генератора она достигла критической отметки."

    show v ruki osharashen
    show d osharashen

    R_t thinking osharashen "Не сразу, но мы почувствовали запах гари."
    R_t "Огонь?.."
    R_t "Секунда{w}, две."

    play sfx sfx_explosion
    R_t "И генератор вспыхнул ярким огнём."

    play sfx2 sfx_burning_fire
    #цг огонь взрыв
    call scene_fire

    R_t serious fainting_blood "Жаркий воздух и вентиляция мгновенно разнесли искры по помещению."
    R_t  "Я больше не мог сдерживаться и зашелся в удушающем кашле."
    R_t "Кажется, мы не успели…"
    R_t serious fainting_blood "Я потерял сознание."

    stop sound fadeout 1.0
    play sfx sfx_fall_body
    scene black with dissolve
    
    "И снова этот уже знакомый голос:"
    play sfx sfx_hiss_with_voice1 fadein 0.5 fadeout 1.0
    N "Опять… Ну что же ты, давай, давай… Ты же слышишь меня?.."
    jump day_3