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
        "5) Шифр-коммутатор":
            call test_cipher_switch_minigame
            jump test_new_minigames_pack
        "6) Охота на сигнал":
            call test_signal_hunt_minigame
            jump test_new_minigames_pack
        "8) Спектральная калибровка":
            call test_spectral_calibration_minigame
            jump test_new_minigames_pack
        "Выход":
            return
