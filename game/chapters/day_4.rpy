label day_4:
    scene bg_black
    with dissolve
    pause 2.0

    show cosmos_fon with dissolve
    #play sfx2 music_space_ambient fadein 1.0 fadeout 1.0 loop
    pause 1.0
    R_t ear surprised "Где я?"
    R_t "Вокруг летели миллиарды звёзд с огромной скоростью, унося меня куда-то."
    R_t "Никаких ощущений — будто моего тела не существует. Но мысли вернулись."
    R_t thinking suspicious "Что всё это было? Я умер? Или это очередной сон?"
    R_t "Нет, это уже не похоже на обычные тревожные сны. Нужно думать критически."

    stop sfx2 fadeout 1.0
    $ show_space_bg("bg_room_rayan_default")

    R_t ear surprised "Я сразу открыл глаза. Сна не было ни в одном глазу."
    R_t "Часы показывали 08:00 — время, когда я просыпаюсь каждый день."
    R_t thinking not_sure "Но вчера я не засыпал в своей кровати. Я, чёрт возьми, умер от отравления."

    play sfx sfx_click2
    pause 0.2
    play sfx sfx_click2
    call scene_mirror_water
    with dissolve
    cutscene "В зеркале — мой обычный вид: всё тот же усталый и измождённый парень вдали от дома."
    cutscene "Не было и следа той боли, что преследовала меня — во сне или вчера."
    $ show_space_bg("bg_room_rayan_default")
    R "Расслабляться рано, Райан…"

    scene bg_coridor1_default
    with dissolve
    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop

    R_t "Быстро накинув форму, я выдвинулся в сторону кухни. Нужно быть начеку и понять, что происходит."
    
    stop sfx fadeout 0.5
    scene bg_black with dissolve
    pause 0.5
    scene bg_dinner_block
    show i smoke happy left at Transform(xalign=0.7, yalign=1.0)
    show s ruki neutral right at quad_left_center
    show v profile tricky right at Transform(xalign=-0.1, yalign=1.0)
    show d serious neutral left at Transform(xalign=1.1, yalign=1.0)
    with dissolve
    play sfx2 sfx_talk_people fadein 0.5 fadeout 0.5 loop

    R_t ear neutral "Я аккуратно заглянул внутрь. Внутри собрались все — было весело и шумно."
    R_t "Экипаж собрался пораньше и уже успел позавтракать. На столе — карты."
    R_t "Стараясь войти незамеченным, я шагнул в проход и встал у стены."
    R_t "Кажется, сегодня все поели заготовленную еду из вакуумных упаковок."
    R_t dissatisfied "Я же, пожалуй, устрою себе разгрузочный день."

    show s ruki neutral left at fear

    S "Я побью твою карту!.."

    show v pockets happy at fear

    V "Ха-ха, как бы не так! Лови козырь. Минус три очка и потеря хода!"

    show s ozadachen
    show d smile

    R_t "Софи насупилась. Дэвид стоял рядом и усмехаясь попивал чай."

    show i tricky

    R_t "Ирис лишь загадочно улыбалась, разглядывая свои карты. Она явно ждала, когда Софи и Виктор потратят потенциал друг на друга."

    show s shy happy

    S "О, Райан! Доброе утро!"

    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    stop sfx2 fadeout 0.5
    scene bg_coridor1_default
    with dissolve
    
    R_t serious think "Я уже был в коридоре: первым делом — проверить генератор."

    scene bg_black with dissolve
    pause 0.5
    stop sfx fadeout 0.5
    scene bg_generator_blue_screen
    with dissolve

    R_t "На первый взгляд всё было в норме. Подача энергии есть, охлаждение в порядке."
    R_t thinking suspicious "Я вскрыл люк и принюхался — никаких следов спирта."

    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    scene bg_black with dissolve
    pause 0.5
    scene bg_coridor2_default
    with dissolve
    R_t "Двигательная?"

    scene bg_black with dissolve
    pause 0.5
    scene bg_engine
    stop sfx fadeout 0.5
    play sfx2 sfx_fon_generator2 fadein 0.5 fadeout 0.5 loop
    with dissolve
    R_t ear neutral "Никаких аномалий. Панели закрыты и хорошо закручены."
    R_t ear dissatisfied "Воспользовавшись своей картой заместителя капитана, я заблокировал дверь."

    play sfx sfx_pisk_one
    scene bg_black with dissolve
    stop sfx2 fadeout 1.0
    pause 0.5
    scene bg_coridor1_default
    play sfx sfx_steps_fast fadein 0.5 fadeout 0.5 loop
    with dissolve
    
    R_t serious angry "Лазарет. Я уже бежал к нему, понимая, что скоро все разойдутся по рабочим местам."

    scene bg_black with dissolve
    stop sfx
    pause 0.5
    scene bg_med_block_dark
    with dissolve

    R_t ear neutral "В помещении было темно и прохладно. Запах лекарств щекотал нос."
    R_t "Сейф стоял под столом, но времени проверять не было — может быть, позже."
    R_t "В шкафчиках находились наши запасы — всё на месте. Ничего подозрительного."

    play sfx sfx_steps_short fadein 0.5 fadeout 0.5

    R_t "За дверью послышались шаги."

    stop sfx fadeout 0.5

    I "Ладно, мне пора, увидимся за обедом!.."
    R_t ear dissatisfied "В голосе Ирис слышалась смешинка."
    I "Если, конечно, ты снова не поранишься."
    S "Хи-хи, я очень постараюсь не прийти к тебе лишний раз."
    S "Ой, подожди. Я совсем забыла — я должна была отдать тебе свой дневник наблюдений…"
    I "Вообще, я собиралась заняться его анализом прямо сейчас."
    S "Пойдём, я тебе его отдам? Прогуляемся."
    play sfx sfx_steps_short
    I "Эх… ну что с тобой поделать, пойдём."
    R_t surprised "Я шумно выдохнул. Кажется, пронесло. Дождавшись, пока шаги стихнут, я выскользнул из кабинета."
    
    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    scene bg_black with dissolve
    pause 0.5
    scene bg_coridor1_default
    with dissolve

    R_t thinking not_sure "Неужели мне действительно всё померещилось? Кажется, недосып сыграл злую шутку."
    R_t ne_ponyal "Нужно возвращаться в командный центр."

    scene bg_black with dissolve
    pause 0.5
    stop sfx fadeout 0.5
    $ show_space_bg("bg_commander_block_transparent_default")

    R_t thinking ne_ponyal "Наконец я на своём рабочем месте, но тревога не отпускала."
    R_t "Некоторое время я пытался понять её причину. Откинулся на кресле — и дёрнулся как ошпаренный."
    R_t osharashen "Вот что я не проверил…"

    $ show_space_bg("bg_stul_bez_igl")

    R_t serious think "Ни одной дырки в обшивке, никаких следов порезов."
    R_t thinking ne_ponyal "Пожалуй, не помешало бы обратиться к психиатру — у Ирис есть соответствующий сертификат."

    $ show_space_bg("bg_commander_block_transparent_default")

    R_t "Цифры и графики плыли перед глазами. Облегчение приносил только вид из окна."

    #play sfx sfx_heart_beat_neutral fadein 0.5 fadeout 0.5 loop

    scene bg_black_t_90
    with dissolve

    # 8 начало
    $ show_scene_cosmos("8")
    cutscene "Я перестал чувствовать себя в безопасности."
    cutscene "Будто вернулся в подростковые годы, когда к нам переехала тётя по отцовской линии."
    cutscene "Вызвать её приступ ярости не составляло труда. Страшнее всего было по вечерам, когда она возвращалась с работы и выпивала."
    cutscene "Позже я понял, что её зависимость не ограничивалась алкоголем."
    $ hide_scene_cosmos()
    # 8 конец
    # 9 начало
    $ show_scene_cosmos("9")
    cutscene "Иногда она запиралась в своей комнате, и мы слышали её приглушённые крики от обиды на весь мир."
    cutscene "Она не состоялась в карьере, не завела семью и во всём винила окружающих."
    cutscene "В худшем случае она кошмарила домочадцев и громила дом."
    cutscene "После бури мы выбирались из своих комнат и прибирали беспорядок."
    $ hide_scene_cosmos()
    # 9 конец
    # 13 начало
    $ show_scene_cosmos("13")
    cutscene "В такие моменты я брал младшую сестру за руку, и мы уходили к морю."
    cutscene "Сестра набирала сухих веток и листьев, а я разжигал небольшой костёр, чтобы не замёрзнуть в вечерней прохладе."
    cutscene "А затем мы рассказывали друг другу смешные и страшные истории. Это было неплохое время, несмотря ни на что."
    $ hide_scene_cosmos()
    # 13 конец


    D "Райан! Хватит витать в облаках."
    D "Ты слышишь меня?!"
    $ show_space_bg("bg_commander_block_transparent_default")

    show d fist angry
    with dissolve

    R_t thinking osharashen "Я резко дёрнулся от неожиданности." with hpunch
    D serious neutral "Ты проверил, что автопилот ведёт нас правильно? Где мы сейчас находимся?"

    play sfx sfx_pisk_one

    R_t "Я обратил внимание на приборы. Координаты… Вот что я забыл проверить."
    R_t "По координатам мы там же, где были пять дней назад."
    R ear surprised "Командир, кажется, мы стоим на месте."

    show d serious angry with dissolve

    R_t "Лицо Дэвида побагровело."
    D "Что ты сказал? Почему я узнаю об этом только сейчас?"    
    R_t "Капитан яростно зашипел себе под нос."

    show d at angry

    D "Я знал, что не могу вам доверять… никому."

    play sfx sfx_door_open
    play sfx2 sfx_steps_two
    show v ruki puzzled left at enter_scene(time=1.0, xalign=1.1)

    R_t "В этот момент в помещение зашёл Виктор — и сразу принял весь гнев на себя."

    show d right at angry
    show v osharashen

    D "Ты!.. Ты тоже виноват."
    V pockets nedovolen "Я ещё не успел войти и уже в чём-то виноват? О чём ты вообще?"

    show d right at angry

    D "Молчать! Были ли данные от начальства в ближайшие дни? Где координаты, которые нам должны были прислать?!"
    V "Новых указаний не было. Ты сам понимаешь, что мы практически в изоляции."
    V "Сюда почти не доходят сигналы."

    show d right at angry

    D "Просто никто из вас не хочет заниматься своей работой. Я должен всё делать за вас!"

    play sfx2 sfx_steps_fast
    show d at move_on_scene(time=0.5, xalign=1.0)
    pause 0.5
    show d at angry
    play sfx sfx_hit
    show v profile angry at move_step(30), fear
    show d fist confused at move_on_scene(time=1.0, xalign=1.7) 

    R_t "Дэвид толкнул Виктора плечом и вышел из командного центра."

    stop sfx2 fadeout 1.0
    play sfx sfx_fall_body
    show v scared at jump, fear with dissolve

    R_t "Не успевший отреагировать Виктор потерял равновесие и приземлился на пятую точку."
    V ruki osharashen "И что это было?"
    R_t serious think "Я лишь пожал плечами."
    V "Он и раньше был себе на уме — это что-то новенькое."
    R thinking suspicious "Нет, в чём-то он прав…"
    V "О чём ты?"
    R "Наше местоположение действительно странное. Похоже, нас что-то держит на одних координатах."
    R not_sure "Как будто и вчера, и позавчера…"
    V pockets nedovolen "Думаю, эту проблему решим позже, а сейчас проследим за капитаном, пока он не натворил делов!"

    show v pockets think at Transform(xalign=1.1, yalign=1.0) with dissolve

    R_t "Я помог радисту подняться. Мы увидели, куда пошёл Дэвид, и двинулись за ним."

    play sfx sfx_steps_two
    scene bg_black with dissolve
    pause 0.5
    scene bg_coridor2_default
    show d serious angry left at Transform(xalign=-0.1, yalign=1.0)
    with dissolve
    play sfx3 sfx_strem_steps fadein 0.5 fadeout 0.5 loop
    show v profile scared left at Transform(xalign=1.1, yalign=1.0)
    with dissolve

    show d at angry
    play sfx sfx_hit

    R_t serious think "Он шёл и кричал что-то невразумительное, будто сошёл с ума."

    show d at angry
    play sfx2 sfx_hit_reverb

    R_t serious think "Периодически бил стены, разбивая кулаки и оставляя кровавые следы."

    play sfx2 sfx_hit_reverb
    show d at angry

    R_t "Заходил в отсек за отсеком, задерживаясь ненадолго. Ближе подойти мы не решались."

    stop sfx3 fadeout 0.5
    scene bg_coridor1_default
    show v profile scared left at Transform(xalign=1.1, yalign=1.0)
    with dissolve

    play sfx sfx_ballons2

    R_t serious think "Дольше всего он возился у отсека с баллонами: слышались вентили и грохот."
    V tricky "Не выпил таблетки, да?"
    R_t angry "Мне было не до шуток: у капитана явно было не всё в порядке."
    R_t think "Я успокоился было, решив, что сны — просто сны. Теперь понимаю, что нет."
    R_t angry "Каждый из членов экипажа поочерёдно свихнулся. Что дальше?.."

    scene bg_coridor3_red_cylinders_smoke
    show d serious angry left at Transform(xalign=-0.1, yalign=1.0)
    with dissolve
    show v profile scared left at Transform(xalign=1.1, yalign=1.0)
    with dissolve

    play sfx sfx_ballons2
    play sfx2 sfx_cough_man2
    R_t ear sick "Я открыл дверь и сразу закашлялся: едкий дым ударил в нос."

    play sfx3 sfx_steps_fast_two
    show d at move_on_scene(xalign=-1.7)

    R serious very_angry "Нужно срочно всё перекрыть!"
    play sfx2 sfx_cough_man2
    R_t "Мы бросились останавливать утечку. Горло жгло; я заходился в кашле."
    R "О чём он вообще думал? Надо догнать его."

    play sfx3 sfx_steps_fast fadein 0.5 fadeout 0.5 loop
    scene bg_black with dissolve
    pause 0.5
    stop sfx3 fadeout 0.5
    scene bg_med_block_red
    #show d fist confused right at Transform(xalign=0.8, yalign=1.0)
    #show i profile osharashen left at Transform(xalign=1.1, yalign=1.0)
    #show s shy surprised right at Transform(xalign=0.3, yalign=1.0)
    with dissolve
    show v profile angry right at Transform(xalign=-0.1, yalign=1.0)
    with dissolve

    R_t serious angry "Обнаружили мы его уже в лазарете. Внутри был полный погром."
    R_t "Дэвид опрокинул шкафы и держал Ирис."

    play sfx sfx_drama
    call scene_pogrom_v_lazarete
    
    #show s at angry

    cutscene "Нет, прекрати!"

    #show i at fear

    cutscene "Отпусти меня!.."

    stop sfx fadeout 0.5
    scene bg_med_block_red
    show d fist confused right at Transform(xalign=0.8, yalign=1.0)
    show i profile osharashen left at Transform(xalign=1.1, yalign=1.0)
    show s shy surprised right at Transform(xalign=0.3, yalign=1.0)
    show v profile angry right at Transform(xalign=-0.1, yalign=1.0)
    with dissolve
    pause 0.5

    play sfx sfx_steps_two
    show v crazy at move_step(200)
    show s ruki crazy at move_step(200)
    pause 0.5
    play sfx2 sfx_hit
    show d serious angry at move_step(50)
    show i at move_step(100)
    pause 1.0
    play sfx sfx_steps_fast_short
    show d left at move_on_scene(time=3.0, xalign=-1.7)

    R_t very_angry "Мы рванули на помощь, но он вытолкнул Ирис внутрь и рванул к выходу."
    D "Пока вы не натворили ещё чего-нибудь, посидите здесь!"

    play sfx3 sfx_door_open
    $ renpy.transition(hpunch)
    pause 0.7
    play sfx2 sfx_pisk_one

    R_t "Дверь захлопнулась: он успел воспользоваться карточкой командира."
    V ruki osharashen "С тобой всё в порядке?"
    I oooops "Д-да… Небольшая ссадина, ничего страшного."
    R angry "Что он сделал?"
    S shy nedovolen "Влетел и начал кричать, что Ирис крадёт лекарства… Бред."
    R "Мы должны выбраться и обезвредить его."

    hide d
    hide s
    hide i
    hide v
    with dissolve

# эскейп рум
#ГЕЙМДЕЗИГН

# Активные элементы: дверь, экран, ноут, сейф
# Дверь:
# R Не поддаётся. Нужно придумать, как разблокировать её.

# Экран:
# R Экран требует приложить руку.

# Выбор:
# Кому попробовать?

# Райан: отпечаток не распознан.
# Ирис: отпечаток не распознан.
# Виктор: отпечаток не распознан.
# Софи: отпечаток не распознан.

# R ear dissatisfied Не получится.
# R Требует отпечаток Дэвида.

# Сейф:
# R thinking suspicious Может, здесь есть что-то полезное.
# Выбор открыть/не открыть.

# Открыть:
# R Что ж, попробуем. Какой там был пароль?
# R neutral Что-то знакомое…
# R not_sure Ирис, ты же знаешь пароль?
# I Нет, я не пользуюсь им…
# R Что ж…
# Пароль 1734.

# Удачно:
# R_t Внутри пусто… и достаточно пыльно.
# R_t Но в середине сейфа я увидел место, не покрытое пылью.
# R_t Очень похоже, что недавно здесь что-то лежало.

# Выход:
# R_t Я так и не смог понять, какой был пароль.
# R_t Не важно. Времени перебирать нет.

# Не открывать:
# R Не будем тратить на это время.
# R Мы должны решить, как выбраться.

# Ноут:
# S Кажется, я могу попробовать взломать систему.
# V Ты и такое умеешь?
# R_t Софи мило смутилась.
# S Немножко.
# Открывается игра «сбор квадратиков».

# Выход:
# R Ладно, поищем альтернативу.

# Удачно:
# R Есть!
# play sfx sfx_door_open
# R_t Дверь с небольшим металлическим скрипом отворилась.
# R Поспешим!
# V Постойте!
# R_t Виктор набрал тканевых салфеток из контейнера, намочил их в воде и раздал членам экипажа.
# I Для чего это?..
# R Надеюсь, это не пригодится.

    scene bg_black with dissolve
    pause 0.5
    scene bg_coridor2_red_smoke
    play sfx3 sfx_noise_banging fadein 0.5 fadeout 0.5 loop
    show i profile neutral left at Transform(xalign=1.15, yalign=1.0)
    show s profile sad left at Transform(xalign=0.85, yalign=1.0)
    show v profile sad left at Transform(xalign=0.5, yalign=1.0)
    with dissolve

    R_t serious think "Только мы вышли из лазарета, как я почувствовал тяжесть в воздухе."

    play sfx sfx_cough_women
    show s despair at fear
    show i osharashen
    show v angry
    
    S "Кх…"

    show v pockets sorry right with dissolve

    V "Приложи к носу!"
    R_t serious angry "Мокрая ткань помогала фильтровать воздух, но идти быстро было нельзя."

    play sfx2 sfx_steps_slow fadein 0.5 fadeout 0.5 loop
    show v profile sad left with dissolve

    I angry "До противогазов мы не доберёмся…"
    R very_angry "Видимо, Дэвид всё же открыл баллоны. Мы потеряли много времени."
    V crazy "Остановим его!"
    R_t ear dissatisfied "Пытаясь дышать через мокрую ткань, мы шли по коридору. Я дышал через раз, но лёгкие всё равно наполнялись газом."
    
    stop sfx3 fadeout 0.5
    show d fist fainting right at Transform(xalign=-0.1, yalign=4.0) with dissolve
    stop sfx2 fadeout 1.0

    R_t surprised "Со временем видимость ухудшилась; в лёгкой дымке мы разглядели капитана — он лежал на полу и не двигался."
    
    call scene_pulse
    play sfx2 sfx_heart_beat_neutral loop

    R_t serious fainting "Похоже, слишком поздно. Ноги подкашивались — я не был уверен, что доберусь до баллонов…"
    S shy surprised "Райан!.."
    I ahui "Он падает!.."

    play sfx sfx_fall_body
    stop sfx2 fadeout 0.5
    stop sfx3 fadeout 0.8
    scene bg_black
    with fade

    R_t serious fainting "Уже теряя сознание, я услышал:"
    play sfx sfx_hiss_with_voice1
    N "Возвращаем назад… Он почти смог… Ещё раз…"
    N "Это последний шанс для него!.. Дайте мне попробовать! Пустите!.."
    stop sfx fadeout 0.5
    jump day_5
