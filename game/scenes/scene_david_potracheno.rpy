image scene_david_potracheno_fon = "CG/CG_David_potracheno/CG_David_potracheno_0001_fon.png"
image scene_david_potracheno_cherkash = "CG/CG_David_potracheno/CG_David_potracheno_0000_cherkash.png"

label scene_david_potracheno:
    show scene_david_potracheno_fon
    show scene_david_potracheno_cherkash at soot_drift_bottom(speed=1.0, amplitude=3, x_amplitude=2)
    with dissolve

    cutscene "Дэвид лежал на полу в луже крови, вяло пытаясь вынуть нож из груди."
    cutscene "Алые брызги окропили всё вокруг. Аппаратура радиста была сломана; в комнате — следы схватки."
    cutscene "Капитан смотрел на нас помутневшим взглядом."

    hide scene_david_potracheno_fon
    hide scene_david_potracheno_cherkash
    with dissolve
    return

label scene_david_potracheno_2:
    show scene_david_potracheno_fon
    show scene_david_potracheno_cherkash at soot_drift_bottom(speed=1.0, amplitude=3, x_amplitude=2)
    with dissolve

    cutscene "Я держал его за руку."
    cutscene "Мы были знакомы совсем немного и лишь последние несколько недель провели на одном корабле, но я не мог сглотнуть горький ком, застрявший в горле."
    cutscene "Я смотрел, как в нём угасала жизнь, и наполнялся яростью."

    hide scene_david_potracheno_fon
    hide scene_david_potracheno_cherkash
    with dissolve
    return
