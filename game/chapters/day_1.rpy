label day_1:
    #День 1—перебивка
    scene bg_black
    with dissolve
    pause 1.0
    $ show_space_bg("bg_room_rayan_default")
    with dissolve
    R_t ear surprised "Всю ночь мерещились тревожные сны."
    R_t "Спустя годы осознанных сновидений, сонных параличей и прочих шалостей измученного мозга подобное уже не удивляло."
    R_t dissatisfied "Сегодня мне снились призрачные неосязаемые сущности: они пытались общаться со мной, хватали за руки, тянули моё тело в темноту."
    R_t "Похоже на что-то из фильмов ужасов с привидениями в старых домах, которые я так любил смотреть в детстве."
    R_t neutral "Впечатлило? Ни капли."
    R_t "Умывшись прохладной водой, я взглянул в своё отражение в зеркале."

    call scene_mirror_water

    cutscene "Из него на меня уставшим взглядом смотрел обычный парень лет двадцати пяти."
    cutscene "Капли воды стекали по лицу, охлаждая кожу. Вода всегда напоминала мне о доме."
    cutscene "Больше нельзя было мешкать — по протоколу рабочий день начинается строго в восемь утра."
    $ show_space_bg("bg_room_rayan_default")
    R_t "Быстро натянув костюм, я отметился в терминале и направился в кухонный модуль."
    play sfx2 sfx_push_button

    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    scene black with dissolve
    pause 1.0
    scene bg_dinner_block
    show i smoke puzzled left at quad_left_center
    show s ruki ozadachen left at Transform(xalign=0.7, yalign=1.0)
    show d left at Transform(xalign=1.15, yalign=1.0)
    show v profile smile right at Transform(xalign=-0.1, yalign=1.0)
    with dissolve
    stop sfx fadeout 0.5
    play sfx2 sfx_talk_people fadein 0.5 fadeout 0.5 loop

    R_t "На удивление, в помещении было шумно."
    R_t "Команда что-то активно обсуждала."

    play sfx sfx_steps_two
    R_t "Я подошёл ближе."
    R_t "В воздухе чувствовалось волнение."
    R_t thinking ne_ponyal "Кажется, наконец у нас выйдет получить указания от командного центра и более точные координаты базы, к которой мы движемся."
    R_t "Экипаж склонился над столом, в центре которого был расположен планшет."
    R_t "Радист сидел перед ним, руками цепко обхватив кружку с дегидратированным куриным супом."
    R_t "Виктор выглядел очень довольным."
    stop sfx2 fadeout 2.0

    show v profile tricky

    R_t "Благосклонно осмотрев присутствующих, он сказал:"
    V pockets happy "Коллеги, я всё-таки смог считать пакет. Но, чёрт побери, это звучит… странно."

    play sfx sfx_pisk

    show v profile smile

    R_t "Радист осторожно поставил планшет в центр стола; экран мигал грязновато-фиолетовыми гребнями спектрограммы."

    show i normal angry

    R_t "Врач нервно подняла бровь, медленно вскрывая термопакет с пищей."

    show i normal angry at shaky_fast

    I "Странно — это как?"
    R_t "Радист постучал пальцем по диаграмме."

    play sfx sfx_radist_hit_table
    pause 0.2
    play sfx sfx_radist_hit_table
    pause 0.2
    play sfx sfx_radist_hit_table
    pause 0.5
    V ruki puzzled "Частота не наша, четыреста двенадцать мегагерц."
    V "Формально — помехи. Но пакет чётко повторился три раза с паузой ровно 4,2 секунды."
    play sfx sfx_slurp
    show d calm

    R_t calm "Командир отхлебнул из кружки и прислушался:"

    show i smoke calm

    D serious neutral "Может, отражение от ионосферы? Заметь, мы в апогее — угол наклона достаточно большой."

    show v pockets happy
    show d neutral

    R_t "Радист удовлетворённо кивнул, словно у него был заготовлен ответ." 
    V "Думал об этом."
    V think "Словно кто-то специально прятал голос в плазме."

    play sfx sfx_push_button
    show v happy

    R_t "Он нажал «Play»."

    play sfx sfx_glitch

    show i smoke surprised
    show d fear
    show s shy worried

    R_t "Из динамиков выползло металлическое шипение, будто струна скребла по железу, затем — обрывочное неразборчивое пищание и протяжные повторяющиеся звуки."
    R_t thinking not_sure "Как по мне, звучало сомнительно: в нём не могло быть никакой информации."
    D fear "Мы все ждали определённого сообщения. Неужели командный центр пытается достучаться до нас, но не получается?"
    V ruki puzzled "На мой взгляд, в этом сообщении что-то есть. Его необходимо изучить. Вам не кажется, что в нём закодирован голос?"
    
    show i profile osharashen at shaky_fast

    R_t ear neutral "Ирис в очередной раз пробрала мелкая дрожь."
    pause 0.5
    
    play sfx sfx_cup_on_table
    show i normal crazy at shaky_fast

    R_t "Она схватилась за стол так, что костяшки пальцев побелели."

    pause 0.5

    R_t "Мы привыкли к этому: такова была особенность её организма, что-то связанное с болезнями в прошлом."

    show i ridicule
    play sfx sfx_laugh_female3

    R_t serious think "Она усмехнулась:"
    I normal very_ridicule "Как по мне, похоже на какой-то колокольный звон."
    S ruki neutral "По ком звонил колокол?"

    show d happy at giggle
    show s happy at fear
    show i neutral_happy at angry
    show v ruki tricky at giggle
    play sfx sfx_laugh_people

    R_t "Экипаж засмеялся. Было бы неплохо разрядить обстановку."

    show i smoke happy

    V cunning "Пхах. В течение дня я всё настрою, вот увидите."
    R_t "Радист подмигнул."
    V pockets dream "Точнее, услышите!"

    show d neutral
    show s ruki neutral
    show i smoke calm

    R_t thinking ne_ponyal "Мы кивнули."
    R_t "Как специалист в радиотехнике и метеорологии, он слышит и понимает в этом больше нас."
    R_t ear hehe "Если ему удастся вычленить оттуда данные о координатах, моя работа станет проще."
    
    play sfx sfx_cup_on_table

    R_t "Я допил чай, поставил кружку на магнитную подставку и встал из-за стола."

    play sfx sfx_hit
    show v pockets angry at angry
    show d osharashen
    show s shy surprised
    show i surprised

    V "Нет!"
    V "Сядь, пожалуйста."
    R_t thinking osharashen "Я опешил и от неожиданности плюхнулся обратно на стул."
    R_t ear surprised "Все мы вопросительно взглянули на радиста."
    V angry "Разве ты забыл, что первым из-за стола может встать только капитан?"
    V "Иначе у нас точно всё пойдёт наперекосяк."
    
    play sfx sfx_laugh_female1
    show i normal ridicule

    R_t "Ирис тихо фыркнула."

    show s neutral

    R_t "Ситуацию разрешила Софи:"

    show i neutral_happy

    S neutral "Ребята, это не повод расстраиваться. Всего лишь глупые суеверия. Мы же все — люди науки, неужели вы не поняли шутку?"
    R_t serious think "Но Виктор не был настроен шутить."

    show i very_ridicule
    pause 1.0

    R_t ear neutral "Ирис насмешливо посмотрела на радиста…" 

    pause 0.5
    show i profile tricky left at move_on_scene(time=3.0, xalign=-1.0)
    play sfx sfx_steps_short
    play sfx2 sfx_whistling
    show s shy worried left 
    show d osharashen left

    R_t "…встала и, насвистывая какой-то незатейливый мотив, вышла из комнаты."

    stop sfx fadeout 0.5
    stop sfx2 fadeout 0.5
    show v pockets suspects
    
    R_t serious think "Лицо Виктора помрачнело."

    play sfx sfx_steps_short 
    show d neutral 
    show v profile sad left at move_on_scene(time=2.0, xalign=-1.0)
    pause 1.0

    R_t "Быстрым шагом он вышел из кухни и скрылся в коридоре."
    R_t thinking not_sure "Мы смогли расслышать лишь его бормотание."
    R_t "Нам было некогда обращать внимание на поведение радиста."

    show s ruki calm

    R_t thinking neutral "Необходимо было приниматься за работу."

    show d left at move_on_scene(time=3.0, xalign=-1.0)
    play sfx sfx_steps_short

    R_t ear neutral "Члены экипажа не спеша разбрелись по своим точкам."

    show s profile neutral right

    R_t ear neutral "На кухне осталась только Софи, чтобы продезинфицировать все поверхности — эта любительница чистоты не могла потерпеть ни одной крошки."

    scene black with dissolve
    pause 1.5
    $ show_space_bg("bg_commander_block_transparent_default")
    
    R_t ear neutral "Моим бессменным местом пребывания была навигационная рубка."
    R_t "Это был просторный кабинет на два рабочих места — моё и капитана."
    R_t surprised "Капитан временно отсутствовал — по протоколу он должен осуществить обход и проверку всех датчиков и приборов."
    R_t "Поэтому я мог некоторое время наслаждаться одиночеством."
    R_t hehe "Но я вовсе не чувствовал себя одиноким."

    #цг 7 начало
    $ show_scene_cosmos("7")
    cutscene "Напротив, находиться здесь было приятно."
    cutscene "Вид, который открывался из нашего большого окна, был просто потрясающим."
    cutscene "Мимо проносились огоньки сгорающих и снова зажигающихся звёзд, целые системы, пути."
    cutscene "Возможно, созерцание этого необъятного пространства было одной из причин..." 
    cutscene "...Почему я решился стать членом экспедиции и совершить полёт в эту холодную бесконечную пустошь."
    cutscene "Конечно, было немного жаль, что не повезло с командой."
    $ hide_scene_cosmos()
    #цг 7 конец
    
    #цг 6 начало
    $ show_scene_cosmos("6")
    cutscene "Я планировал попасть в заранее сработавшийся коллектив и стать в нём тихим, не привлекающим особого внимания аутсайдером."
    cutscene "Но что ни день — какое-то событие, не соскучишься."
    cutscene "Я откинулся на кресле и закинул руки за голову. Всего лишь месяц."
    cutscene "Это совсем не срок для космической экспедиции."
    cutscene "Поэтому нет разницы в персонале: главное — все они отличные специалисты, которые знают своё дело и были хорошо подготовлены."
    cutscene "Приключение туда-обратно не должно было доставить проблем."
    cutscene "Я прищурил глаза и всмотрелся в тёмную даль."
    $ hide_scene_cosmos()
    #цг 6 конец

    #цг 12 начало
    $ show_scene_cosmos("12")
    cutscene "Полёт внутри корабля почти не ощущался."
    cutscene "Это ощущение лёгкости в теле и изредка небольшая дрожь."
    cutscene "Она не сравнится с ощущением полёта вне гравитации."
    cutscene "Я знал, каково это — через это проходят все, кто стремится стать членом экипажа."
    cutscene "Искусственные условия для тренировки, когда твоё тело помещают в быстро раскручивающуюся вокруг своей оси гигантскую центрифугу…"
    cutscene "…и ты крутишься, словно волчок, — захватывают дух."
    cutscene "Но это никогда не сравнится с ощущением «плавания» в открытом космосе. По-настоящему."
    cutscene "В скафандре и за пределами корабля."
    cutscene "Отчасти это можно назвать моей мечтой."
    cutscene "Все экспедиции, членом которых мне удалось побывать, проходили без инцидентов, потому для меня не было острой необходимости покидать корабль."
    $ hide_scene_cosmos()
    #цг 12 конец
    
    #цг 5 начало
    $ show_scene_cosmos("5")
    cutscene "По протоколу мы имеем право делать это лишь в исключительных случаях — для устранения поломки или определения неполадок."
    cutscene "Более того, являясь навигатором, вряд ли мне когда-либо удастся осуществить это небольшое желание…"
    cutscene "… в починке механических повреждений или устранении неполадок электроники я, увы, ничего не смыслю."
    cutscene "Но у меня всегда было ощущение, что рано или поздно я познаю эти ощущения."
    cutscene "Они были так знакомы где-то в глубине сознания, будто я уже много раз их испытывал."
    $ hide_scene_cosmos()
    #цг 5 конец

    $ show_space_bg("bg_commander_block_transparent_default")

    R_t thinking ne_ponyal "Корабль летел на автопилоте, до базы было ещё пять дней пути, потому большого количества работы не предвещалось."
    R_t "Всего лишь необходимо следить за датчиками."
    R_t serious think "Вот-вот должен был вернуться капитан после утреннего обхода."
    R_t "Я решил достать заранее заготовленную книгу, чтобы продолжить чтение."
    R_t angry "Оперевшись рукой на подлокотник, чтобы дотянуться до небольшого отсека с личными вещами, я почувствовал резкую боль в руке."

    #цг игла в руке
    $ hide_space_bg()
    call scene_hand_needle
    with dissolve

    pause 0.5
    $ show_space_bg("bg_commander_block_transparent_default")
    
    R_t thinking osharashen "Не теряя самообладания, я взглянул на подлокотник и увидел еле заметную, но довольно крупную иглу."
    R_t "Брак обшивки кресла?"
    R_t serious think "Сжав пальцами рану на ладони, я хотел было поспешить в медпункт."
    R_t "Рана была пустяковой, по протоколу я обязан сообщать обо всех изменениях в моём теле, включая небольшие раны."
    R_t "Как минимум стоило обеззаразить её."
    R_t thinking suspicious "Но что-то не складывалось."
    R_t "Прежде чем направиться в лазарет, было необходимо осмотреть кресло."
    R_t ne_ponyal "Как я объясню характер этого недоразумения?"
    R_t thinking osharashen "Увы, увиденное не обрадовало меня."
    #цг стул с иглами
    $ hide_space_bg()
    $ show_space_bg("bg_stul_s_iglami")

    cutscene "Ряд мелких игл был воткнут по всему периметру кресла в хаотичном порядке."
    cutscene "Я пригнулся, чтобы осмотреть сиденье со всех сторон."
    cutscene "Мебель была безнадёжно испорчена и совершенно небезопасна для использования."
    cutscene "Помимо металлических штырей в самой обшивке, некоторое их количество лежало вокруг."
    cutscene "Какого чёрта?! Это точно ненормально."
    cutscene "Я обязан доложить обо всём капитану."
    cutscene "Я вытащил несколько игл в качестве образца (благо их было достаточно много, чтобы оставить часть на месте для демонстрации)."
    cutscene "Особенно много странных металлических шипов находилось у основания спинки стула."
    cutscene "Вынимая одну иглу за другой, я заметил, что кожаная обивка рядом с этим местом располосована ножом."
    cutscene "И внутри явно что-то спрятано."
    cutscene "Ком встал в горле."
    cutscene "Сказать честно, я никогда не был из пугливых, но данная ситуация выходила за рамки рядовых приключений космонавта."
    cutscene "Я аккуратно раздвинул края рваной ткани и, зацепив двумя пальцами, вытащил то, что находилось под обшивкой."
    cutscene "Это был предмет, который, пожалуй, я ожидал там обнаружить меньше всего."

    #раян фото девушки
    call scene_photo_found_cut

    $ show_space_bg("bg_commander_block_transparent_default")

    R_t serious very_angry "Внутри меня росла злость."
    R_t "Какого чёрта кто-то копался в моих вещах? В моей каюте?!"
    R_t "Это фото явно не лежало на самом видном месте."
    R_t angry "С камнем на сердце, раной на руке и тихой яростью я вышел из навигационной рубки."

    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    scene black with dissolve
    pause 0.5
    scene bg_coridor2_default with dissolve

    R_t serious angry "Первым делом — лазарет для фиксации, а там будем решать ситуацию."

    pause 1.5

    R_t serious angry "Это происшествие заставило меня почувствовать напряжение — на корабле всего пять человек; за вычетом меня — четыре."
    R_t thinking suspicious "Зачем кому-то было нужно поступать таким образом?"
    R_t "Неужели лично я чем-то не угодил одному из членов экипажа?"
    R_t ear sick "Рука саднила."
    R_t "Рана была небольшой, но всё ещё достаточно неприятной — прямо на сгибе ладони."
    R_t neutral "Я тихо следовал по коридорам в сторону лазарета."
    R_t "Было опасно привлекать внимание."
    R_t serious think "В лазарете горел свет. Его было видно сквозь прикрытую дверь."
    R_t "Подходя к помещению, я услышал, что внутри кто-то был — они разговаривали."
    R_t "Судя по голосам, это были Ирис и Софи."
    R_t thinking ne_ponyal "Очень сомневаюсь, что совершить это мог кто-то из них."
    R_t ear dissatisfied "Собравшись с духом, я вошёл внутрь."

    stop sfx fadeout 1.0
    play sfx2 sfx_door_creaking
    call scene_vhod_v_lazaret

    #цг вход в лазарет
    scene bg_med_block
    show i pen ozadachen right at left
    show s shy surprised left at right
    with dissolve

    #цг руки вверх
    R_t ear hehe "Я сразу же поднял руки в жесте «Сдаюсь»."

    show i pen nervous
    show s shy neutral

    R_t "Девушки нервно улыбнулись. Ирис вздохнула."
    I normal neutral "И у тебя тоже? Где ты это нашёл?"
    R ear sick "Одна из игл воткнулась мне в руку, когда я сидел на своём рабочем месте. Они оказались везде вокруг."

    show s ruki hurt at fear
    play sfx sfx_hiss_pain
    R_t surprised "Софи неожиданно зашипела. Она попыталась опереться на ногу, но, очевидно, ей стало очень больно."
    S "Кто-то вставил иглу мне в ботинок, когда я отошла в раздевалку, чтобы надеть форму."
    I pen ozadachen "Она вошла в ногу почти полностью. Мне с трудом удалось её достать."

    show s shy worried

    R_t "Софи грустно и даже как-то виновато улыбнулась."

    show i normal neutral

    S "Кажется, я снова бесполезна."
    I profile neutral "Некоторое время тебе придётся побыть в покое."
    R_t thinking suspicious "Я осмотрел её рану."
    R_t "Ей однозначно повезло намного меньше, чем мне: штырь, на который она наступила, был гораздо толще."
    R_t ne_ponyal "А ещё его не сразу получилось вынуть — поэтому стопа сильно покраснела и отекла."
    R_t "Нужно было действовать."
    R serious think "Я собираюсь доложить об этом капитану."
    I normal neutral "На твоём месте я бы не спешила."
    I normal neutral_happy "Как и у капитана, у меня хранятся досье на всех членов экспедиции."
    R_t ear dissatisfied "Я напрягся."
    R "К чему ты клонишь?"

    show s ruki ozadachen

    I normal angry "Кое-кто из нашей команды много лет увлекался оккультной тематикой, собрал у себя приличную библиотеку, изучал историю оккультизма."
    I bychit "И даже пару лет состоял в секте."
    R thinking osharashen "Как такое вообще может быть?"
    I profile neutral "В первую очередь необходимо пообщаться с Виктором."
    I "Нам нужно заручиться поддержкой ещё одного члена экипажа, прежде чем вести переговоры с бывшим любителем оккультизма."
    R_t thinking suspicious "Предложение звучало резонно."
    S shy worried "Я помню свой первый день на этом судне и, кажется, замечала знаки, нарисованные мелом на стенах возле кают и склада…"
    S "Но я никогда не придавала этому значения."
    I normal bychit "Мало ли что это могло быть."
    R thinking neutral "Но теперь я начинаю догадываться."
    R suspicious "Всё здесь было ненормально с самого начала."

    show s ruki ozadachen
    show i profile neutral

    R_t "Коллеги кивнули."
    R_t "Необходимо было выдвигаться."

    R_t serious think "Я уже было развернулся обратно к двери, как Ирис схватила меня за плечо."

    show i pen ozadachen at move_step(50)
    play sfx sfx_pat
    I "Нужно идти вдвоём. Сейчас опасно разделяться."
    R_t ear smile "Я усмехнулся."
    R ear neutral "Мы можем пойти вдвоём, но лазарет с Софи необходимо закрыть на ключ. Она сейчас не в состоянии двигаться."

    show i neutral
    S ruki neutral "Нет, всё в порядке, я пойду с вами!"

    show s hurt at move_step(-30)
    play sfx sfx_hiss_pain

    R_t ear surprised "Тихонько ругаясь, она встала на ноги. Одной ногой опиралась на носок, чтобы не тревожить рану."
    R_t "Идти можно, но медленно."
    S shy worried "Ирис, могу я попросить у тебя обезболивающее?"
    S neutral "Я смогу лучше передвигаться, если не буду ежесекундно думать о боли."

    show i normal angry

    R_t "Ирис мгновенно скривилась."
    I "Оно тебе не нужно. Мы должны наблюдать динамику твоей раны."
    I bychit "Тем более, обезболив рану, ты станешь менее аккуратной и будешь на неё наступать."
    I angry "Однозначно нет."

    show s ruki calm

    R_t "Софи погрустнела, но ничего не сказала."

    show i profile neutral with dissolve

    R_t "Ирис перебинтовала ей ногу, обработала мою рану и мы все вышли за дверь медпункта."

    scene black with dissolve
    pause 0.5
    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    scene bg_coridor2_default 
    show i profile neutral left at Transform(xalign=0.6, yalign=1.0)
    show s profile neutral left at Transform(xalign=1.0, yalign=1.0)
    with dissolve

    R_t thinking ne_ponyal "Тёмные коридоры, которые ещё недавно казались такими знакомыми, теперь выглядели зловеще."
    R_t "Потолок словно давил на нас своей массой — так, что хотелось пригнуться, сжаться и спрятаться в угол."
    R_t serious think "Конечно же, я не мог позволить себе показать слабину."
    R_t "Сейчас я — наиболее обороноспособная единица в нашем небольшом отряде."
    R_t "Как навигатор, второй человек после капитана, я имел право носить при себе табельное оружие."
    R_t "Это был небольшой электрошокер, которым в случае чего я мог подавлять бунт."
    R_t ear neutral "Он придавал мне толику уверенности, поэтому я держал ладонь на кобуре — будто просто опирался пальцем о карман."
    R_t surprised "Но рука всё равно предательски дрожала."
    R_t "Не этого я ожидал от рядового полёта."

    scene bg_coridor3_default
    show i profile neutral right at Transform(xalign=0.4, yalign=1.0)
    show s profile neutral right at Transform(xalign=0, yalign=1.0)
    with dissolve
    stop sfx fadeout 1.0
    pause 1.0
    show i profile osharashen right at Transform(xalign=0.4, yalign=1.0)
    show s profile despair right at Transform(xalign=0, yalign=1.0)

    R_t serious think "Мы уже приблизились к развилке коридоров, один из путей которой вёл к радиорубке, когда вдалеке показалась фигура."

    play sfx sfx_strem_steps_david fadein 0.5 fadeout 1.0 loop
    show i osharashen at move_on_scene(time=0.7, xalign=0)
    show s profile despair at move_step(xoffset=-300)

    R_t thinking osharashen "Мы резко прижались к стене."

    show i profile ahui at shaky_fast
    pause 1.0
    show i oooops

    R_t "Ирис снова нервно затряслась, прикрыла рот рукой, чтобы не выдать себя."

    show s profile annoyed

    R_t "Софи старалась держаться, но морщилась от боли."
    R_t ear dissatisfied "Я показал рукой всем держаться сзади и не издавать ни звука."

    #цг кэп в конце коридора +
    call scene_coridor

    stop sfx fadeout 1.0
    hide i
    hide s 
    with dissolve


    $ show_space_bg("bg_room_viktor_dark")

    R_t serious think "Это оказалась каюта. Каюта Виктора."
    R_t "В полумраке мы сидели как мыши, стараясь ничем не выдать своё присутствие."

    R_t ear dissatisfied "Я смотрел в узкую щель двери, дожидаясь, когда Дэвид пройдёт мимо."
    R_t "Софи, уставшая стоять на одной ноге, решила присесть на кровать, но в темноте задела что-то на столе."

    play sfx sfx_falling_objects

    R_t thinking osharashen "Мы услышали шум падающих вещей."
    R_t neutral "Скрываться дальше смысла не было. Я включил свет."
    play sfx sfx_click2
    $ show_space_bg("bg_room_viktor_default")
    show i profile osharashen left at right
    show s shy surprised right at left
    with dissolve

    R_t osharashen "То, что мы увидели, ошарашило нас."
    R_t "Вся каюта была завалена вещами."

    scene room_viktor2 with dissolve
    pause 1.0

    cutscene "Кости. Нити. Иглы."

    $ show_space_bg("room_viktor1")
    pause 1.0
    
    cutscene "Какие-то странного и неприятного вида тотемы, собранные из множества частей."

    scene room_viktor3 with dissolve
    pause 1.0
    
    cutscene "Лоскуты ткани, рисунки."

    $ show_space_bg("bg_room_viktor_default")
    show i pen ozadachen left at right
    show s shy surprised right at left
    with dissolve
    pause 0.5

    show s shy nedovolen at fear

    R_t "Софи резко одёрнула руку, которой опиралась на стол, вытащила спирт и обтерла ладони."
    R_t serious think "Всё было ясно. Кроме его мотивов."
    R_t thinking not_sure "Ребячество или диверсия?"
    R serious think "Всё отменяется. Мы должны доложить капитану."
    S ruki ozadachen "Он был здесь совсем недавно, мы успеем его догнать!"

    show i profile neutral right at step_up with dissolve

    R_t "Ирис на дрожащих ногах выглянула за дверь."
    I profile oooops "Я не вижу его."
    R ear dissatisfied "Мы должны поспешить."

    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    scene bg_black with dissolve
    pause 0.5
    scene bg_coridor3_default
    show i profile neutral right at Transform(xalign=0.4, yalign=1.0)
    show s profile sad right at Transform(xalign=0, yalign=1.0)
    with dissolve
    pause 1.0

    R_t thinking neutral "Капитана нигде не было видно."

    scene bg_coridor2_default
    show i profile neutral left at Transform(xalign=0.6, yalign=1.0)
    show s profile neutral left at Transform(xalign=1.0, yalign=1.0)
    with dissolve
    pause 1.0

    R_t serious think "Мы обошли все ближайшие коридоры."

    scene bg_coridor1_default
    show i profile neutral right at Transform(xalign=0.4, yalign=1.0)
    show s profile sad right at Transform(xalign=0, yalign=1.0)
    with dissolve
    pause 1.0

    R_t "Поднялись обратно к основным блокам. Ни на своём рабочем месте, ни на кухне, ни в курилке его не было."
    R_t ear dissatisfied "Я собрался с духом, взял в руки шокер и направился в сторону комнаты видеонаблюдения."
    R_t "Если капитана нигде не видно, я должен взять на себя решение проблемы."

    scene bg_coridor2_default
    show i profile neutral left at Transform(xalign=0.6, yalign=1.0)
    show s profile neutral left at Transform(xalign=1.0, yalign=1.0)
    with dissolve
    stop sfx fadeout 1.0
    pause 1.0

    $ renpy.music.set_volume(0.1, delay=0, channel="sfx")
    play sfx sfx_pisk fadein 0.5 fadeout 1.0 loop
    play sfx2 sfx_noise_banging fadein 0.5 fadeout 1.0 loop

    R_t "Мы стояли перед входом в помещение."
    R_t "Тихое пищание и какая-то возня были слышны изнутри. Внутри явно кто-то был."
    R_t serious think "Моя рука уже лежала на ручке двери, как…"
    stop sfx fadeout 0.5
    stop sfx2 fadeout 0.5
    $ renpy.music.set_volume(1.0, delay=0.5, channel="sfx")

    play sfx3 sfx_heat_metal

    R_t thinking osharashen "Резкий удар."

    show v pockets angry right at Transform(xalign=-0.1, yalign=1.0), angry
    show i profile osharashen 
    show s shy surprised
    play sfx sfx_door_open

    R_t "Дверь распахнулась, и радист выскочил изнутри." with hpunch

    play sfx sfx_scream_women_ah
    show i profile ahui at fear

    R_t "Ирис вскрикнула от страха."

    play sfx sfx_hit

    show expression Solid("#000000") as overlay_light at alpha_mask_fade(0.6)

    R_t serious fainting "Я ударился затылком о стену, и в глазах на миг потемнело." with hpunch
    play sfx sfx_steps_fast
    scene bg_black
    with fade
    pause 0.5
    scene bg_coridor2_default
    show i profile osharashen left at Transform(xalign=0.6, yalign=1.0)
    show s shy surprised left at Transform(xalign=1.0, yalign=1.0)
    with dissolve
    stop sfx
    R_t ear sick "Прижавшись к стене, я пытался прийти в себя."

    show s shy worried at fear

    R_t "Софи успела заметить, в какую сторону он направился, и пыталась растормошить меня."
    R_t surprised "Немного проморгавшись, я смог оценить ситуацию. {w=0.4} Дерьмово."
    R_t dissatisfied "Мы должны были догнать его, но…"

    show s profile sad at move_on_scene(time=2.0, xalign=-0.1)
    play sfx sfx_steps_two
    pause 2.5
    show s profile cry with dissolve

    R_t "Софи неожиданно остановилась у входа в комнату."
    R_t surprised "По её взгляду было понятно, что ничего хорошего внутри мы не увидим."

    show i at move_on_scene(time=1.0, xalign=0.2)
    play sfx sfx_steps_two
    pause 2.0
    play sfx sfx_fall_body
    show i profile ahui at jump with dissolve

    R_t "Ирис на дрожащих ногах подошла к двери и сразу же рухнула на пол, зажав рот руками в ужасе."
    R_t thinking osharashen "Перед нами открылась картина:"

    #цг Дэвид с ножом +
    hide i
    hide s
    scene bg_monitors_block
    play sfx sfx_drama
    call scene_david_potracheno

    
    show i profile ahui left at Transform(xalign=0.7, yalign=1.0)
    show s profile cry left at Transform(xalign=1.1, yalign=1.0)
    show d fist fainting right at Transform(xalign=0, yalign=4.0)
    with dissolve
    stop sfx fadeout 1.0
    R_t "Ирис бросилась к нему:"

    show i at move_step(-300), fear
    play sfx2 sfx_steps_fast_two
    I "Дэв, что случилось? Он напал на тебя?"
    R serious angry "Окажи ему помощь, срочно!"

    show s at move_step(50), fear
    play sfx sfx_steps_two
    pause 0.5
    show s despair at Transform(xalign=1.15, yalign=1.0), move_step(50), fear

    R_t "Софи сделала пару шагов назад. Лицо её позеленело."
    I osharashen "Оцениваю ситуацию!"
    D "Он… {w=0.4} Он сошёл… {w=0.4} C ума…"
    R_t angry "Я наклонился к капитану."
    R thinking not_sure "Расскажи мне, что произошло?"
    D "Он говорил о каком-то шёпоте по радио… О том, что ты всё испортил…"

    play sfx sfx_cough_man
    show d at fear

    R_t "Дэвид начал кашлять. Изо рта потекла струйка крови."
    I "Дело плохо, у него пробито лёгкое. Он потерял уже очень много крови!"
    I normal angry "К сожалению, он не жилец."
    R serious very_angry "Дай ему медикаменты, чтобы он смог протянуть ещё немного! Мы должны хотя бы выяснить…"

    show i normal crazy with dissolve
    show s shy surprised
    pause 1.0

    R_t "Ирис резко прервала меня."

    play sfx sfx_drama_boom
    call scene_Iris_zlaya

    I "Запрещено по протоколу."
    R_t thinking osharashen "Я удивлённо взглянул на неё."
    R serious angry "Ты шутишь?"
    R serious very_angry "Мы должны бороться за жизни экипажа и за любую информацию!"

    scene bg_monitors_block
    show i normal crazy left at Transform(xalign=0.8, yalign=1.0)
    show s shy surprised left at Transform(xalign=1.2, yalign=1.0)
    show d fist fainting right at Transform(xalign=0, yalign=4.0)
    with dissolve
    play sfx sfx_cough_man
    show d at fear
    R_t "В это время командир прокашлялся ещё сильнее, рука его отпустила нож."

    show i smoke tricky
    show s profile despair

    R_t "Я был зол на Ирис."
    R_t "У него был шанс."
    R_t "Но сейчас вся судьба экспедиции под угрозой."
    R_t thinking suspicious "Разбираться будем после."
    R_t osharashen "Дэв неожиданно открыл глаза."
    D "Райан, я передаю тебе свои полномочия… Теперь ты командир этого отряда."
    R ear dissatisfied "Так точно, капитан…"

    #цг Дэвид потрачено +
    call scene_david_potracheno_2
    R_t serious very_angry "Если бы мы не потратили время…"

    show i calm

    R_t "Ирис холодно наблюдала за Дэвидом, лежавшим на полу."

    #цг время в блокноте +
    play sfx sfx_writing fadeout 1.0
    call scene_password
    show s cry with dissolve
   
    R_t serious think "Забрал карточку доступа из кармана капитана, а также небольшой пистолет."
    R_t "Мы вышли из комнаты видеонаблюдения. Я бросил последний взгляд на Дэвида."
    R ear neutral "Мы вернёмся, дружище…"

    scene black with dissolve
    pause 0.5
    scene bg_coridor2_default
    show i smoke calm right at Transform(xalign=-0.1, yalign=1.0)
    show s profile despair right at Transform(xalign=0.4, yalign=1.0)
    with dissolve
    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop

    R_t serious think "Следующие несколько минут мы провели в тишине."
    R_t "Слышны были лишь наши шаги: я шёл уверенно и быстро, Ирис кралась сзади, Софи старалась спешить, но хромала."

    show i puzzled

    R_t ear dissatisfied "Заранее я передал свой электрошокер Софи, указав глазами на Ирис."

    show s shy surprised
    pause 1.0
    show s ruki calm with dissolve

    R_t "Механик испуганно взглянула на меня и кивнула."
    R serious angry "При любой странности — поняла?"
    show s profile sad
    R_t thinking suspicious "Судя по камерам, Виктор бежал в сторону отсека с главным двигателем."
    R_t "По протоколу там разрешено находиться только механику и командиру."
    R_t neutral "Поэтому ничего хорошего я не ожидал."
    pause 1.0
    play sfx sfx_pisk_one
    R_t serious think "Я нажал на кнопку входа в отсек."

    play sfx sfx_metal_door
    R_t "Раздвижная дверь со скрипом открылась."

    scene bg_engine
    play sfx3 sfx_fon_generator2 fadein 0.5 fadeout 0.5 loop
    with dissolve
    R_t "На первый взгляд никого видно не было, но стоило мне посветить фонариком — я увидел его."

    #цг Виктор у панели +
    play sfx sfx_drama_boom
    call scene_viktor_dal_ebu

    show v ruki crazy_down left at Transform(xalign=1.1, yalign=4.0) with dissolve
    show i profile osharashen right at Transform(xalign=0.1, yalign=1.0)
    show s profile despair right at Transform(xalign=-0.1, yalign=1.0) 
    with dissolve
    pause 0.5

    I "Это не кровь капитана…"
    R_t serious think "И правда: приглядевшись, я заметил, что алая жидкость медленно льётся из ушей радиста."
    R_t "В темноте мы смогли разглядеть, как он держится за наушники и прижимает их к голове."

    show v at fear

    V "Эта экспедиция… была обречена…"
    V crazy "Всё! Все знаки указывали на это…"
    V "Мы всё равно не сможем выжить…"

    show v pockets angry at fear
    show s ruki ozadachen

    V pockets angry "Ты!.."
    R_t thinking osharashen "Виктор указал на меня окровавленным пальцем. Рука его дрожала, но во взгляде будто на секунду мелькнул проблеск разума."
    
    show v ruki crazy_down at fear

    V "Всё началось с тебя!.."
    R_t thinking neutral "Я почти не слушал его. Напряжение нарастало, нужно было обдумать план действий."

    show v at angry

    V "Ты один… Один и натворил всё это!.."

    show s shy surprised
    R_t "Софи недоумённо посмотрела на радиста, потом на меня."
    V crazy "Колокольный звон… Шёпот… Скрип колёс… Все эти звуки…"

    show v at fear

    V "Они постоянно преследуют меня!"

    show i at angry

    I ahui "Он просто съехал с катушек, мы должны что-то сделать!"

    call scene_viktor

    jump day_2
