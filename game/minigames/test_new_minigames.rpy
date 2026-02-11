label test_new_minigames_pack:
    scene black
    with fade

    menu:
        "Пакет тестов мини-игр"

        "1) Найти пару":
            call test_memory_pairs
            jump test_new_minigames_pack
        "2) Трубы":
            call test_pipes_minigame
            jump test_new_minigames_pack
        "3) Вентили":
            call test_valves_minigame
            jump test_new_minigames_pack
        "4) Ремонт матрицы":
            call test_repair_matrix_minigame
            jump test_new_minigames_pack
        "Выход":
            return
