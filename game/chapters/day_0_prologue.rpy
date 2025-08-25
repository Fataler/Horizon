label day_0_prologue:

    # Пролог

    scene bg_black
    with dissolve
    pause 1.0
    play sfx sfx_click2

    R_t "Щёлк."

    play sfx sfx_click2
    pause 0.2
    play sfx sfx_click2

    R_t "Щёлк-щёлк."

    #цг гг лицом в экран

    R_t thinking not_sure "Фух, вроде работает."
    R_t thinking ne_ponyal "Ну и ну."
    R_t serious think "Запишу в следующем докладе, что у нас неполадки с основным генератором."

    scene bg_coridor2_default
    with dissolve

    R_t serious think "При всей педантичности нашего механика, видать, ей недостаёт знаний или опыта для починки этого недоразумения."
    
    play sfx sfx_steps fadein 0.5 fadeout 0.5 loop

    R_t ear neutral "Пора возвращаться в общий зал."

    scene black with dissolve
    pause 0.5
    scene bg_dinner_block
    stop sfx fadeout 1.0
    show i smoke puzzled left at Transform(xalign=0.8, yalign=1.0)
    show s profile neutral left at Transform(xalign=1.2, yalign=1.0)
    show v pockets suspects left at quad_left_center
    show d serious osharashen right at Transform(xalign=-0.1, yalign=1.0)
    with dissolve

    R_t serious think "Остальные члены экипажа уже ждали меня."
    R_t serious think "Лица их выражали мрачное недовольство."
    R_t serious think "Ужин начинал остывать."
    I normal angry "Это уже надоедает."
    R_t ear hehe "Я усмехнулся."
    R ear hehe "Следующая очередь — твоя, не так ли?"
    V "Давно ли нам приходится определять очередь для того, чтобы пощёлкать выключателем?"
    I smoke calm "Предлагаю делегировать эту задачу тому, кто не может справиться со своими рабочими обязанностями."

    show s despair

    R_t thinking ne_ponyal "Механик виновато улыбнулась и пожала плечами."
    S shy worried "Увы, я делаю всё возможное."
    R_t "Я решил немного утешить коллег."
    R ear hehe "Не вижу сложности размяться и сходить прогуляться в генераторную."
    R "Разминка очень полезна для мышц и суставов."
    R "Приступим к ужину или будем продолжать попытки переложить ответственность?"

    play sfx sfx_kitchen fadein 0.5 fadeout 0.5 loop
    show i normal neutral
    show s profile neutral
    show v pockets sad
    show d neutral

    R_t "Команда опустила глаза и принялась орудовать вилками."

    pause 1.0

    R_t "Некоторое время мы сидели в тишине."
    R_t "Первым её решил прервать капитан."

    show i smoke surprised
    show s ruki ozadachen
    show v ruki puzzled left
    show d calm
    stop sfx fadeout 0.5

    D "Что ж… Вы, наверное, хотите узнать, какие у нас дальнейшие планы?"
    R_t serious think "Ответа не последовало, но всё внимание было обращено на оратора."
    D fist annoyed "Как вы уже знаете, третий день мы находимся без связи."
    D fist confused "Виктор пытается связаться с командным центром на протяжении всего этого времени, но безуспешно."

    show v pockets sad

    R_t "Радист развёл руками и продолжил натыкать синтетические овощи на вилку."
    D happy "Рано унывать — у нас всё ещё есть планы на миссию и возможность их осуществить."
    D serious smile "По прогнозам, мы прибудем на планету через пять дней. Всё верно, Райан?"
    R_t thinking ne_ponyal "Я кивнул."
    R not_sure "Согласно изначальным координатам — всё так."
    D neutral "Там, на базе, нам точно удастся связаться с начальством."

    play sfx sfx_cup_on_table
    show d fist smug
    R_t ne_ponyal "Капитан потёр лоб, улыбнулся и стукнул по столу."
    D fist annoyed "Поэтому приказ на сегодня такой: умерить свою гордыню и пересмотреть отношение к членам экипажа."
    D confused "Это относится ко всем тем, кто по какой-то причине не уверен в коллегах."
    D serious neutral "На этом всё, ужин окончен. Всем спокойного сна."

    hide d with dissolve
    play sfx sfx_kitchen_table fadein 0.5 fadeout 1.0
    play sfx2 sfx_steps fadein 0.5 fadeout 1.0 loop

    R_t "Экипаж неспешно прибрал за собой столы и начал расходиться по своим каютам."

    scene black with dissolve
    pause 0.5
    scene bg_coridor1_default
    with dissolve
    stop sfx2
    stop sfx fadeout 1.0

    R_t thinking not_sure "Экспедиция словно не задалась с самого начала."
    R_t "Надежды на дружный экипаж не оправдались, но это было не так важно."
    R_t serious think "В крайнем случае, я всегда мог уткнуться в одну из тех книг, что взял с собой."
    R_t "В какой-то степени они — отдушина для моего уставшего после тяжёлого дня разума."
    R_t thinking neutral "Книги — это своеобразные галлюцинации, которые ты можешь генерировать в своём мозгу при чтении."
    R_t "Таким образом, даже будучи далеко, на просторах холодного недружелюбного космического вакуума, ты можешь оказаться в любом месте этой вселенной."
    R_t ne_ponyal "Чем я и собрался сейчас заняться."

    stop sfx2 fadeout 1.0
    scene bg_room_rayan_default
    with dissolve
    #музыка Anxious space ambient

    R_t ear neutral "Наш корабль был неплохо оборудован."
    R_t "Да, никто из нас не смог попасть в ту команду, членом экипажа которой хотел бы быть."
    R_t hehe "Волею случая нас распределили в команду «Сборная солянка из отбросов»."
    R_t thinking neutral "Тем не менее, нам дали достойную машину с вполне комфортными жилыми отсеками."
    R_t ear neutral "Даже более комфортными, чем в моей обычной прошлой жизни."
    R_t serious think "Я снял рабочую форму, потянулся."
    R_t "Размял уставшие после целого дня ступни и с большим удовольствием нырнул под тёплое тяжёлое одеяло."
    R_t "Прямо над койкой находился отсек, в котором я хранил свои излюбленные истории."
    R_t thinking ne_ponyal "Где бы мне хотелось оказаться сегодня?"
    R_t "Кто-то больше всего грустит по зелёной траве у дома, кто-то — о близких."
    R_t not_sure "Я же жалел о странном — что не могу вдохнуть дым от сигарет вместе с запахом моря. Потому сегодня, думаю, остановлю свой выбор на Хемингуэе."
    R_t neutral "Во время чтения незаметно и вкрадчиво сон накрывал меня с головой, поэтому лишь в полудрёме я заметил, как погас ночник."

    scene bg_black
    with fade
    jump day_1