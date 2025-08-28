define PZ_COL_BG = "#101010"
define PZ_COL_FIELD = "#1e1e1e"
define PZ_COL_GRID = "#3c3c3c"
define PZ_COL_DIM = "#000000"
define PZ_COL_HIL = "#ffff00a0"
define PZ_W_GRID = 4
define PZ_PAD = 12
define PZ_DIM_FADE = 1.5

screen _pz_highlight(cell, color=PZ_COL_HIL, t=PZ_W_GRID):
    add Solid(color) xysize (cell, t)
    add Solid(color) xpos 0 ypos cell - t xysize (cell, t)
    add Solid(color) xysize (t, cell)
    add Solid(color) xpos cell - t ypos 0 xysize (t, cell)

transform _pz_dim_in:
    alpha 0.0
    linear 0.5 alpha 0.50

transform _pz_dim_hold:
    alpha 0.50

transform _pz_dim_out:
    alpha 0.50
    linear PZ_DIM_FADE alpha 0.0

screen puzzle_grid_pure(image, grid=4, size=720):
    modal True

    default g = int(grid)
    default n = g * g
    default cell = int(size) // g
    default order = []
    default selection = None
    default lock_hits = []
    default _inited = False
    default was_complete = False
    default win_fade = False

    python:
        def _pz_swap(order, a, b):
            L = list(order)
            if a is None or b is None: return L
            if a == b: return L
            if 0 <= a < len(L) and 0 <= b < len(L):
                L[a], L[b] = L[b], L[a]
            return L

    if not _inited:
        $ order = [i for i in range(n)]
        $ renpy.random.shuffle(order)
        $ _inited = True

    $ is_complete = all(i == order[i] for i in range(n))
    $ just_completed = (is_complete and not was_complete)

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12

        frame:
            background Solid(PZ_COL_BG)
            padding (PZ_PAD, PZ_PAD, PZ_PAD, PZ_PAD)
            xmaximum size + PZ_PAD * 2
            ymaximum size + PZ_PAD * 2
            xminimum size + PZ_PAD * 2
            yminimum size + PZ_PAD * 2

            add Solid(PZ_COL_FIELD)

            for r in range(g):
                for c in range(g):
                    $ pos = r * g + c
                    $ src_idx = order[pos]
                    $ sr = src_idx // g
                    $ sc = src_idx % g
                    $ is_locked = (order[pos] == pos)
                    $ just_locked = (pos in lock_hits)

                    fixed:
                        xpos c * cell
                        ypos r * cell
                        xysize (cell, cell)
                        clipping True

                        fixed:
                            xfill True
                            yfill True
                            add Transform(image, xoffset = -sc * cell, yoffset = -sr * cell)

                            if is_locked:
                                if win_fade:
                                    add Solid(PZ_COL_DIM) id ("dim_%d" % pos) at _pz_dim_out
                                elif just_locked:
                                    add Solid(PZ_COL_DIM) id ("dim_%d" % pos) at _pz_dim_in
                                elif not was_complete:
                                    add Solid(PZ_COL_DIM) id ("dim_%d" % pos) at _pz_dim_hold

                        button:
                            xfill True
                            yfill True
                            sensitive (not is_locked)
                            background None
                            hover_background None
                            action If(
                                selection is None,
                                true=SetScreenVariable("selection", pos),
                                false=[
                                    SetScreenVariable(
                                        "lock_hits",
                                        [ i for i in range(n) if (_pz_swap(order, selection, pos))[i] == i and order[i] != i ]
                                    ),
                                    SetScreenVariable("order", _pz_swap(order, selection, pos)),
                                    SetScreenVariable("selection", None),
                                ]
                            )

            $ col = PZ_COL_GRID
            $ w = int(PZ_W_GRID)
            for r in range(g):
                for c in range(g):
                    $ p = r * g + c
                    $ ok = (order[p] == p)
                    if c < g - 1:
                        $ p2 = r * g + (c + 1)
                        $ ok2 = (order[p2] == p2)
                        if not (ok and ok2):
                            add Solid(col) xpos ((c + 1) * cell - w) ypos (r * cell) xsize w ysize cell
                    if r < g - 1:
                        $ p3 = (r + 1) * g + c
                        $ ok3 = (order[p3] == p3)
                        if not (ok and ok3):
                            add Solid(col) xpos (c * cell) ypos ((r + 1) * cell - w) xsize cell ysize w

            add Solid(col) xpos 0 ypos 0 xsize size ysize w
            add Solid(col) xpos 0 ypos (size - w) xsize size ysize w
            add Solid(col) xpos 0 ypos 0 xsize w ysize size
            add Solid(col) xpos (size - w) ypos 0 xsize w ysize size

            if selection is not None:
                $ rs = selection // g
                $ cs = selection % g
                fixed:
                    xpos cs * cell
                    ypos rs * cell
                    xysize (cell, cell)
                    use _pz_highlight(cell, color=PZ_COL_HIL, t=PZ_W_GRID)

        if lock_hits:
            timer 0.45 action SetScreenVariable("lock_hits", []) repeat False

        if just_completed:
            timer 0.55 action [ SetScreenVariable("was_complete", True), SetScreenVariable("win_fade", True) ] repeat False
        if win_fade:
            timer PZ_DIM_FADE action SetScreenVariable("win_fade", False) repeat False

        hbox:
            spacing 12
            xalign 0.5

            if not is_complete:
                textbutton _("Уйти") action Return(False)

                textbutton _("Сбросить") action [
                    SetScreenVariable("order", renpy.random.sample(range(n), n)),
                    SetScreenVariable("selection", None),
                    SetScreenVariable("lock_hits", []),
                    SetScreenVariable("was_complete", False),
                    SetScreenVariable("win_fade", False),
                ]

            if is_complete:
                textbutton _("Окей") action Return(True)

    key "game_menu" action NullAction()


label test_puzzle_grid_safe:
    scene black
    $ img_path = "images/test_puzzle_2.png"
    call screen puzzle_grid_pure(img_path, grid=2, size=1050)
    if _return:
        "Пазл собран!"
    return
