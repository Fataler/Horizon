label test_talking_system:
    "Тестирование системы говорящих персонажей"
    
    "Конец"
    return

label test_simple_conditions:
    "Тестирование простых условий доступности"
    
    menu:
        "Вариант 1" if False:
            "Вы выбрали вариант 1"
        "Вариант 2":
            "Вы выбрали вариант 2"
        "Вариант 3" if False:
            "Вы выбрали вариант 3"

    return

label test_rayan_states:
    "Тестирование всех состояний персонажа Rayan"
    
    show bg room_rayan

    show r_f serious think
    r_f serious think "r serious think"

    show r_f serious angry
    r_f serious angry "r serious angry"

    show r_f serious very_angry
    r_f serious very_angry "r serious very_angry"

    show r_f serious fainting
    r_f serious fainting "r serious fainting"

    show r_f serious fainting_blood
    r_f serious fainting_blood "r serious fainting_blood"

    show r_f thinking neutral
    r_f thinking neutral "r thinking neutral"

    show r_f thinking not_sure
    r_f thinking not_sure "r thinking not_sure"

    show r_f thinking ne_ponyal
    r_f thinking ne_ponyal "r thinking ne_ponyal"

    show r_f thinking osharashen
    r_f thinking osharashen "r thinking osharashen"

    show r_f thinking suspicious
    r_f thinking suspicious "r thinking suspicious"

    show r_f ear neutral
    r_f ear neutral "r ear neutral"

    show r_f ear dissatisfied
    r_f ear dissatisfied "r ear dissatisfied"

    show r_f ear hehe
    r_f ear hehe "r ear hehe"

    show r_f ear sick
    r_f ear sick "r ear sick"

    show r_f ear surprised
    r_f ear surprised "r ear surprised"
    
    show r_f crazy mnogo
    r_f crazy mnogo "r crazy mnogo"

    show r_f crazy nemnogo
    r_f crazy nemnogo "r crazy nemnogo"

    show r_f crazy pizdec
    r_f crazy pizdec "r crazy pizdec"
    
    return

label test_izumi_states:
    
    show i neutral
    i "izumi neutral"
    show i angry
    i "izumi angry"
    show i asharashen
    i "izumi asharashen"
    show i calm
    i "izumi calm"
    show i dreamy
    i "izumi dreamy"
    show i interested
    i "izumi interested"
    show i neutral_2
    i "izumi neutral_2"
    show i thinking
    i "izumi thinking"
    show i tricky
    i "izumi tricky"
    show i very_angry
    i "izumi very_angry"

    hide i

    return

label test_umi_states:
    "Тестирование всех состояний персонажа Umi"
    
    show bg_amusement_park
    "=== ПОЗА OPEN (ШКОЛЬНАЯ ФОРМА) ==="
    
    show u open neutral school
    u "u open neutral school"
    
    show u open angry school
    u "u open angry school"
    
    show u open cute school
    u "u open cute school"
    
    show u open embarrassed school
    u "u open embarrassed school"
    
    show u open happy school
    u "u open happy school"
    
    show u open happy_4stena school
    u "u open happy_4stena school"
    
    show u open surprised school
    u "u open surprised school"
    
    show u open thinking school
    u "u open thinking school"
    
    "=== ПОЗА OPEN (ЛЕТНЯЯ ФОРМА) ==="

    show u open neutral summer
    u "u open neutral summer"
    
    show u open angry summer
    u "u open angry summer"
    
    show u open cute summer
    u "u open cute summer"
    
    show u open embarrassed summer
    u "u open embarrassed summer"
    
    show u open happy summer
    u "u open happy summer"
    
    show u open happy_4stena summer
    u "u open happy_4stena summer"
    
    show u open surprised summer
    u "u open surprised summer"
    
    show u open thinking summer
    u "u open thinking summer"
    
    "=== ПОЗА CLOSED (ШКОЛЬНАЯ ФОРМА) ==="
    
    show u closed neutral school
    u "u closed neutral school"
    
    show u closed cute school
    u "u closed cute school"
    
    show u closed cry_2 school
    u "u closed cry_2 school"
    
    show u closed asharashen school
    u "u closed asharashen school"
    
    show u closed cry school
    u "u closed cry school"
    
    show u closed touched school
    u "u closed touched school"
    
    show u closed tricky school
    u "u closed tricky school"
    
    "=== ПОЗА CLOSED (ЛЕТНЯЯ ФОРМА) ==="
    
    show u closed neutral summer
    u "u closed neutral summer"
    
    show u closed cute summer
    u "u closed cute summer"
    
    show u closed cry_2 summer
    u "u closed cry_2 summer"
    
    show u closed asharashen summer
    u "u closed asharashen summer"
    
    show u closed cry summer
    u "u closed cry summer"
    
    show u closed touched summer
    u "u closed touched summer"
    
    show u closed tricky summer
    u "u closed tricky summer"
    
    "=== ПОЗА GREETING (ШКОЛЬНАЯ ФОРМА) ==="
    
    show u greeting smile school
    u "u greeting smile school"

    show u greeting confused school
    u "u greeting confused school"
    
    show u greeting offended school
    u "u greeting offended school"
    
    show u greeting sad school
    u "u greeting sad school"
    
    hide u
    "Тест состояний Umi завершён!"
    
    return

label test_taida_states:
    "Тестирование всех состояний персонажа Taida"
    
    show bg_class_room
    
    "=== ПОЗА EAR (БЕЗ ШКОЛЬНОЙ ФОРМЫ) ==="
    
    show t_f ear neutral
    t ear neutral "ear neutral (default)"
    
    show t_f ear careless
    t ear careless "ear careless (беззаботный)"
    
    show t_f ear cute
    t ear cute "ear cute (милый)"
    
    show t_f ear shy
    t ear shy "ear shy"
    
    show t_f ear embarrassed
    t ear embarrassed "ear embarrassed (смущенный)"
    
    show t_f ear happy
    t ear happy "ear happy"
    
    show t_f ear neutral_4stena
    t ear neutral_4stena "ear neutral_4stena"
    
    show t_f ear silly
    t ear silly "ear silly"
    
    show t_f ear confused
    t ear confused "ear confused"
    
    show t_f ear surprised
    t ear surprised "ear surprised"

    show t_f ear cry
    t ear cry "ear cry"

    show t_f ear crazy
    t ear crazy "ear crazy"

    show t_f ear angry
    t ear angry "ear angry"

    show t_f ear asharashen
    t ear asharashen "ear asharashen"

    
    "=== ПОЗА EAR_SCHOOL (В ШКОЛЬНОЙ ФОРМЕ) ==="
    
    show t_f ear_school neutral
    t ear_school neutral "ear_school neutral (default)"
    
    show t_f ear_school cry
    t ear_school cry "ear_school cry (плачет)"
    
    show t_f ear_school dream
    t ear_school dream "ear_school dream (мечтательный)"
    
    show t_f ear_school surprised
    t ear_school surprised "ear_school surprised (удивлен)"
    
    show t_f ear_school angry
    t ear_school angry "ear_school angry"
    
    show t_f ear_school cry_angry
    t ear_school cry_angry "ear_school cry_angry"
    
    show t_f ear_school sad
    t ear_school sad "ear_school sad (печальный)"
    
    show t_f ear_school fear
    t ear_school fear "ear_school fear (испуганный)"
    
    show t_f ear_school crazy
    t ear_school crazy "ear_school crazy (безумие)"
    
    show t_f ear_school happy
    t ear_school happy "ear_school happy (счастливый)"
    
    show t_f ear_school tricky
    t ear_school tricky "ear_school tricky (хитрость)"
    
    show t_f ear_school smile
    t ear_school smile "ear_school smile"
    
    show t_f ear_school think
    t ear_school think "ear_school think"
    
    show t_f ear_school asharashen
    t ear_school asharashen "ear_school asharashen"
    
    show t_f ear_school calm
    t ear_school calm "ear_school calm (спокойный)"
    
    show t_f ear_school depressed
    t ear_school depressed "ear_school depressed (депрессивный)"
    
    "=== ПОЗА THINKING (ПОЗА 2) ==="
    
    show t_f thinking neutral school
    t thinking neutral "thinking neutral (default)"
    
    show t_f thinking cunning school
    t thinking cunning "thinking cunning (хитрый)"
    
    show t_f thinking neutral_4stena school
    t thinking neutral_4stena "thinking neutral_4stena (4 стена)"
    
    show t_f thinking asharashen school
    t thinking asharashen "thinking asharashen (ашарашен)"
    
    show t_f thinking genius stars school
    t thinking genius stars "thinking genius (гений)"
    
    show t_f thinking sleepy school
    t thinking sleepy "thinking sleepy (сонный)"
    
    show t_f thinking think school
    t thinking think "thinking thinking (думает)"
    
    show t_f thinking thinking_hard school
    t thinking thinking_hard "thinking thinking_hard (сильно думает)"
    
    show t_f thinking tired school
    t thinking tired "thinking tired (устал)"
    
    "=== ПОЗА HZ (ПОЗА 1) ==="
    
    show t_f hz neutral school
    t hz neutral "hz neutral (default)"
    
    show t_f hz cry_4stena school
    t hz cry_4stena "hz cry_4stena (плачет 4 стена)"
    
    show t_f hz cry_sad school
    t hz cry_sad "hz cry_sad (плачет подавленно)"
    
    show t_f hz cry_why school
    t hz cry_why "hz cry_why (плачет вопросительно)"
    
    show t_f hz happy school
    t hz happy "hz happy (счастлив)"
    
    show t_f hz smile school
    t "hz smile (улыбается)"
    
    show t_f hz dissatisfied school
    t hz dissatisfied "hz dissatisfied (недоволен)"
    
    show t_f hz neutral_4stena school left
    t hz neutral_4stena "hz neutral_4stena (нейтральный 4 стена)"
    
    show t_f hz glad school right
    t hz glad "hz glad (радуется)"
    
    show t_f hz wtf school
    t hz wtf "hz wtf"
    
    "=== ТЕСТ ЛЕТНЕЙ ФОРМЫ ==="
    
    show t_f ear neutral summer_norm
    t ear neutral summer_norm "ear neutral summer_norm"
    
    show t_f thinking neutral summer_strem
    t thinking neutral summer_strem "thinking neutral summer_strem"
    
    show t_f hz neutral summer_norm
    t hz neutral summer_norm "hz neutral summer_norm"

    show t_f hz neutral summer_strem
    t hz neutral summer_strem "hz neutral summer_strem"

    show t_f thinking genius school
    t thinking genius school "ear neutral school"
    
    hide t_f
    "Тест состояний Taida завершён!"
    
    return

label test_dzinzo_states:
    "Тестирование всех состояний персонажа Dzinzo"
    
    show bg_near_school
    "=== ПОЗА POSE1 (ШКОЛЬНАЯ ФОРМА) ==="
    
    show d_f pose1 neutral school
    d pose1 neutral school "d pose1 neutral school"
    
    show d_f pose1 happy school
    d pose1 happy school "d pose1 happy school"
    
    show d_f pose1 very_happy school
    d pose1 very_happy school "d pose1 very_happy school"
    
    show d_f pose1 surprised school
    d pose1 surprised school "d pose1 surprised school"
    
    show d_f pose1 thinking school
    d pose1 thinking school "d pose1 thinking school"
    
    show d_f pose1 cunning school
    d pose1 cunning school "d pose1 cunning school"
    
    show d_f pose1 relief school
    d pose1 relief school "d pose1 relief school"
    
    "=== ПОЗА POSE1 (ЛЕТНЯЯ ФОРМА) ==="
    
    show d_f pose1 neutral summer
    d pose1 neutral summer "d pose1 neutral summer"
    
    show d_f pose1 happy summer
    d pose1 happy summer "d pose1 happy summer"
    
    show d_f pose1 very_happy summer
    d pose1 very_happy summer "d pose1 very_happy summer"
    
    show d_f pose1 surprised summer
    d pose1 surprised summer "d pose1 surprised summer"
    
    show d_f pose1 thinking summer
    d pose1 thinking summer "d pose1 thinking summer"
    
    show d_f pose1 cunning summer
    d pose1 cunning summer "d pose1 cunning summer"
    
    show d_f pose1 relief summer
    d pose1 relief summer "d pose1 relief summer"
    
    "=== ПОЗА POSE2 (ШКОЛЬНАЯ ФОРМА) ==="
    
    show d_f pose2 neutral school
    d pose2 neutral school "d pose2 neutral school"
    
    show d_f pose2 sad school
    d pose2 sad school "d pose2 sad school"
    
    show d_f pose2 melancholy school
    d pose2 melancholy school "d pose2 melancholy school"
    
    show d_f pose2 asharashen school
    d pose2 asharashen school "d pose2 asharashen school"
    
    show d_f pose2 pupupu school
    d pose2 pupupu school "d pose2 pupupu school"
    
    "=== ПОЗА POSE2 (ЛЕТНЯЯ ФОРМА) ==="
    
    show d_f pose2 neutral summer
    d pose2 neutral summer "d pose2 neutral summer"
    
    show d_f pose2 sad summer
    d pose2 sad summer "d pose2 sad summer"
    
    show d_f pose2 melancholy summer
    d pose2 melancholy summer "d pose2 melancholy summer"
    
    show d_f pose2 asharashen summer
    d pose2 asharashen summer "d pose2 asharashen summer"
    
    show d_f pose2 pupupu summer
    d pose2 pupupu summer "d pose2 pupupu summer"

    "=== ПОЗА POSE3 ==="
    
    show d_f pose3 neutral school
    d pose3 neutral school "d pose3 neutral school"
    
    show d_f pose3 smile school
    d pose3 smile school "d pose3 smile school"
    
    hide d_f
    "Тест состояний Dzinzo завершён!"
    
    return

label test_hikaru_states:
    "Тестирование всех состояний персонажа Hikaru"

    show bg_amusement_park

    "=== ПОЗА idle (ШКОЛЬНАЯ ФОРМА) ==="

    show h idle neutral school right
    h "h idle neutral school"

    show h idle angry school right
    h "h idle angry school"

    show h idle cunning school right
    h "h idle cunning school"

    show h idle shy school right
    h "h idle shy school"

    show h idle happy school right
    h "h idle happy school"

    show h idle smile school right
    h "h idle smile school"

    show h idle surprised school right
    h "h idle surprised school"

    show h idle smug school right
    h "h idle smug school"

    "=== ПОЗА idle (ЛЕТНЯЯ ФОРМА) ==="

    show h idle neutral summer right
    h "h idle neutral summer"

    show h idle angry summer right
    h "h idle angry summer"

    show h idle cunning summer right
    h "h idle cunning summer"

    show h idle shy summer right
    h "h idle shy summer"

    show h idle happy summer right
    h "h idle happy summer"

    show h idle smile summer right
    h "h idle smile summer"

    show h idle surprised summer right
    h "h idle surprised summer"

    show h idle smug summer right
    h "h idle smug summer"

    "=== ПОЗА explain (ШКОЛЬНАЯ ФОРМА) ==="

    show h explain neutral school right
    h "h explain neutral school"

    show h explain neutral_talk school right
    h "h explain neutral_talk school"

    show h explain asharashen school
    h "h explain asharashen school"

    show h explain sad school right
    h "h explain sad school"

    show h explain surprised school right
    h "h explain surprised school"

    "=== ПОЗА explain (ЛЕТНЯЯ ФОРМА) ==="

    show h explain neutral summer right
    h "h explain neutral summer"

    show h explain neutral_talk summer left
    h "h explain neutral_talk summer"

    show h explain asharashen summer right
    h "h explain asharashen summer"

    show h explain surprised summer right
    h "h explain surprised summer"

    "=== Проверка направления LEFT (выборочно) ==="

    show h idle neutral school left
    h "h idle neutral school left"

    show h explain neutral summer left
    h "h explain neutral summer left"

    hide h
    "Тест состояний Hikaru завершён!"

    return

label test_den_states:
    "Тестирование всех состояний персонажа Den"

    show bg_amusement_park

    "=== idle‑RIGHT (ШКОЛЬНАЯ ФОРМА) ==="

    show den idle neutral school right
    den "den idle neutral school"

    show den idle cry school right
    den "den idle cry school"

    show den idle sad school right
    den "den idle sad school"

    show den idle nervous school right
    den "den idle nervous school"

    show den idle asharashen school right
    den "den idle asharashen school"

    "=== idle‑LEFT (ШКОЛЬНАЯ ФОРМА) ==="

    show den idle neutral school left
    den "den idle neutral school left"

    show den idle cry school left
    den "den idle cry school left"

    "=== idle‑RIGHT (ЛЕТНЯЯ ФОРМА) ==="

    show den idle neutral summer right
    den "den idle neutral summer"

    show den idle cry summer right
    den "den idle cry summer"

    show den idle nervous summer right
    den "den idle nervous summer"

    show den idle asharashen summer right
    den "den idle asharashen summer"

    "=== idle‑LEFT (ЛЕТНЯЯ ФОРМА) ==="

    show den idle neutral summer left
    den "den idle neutral summer left"

    show den idle nervous summer left
    den "den idle nervous summer left"

    "=== awesome‑RIGHT (ШКОЛЬНАЯ ФОРМА) ==="

    show den awesome neutral school right
    den "den awesome neutral school"

    show den awesome happy school right
    den "den awesome happy school"

    show den awesome tricky school right
    den "den awesome tricky school"

    show den awesome surprised school right
    den "den awesome surprised school"

    show den awesome sad school right
    den "den awesome sad school"

    show den awesome shy school right
    den "den awesome shy school"

    show den awesome wink school right
    den "den awesome wink school"

    "=== awesome‑LEFT (ШКОЛЬНАЯ ФОРМА) ==="

    show den awesome neutral school left
    den "den awesome neutral school left"

    show den awesome sad school left
    den "den awesome sad school left"

    "=== awesome‑RIGHT (ЛЕТНЯЯ ФОРМА) ==="

    show den awesome neutral summer right
    den "den awesome neutral summer"

    show den awesome happy summer right
    den "den awesome happy summer"

    show den awesome tricky summer right
    den "den awesome tricky summer"

    show den awesome surprised summer right
    den "den awesome surprised summer"

    show den awesome shy summer right
    den "den awesome shy summer"

    show den awesome wink summer right
    den "den awesome wink summer"

    "=== awesome‑LEFT (ЛЕТНЯЯ ФОРМА) ==="

    show den awesome neutral summer left
    den "den awesome neutral summer left"

    show den awesome surprised summer left
    den "den awesome surprised summer left"

    hide den
    "Тест состояний Den завершён!"

    return

label test_teacher_states:
    "Тестирование всех состояний персонажа teacher"
    
    show bg_amusement_park
    "=== ПОЗА idle ==="

    show teacher idle neutral
    teacher "teacher idle neutral"

    show teacher idle angry
    teacher "teacher idle angry"

    show teacher idle smile
    teacher "teacher idle smile"

    show teacher idle surprised
    teacher "teacher idle surprised"

    show teacher idle happy
    teacher "teacher idle happy"
    
    show teacher idle sad
    teacher "teacher idle sad"

    hide teacher
    "Тест состояний teacher завершён!"
    return

label test_seller_states:
    "Тестирование всех состояний персонажа seller"
    
    show bg_amusement_park
    "=== ПОЗА idle ==="

    show seller idle
    seller "teacher idle neutral"

    hide seller
    "Тест состояний seller завершён!"
    return