label day_5_2_2_dont_belive:
    stop music fadeout 1.0
    scene bg_black 
    with dissolve
    pause 1.0
    $ unlock_achievement(ACHIEVEMENT_CRITICAL_MIND)
    pause 1.0
    $ show_space_bg("bg_room_rayan_dark")
    with dissolve
    R_t beard_on serious think "Я снова вернулся на койку."
    R_t thinking neutral "Закрыл глаза и попытался сосредоточиться."
    scene bg_black with eye_off()
    pause 2.0

    R_t beard_on "Спустя некоторое время у меня получилось настроиться."
    call scene_elis from _call_scene_elis_5
    show screen waveform_show
    show scene_talk_in_end_7
    with Dissolve(2.0)
    play sfx2 sfx_hiss_with_voice1 fadein 0.5 fadeout 1.0 loop
    pause 1.0
    N "Ты вернулся!"
    N "Я думала, мы больше не сможем связаться с тобой…"
    R serious angry "Почему?"
    hide scene_talk_in_end_7
    show scene_talk_in_end_9
    R "Что ты несёшь?"
    R "В ваших записях явно какая-то ошибка!"
    R "Членов моей экспедиции зовут Дэвид, Ирис, Виктор и Софи."
    R "Впятером мы направляемся на базу N117 для выгрузки контейнеров с запасами расходных материалов."
    R "Затем планируем вернуться на Землю."
    hide scene_talk_in_end_9
    show scene_talk_in_end_15
    N "Частично это так…"
    R "Частично?!"
    R "О чём вы умалчиваете? Кто вы?!"
    hide scene_talk_in_end_15
    show scene_talk_in_end_13
    N "Райан, это я, Элис."
    N "Знаю, это внезапно, но…"
    N "Я рада, что мне удалось с тобой поговорить."
    R ear dissatisfied "Я не понимаю…"
    hide scene_talk_in_end_13
    show scene_talk_in_end_14
    N "Учёные пригласили меня, потому что тональность моего голоса тебе знакома."
    N "Технология не безупречна. Их голоса не пробивались через барьер в твой разум."
    N "А со мной была хоть какая-то вероятность успеха."
    R_t thinking osharashen "Наконец я узнал её…"
    hide scene_talk_in_end_14
    show scene_talk_in_end_10
    R serious angry "Это какая-то злобная шутка!"
    R "Вы имитируете голос моей девушки, чтобы навязать своё мнение."
    R_t serious think "Я резко осёкся."
    R_t thinking suspicious"Вообще, какого чёрта, какой-то голос в моей голове пытается диктовать мне, что делать?"
    R_t neutral "Возможно, я медленно схожу с ума."
    hide scene_talk_in_end_10
    show scene_talk_in_end_15
    N "Нет, послушай…"
    N "Твоё время на исходе. Мы больше не можем помогать тебе… воскресать."
    N "Раз за разом аномалия доводит тебя до помешательства, нельзя долго оставаться в её поле!"
    N "Это чудо, что ты всё ещё жив…"
    hide scene_talk_in_end_15
    show scene_talk_in_end_10
    R crazy nemnogo "Я уже сошёл с ума! Разве не ясно…"
    R "За миллионы световых лет от Земли я разговариваю не с диспетчером, ха-ха, а со своей девушкой, не имеющей ничего общего с наукой?"
    pause 1.0
    stop sfx2 fadeout 0.5
    hide screen waveform_show with dissolve
    R_t suspicious "Голос вдруг замолчал."
    pause 1.5
    R_t "Спустя небольшую паузу она сказала:"
    pause 1.0
    play sfx2 sfx_drama_boom
    hide scene_talk_in_end_10
    show scene_talk_in_end_19
    pause 1.5
    show screen waveform_show() with dissolve
    play sfx sfx_hiss_with_voice1 fadein 0.5 fadeout 1.0 loop
    N "Все члены экипажа твоей миссии давно мертвы."
    N "Долгое время мы наблюдали за тобой."
    N "И раз за разом ты умирал в полном одиночестве."
    R_t thinking osharashen "Члены экипажа… Всё это время они были лишь фикцией?"
    R_t suspicious "Был один способ проверить."
    hide screen waveform_show with dissolve
    stop sfx2 fadeout 0.5
    stop sfx fadeout 0.5
    $ show_space_bg("bg_room_rayan_dark")
    play music music_anxiety loop

    R_t serious angry"Я без сожаления прервал контакт, встал с постели и пошёл в комнату видеонаблюдения."
    
    play sfx sfx_steps_coridor fadein 0.5 fadeout 0.5 loop
    scene bg_black with dissolve
    pause 1.0
    stop sfx fadeout 1.0
    scene bg_monitors_block with dissolve
    R_t beard_on thinking suspicious "То, что на камерах не было ни одного человека, я уже понял."
    R_t "Но я просто должен проверить записи."
    play sfx sfx_drama_boom
    #music чето сюда возможно надо вставить триллерное подстать цгшке
    call scene_monitory from _call_scene_monitory
    cutscene "Вот я иду к двигателю и… Бью его ножом?"
    cutscene "Следующая запись… Всё в красном свете. Тревога?"
    cutscene  "Перематываю время. Вот я… В отсеке генератора. Падаю в люк?!"
    cutscene "Лежу в коридоре… Вокруг дымка."
    cutscene "В лазарете в окружении пустых блистеров?.."

    stop music fadeout 1.0
    scene bg_black
    with dissolve
    pause 1.0
    R_t crazy mnogo "Всё это время…"

    scene bg_black
    with dissolve
    pause 1.0
    #music чето безнадежное, смирение
    play music music_quite_ambient2 fadein 0.5 fadeout 0.5 loop
    $ show_space_bg("bg_commander_block_transparent_default")
    with dissolve
    pause 1.0
    R_t beard_on thinking suspicious "Впереди был лишь бесконечный космос."
    R_t "Пространство, наполненное рождающимися и погибающими звёздами."
    R_t "Яркими точками на чёрной бархатной ткани."
    R_t "Они то затухали, то загорались снова, словно подмигивая."
    R_t neutral "Холод за стеклом словно пробирался под кожу и заставлял её покрыться мурашками."
    R_t "Я уже давно потерял надежду."
    R_t suspicious "Если голос, который связался со мной, и был настоящим, больше он не выходил на контакт."
    R_t "Всё, что мне оставалось, это сидеть на своём кресле и наблюдать, как движется весь этот разноцветный поток."
    R_t ear dissatisfied "Я взял спиртовую салфетку, протёр руки и блестящий металлический блистер, лежащий на моей приборной панели."
    R_t "А затем принял сразу пять таблеток."
    R_t "Они помогают мне чувствовать себя спокойно."
    R_t thinking neutral "Я перекрестился, закрыл глаза и зашептал слова своей собственной молитвы."
    R_t "Затем пальцами потёр виски."
    R_t "Когда я это делаю, я вижу не темноту скрытого за веками мира."
    R_t "А всё тот же вид — бескрайний и чуждый."
    R_t not_sure "Возможно, пришло время исполнить свою мечту?.."
    R_t suspicious "Как я всегда и хотел."
    R_t "Плыть в бесконечности."
    R_t "Совсем как дома у моря, только в нескончаемую пустошь."
    pause 1.0
    R_t crazy nemnogo "…"
    pause 1.0
    call scene_photo from _call_scene_photo
    stop music fadeout 1.0
    
    pause 1.0
    $ show_space_bg("bg_commander_block_transparent_default")
    with dissolve
    R_t beard_on crazy nemnogo "…"
    pause 1.0
    R_t mnogo "Что ж. Время настало."

    scene bg_black
    with dissolve
    pause 1.5
    play music music_quite_ambient2 loop
    show space_bg_image 
    show bg_exit_open zorder 10
    show exit_door
    with dissolve
    R_t beard_on crazy nemnogo "Я стоял на пороге шлюза."
    R_t "Мне не нужен был скафандр."
    R_t "Он помешал бы мне дрейфовать в волнах."
    R_t "Последний раз окинул базу взглядом."
    play sfx sfx_push_button
    R_t "И нажал на рычаг."
    play sfx sfx_metal_door
    show exit_door at space_door_open() zorder 9
    R_t "С медленным звуком большая железная дверь шлюза начала отворяться."
    
    play sfx2 sfx_steps_one
    show layer master at screen_step_zoom(zoom1=1.00, zoom_str=0.05)
    $ renpy.pause(2.0, hard=True)
    play sfx2 sfx_steps_one
    show layer master at screen_step_zoom(zoom1=1.05, zoom_str=0.05)
    
    R_t mnogo "Впереди — только бесконечность."
    
    $ renpy.pause(1.0, hard=True)
    play sfx2 sfx_steps_one
    show layer master at screen_step_zoom(zoom1=1.1, zoom_str=0.05)
    $ renpy.pause(2.0, hard=True)
    play sfx2 sfx_steps_one
    show layer master at screen_step_zoom(zoom1=1.15, zoom_str=0.05)
    $ renpy.pause(2.0, hard=True)

    #music может немного раньше надо посмтреть

    scene cosmos_fon 
    with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    scene bg_black 
    with Dissolve(3.0)
    $ renpy.pause(3.0, hard=True)

    $ unlock_achievement(ACHIEVEMENT_DREAM)
    $ renpy.pause(1.0, hard=True)
    call label_credits from _call_label_credits
