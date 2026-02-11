init python:
    import copy

    MG_PIPE_N = 1
    MG_PIPE_E = 2
    MG_PIPE_S = 4
    MG_PIPE_W = 8

    MG_PIPE_DIRS = {
        MG_PIPE_N: (0, -1),
        MG_PIPE_E: (1, 0),
        MG_PIPE_S: (0, 1),
        MG_PIPE_W: (-1, 0),
    }

    MG_PIPE_OPPOSITE = {
        MG_PIPE_N: MG_PIPE_S,
        MG_PIPE_E: MG_PIPE_W,
        MG_PIPE_S: MG_PIPE_N,
        MG_PIPE_W: MG_PIPE_E,
    }

    MG_PIPE_ROTATE_MAP = {
        MG_PIPE_N: MG_PIPE_E,
        MG_PIPE_E: MG_PIPE_S,
        MG_PIPE_S: MG_PIPE_W,
        MG_PIPE_W: MG_PIPE_N,
    }

    PIPES_FLOW_LEVELS = {
        "easy": {
            "mode": "generated",
            "width": 5,
            "height": 5,
            "min_path_ratio": 0.34,
            "min_path_extra": 2,
        },
        "standard": {
            "mode": "generated",
            "width": 6,
            "height": 6,
            "min_path_ratio": 0.40,
            "min_path_extra": 2,
        },
        "hard": {
            "mode": "generated",
            "width": 8,
            "height": 7,
            "min_path_ratio": 0.48,
            "min_path_extra": 3,
        },
        "fixed_demo": {
            "mode": "fixed",
            "start": (0, 2),
            "end": (5, 2),
            "target_masks": [
                [0, 0, MG_PIPE_E | MG_PIPE_S, MG_PIPE_E | MG_PIPE_W, MG_PIPE_S | MG_PIPE_W, 0],
                [0, MG_PIPE_E | MG_PIPE_S, MG_PIPE_W | MG_PIPE_N, 0, MG_PIPE_N | MG_PIPE_S, 0],
                [MG_PIPE_E, MG_PIPE_E | MG_PIPE_W, MG_PIPE_E | MG_PIPE_W, MG_PIPE_E | MG_PIPE_W, MG_PIPE_W | MG_PIPE_N, MG_PIPE_W],
                [0, MG_PIPE_N | MG_PIPE_S, 0, 0, 0, 0],
                [0, MG_PIPE_N | MG_PIPE_E, MG_PIPE_E | MG_PIPE_W, MG_PIPE_E | MG_PIPE_W, MG_PIPE_S | MG_PIPE_W, 0],
                [0, 0, 0, 0, MG_PIPE_N | MG_PIPE_E, MG_PIPE_W],
            ],
            "locked_positions": [(0, 2), (5, 2)],
        },
    }


    def mg_pipe_rotate_mask(mask, times):
        result = int(mask)
        for _i in range(int(times) % 4):
            next_mask = 0
            for bit in (MG_PIPE_N, MG_PIPE_E, MG_PIPE_S, MG_PIPE_W):
                if result & bit:
                    next_mask |= MG_PIPE_ROTATE_MAP[bit]
            result = next_mask
        return result


    def _pipes_norm_pos(value):
        if isinstance(value, (list, tuple)) and len(value) >= 2:
            return (int(value[0]), int(value[1]))
        return None


    def _pipes_norm_grid(grid):
        if not isinstance(grid, (list, tuple)) or len(grid) == 0:
            return None

        rows = []
        width = 0
        for row in grid:
            if not isinstance(row, (list, tuple)):
                continue
            cleaned = [int(v) for v in row]
            if len(cleaned) > width:
                width = len(cleaned)
            rows.append(cleaned)

        if not rows or width <= 0:
            return None

        normalized = []
        for row in rows:
            if len(row) < width:
                row = list(row) + [0] * (width - len(row))
            normalized.append(list(row[:width]))
        return normalized


    def _pipes_norm_positions(raw_list):
        if not isinstance(raw_list, (list, tuple)):
            return []
        out = []
        for item in raw_list:
            pos = _pipes_norm_pos(item)
            if pos is not None:
                out.append(pos)
        return out


    def pipes_flow_resolve_level(
        level=None,
        width=None,
        height=None,
        mode=None,
        target_masks=None,
        start=None,
        end=None,
        initial_rotations=None,
        locked_positions=None,
        min_path_ratio=None,
        min_path_extra=None,
    ):
        cfg = copy.deepcopy(PIPES_FLOW_LEVELS["standard"])
        level_id = "standard"

        if isinstance(level, str):
            if level in PIPES_FLOW_LEVELS:
                cfg = copy.deepcopy(PIPES_FLOW_LEVELS[level])
                level_id = str(level)
        elif isinstance(level, dict):
            preset = level.get("preset")
            if isinstance(preset, str) and preset in PIPES_FLOW_LEVELS:
                cfg = copy.deepcopy(PIPES_FLOW_LEVELS[preset])
                level_id = str(preset)
            for key, val in level.items():
                if key in ("id", "preset"):
                    continue
                cfg[key] = copy.deepcopy(val)
            level_id = str(level.get("id", level_id if level_id else "custom"))

        if width is not None:
            cfg["width"] = width
        if height is not None:
            cfg["height"] = height
        if mode is not None:
            cfg["mode"] = mode
        if target_masks is not None:
            cfg["target_masks"] = target_masks
        if start is not None:
            cfg["start"] = start
        if end is not None:
            cfg["end"] = end
        if initial_rotations is not None:
            cfg["initial_rotations"] = initial_rotations
        if locked_positions is not None:
            cfg["locked_positions"] = locked_positions
        if min_path_ratio is not None:
            cfg["min_path_ratio"] = min_path_ratio
        if min_path_extra is not None:
            cfg["min_path_extra"] = min_path_extra

        cfg["mode"] = "fixed" if str(cfg.get("mode", "generated")).lower() == "fixed" else "generated"
        cfg["min_path_ratio"] = max(0.20, float(cfg.get("min_path_ratio", 0.40)))
        cfg["min_path_extra"] = max(1, int(cfg.get("min_path_extra", 2)))

        cfg["target_masks"] = _pipes_norm_grid(cfg.get("target_masks"))
        cfg["initial_rotations"] = _pipes_norm_grid(cfg.get("initial_rotations"))

        if cfg["mode"] == "fixed" and cfg["target_masks"]:
            cfg["height"] = len(cfg["target_masks"])
            cfg["width"] = len(cfg["target_masks"][0])

        cfg["width"] = max(4, int(cfg.get("width", 6)))
        cfg["height"] = max(4, int(cfg.get("height", 6)))

        cfg["start"] = _pipes_norm_pos(cfg.get("start"))
        cfg["end"] = _pipes_norm_pos(cfg.get("end"))
        cfg["locked_positions"] = _pipes_norm_positions(cfg.get("locked_positions"))

        return {
            "width": cfg["width"],
            "height": cfg["height"],
            "mode": cfg["mode"],
            "target_masks": cfg["target_masks"],
            "start": cfg["start"],
            "end": cfg["end"],
            "initial_rotations": cfg["initial_rotations"],
            "locked_positions": cfg["locked_positions"],
            "min_path_ratio": cfg["min_path_ratio"],
            "min_path_extra": cfg["min_path_extra"],
            "level_id": level_id,
        }


    class PipesFlowGame(object):
        def __init__(
            self,
            width=6,
            height=6,
            mode="generated",
            target_masks=None,
            start=None,
            end=None,
            initial_rotations=None,
            locked_positions=None,
            min_path_ratio=0.40,
            min_path_extra=2,
            level_id="custom",
        ):
            self.width = max(4, int(width))
            self.height = max(4, int(height))
            self.mode = "fixed" if str(mode).lower() == "fixed" else "generated"
            self.min_path_ratio = max(0.20, float(min_path_ratio))
            self.min_path_extra = max(1, int(min_path_extra))
            self.level_id = str(level_id)

            self.moves = 0
            self.completed = False
            self.message = "Соберите поток от S к E."

            self.tiles = {}
            self.path = []
            self.start = None
            self.end = None

            self._config = {
                "width": self.width,
                "height": self.height,
                "mode": self.mode,
                "target_masks": copy.deepcopy(target_masks),
                "start": copy.deepcopy(start),
                "end": copy.deepcopy(end),
                "initial_rotations": copy.deepcopy(initial_rotations),
                "locked_positions": copy.deepcopy(locked_positions),
                "min_path_ratio": self.min_path_ratio,
                "min_path_extra": self.min_path_extra,
                "level_id": self.level_id,
            }

            if self.mode == "fixed" and isinstance(target_masks, (list, tuple)) and target_masks:
                self._build_fixed_level(target_masks, start, end, initial_rotations, locked_positions)
            else:
                self._build_generated_level()

            self._refresh_completion()

        def _decoy_masks(self):
            return [
                MG_PIPE_N | MG_PIPE_S,
                MG_PIPE_E | MG_PIPE_W,
                MG_PIPE_N | MG_PIPE_E,
                MG_PIPE_E | MG_PIPE_S,
                MG_PIPE_S | MG_PIPE_W,
                MG_PIPE_W | MG_PIPE_N,
                MG_PIPE_N | MG_PIPE_E | MG_PIPE_S,
                MG_PIPE_E | MG_PIPE_S | MG_PIPE_W,
                MG_PIPE_S | MG_PIPE_W | MG_PIPE_N,
                MG_PIPE_W | MG_PIPE_N | MG_PIPE_E,
                MG_PIPE_N | MG_PIPE_E | MG_PIPE_S | MG_PIPE_W,
            ]

        def _neighbors(self, x, y):
            cands = []
            for bit, (dx, dy) in MG_PIPE_DIRS.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    cands.append((bit, nx, ny))
            return cands

        def _build_path(self):
            start = (0, renpy.random.randint(0, self.height - 1))
            min_len = max(self.width + self.min_path_extra, int((self.width * self.height) * self.min_path_ratio))

            visited = set([start])
            stack = [start]

            def dfs(x, y):
                if x == self.width - 1 and len(stack) >= min_len:
                    return True

                neigh = self._neighbors(x, y)
                neigh.sort(key=lambda item: (0 if item[1] > x else 1, renpy.random.random()))

                for _bit, nx, ny in neigh:
                    if (nx, ny) in visited:
                        continue

                    visited.add((nx, ny))
                    stack.append((nx, ny))

                    if dfs(nx, ny):
                        return True

                    stack.pop()
                    visited.remove((nx, ny))

                return False

            if not dfs(start[0], start[1]):
                while stack[-1][0] != self.width - 1 and len(stack) > self.width:
                    stack.pop()

            return list(stack)

        def _path_masks(self, path):
            masks = {}
            for i, (x, y) in enumerate(path):
                mask = 0

                if i > 0:
                    px, py = path[i - 1]
                    if px == x and py == y - 1:
                        mask |= MG_PIPE_N
                    elif px == x + 1 and py == y:
                        mask |= MG_PIPE_E
                    elif px == x and py == y + 1:
                        mask |= MG_PIPE_S
                    elif px == x - 1 and py == y:
                        mask |= MG_PIPE_W

                if i < len(path) - 1:
                    nx, ny = path[i + 1]
                    if nx == x and ny == y - 1:
                        mask |= MG_PIPE_N
                    elif nx == x + 1 and ny == y:
                        mask |= MG_PIPE_E
                    elif nx == x and ny == y + 1:
                        mask |= MG_PIPE_S
                    elif nx == x - 1 and ny == y:
                        mask |= MG_PIPE_W

                masks[(x, y)] = mask

            return masks

        def _build_generated_level(self):
            path = self._build_path()
            path_masks = self._path_masks(path)
            path_set = set(path)

            self.path = path
            self.start = path[0]
            self.end = path[-1]

            decoys = self._decoy_masks()

            for y in range(self.height):
                for x in range(self.width):
                    pos = (x, y)
                    is_path = pos in path_set

                    if is_path:
                        base_mask = path_masks[pos]
                    else:
                        base_mask = renpy.random.choice(decoys)

                    rot = renpy.random.randint(0, 3)
                    locked = (pos == self.start or pos == self.end)
                    if locked:
                        rot = 0

                    self.tiles[pos] = {
                        "base": base_mask,
                        "rot": rot,
                        "path": is_path,
                        "target": path_masks.get(pos, 0),
                        "locked": locked,
                    }

            if self.path and all(self.tile_mask(x, y) == self.tiles[(x, y)]["target"] for (x, y) in self.path):
                for (x, y) in self.path:
                    if not self.tiles[(x, y)]["locked"]:
                        self.tiles[(x, y)]["rot"] = (self.tiles[(x, y)]["rot"] + 1) % 4
                        break

        def _build_fixed_level(self, target_masks, start, end, initial_rotations, locked_positions):
            grid = _pipes_norm_grid(target_masks)
            if not grid:
                self._build_generated_level()
                return

            self.height = len(grid)
            self.width = len(grid[0])

            if self.width < 4 or self.height < 4:
                self.width = max(4, self.width)
                self.height = max(4, self.height)

            rot_grid = _pipes_norm_grid(initial_rotations)
            if rot_grid and (len(rot_grid) != self.height or len(rot_grid[0]) != self.width):
                rot_grid = None

            target_cells = []
            for y in range(self.height):
                for x in range(self.width):
                    if int(grid[y][x]) != 0:
                        target_cells.append((x, y))

            if target_cells:
                default_start = min(target_cells, key=lambda p: (p[0], p[1]))
                default_end = max(target_cells, key=lambda p: (p[0], p[1]))
            else:
                default_start = (0, self.height // 2)
                default_end = (self.width - 1, self.height // 2)

            start_pos = _pipes_norm_pos(start)
            end_pos = _pipes_norm_pos(end)

            if not start_pos or not (0 <= start_pos[0] < self.width and 0 <= start_pos[1] < self.height):
                start_pos = default_start
            if not end_pos or not (0 <= end_pos[0] < self.width and 0 <= end_pos[1] < self.height):
                end_pos = default_end

            self.start = start_pos
            self.end = end_pos

            locked = set(_pipes_norm_positions(locked_positions))
            locked.add(self.start)
            locked.add(self.end)

            decoys = self._decoy_masks()
            self.path = list(target_cells)

            for y in range(self.height):
                for x in range(self.width):
                    pos = (x, y)
                    target_mask = int(grid[y][x])
                    is_path = target_mask != 0

                    if is_path:
                        base_mask = target_mask
                    else:
                        base_mask = renpy.random.choice(decoys)

                    if rot_grid is not None:
                        rot = int(rot_grid[y][x]) % 4
                    else:
                        rot = renpy.random.randint(0, 3)

                    is_locked = pos in locked
                    if is_locked and target_mask != 0:
                        base_mask = target_mask
                        rot = 0

                    self.tiles[pos] = {
                        "base": int(base_mask),
                        "rot": int(rot),
                        "path": bool(is_path),
                        "target": int(target_mask),
                        "locked": bool(is_locked),
                    }

            if self.path and all(self.tile_mask(x, y) == self.tiles[(x, y)]["target"] for (x, y) in self.path):
                for (x, y) in self.path:
                    if not self.tiles[(x, y)]["locked"]:
                        self.tiles[(x, y)]["rot"] = (self.tiles[(x, y)]["rot"] + 1) % 4
                        break

        def reset(self):
            self.__init__(**copy.deepcopy(self._config))

        def tile_mask(self, x, y):
            tile = self.tiles[(x, y)]
            return mg_pipe_rotate_mask(tile["base"], tile["rot"])

        def rotate(self, x, y):
            if self.completed:
                return

            tile = self.tiles[(x, y)]
            if tile["locked"]:
                self.message = "Старт и выход фиксированы."
                return

            tile["rot"] = (int(tile["rot"]) + 1) % 4
            self.moves += 1
            self._refresh_completion()

        def connected_from_start(self):
            if self.start is None:
                return set()

            visited = set([self.start])
            stack = [self.start]

            while stack:
                x, y = stack.pop()
                mask = self.tile_mask(x, y)

                for bit, (dx, dy) in MG_PIPE_DIRS.items():
                    if not (mask & bit):
                        continue

                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < self.width and 0 <= ny < self.height):
                        continue

                    nmask = self.tile_mask(nx, ny)
                    if not (nmask & MG_PIPE_OPPOSITE[bit]):
                        continue

                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        stack.append((nx, ny))

            return visited

        def _refresh_completion(self):
            solved = True
            for (x, y) in self.path:
                tile = self.tiles[(x, y)]
                if self.tile_mask(x, y) != int(tile["target"]):
                    solved = False
                    break

            self.completed = solved
            if solved:
                self.message = "Поток стабилизирован."
            else:
                self.message = "Кликайте по сегментам и соберите непрерывный маршрут."


    class PipesFlowBoard(renpy.Displayable):
        def __init__(self, game, cell=92, padding=18, **kwargs):
            super(PipesFlowBoard, self).__init__(**kwargs)
            self.game = game
            self.cell = int(cell)
            self.padding = int(padding)
            self.width = self.padding * 2 + self.game.width * self.cell
            self.height = self.padding * 2 + self.game.height * self.cell

        def _draw_text(self, render, text, x, y, size=24, color="#f5fbff", align=0.5):
            d = Text(str(text), size=int(size), color=str(color), outlines=[(1, "#00000099", 0, 0)])
            tr = renpy.render(d, self.width, self.height, 0, 0)
            tw, _th = tr.get_size()
            render.blit(tr, (int(x - tw * align), int(y)))

        def _cell_rect(self, gx, gy):
            x0 = self.padding + gx * self.cell
            y0 = self.padding + gy * self.cell
            return (x0, y0, self.cell, self.cell)

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                gx = int((x - self.padding) // self.cell)
                gy = int((y - self.padding) // self.cell)
                if 0 <= gx < self.game.width and 0 <= gy < self.game.height:
                    self.game.rotate(gx, gy)

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            canvas = render.canvas()

            canvas.rect((12, 22, 36, 255), (0, 0, self.width, self.height), 0)

            connected = self.game.connected_from_start()
            path_set = set(self.game.path)

            for gy in range(self.game.height):
                for gx in range(self.game.width):
                    x0, y0, cw, ch = self._cell_rect(gx, gy)
                    pos = (gx, gy)
                    tile = self.game.tiles[pos]
                    mask = self.game.tile_mask(gx, gy)

                    if pos == self.game.start:
                        cell_bg = (62, 86, 46, 255)
                    elif pos == self.game.end:
                        cell_bg = (84, 64, 38, 255)
                    else:
                        cell_bg = (30, 46, 64, 255)

                    canvas.rect(cell_bg, (x0 + 2, y0 + 2, cw - 4, ch - 4), 0)

                    solved_path_tile = (tile["path"] and mask == tile["target"])
                    active = pos in connected

                    if solved_path_tile:
                        pipe_color = (106, 225, 144, 255)
                    elif active:
                        pipe_color = (101, 205, 255, 255)
                    else:
                        pipe_color = (111, 145, 176, 255)

                    cx = x0 + cw // 2
                    cy = y0 + ch // 2
                    thick = max(12, self.cell // 6)

                    if mask & MG_PIPE_N:
                        canvas.rect(pipe_color, (cx - thick // 2, y0 + 8, thick, cy - y0), 0)
                    if mask & MG_PIPE_S:
                        canvas.rect(pipe_color, (cx - thick // 2, cy, thick, y0 + ch - 8 - cy), 0)
                    if mask & MG_PIPE_W:
                        canvas.rect(pipe_color, (x0 + 8, cy - thick // 2, cx - x0, thick), 0)
                    if mask & MG_PIPE_E:
                        canvas.rect(pipe_color, (cx, cy - thick // 2, x0 + cw - 8 - cx, thick), 0)

                    core_color = (223, 245, 255, 255) if active else (190, 209, 226, 255)
                    canvas.circle(core_color, (cx, cy), max(8, thick // 2 + 1), 0)

                    border = (108, 151, 194, 170)
                    if pos in path_set:
                        border = (123, 179, 220, 220)
                    canvas.rect(border, (x0 + 1, y0 + 1, cw - 2, ch - 2), 2)

                    if pos == self.game.start:
                        self._draw_text(render, "S", cx, y0 + ch // 2 - 14, 24, "#0d1a08", 0.5)
                    elif pos == self.game.end:
                        self._draw_text(render, "E", cx, y0 + ch // 2 - 14, 24, "#2a1305", 0.5)

            if self.game.completed:
                self._draw_text(render, "ПОТОК ВОССТАНОВЛЕН", self.width * 0.5, self.height * 0.5 - 18, 44, "#b6ffbe", 0.5)

            renpy.redraw(self, 0.016)
            return render


screen pipes_flow_screen(game):
    modal True
    tag pipes_flow

    default board = PipesFlowBoard(game)

    add Solid("#060b12ef")

    frame:
        xalign 0.5
        yalign 0.5
        background "#0d1a2af0"
        padding (20, 18)

        hbox:
            spacing 18

            add board

            vbox:
                spacing 11
                xmaximum 420

                text "Трубы" size 58 color "#f7fbff"
                text "Уровень: [game.level_id] ([game.mode])" size 21 color "#93b8dc"
                text "ЛКМ по секции = поворот.\nЗеленый контур — собранная часть маршрута." size 24 color "#bedcff"
                text "Ходы: [game.moves]" size 27 color "#b6d8f7"
                text "[game.message]" size 22 color "#ffe8a6"

                frame:
                    background "#12233a"
                    padding (10, 10)
                    vbox:
                        spacing 4
                        text "Легенда" size 24 color "#e4f2ff"
                        text "S — вход потока" size 20 color "#b9d8f5"
                        text "E — выход" size 20 color "#b9d8f5"
                        text "Цель: непрерывный маршрут от S к E" size 20 color "#b9d8f5"

                if game.completed:
                    text "Успех!" size 38 color "#b6ffbe"

                hbox:
                    spacing 10
                    textbutton "Пересобрать":
                        action Function(game.reset)
                        text_size 34
                    if game.completed:
                        textbutton "Готово":
                            action Return(True)
                            text_size 34
                    else:
                        textbutton "Уйти":
                            action Return(False)
                            text_size 34


label pipes_minigame(
    level=None,
    width=None,
    height=None,
    mode=None,
    target_masks=None,
    start=None,
    end=None,
    initial_rotations=None,
    locked_positions=None,
    min_path_ratio=None,
    min_path_extra=None,
):
    $ _pipes_cfg = pipes_flow_resolve_level(
        level=level,
        width=width,
        height=height,
        mode=mode,
        target_masks=target_masks,
        start=start,
        end=end,
        initial_rotations=initial_rotations,
        locked_positions=locked_positions,
        min_path_ratio=min_path_ratio,
        min_path_extra=min_path_extra,
    )
    $ _pipes_game = PipesFlowGame(**_pipes_cfg)
    call screen pipes_flow_screen(_pipes_game)
    return _return


label test_pipes_minigame:
    scene black
    with fade
    "Тест мини-игры: трубы."
    call pipes_minigame(level="standard")
    if _return:
        "Поток восстановлен."
    else:
        "Выход из теста."
    return
