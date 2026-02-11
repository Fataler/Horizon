init python:
    import copy

    CIPHER_SWITCH_LEVELS = {
        "standard": {
            "width": 7,
            "height": 7,
            "channels": [
                {"id": "A", "a": (0, 1), "b": (6, 5), "color": "#6CC6FF"},
                {"id": "B", "a": (0, 5), "b": (6, 1), "color": "#FFB870"},
                {"id": "C", "a": (1, 0), "b": (5, 6), "color": "#9EE48D"},
            ],
        },
        "compact": {
            "width": 6,
            "height": 6,
            "channels": [
                {"id": "A", "a": (0, 0), "b": (5, 5), "color": "#6CC6FF"},
                {"id": "B", "a": (0, 5), "b": (5, 0), "color": "#FFB870"},
                {"id": "C", "a": (2, 0), "b": (3, 5), "color": "#9EE48D"},
            ],
        },
    }


    def _cipher_norm_pos(raw):
        if isinstance(raw, (list, tuple)) and len(raw) >= 2:
            return (int(raw[0]), int(raw[1]))
        return None


    def _cipher_norm_channels(raw_channels, width, height):
        channels = []
        if not isinstance(raw_channels, (list, tuple)):
            raw_channels = []

        used_terminal = set()
        for idx, item in enumerate(raw_channels):
            if not isinstance(item, dict):
                continue

            cid = str(item.get("id", chr(ord("A") + (idx % 26))))
            a = _cipher_norm_pos(item.get("a"))
            b = _cipher_norm_pos(item.get("b"))
            if a is None or b is None:
                continue

            if not (0 <= a[0] < width and 0 <= a[1] < height):
                continue
            if not (0 <= b[0] < width and 0 <= b[1] < height):
                continue
            if a == b:
                continue
            if a in used_terminal or b in used_terminal:
                continue

            channels.append(
                {
                    "id": cid,
                    "a": a,
                    "b": b,
                    "color": str(item.get("color", "#8DC8FF")),
                }
            )
            used_terminal.add(a)
            used_terminal.add(b)

        if len(channels) >= 2:
            return channels

        fallback = []
        for item in CIPHER_SWITCH_LEVELS["standard"]["channels"]:
            fallback.append(copy.deepcopy(item))
        return fallback


    def cipher_switch_resolve_level(level=None, width=None, height=None, channels=None):
        cfg = copy.deepcopy(CIPHER_SWITCH_LEVELS["standard"])
        level_id = "standard"

        if isinstance(level, str) and level in CIPHER_SWITCH_LEVELS:
            cfg = copy.deepcopy(CIPHER_SWITCH_LEVELS[level])
            level_id = str(level)
        elif isinstance(level, dict):
            preset = level.get("preset")
            if isinstance(preset, str) and preset in CIPHER_SWITCH_LEVELS:
                cfg = copy.deepcopy(CIPHER_SWITCH_LEVELS[preset])
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
        if channels is not None:
            cfg["channels"] = channels

        cfg["width"] = max(5, int(cfg.get("width", 7)))
        cfg["height"] = max(5, int(cfg.get("height", 7)))
        cfg["channels"] = _cipher_norm_channels(cfg.get("channels"), cfg["width"], cfg["height"])

        return {
            "width": cfg["width"],
            "height": cfg["height"],
            "channels": cfg["channels"],
            "level_id": level_id,
        }


    class CipherSwitchGame(object):
        def __init__(self, width=7, height=7, channels=None, level_id="custom"):
            self.width = max(5, int(width))
            self.height = max(5, int(height))
            self.level_id = str(level_id)

            self.channels = _cipher_norm_channels(channels, self.width, self.height)
            self.channel_order = [item["id"] for item in self.channels]
            self.channel_map = {item["id"]: item for item in self.channels}

            self.terminals = {}
            for item in self.channels:
                self.terminals[item["a"]] = item["id"]
                self.terminals[item["b"]] = item["id"]

            self.grid = [[None for _x in range(self.width)] for _y in range(self.height)]

            self.selected_channel = self.channel_order[0]
            self.moves = 0
            self.completed = False
            self.message = "Соедините пары узлов без пересечений."

            self._config = {
                "width": self.width,
                "height": self.height,
                "channels": copy.deepcopy(self.channels),
                "level_id": self.level_id,
            }

        def _in_bounds(self, x, y):
            return 0 <= x < self.width and 0 <= y < self.height

        def channel_color(self, cid):
            item = self.channel_map.get(str(cid))
            if item is None:
                return "#6F8296"
            return item["color"]

        def cell_channel(self, x, y):
            if not self._in_bounds(int(x), int(y)):
                return None
            return self.grid[int(y)][int(x)]

        def terminal_channel(self, x, y):
            return self.terminals.get((int(x), int(y)))

        def select_channel(self, cid):
            cid = str(cid)
            if cid in self.channel_map:
                self.selected_channel = cid
                self.message = "Активный канал: %s." % cid

        def clear_channel(self, cid):
            cid = str(cid)
            changed = False
            for y in range(self.height):
                for x in range(self.width):
                    if self.grid[y][x] == cid:
                        self.grid[y][x] = None
                        changed = True
            if changed:
                self.moves += 1
                self._refresh_completion()

        def click_cell(self, x, y):
            if self.completed:
                return

            x = int(x)
            y = int(y)
            if not self._in_bounds(x, y):
                return

            terminal_cid = self.terminals.get((x, y))
            if terminal_cid is not None:
                self.selected_channel = terminal_cid
                self.message = "Выбран канал %s по терминалу." % terminal_cid
                return

            cid = self.selected_channel
            current = self.grid[y][x]

            if current == cid:
                self.grid[y][x] = None
                self.moves += 1
                self._refresh_completion()
                return

            if current is not None and current != cid:
                self.message = "Ячейка занята каналом %s." % current
                return

            self.grid[y][x] = cid
            self.moves += 1
            self._refresh_completion()

        def _neighbors(self, x, y):
            return [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

        def _connected(self, cid):
            item = self.channel_map[str(cid)]
            start = item["a"]
            finish = item["b"]

            visited = set([start])
            stack = [start]

            while stack:
                x, y = stack.pop()
                if (x, y) == finish:
                    return True

                for nx, ny in self._neighbors(x, y):
                    if not self._in_bounds(nx, ny):
                        continue
                    if (nx, ny) in visited:
                        continue

                    term = self.terminals.get((nx, ny))
                    if term is not None and term != cid:
                        continue

                    cell = self.grid[ny][nx]
                    if term == cid or cell == cid:
                        visited.add((nx, ny))
                        stack.append((nx, ny))

            return False

        def _refresh_completion(self):
            self.completed = all(self._connected(cid) for cid in self.channel_order)
            if self.completed:
                self.message = "Шифр-коммутатор собран."
            else:
                done = 0
                for cid in self.channel_order:
                    if self._connected(cid):
                        done += 1
                self.message = "Связано каналов: %s/%s." % (done, len(self.channel_order))

        def reset(self):
            self.__init__(**copy.deepcopy(self._config))


    def cipher_switch_cell_bg(game, x, y):
        terminal = game.terminal_channel(x, y)
        if terminal is not None:
            return game.channel_color(terminal)

        cell = game.cell_channel(x, y)
        if cell is not None:
            return game.channel_color(cell)

        return "#1E2A38"


    def cipher_switch_cell_text(game, x, y):
        terminal = game.terminal_channel(x, y)
        if terminal is not None:
            return terminal

        cell = game.cell_channel(x, y)
        if cell is not None:
            return "•"

        return ""


screen cipher_switch_screen(game):
    modal True
    tag cipher_switch

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

                text "Шифр-коммутатор" size 52 color "#f7fbff"
                text "Уровень: [game.level_id]" size 21 color "#93b8dc"
                text "Ходы: [game.moves]" size 25 color "#b6d8f7"
                text "[game.message]" size 21 color "#ffe8a6"

                frame:
                    background "#13243a"
                    padding (10, 8)
                    vbox:
                        spacing 6
                        text "Каналы" size 26 color "#e8f4ff"

                        for cid in game.channel_order:
                            $ selected = (cid == game.selected_channel)
                            $ _btn_bg = game.channel_color(cid) if selected else "#2b3e56"
                            $ _btn_fg = "#081220" if selected else "#d8e9ff"
                            textbutton "[cid]":
                                action Function(game.select_channel, cid)
                                background _btn_bg
                                text_color _btn_fg
                                text_size 30

                        textbutton "Очистить выбранный":
                            action Function(game.clear_channel, game.selected_channel)
                            text_size 28

                if game.completed:
                    text "Успех!" size 38 color "#b6ffbe"

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
                        $ _cell_text = cipher_switch_cell_text(game, gx, gy)
                        $ _cell_bg = cipher_switch_cell_bg(game, gx, gy)
                        button:
                            xysize (66, 66)
                            background _cell_bg
                            hover_background "#6ea3d0"
                            action Function(game.click_cell, gx, gy)

                            text _cell_text:
                                xalign 0.5
                                yalign 0.5
                                size 30
                                color "#09111c"


label cipher_switch_minigame(level=None, width=None, height=None, channels=None):
    $ _cipher_cfg = cipher_switch_resolve_level(level=level, width=width, height=height, channels=channels)
    $ _cipher_game = CipherSwitchGame(**_cipher_cfg)
    call screen cipher_switch_screen(_cipher_game)
    return _return


label test_cipher_switch_minigame:
    scene black
    with fade
    "Тест мини-игры: шифр-коммутатор."
    call cipher_switch_minigame(level="standard")
    if _return:
        "Коммутация завершена."
    else:
        "Выход из теста."
    return
