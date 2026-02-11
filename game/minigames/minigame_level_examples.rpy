init python:
    # Примеры конфигов уровней для повторного использования в сюжете.

    memory_pairs_level_story_a = {
        "id": "bridge_memory_a",
        "rows": 4,
        "cols": 4,
        "hide_delay": 0.62,
    }

    pipes_level_story_a = {
        "id": "generator_pipes_a",
        "preset": "fixed_demo",
        # Можно переопределять отдельные поля пресета:
        # "initial_rotations": [[0,1,2,3,0,1], ...]
    }

    valves_level_story_a = {
        "id": "pressure_valves_a",
        "marks": 8,
        "target": 0,
        "ops": [[1, 1, 2], [2, 1, 1], [1, 2, 1]],
        "start_values": [5, 2, 7],
        "scramble": False,
    }

    repair_matrix_level_story_a = {
        "id": "repair_core_a",
        "preset": "compact_demo",
        "require_all_blocks": False,
    }


label test_minigame_level_examples:
    scene black
    with fade

    "Пример: уровни из словарей-конфигов."

    call memory_pairs_minigame(level=memory_pairs_level_story_a)
    call pipes_minigame(level=pipes_level_story_a)
    call valves_minigame(level=valves_level_story_a)
    call repair_matrix_minigame(level=repair_matrix_level_story_a)

    "Тест завершен."
    return
