init python:
    import copy
    import random

    SIGNAL_HUNT_LEVELS = {
        "standard": {
            "width": 8,
            "height": 8,
            "max_scans": 8,
            "seed": None,
        },
        "hard": {
            "width": 10,
            "height": 10,
            "max_scans": 8,
            "seed": None,
        },
    }


    def _signal_norm_pos(raw):
        if isinstance(raw, (list, tuple)) and len(raw) >= 2:
            return (int(raw[0]), int(raw[1]))
        return None


    def signal_hunt_resolve_level(level=None, width=None, height=None, max_scans=None, source=None, seed=None):
        cfg = copy.deepcopy(SIGNAL_HUNT_LEVELS["standard"])
        level_id = "standard"

        if isinstance(level, str) and level in SIGNAL_HUNT_LEVELS:
            cfg = copy.deepcopy(SIGNAL_HUNT_LEVELS[level])
            level_id = str(level)
        elif isinstance(level, dict):
            preset = level.get("preset")
            if isinstance(preset, str) and preset in SIGNAL_HUNT_LEVELS:
                cfg = copy.deepcopy(SIGNAL_HUNT_LEVELS[preset])
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
        if max_scans is not None:
            cfg["max_scans"] = max_scans
        if source is not None:
            cfg["source"] = source
        if seed is not None:
            cfg["seed"] = seed

        cfg["width"] = max(6, int(cfg.get("width", 8)))
        cfg["height"] = max(6, int(cfg.get("height", 8)))
        cfg["max_scans"] = max(3, int(cfg.get("max_scans", 8)))
        cfg["source"] = _signal_norm_pos(cfg.get("source"))

        return {
            "width": cfg["width"],
            "height": cfg["height"],
            "max_scans": cfg["max_scans"],
            "source": cfg["source"],
            "seed": cfg.get("seed"),
            "level_id": level_id,
        }


    class SignalHuntGame(object):
        def __init__(self, width=8, height=8, max_scans=8, source=None, seed=None, level_id="custom"):
            self.width = max(6, int(width))
            self.height = max(6, int(height))
            self.max_scans = max(3, int(max_scans))
            self.seed = seed
            self.level_id = str(level_id)

            src = _signal_norm_pos(source)
            if src is not None and 0 <= src[0] < self.width and 0 <= src[1] < self.height:
                self.source = src
            else:
                if seed is not None:
                    rnd = random.Random(int(seed))
                    self.source = (rnd.randint(0, self.width - 1), rnd.randint(0, self.height - 1))
                else:
                    self.source = (renpy.random.randint(0, self.width - 1), renpy.random.randint(0, self.height - 1))

            self.probes = {}
            self.scans_used = 0
            self.completed = False
            self.failed = False
            self.message = "Ищите источник, используя дальность эха."

            self._config = {
                "width": self.width,
                "height": self.height,
                "max_scans": self.max_scans,
                "source": self.source,
                "seed": self.seed,
                "level_id": self.level_id,
            }

        def _in_bounds(self, x, y):
            return 0 <= x < self.width and 0 <= y < self.height

        def _distance(self, x, y):
            return abs(int(x) - self.source[0]) + abs(int(y) - self.source[1])

        def scan(self, x, y):
            if self.completed or self.failed:
                return

            x = int(x)
            y = int(y)
            if not self._in_bounds(x, y):
                return

            if (x, y) in self.probes:
                self.message = "Этот сектор уже сканирован."
                return

            self.scans_used += 1

            if (x, y) == self.source:
                self.completed = True
                self.probes[(x, y)] = 0
                self.message = "Источник сигнала найден."
                return

            self.probes[(x, y)] = self._distance(x, y)

            left = self.max_scans - self.scans_used
            if left <= 0:
                self.failed = True
                self.message = "Сканов не осталось. Источник ушел."
            else:
                self.message = "Эхо: %s. Осталось сканов: %s." % (self.probes[(x, y)], left)

        def reset(self):
            self.__init__(**copy.deepcopy(self._config))


    def signal_hunt_cell_bg(game, x, y):
        pos = (int(x), int(y))
        if game.completed and pos == game.source:
            return "#8adf98"
        if game.failed and pos == game.source:
            return "#ff9f8f"
        if pos in game.probes:
            return "#355877"
        return "#1e2a38"


    def signal_hunt_cell_text(game, x, y):
        pos = (int(x), int(y))
        if game.completed and pos == game.source:
            return "S"
        if game.failed and pos == game.source:
            return "S"
        if pos in game.probes:
            return str(game.probes[pos])
        return ""


screen signal_hunt_screen(game):
    modal True
    tag signal_hunt

    add Solid("#080d14ef")

    frame:
        xalign 0.5
        yalign 0.5
        background "#0f1a29f0"
        padding (20, 18)

        hbox:
            spacing 18

            vbox:
                spacing 10
                xmaximum 420

                text "Охота на сигнал" size 52 color "#f7fbff"
                text "Уровень: [game.level_id]" size 21 color "#93b8dc"
                text "Сканы: [game.scans_used]/[game.max_scans]" size 25 color "#b6d8f7"
                text "[game.message]" size 21 color "#ffe8a6"
                text "Число в ячейке = манхэттенская дистанция до источника." size 19 color "#b9d8f5"

                if game.completed:
                    text "Источник локализован" size 36 color "#b6ffbe"
                elif game.failed:
                    text "Источник потерян" size 36 color "#ffb8a8"

                hbox:
                    spacing 10
                    textbutton "Сброс":
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

            grid game.width game.height:
                spacing 6
                transpose False

                for gy in range(game.height):
                    for gx in range(game.width):
                        $ _cell_text = signal_hunt_cell_text(game, gx, gy)
                        $ _cell_bg = signal_hunt_cell_bg(game, gx, gy)
                        button:
                            xysize (58, 58)
                            background _cell_bg
                            hover_background "#6ea3d0"
                            action Function(game.scan, gx, gy)
                            sensitive (not game.completed and not game.failed)

                            text _cell_text:
                                xalign 0.5
                                yalign 0.5
                                size 26
                                color "#ecf6ff"


label signal_hunt_minigame(level=None, width=None, height=None, max_scans=None, source=None, seed=None):
    $ _signal_cfg = signal_hunt_resolve_level(level=level, width=width, height=height, max_scans=max_scans, source=source, seed=seed)
    $ _signal_game = SignalHuntGame(**_signal_cfg)
    call screen signal_hunt_screen(_signal_game)
    return _return


label test_signal_hunt_minigame:
    scene black
    with fade
    "Тест мини-игры: охота на сигнал."
    call signal_hunt_minigame(level="standard")
    if _return:
        "Источник найден."
    else:
        "Выход из теста."
    return
