init python:
    import copy

    VALVE_SYNC_LEVELS = {
        "tutorial": {
            "marks": 6,
            "scramble_steps": 7,
            "target": 0,
            "ops": [[1, 1, 2], [2, 1, 1], [1, 2, 1]],
            "scramble": True,
        },
        "standard": {
            "marks": 8,
            "scramble_steps": 14,
            "target": 0,
            "ops": [[1, 1, 2], [2, 1, 1], [1, 2, 1]],
            "scramble": True,
        },
        "hard": {
            "marks": 10,
            "scramble_steps": 24,
            "target": 0,
            "ops": [[1, 2, 3], [3, 1, 2], [2, 3, 1]],
            "scramble": True,
        },
        "fixed_demo": {
            "marks": 8,
            "target": 0,
            "ops": [[1, 1, 2], [2, 1, 1], [1, 2, 1]],
            "start_values": [3, 6, 1],
            "scramble": False,
        },
    }


    def _valve_norm_ops(raw_ops):
        if not isinstance(raw_ops, (list, tuple)) or len(raw_ops) != 3:
            return None
        ops = []
        for row in raw_ops:
            if not isinstance(row, (list, tuple)) or len(row) != 3:
                return None
            ops.append([int(row[0]), int(row[1]), int(row[2])])
        return ops


    def _valve_norm_values(raw_values):
        if not isinstance(raw_values, (list, tuple)) or len(raw_values) != 3:
            return None
        return [int(raw_values[0]), int(raw_values[1]), int(raw_values[2])]


    def valve_sync_resolve_level(level=None, marks=None, scramble_steps=None, target=None, ops=None, start_values=None, scramble=None):
        cfg = copy.deepcopy(VALVE_SYNC_LEVELS["standard"])
        level_id = "standard"

        if isinstance(level, str):
            if level in VALVE_SYNC_LEVELS:
                cfg = copy.deepcopy(VALVE_SYNC_LEVELS[level])
                level_id = str(level)
        elif isinstance(level, dict):
            preset = level.get("preset")
            if isinstance(preset, str) and preset in VALVE_SYNC_LEVELS:
                cfg = copy.deepcopy(VALVE_SYNC_LEVELS[preset])
                level_id = str(preset)
            for key, val in level.items():
                if key in ("id", "preset"):
                    continue
                cfg[key] = copy.deepcopy(val)
            level_id = str(level.get("id", level_id if level_id else "custom"))

        if marks is not None:
            cfg["marks"] = marks
        if scramble_steps is not None:
            cfg["scramble_steps"] = scramble_steps
        if target is not None:
            cfg["target"] = target
        if ops is not None:
            cfg["ops"] = ops
        if start_values is not None:
            cfg["start_values"] = start_values
        if scramble is not None:
            cfg["scramble"] = scramble

        cfg["marks"] = max(4, int(cfg.get("marks", 8)))
        cfg["scramble_steps"] = max(0, int(cfg.get("scramble_steps", 14)))
        cfg["target"] = int(cfg.get("target", 0)) % cfg["marks"]
        cfg["ops"] = _valve_norm_ops(cfg.get("ops")) or [[1, 1, 2], [2, 1, 1], [1, 2, 1]]
        cfg["start_values"] = _valve_norm_values(cfg.get("start_values"))
        cfg["scramble"] = bool(cfg.get("scramble", True))
        return {
            "marks": cfg["marks"],
            "scramble_steps": cfg["scramble_steps"],
            "target": cfg["target"],
            "ops": cfg["ops"],
            "start_values": cfg["start_values"],
            "scramble": cfg["scramble"],
            "level_id": level_id,
        }


    class ValveSyncGame(object):
        def __init__(
            self,
            marks=8,
            scramble_steps=14,
            target=0,
            ops=None,
            start_values=None,
            scramble=True,
            level_id="custom",
        ):
            self.marks = max(4, int(marks))
            self.scramble_steps = max(0, int(scramble_steps))
            self.target = int(target) % self.marks
            self.ops = _valve_norm_ops(ops) or [[1, 1, 2], [2, 1, 1], [1, 2, 1]]
            self.level_id = str(level_id)

            if _valve_norm_values(start_values) is not None:
                self.values = [int(v) % self.marks for v in start_values]
            else:
                self.values = [self.target, self.target, self.target]

            self.moves = 0
            self.completed = False
            self.message = "Поверните вентили и синхронизируйте стрелки."
            self.last_pressed = -1
            self.flash_timer = 0.0

            self._config = {
                "marks": self.marks,
                "scramble_steps": self.scramble_steps,
                "target": self.target,
                "ops": copy.deepcopy(self.ops),
                "start_values": copy.deepcopy(start_values),
                "scramble": bool(scramble),
                "level_id": self.level_id,
            }

            if bool(scramble):
                self._scramble()
            else:
                if all(v == self.target for v in self.values):
                    self._apply(renpy.random.randint(0, 2))

            self._refresh_completion()

        def _scramble(self):
            for _i in range(self.scramble_steps):
                idx = renpy.random.randint(0, 2)
                self._apply(idx)

            if all(v == self.target for v in self.values):
                self._apply(renpy.random.randint(0, 2))

            self.moves = 0
            self.last_pressed = -1
            self.flash_timer = 0.0

        def _apply(self, index):
            delta = self.ops[int(index)]
            for i in range(3):
                self.values[i] = (self.values[i] + int(delta[i])) % self.marks

        def preview_after(self, index):
            delta = self.ops[int(index)]
            return tuple((self.values[i] + int(delta[i])) % self.marks for i in range(3))

        def rotate(self, index):
            if self.completed:
                return

            self._apply(index)
            self.moves += 1
            self.last_pressed = int(index)
            self.flash_timer = 0.45
            self._refresh_completion()

        def tick(self, dt):
            if self.flash_timer > 0.0:
                self.flash_timer = max(0.0, self.flash_timer - float(dt))

        def _refresh_completion(self):
            self.completed = all(v == self.target for v in self.values)
            if self.completed:
                self.message = "Все вентили выставлены по метке X."
            else:
                self.message = "Каждый ход меняет все три вентиля."

        def reset(self):
            self.__init__(**copy.deepcopy(self._config))


    class ValveSyncBoard(renpy.Displayable):
        def __init__(self, game, width=980, height=560, **kwargs):
            super(ValveSyncBoard, self).__init__(**kwargs)
            self.game = game
            self.width = int(width)
            self.height = int(height)
            self.last_st = None

            self.centers = [
                (220, 330),
                (490, 165),
                (760, 330),
            ]
            self.radius = 98

        def _draw_text(self, render, text, x, y, size=24, color="#f5fbff", align=0.5):
            d = Text(str(text), size=int(size), color=str(color), outlines=[(1, "#00000099", 0, 0)])
            tr = renpy.render(d, self.width, self.height, 0, 0)
            tw, _th = tr.get_size()
            render.blit(tr, (int(x - tw * align), int(y)))

        def _dial_hit(self, x, y):
            for i, (cx, cy) in enumerate(self.centers):
                dx = float(x - cx)
                dy = float(y - cy)
                if dx * dx + dy * dy <= float((self.radius + 10) * (self.radius + 10)):
                    return i
            return None

        def _point_at_mark(self, cx, cy, value, marks, radius):
            import math
            angle = -math.pi / 2.0 + (2.0 * math.pi * (float(value) / float(marks)))
            px = cx + math.cos(angle) * radius
            py = cy + math.sin(angle) * radius
            return (int(px), int(py))

        def _draw_link(self, canvas, a, b, color, dots=18):
            ax, ay = a
            bx, by = b
            for i in range(dots + 1):
                t = float(i) / float(dots)
                x = int(ax + (bx - ax) * t)
                y = int(ay + (by - ay) * t)
                canvas.circle(color, (x, y), 3, 0)

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                hit = self._dial_hit(x, y)
                if hit is not None:
                    self.game.rotate(hit)

        def render(self, width, height, st, at):
            if self.last_st is None:
                dt = 0.0
            else:
                dt = max(0.0, min(0.15, st - self.last_st))
            self.last_st = st
            self.game.tick(dt)

            render = renpy.Render(self.width, self.height)
            canvas = render.canvas()

            canvas.rect((11, 20, 34, 255), (0, 0, self.width, self.height), 0)

            self._draw_link(canvas, self.centers[0], self.centers[1], (97, 149, 199, 120))
            self._draw_link(canvas, self.centers[1], self.centers[2], (97, 149, 199, 120))
            self._draw_link(canvas, self.centers[0], self.centers[2], (97, 149, 199, 70))

            for i, (cx, cy) in enumerate(self.centers):
                active = self.game.last_pressed == i and self.game.flash_timer > 0.0
                if active:
                    canvas.circle((120, 208, 255, 120), (cx, cy), self.radius + 18, 0)

                canvas.circle((32, 54, 78, 255), (cx, cy), self.radius + 4, 0)
                canvas.circle((16, 30, 46, 255), (cx, cy), self.radius - 8, 0)

                for mark in range(self.game.marks):
                    px, py = self._point_at_mark(cx, cy, mark, self.game.marks, self.radius - 12)
                    dot_color = (103, 130, 160, 255)
                    dot_size = 5
                    if mark == self.game.target:
                        dot_color = (255, 207, 112, 255)
                        dot_size = 8
                    canvas.circle(dot_color, (px, py), dot_size, 0)

                current = self.game.values[i]
                p2x, p2y = self._point_at_mark(cx, cy, current, self.game.marks, self.radius - 28)
                canvas.circle((132, 228, 255, 255), (p2x, p2y), 12, 0)
                canvas.circle((220, 248, 255, 255), (p2x, p2y), 4, 0)
                canvas.circle((170, 214, 245, 255), (cx, cy), 10, 0)

                self._draw_text(render, "V%s" % (i + 1), cx, cy - 18, 34, "#f2f9ff", 0.5)
                self._draw_text(render, "[%s]" % current, cx, cy + 16, 24, "#ffdda8", 0.5)

            if self.game.completed:
                self._draw_text(render, "СИНХРОНИЗАЦИЯ УСПЕШНА", self.width * 0.5, 485, 42, "#b6ffbe", 0.5)

            renpy.redraw(self, 0.016)
            return render


screen valve_sync_screen(game):
    modal True
    tag valve_sync

    default board = ValveSyncBoard(game)

    add Solid("#080d14ef")

    frame:
        xalign 0.5
        yalign 0.5
        background "#101c2df0"
        padding (18, 16)

        hbox:
            spacing 16

            add board

            vbox:
                spacing 10
                xmaximum 500

                text "Синхронизация вентилей" size 52 color "#f7fbff"
                text "Уровень: [game.level_id]" size 21 color "#93b8dc"
                text "Цель: все три значения на метке X (позиция [game.target])." size 22 color "#c0dcf8"
                text "Ходы: [game.moves]" size 24 color "#b6d8f7"
                text "Сейчас: [game.values[0]] | [game.values[1]] | [game.values[2]]" size 24 color "#ffd9a8"
                text "[game.message]" size 21 color "#ffe8a6"

                for i in range(3):
                    $ after = game.preview_after(i)
                    frame:
                        background "#13243a"
                        padding (10, 8)
                        vbox:
                            spacing 4
                            text "Вентиль [i+1]" size 24 color "#eaf4ff"
                            text "Изменение: +[game.ops[i][0]] / +[game.ops[i][1]] / +[game.ops[i][2]]" size 19 color "#b9d4ec"
                            text "После хода: [after[0]] | [after[1]] | [after[2]]" size 20 color "#ffe3b8"
                            textbutton "Повернуть":
                                action Function(game.rotate, i)
                                sensitive (not game.completed)
                                text_size 30

                if game.completed:
                    text "Успех!" size 38 color "#b6ffbe"

                hbox:
                    spacing 12
                    textbutton "Перемешать":
                        action Function(game.reset)
                        text_size 32
                    if game.completed:
                        textbutton "Готово":
                            action Return(True)
                            text_size 32
                    else:
                        textbutton "Уйти":
                            action Return(False)
                            text_size 32


label valves_minigame(level=None, marks=None, scramble_steps=None, target=None, ops=None, start_values=None, scramble=None):
    $ _valves_cfg = valve_sync_resolve_level(
        level=level,
        marks=marks,
        scramble_steps=scramble_steps,
        target=target,
        ops=ops,
        start_values=start_values,
        scramble=scramble,
    )
    $ _valves_game = ValveSyncGame(**_valves_cfg)
    call screen valve_sync_screen(_valves_game)
    return _return


label test_valves_minigame:
    scene black
    with fade
    "Тест мини-игры: вентили."
    call valves_minigame(level="standard")
    if _return:
        "Синхронизация выполнена."
    else:
        "Выход из теста."
    return
