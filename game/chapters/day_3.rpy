label day_3:
    #"День 3"

    scene bg_black
    with dissolve
    scene bg_room_rayan_default
    with dissolve

    R_t serious angry "Очнуться мне пришлось в холодном поту."
    R_t ear sick "Очередной неприятный сон."
    R_t serious think "Я поднялся на локтях."
    R_t "В руках чувствовалось лёгкое покалывание."
    R_t ear sick "Прислушавшись к своему телу, я ощутил лёгкую боль во всех мышцах."
    R_t "В каюте было настолько жарко, что сложно дышать, хотя поверхности предметов оставались прохладными."
    R_t dissatisfied "Может быть, это побочные эффекты от быстрого пробуждения?"
    R_t "Очень реалистичное сновидение оставило свой след."
    R_t thinking calm "Неприятно, но ничего особенного — такое мы тоже уже проходили."
    R_t ne_ponyal "Судя по всему, я немного проспал: нужно спешить."

    show layer master at screen_shake
    R_t serious fainting "Я резко поднялся с кровати, но ноги сразу подкосились."

    play sfx sfx_fall_body

    R_t "Скованность и резкая боль заставили меня упасть." with vpunch
    R_t "Хватаясь руками за холодный металл пола, я подполз к зеркалу."

    play sfx sfx_hit

    R_t ear sick "Костяшки пальцев побелели от того, как крепко я сжал края умывальника в попытке подняться." with vpunch
    
    #цг зеркало с ожогами
    
    R_t thinking osharashen "С той стороны зеркала на меня смотрел я… но покрытый ожогами."

    play sfx sfx_heart_beat_fast fadein 0.5 fadeout 0.5 loop

    R_t serious angry "Какого чёрта?.."
    R_t "Это был не сон."
    R_t ear dissatisfied "Сердце колотилось как бешеное." 

    play sfx sfx_heart_beat_slow fadein 0.5 fadeout 0.5

    R_t "Я попытался восстановить дыхание."
    R_t "С такими ожогами не живут. Я всё ещё сплю, не иначе."
    R_t ear sick "Я крепко зажмурил глаза, несколько раз поморгал и снова взглянул на своё отражение."

    #цг зеркало нормальное

    R_t surprised "Спокойно, это всего лишь наваждение."
    R_t "Я стал совсем плохо спать."
    R_t dissatisfied "Головная боль накатывала волнами."
    R_t "Никак не получалось собраться с мыслями."
    R_t "Я неспешно оделся, не глядя отметил в терминале начало рабочего дня и вышел в коридор."

    scene bg_coridor1_default
    with dissolve
    play sfx sfx_steps_slow fadein 0.5 fadeout 0.5 loop

    R_t ear surprised "Нетвёрдым шагом я двинулся к кухне."
    R_t "Генератор работал исправно, и в помещениях было светло."
    R_t "Но свет в пищевом блоке был особенно резким."
    R_t sick "Я инстинктивно прикрыл глаза рукой."
    R_t "Экипаж уже собрался за завтраком."

    scene bg_black with dissolve
    pause 0.5
    scene bg_dinner_block
    show i smoke happy left at Transform(xalign=0.7, yalign=1.0)
    show s ruki neutral right at Transform(xalign=-0.1, yalign=1.0)
    show v ruki tricky left at quad_left_center
    show d serious neutral left at Transform(xalign=1.1, yalign=1.0)
    with dissolve
    stop sfx fadeout 1.0
    pause 0.5

    S ruki happy "Доброе утречко!\~"
    D smile "Привет, Райан!"

    show i calm
    show v pockets happy

    R_t ear surprised "Виктор и Ирис дружелюбно кивнули."

    #анимация экрана
    show s shy worried
    show i surprised
    show d osharashen
    show v ruki osharashen

    show layer master at screen_shake
    R_t ear sick "Я попытался кивнуть им в ответ, но слегка пошатнулся."
    V ruki puzzled "Неважно себя чувствуешь сегодня?"
    I pen ozadachen "Может быть, мне посмотреть, что с тобой?"
    R ear hehe "Нет, всё в порядке. Спасибо."

    show s ruki ozadachen left at move_step(-30)

    R_t serious think "Софи помогла мне присесть за стол."

    show s ruki neutral right
    show i normal neutral
    show v ruki shy
    show d serious neutral

    R_t "Пахло очень вкусно — причиной был омлет с помидорами, который приготовила Ирис из наших небольших запасов органической пищи."
    R_t thinking ne_ponyal "Нам приходится чередовать органику с пищей из тюбиков, чтобы растянуть её на более долгий срок."
    R_t neutral "Ведь иногда хочется поесть нормальной человеческой пищи."
    R_t "И вот, сегодня такой день."
    R_t not_sure "Если бы я чувствовал себя хорошо, это бы сильно подняло мне настроение. Но, увы."

    show i profile tricky with dissolve
    play sfx sfx_putting_down_plate

    R_t serious think "Ирис заботливо крутилась у стола, как пчёлка, раздавая каждому по порции."
    I "Я подумала, что мы мало общаемся. И вообще, все такие грустные и серьёзные."
    I normal neutral_happy "Разве это не повод для особенного завтрака?"
    I ridicule "Вы такого ещё не пробовали."

    show i neutral_happy
    show s shy happy at giggle
    show d smile

    R_t "Софи радостно похлопала в ладоши, даже Дэвид усмехнулся."
    V pockets happy "Приятного аппетита, ребята."

    play sfx sfx_kitchen fadein 0.5 fadeout 1.0 loop

    V ruki tricky "И, кстати, тоже готов порадовать вас новостями."
    V cunning "Я ухватил сигнал за хвост. Как доедим — сразу расшифровывать!"

    show d fist happy

    R_t "Дэв одобрительно похлопал Виктора по спине."
    D "Действительно добрые новости."

    show s shy neutral at fear with dissolve
    pause 0.5

    R_t "Софи внезапно засуетилась и встала из-за стола."
    #R_t "Я проследил за ней."

    show s profile happy left at move_step(-50)
    pause 2.0
    play sfx sfx_click2

    R_t "Она подошла к магнитофону у стены, протёрла его и нажала кнопку."

    #музыка лёгкая
    show s ruki neutral right at move_step(50)
    show d serious smile
    show i smoke happy
    show v tricky

    R_t "Лёгкая приятная музыка разлилась по кухне."

    play sfx2 sfx_talk_people fadein 0.5 fadeout 1.0 loop

    R_t ear neutral "Ещё некоторое время они весело болтали, обсуждали новости, свою жизнь и еду."
    R_t surprised "Я одновременно словно был здесь, но и был где-то снаружи."
    R_t dissatisfied "Казалось, будто время включило ускоренную перемотку, и коллеги бегали мимо меня, смеялись и жили где-то в другом, быстром временном потоке."
    
    show v right
    
    V pockets happy "Было очень вкусно, спасибо, Ирис."

    show i profile tricky

    R_t "Ирис улыбнулась."
    I "Обращайтесь."

    pause 1.0
    stop sfx2 fadeout 1.0


    R_t "Народ начал потихоньку расходиться."

    play sfx sfx_steps_short
    show v profile smile left at move_on_scene(xalign=-1.0)
    pause 1.5
    show i left at move_on_scene(xalign=-1.0)

    show s neutral right 

    R_t "Софи осталась, чтобы продезинфицировать стол."

    play sfx sfx_steps_short
    show d serious calm left at move_on_scene(xalign=-1.0)

    R_t "Дэвид, как обычно, направился на обход."
    R_t ear neutral "И мне стоило пойти к себе."

    scene black with dissolve
    pause 0.5
    scene bg_coridor1_default
    with dissolve
    play sfx sfx_steps fadein 0.5 fadeout 1.0 loop

    R_t serious think "День начинался как обычно."
    R_t "Можно даже сказать, что неплохо."
    R_t "Экипаж был явно в приподнятом настроении."
    R_t thinking suspicious "Но меня не покидало ощущение, что что-то не так."
    R_t neutral "Это был первый раз, когда я чувствовал физические последствия после сна."
    R_t not_sure "Почему я вообще ощущаю то, чего не было?"

    stop sfx fadeout 1.0
    scene black with dissolve
    pause 0.5
    scene bg_commander_block_transparent_default
    with dissolve

    R_t serious think "Я добрался до своего рабочего места."
    R_t ear sick "В глазах двоилось от головной боли."
    R_t "Кофе не смог заглушить её."
    R_t surprised "Я проверил показания приборов — всё было в порядке."
    R_t "Никаких аномальных данных, радиация в норме."
    R_t serious think "Это помогло мне немного успокоиться."
    R_t thinking ne_ponyal "Я взглянул в своё огромное окно — этот вид умиротворяет."

    #фон космос
    scene bg_black_t_90
    with dissolve

    R_t thinking ne_ponyal "Мне сразу вспомнилась моя сестра."
    R_t ear hehe "Моя любимая младшая сестрёнка."
    R_t surprised "Она всегда была очень болезненной. С самого детства мне приходилось ухаживать за ней."
    R_t "У неё было очень слабое здоровье, врачи никак не могли найти причину."
    R_t dissatisfied "Любой сквозняк обеспечивал ей простуду на неделю или две."
    R_t ear hehe "А сколько раз мы заболевали на пару после купания в небольшом скалистом заливе у дома — не счесть."
    R_t neutral "Поэтому она всегда была тревожной."
    R_t thinking ne_ponyal "За её лёгкой улыбкой часто скрывались боль и беспокойство."
    R_t "Панический страх грязи, бактерий и чужих прикосновений сопровождал её жизнь с самого раннего возраста."
    R_t suspicious "Я всегда старался быть рядом, но не в моих силах было ей помочь."
    R_t neutral "Со временем она превратилась в затворницу, которая почти не выходила из своей комнаты."
    R_t "Сестрёнка всегда ходила в перчатках, протирала все поверхности и никогда не открывала окна."
    R_t ne_ponyal "Она оставалась всё такой же добродушной, но странной девочкой."
    R_t ear surprised "В какой-то момент мы отдалились друг от друга."
    R_t "Даже проживая под одной крышей."
    R_t dissatisfied "Когда мне стукнуло семнадцать, я просто сбежал."
    R_t thinking ne_ponyal "Мне нужно было учиться и строить свою жизнь."
    R_t "Во время нашей последней встречи она выглядела особенно слабой и грустной."
    R_t serious think "И только сейчас, находясь в бескрайнем космосе вдали от дома, я понял, что просто обязан вернуться."

    scene bg_commander_block_transparent_default
    with dissolve

    play sfx3 sfx_stun
    
    show bg_white at light_hurt
    pause 2.0
    show bg_white at alpha_mask_fade_inverse
    pause 1.0
    stop sfx3 fadeout 2.0
    show bg_black at alpha_mask_fade

    R_t ear sick "Моё тело резко пронзил приступ боли."
    play sfx2 sfx_burning_fire fadein 0.5 fadeout 1.0 loop
    #call scene_pulse
    #play sfx2 sfx_heart_beat_neutral loop
    R_t "Только в этот раз это была не просто головная боль."
    R_t "Я словно снова горел в огне."
    R_t "Я чувствовал, как моя кожа обугливается изнутри."

    play sfx sfx_door_open
    show d serious neutral at right
    show expression Solid("#fff") as overlay_light at light_hurt
    pause 2.0
    show expression Solid("#fff") as overlay_light at alpha_mask_fade_inverse
    pause 1.0
    show expression Solid("#000000") as overlay_light at alpha_mask_fade
    stop sfx2 fadeout 1.0
    with dissolve

    R_t ear sick "В этот момент в помещение зашёл Дэвид."
    D osharashen "Райан, ты в порядке?"
    R serious fainting "Я… Я думаю, мне нужно в лазарет…"
    D "Что с тобой? Тебе нужна помощь?"

    show d fist angry at move_step(-200)
    play sfx3 sfx_stun
    show expression Solid("#fff") as overlay_light at light_hurt
    pause 2.0
    show expression Solid("#fff") as overlay_light at alpha_mask_fade_inverse
    pause 1.0
    stop sfx3 fadeout 2.0
    show expression Solid("#000000") as overlay_light at alpha_mask_fade
    pause 1.0
    call scene_pulse
    play sfx2 sfx_heart_beat_neutral loop

    R_t ear sick "Он поддержал меня под локоть, но от этого боль только усилилась."
    show expression Solid("#000000") at alpha_mask
    show expression Solid("#000000") at alpha_mask_fade
    R serious fainting "Нет… Я доберусь сам…"

    show d serious osharashen

    #R_t "Дэвид посмотрел на меня с сомнением и ушёл к своему рабочему месту."
    R_t "Дэвид посмотрел на меня с сомнением, но останавливать не стал."
    R_t "Мне предстояло преодолеть несколько коридоров."

    play sfx sfx_steps_slow loop
    scene black with dissolve
    pause 0.5
    scene bg_coridor1_default
    call scene_pulse
    show expression Solid("#000000") at alpha_mask(a=0.6)

    R_t ear sick "Ноги плохо слушались."
    R_t serious fainting "Ощущения то стихали, то накатывали с новой силой."
    R_t ear sick "Я держался, как мог."

    #фон коридор 2
    scene bg_coridor2_default
    call scene_pulse
    

    with dissolve

    R_t ear sick "Шаг. Ещё шаг."
    R_t "Я уговаривал себя сделать каждое движение."
    R_t serious fainting "Почти потеряв сознание, я добрался до медблока."

    stop sfx fadeout 0.5
    scene bg_black with dissolve
    pause 0.5
    scene bg_med_block
    show i profile neutral
    call scene_pulse
    show expression Solid("#000000") at alpha_mask(a=0.6)

    R serious fainting "Ирис…"

    show i pen ozadachen with dissolve

    R_t "Врач обернулась на мой зов."
    I "Райан, всё в порядке?!"

    stop sfx2 fadeout 1.0

    R_t ear sick "Я с трудом присел на койку. Боль немного утихла."
    R "Мне кажется… Ты знаешь, такое чувство, как будто…"

    show i normal bychit

    R_t "Ирис снисходительно посмотрела на меня, ожидая продолжения."
    R_t thinking osharashen "Я посмотрел ей прямо в глаза."
    R "Я горю?.."
    I "Опиши поподробнее, в каком месте ты ощущаешь дискомфорт?"
    R ear surprised "Ты не поняла…"
    R sick "Это душераздирающая боль, как будто моя кожа сгорает."
    R "Она сгорает и возрождается, чтобы снова сгореть."

    show i angry

    R_t thinking osharashen "Девушка удивлённо подняла брови, взяла фонарик и осмотрела мои зрачки."
    R_t ear sick "От яркого света стало не по себе."
    I smoke calm "Друг мой, с тобой всё в порядке."
    I happy "Симптомы ещё не должны были проявиться."
    R thinking osharashen "О чём ты говоришь?"
    I calm "Это не важно. Тебе нужно просто немного отдохнуть."
    I normal neutral_happy "Все эти ипохондрические загоны, знаешь, легко снимаются полноценным сном и питанием."
    I ridicule "Питание сегодня уже налажено благодаря мне."
    R ear dissatisfied "Дай мне обезболивающее."

    play sfx sfx_hit
    show i profile oooops with dissolve

    R_t "Ирис машинально прикрыла ладонью дверцу шкафчика и начала отмахиваться от моей просьбы."
    I normal very_ridicule "Запас почти на исходе, да и зачем тебе пичкать себя таблетками лишний раз?"
    R_t serious angry "Я вышел из себя."

    show i bychit

    R serious very_angry "Сейчас же!.." with hpunch

    play sfx sfx_laugh_female3
    show i crazy with dissolve

    R_t "Ирис презрительно фыркнула."
    R_t thinking osharashen "Показалось, что её лицо превратилось в какую-то жуткую маску."

    show i at fear

    R_t "Она, не глядя, вынула из шкафа блистер и кинула мне."
    R_t serious very_angry "Я взглянул на неё волком и понял, что здесь помощи искать не стоит."

    show i at angry

    I "Ты чёртов симулянт. Пошёл прочь."
    R_t serious angry "Такого даже от Ирис я не ожидал."
    R_t ear dissatisfied "Но у меня не было сил ей перечить."
    R_t "Я должен добраться до своей каюты."

    play sfx sfx_steps_slow fadein 0.5 fadeout 0.5 loop
    scene bg_black with dissolve
    pause 0.5
    scene bg_coridor1_default
    call scene_pulse
    show expression Solid("#000000") at alpha_mask(a=0.6)

    R_t ear dissatisfied "Крепко сжимая драгоценный блистер в кулаке так, что края металлической оболочки врезались в руку, я брёл по коридору."
    R_t "Я сделаю то, что всегда помогало мне."

    stop sfx fadeout 0.5
    scene bg_black with dissolve
    pause 0.5
    scene bg_room_rayan_default
    call scene_pulse
    show expression Solid("#000000") at alpha_mask(a=0.6)

    R_t ear dissatisfied "Уже в своей комнате я решил принять лекарство."
    R_t "Набрав воды в стакан прямо из умывальника, я прочитал название на упаковке."
    R_t serious angry "Витамины… Чёртова упёртая психопатка."    
    R_t ear sick "Я медленно прилёг на свою кровать и закрыл глаза."

    scene bg_black with dissolve
    pause 0.5

    R_t ear sick "Всегда, когда мне было плохо, я находил укромное место — уголок, где никто не потревожит меня."
    R_t thinking neutral "Закрывал глаза и слушал."
    R_t "Звук моря всегда успокаивал меня."
    R_t "Он словно смывал боль, волна за волной — понемногу, но становилось легче."
    R_t "Сейчас же я мог слышать только шум вентиляции и редкий металлический стук."
    R_t "Цикличный и глухой, совершенно чужеродный."
    R_t "Я сосредоточился и попытался воссоздать волны в своей голове."

    #голос девушки
    R_t "Но вместо этого услышал голос."
    R_t "Это были обрывки слов."
    R_t "Ненадолго я перестал ощущать что-либо и сосредоточился ещё сильнее."

    #незнакомка

    R_t "Женский голос пробивался сквозь моё сознание."
    #голос девушки
    N "Райан, ты меня слышишь?.."
    #голос девушки
    N "…Разорви круг…"
    #голос девушки
    N "Ты можешь ответить мне?.."
    R_t "Незнакомка звучала растерянно, но настойчиво."
    R_t "Голос был подозрительно знакомым…"
    R_t "Но я не смог разобрать личность говорящей."
    R_t thinking neutral "В растерянности я провалился в сон."
    pause 3.0
    #R_t "…"

    S "Райан!"

    scene bg_room_rayan_default
    with dissolve

    R_t thinking suspicious "Я приоткрыл глаза."
    R_t "Боли больше не было."

    show s shy surprised with dissolve

    S "Райан, помоги!"
    S "С Ирис что-то случилось…"
    S worried "Она и остальные в лазарете."
    R "Что с ней?"
    S ruki ozadachen "Нам нужно поспешить!"

    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop
    scene bg_coridor1_default
    show s profile sad 
    with dissolve

    R_t thinking suspicious "Мрачные мысли лезли в голову."
    R_t neutral "Припоминая её тёплый приём, мне не хотелось лишний раз её видеть."

    scene bg_coridor2_default
    show s profile sad left
    with dissolve
    pause 0.5
    show s annoyed at fear
    R_t "Софи очень суетилась и всё время боролась между желанием ухватить меня за руку, чтобы ускорить шаг, и нежеланием касаться других людей."
    R_t serious think "Я ускорился, чтобы не доставлять ей дискомфорт."

    stop sfx fadeout 0.5
    scene black with dissolve
    pause 0.5
    scene bg_med_block
    show i profile angry left at Transform(xalign=1.15, yalign=3.0)
    show d serious neutral right at Transform(xalign=0.2, yalign=1.0)
    show s ruki ozadachen right at Transform(xalign=-0.15, yalign=1.0)
    show v pockets sad right at Transform(xalign=0.7, yalign=1.0)
    with dissolve

    R_t serious think "В лазарете уже находились все оставшиеся члены экипажа."
    R_t "Я не сразу смог разглядеть, но Ирис лежала на полу у кровати."
    #, Дэвид стоял над ней.
    R_t "Рука врача была прикована наручником к ножке кровати."

    show i angry at angry

    R_t thinking osharashen "Увидев меня, девушка начала биться на полу, как рыба, пытаясь высвободить руку."
    R_t "На коже уже начали появляться тёмно-красные и фиолетовые следы синяков."

    show d at fear

    D fist angry "Что ты делаешь?! Прекрати это сейчас же!"

    show i angry at angry

    I "Ненавижу…"
    R_t serious think "Виктор сидел, скорчившись, на койке."
    R_t "Лицо его приобрело болезненный вид."
    D serious calm "Кажется, Виктор отравился. Я и сам чувствую лёгкое недомогание."
    D osharashen "Как ты? Кажется, сегодня утром тебе тоже было не по себе."
    R ear sick "С самого утра я чувствую, как будто моё тело жжёт…"
    R_t dissatisfied "Я посмотрел на свои руки."
    R_t "Они были абсолютно обычными, без каких-либо признаков ожогов."

    show s profile despair right at move_on_scene(time=1.0, xalign=-0.05)

    R_t "Софи метнулась к шкафам."

    show s shy worried at step_up, fear
    pause 1.0
    play sfx sfx_falling_objects

    R_t "Она открывала створку за створкой, заглядывала на полки и выдвигала ящики."    

    show s shy worried at fear
    play sfx sfx_falling_objects

    R_t "Пустые блистеры звякали об металл."
    S shy surprised "Здесь пусто…"
    S "Обезболивающих нет."
    R serious angry "Она ещё утром отказывалась мне их дать. Я знал, что она что-то скрывает."
    S shy angry "Запас на полгода... пуст?"

    show s ruki ozadachen with dissolve

    R_t "Она подняла потрёпанный блокнот."
    S shy worried "Смотри — журнал."
    R_t thinking osharashen "На страницах были записи: перечни «проступков» экипажа и злые заметки."
    R serious angry "Ирис, это твой почерк."
    I normal crazy "А тебе какое дело?"

    show i at angry
    play sfx sfx_heat_metal

    R_t "Ирис резко дёрнула наручник, заскрежетал металл."
    R_t "Глаза её стекленели."
    I "Обезболивающего хватит только на меня."

    show i at angry

    I angry "Я не собираюсь делиться."
    I "Вы всё равно не достойны."
    V nedovolen "Ч-что ты сделала?.."
    I very_ridicule "Немного добавки к вашему идеальному рациону."
    I crazy "Вы все почувствуете — скоро."

    play sfx3 sfx_stun fadein 0.5 fadeout 0.5 loop
    show bg_white at light_hurt
    pause 2.0
    show bg_white at alpha_mask_fade_inverse
    play sfx2 sfx_heart_beat_neutral loop
    call scene_pulse
    pause 1.0
    show bg_black at alpha_mask_fade

    R_t serious fainting "Меня повело."
    R_t "Пол поплыл, в ушах зашумело."

    show d fist fainting at jump, fear 
    play sfx sfx_hit

    R_t "Дэвид схватился за край стола."
    D fainting "Голова…"

    show v ruki crazy at jump, fear 

    R_t "Виктор сжал виски и осел на койку."
    V "Тошнит…"

    show s shy fainting at jump, fear 

    R_t "Софи попыталась поднять меня за плечо, но сама пошатнулась."
    S "Держись…"
    R_t "Я держался крепче всех и наблюдал, как один за другим члены экипажа теряют сознание."
    R_t "Я взглянул на часы."
    R_t "Время показывало 21:59."

    show bg_black at alpha_mask_fade(a=0.7)
    R_t serious fainting "Головокружение накатывало, но прежде чем я потерял сознание, я отчётливо услышал голос."
    
    #голос девушки
    N "Ты должен понять."
    N "Никто не поможет тебе, кроме тебя самого."

    play sfx sfx_fall_body
    stop sfx2 fadeout 1.0
    stop sfx3 fadeout 1.0
    scene bg_black with dissolve
    return
