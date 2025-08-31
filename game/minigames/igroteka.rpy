label igroteka_puzzle(id, grid=3):
    $ renpy.block_rollback()
    $ renpy.call_in_new_context("igroteka_puzzle_internal", id, grid)
    jump extra_menu_return

label igroteka_puzzle_internal(id, grid=3):
    call screen puzzle_grid_pure("minigames/puzzle/Puzzle.png", grid=grid, size=720)
    if _return:
        $ mark_igroteka_completed(id)
    return

label igroteka_hanoi(id, blocks=3):
    $ renpy.block_rollback()
    $ renpy.call_in_new_context("igroteka_hanoi_internal", id, blocks)
    jump extra_menu_return

label igroteka_hanoi_internal(id, blocks=3):
    call hanoi_game(blocks_number=blocks)
    if _return:
        $ mark_igroteka_completed(id)
    return

label igroteka_placeholder(id):
    "Игра пока недоступна"
    jump extra_menu_return

label extra_menu_return:
    call screen extra_menu
    return
