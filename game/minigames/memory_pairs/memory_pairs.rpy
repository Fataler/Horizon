init python:
    import math
    import random

    MEMORY_PAIRS_LEVELS = {
        "easy": {"rows": 2, "cols": 4, "hide_delay": 0.85},
        "normal": {"rows": 4, "cols": 4, "hide_delay": 0.70},
        "hard": {"rows": 4, "cols": 6, "hide_delay": 0.55},
    }

    def memory_pairs_resolve_level(level=None, rows=None, cols=None, hide_delay=None, symbols=None, deck=None, seed=None):
        cfg = dict(MEMORY_PAIRS_LEVELS["normal"])
        level_id = "normal"

        if isinstance(level, str):
            if level in MEMORY_PAIRS_LEVELS:
                cfg.update(MEMORY_PAIRS_LEVELS[level])
                level_id = str(level)
        elif isinstance(level, dict):
            cfg.update(level)
            level_id = str(level.get("id", "custom"))

        if rows is not None:
            cfg["rows"] = rows
        if cols is not None:
            cfg["cols"] = cols
        if hide_delay is not None:
            cfg["hide_delay"] = hide_delay
        if symbols is not None:
            cfg["symbols"] = symbols
        if deck is not None:
            cfg["deck"] = deck
        if seed is not None:
            cfg["seed"] = seed

        cfg["rows"] = max(2, int(cfg.get("rows", 4)))
        cfg["cols"] = max(2, int(cfg.get("cols", 4)))

        if (cfg["rows"] * cfg["cols"]) % 2 != 0:
            cfg["cols"] += 1

        cfg["hide_delay"] = max(0.15, float(cfg.get("hide_delay", 0.7)))
        cfg["level_id"] = level_id
        return cfg


    class MemoryPairsGame(object):
        def __init__(self, rows=4, cols=4, hide_delay=0.7, symbols=None, deck=None, seed=None, level_id="custom"):
            rows = int(rows)
            cols = int(cols)

            if rows < 2:
                rows = 2
            if cols < 2:
                cols = 2

            if (rows * cols) % 2 != 0:
                cols += 1

            self.rows = rows
            self.cols = cols
            self.size = rows * cols
            self.hide_delay = max(0.15, float(hide_delay))
            self.level_id = str(level_id)
            self.seed = seed

            self.config = {
                "rows": self.rows,
                "cols": self.cols,
                "hide_delay": self.hide_delay,
                "symbols": list(symbols) if isinstance(symbols, (list, tuple)) else None,
                "deck": list(deck) if isinstance(deck, (list, tuple)) else None,
                "seed": seed,
                "level_id": self.level_id,
            }

            self.symbols = self._resolve_symbols(symbols)
            self.deck = self._resolve_deck(deck)

            self.matched = [False] * self.size
            self.opened = []

            self.moves = 0
            self.matches = 0
            self.completed = False

            self.pending_hide = None
            self.pending_timer = 0.0
            self.message = "Откройте все пары."

        def _resolve_symbols(self, symbols):
            if isinstance(symbols, (list, tuple)) and len(symbols) > 0:
                clean = [str(s) for s in symbols]
                needed = self.size // 2
                if len(clean) >= needed:
                    return list(clean[:needed])

            return self._build_symbols(self.size // 2)

        def _resolve_deck(self, deck):
            if isinstance(deck, (list, tuple)):
                clean = [str(s) for s in deck]
                if len(clean) % 2 == 1:
                    clean = clean[:-1]
                if len(clean) >= 4:
                    if len(clean) != self.size:
                        pairs = len(clean) // 2
                        self.rows, self.cols = self._fit_grid_for_cards(len(clean), self.rows, self.cols)
                        self.size = self.rows * self.cols
                        pairs = self.size // 2
                        clean = clean[: self.size]
                    return list(clean)

            generated = list(self.symbols) + list(self.symbols)
            if self.seed is not None:
                rnd = random.Random(int(self.seed))
                rnd.shuffle(generated)
            else:
                renpy.random.shuffle(generated)
            return generated

        def _fit_grid_for_cards(self, cards, pref_rows, pref_cols):
            cards = int(cards)
            if cards < 4:
                return (2, 2)

            if cards % int(pref_rows) == 0:
                return (int(pref_rows), int(cards // int(pref_rows)))
            if cards % int(pref_cols) == 0:
                return (int(cards // int(pref_cols)), int(pref_cols))

            best = (2, cards // 2)
            best_score = 10 ** 9

            for r in range(2, int(math.sqrt(cards)) + 1):
                if cards % r != 0:
                    continue
                c = cards // r
                score = abs(r - pref_rows) + abs(c - pref_cols)
                if score < best_score:
                    best = (r, c)
                    best_score = score

            return best

        def _build_symbols(self, pairs):
            base = []
            for i in range(pairs):
                letter = chr(ord("A") + (i % 26))
                number = (i // 26) + 1
                base.append(letter if number == 1 else "%s%d" % (letter, number))
            return base

        def is_revealed(self, idx):
            return self.matched[idx] or (idx in self.opened)

        def click(self, idx):
            if self.completed:
                return

            idx = int(idx)
            if idx < 0 or idx >= self.size:
                return

            if self.pending_hide is not None:
                return

            if self.matched[idx]:
                return

            if idx in self.opened:
                return

            if len(self.opened) >= 2:
                return

            self.opened.append(idx)

            if len(self.opened) < 2:
                return

            a, b = self.opened[0], self.opened[1]
            self.moves += 1

            if self.deck[a] == self.deck[b]:
                self.matched[a] = True
                self.matched[b] = True
                self.matches += 1
                self.opened = []
                self.message = "Пара найдена."

                if self.matches >= len(self.symbols):
                    self.completed = True
                    self.message = "Все пары собраны."
            else:
                self.pending_hide = (a, b)
                self.pending_timer = self.hide_delay
                self.message = "Не совпало, запоминайте позиции."

        def tick(self, dt):
            if self.pending_hide is None:
                return

            self.pending_timer -= float(dt)
            if self.pending_timer > 0.0:
                return

            self.opened = []
            self.pending_hide = None
            self.pending_timer = 0.0

        def restart(self):
            self.__init__(**dict(self.config))


screen memory_pairs_screen(game):
    modal True
    tag memory_pairs

    timer 0.05 action Function(game.tick, 0.05) repeat True

    add Solid("#090c12ee")

    frame:
        xalign 0.5
        yalign 0.5
        background "#0f1726f2"
        padding (24, 22)

        vbox:
            spacing 14

            text "Найти пару" size 56 color "#f6fbff"
            text "Уровень: [game.level_id]" size 22 color "#93b8dc"
            text "Ходы: [game.moves]  |  Пар: [game.matches]/[len(game.symbols)]" size 28 color "#b6d8f7"
            text "[game.message]" size 24 color "#ffe8a6"

            grid game.cols game.rows:
                spacing 8
                transpose False

                for idx in range(game.size):
                    $ opened = game.is_revealed(idx)
                    $ symbol = game.deck[idx] if opened else "?"
                    $ bg = "#2a5a8a" if opened else "#203142"

                    button:
                        xysize (145, 120)
                        background bg
                        hover_background "#3270a8"
                        action Function(game.click, idx)
                        sensitive (not game.completed)

                        text symbol:
                            xalign 0.5
                            yalign 0.5
                            size 34
                            color "#f3f9ff"

            if game.completed:
                text "Успех!" size 40 color "#b6ffbe" xalign 0.5

            hbox:
                spacing 14
                xalign 0.5

                textbutton "Сброс":
                    action Function(game.restart)
                    text_size 36

                if game.completed:
                    textbutton "Готово":
                        action Return(True)
                        text_size 36
                else:
                    textbutton "Уйти":
                        action Return(False)
                        text_size 36


label memory_pairs_minigame(level=None, rows=None, cols=None, hide_delay=None, symbols=None, deck=None, seed=None):
    $ _memory_cfg = memory_pairs_resolve_level(
        level=level,
        rows=rows,
        cols=cols,
        hide_delay=hide_delay,
        symbols=symbols,
        deck=deck,
        seed=seed,
    )
    $ _memory_pairs_game = MemoryPairsGame(**_memory_cfg)
    call screen memory_pairs_screen(_memory_pairs_game)
    return _return


label test_memory_pairs:
    scene black
    with fade
    "Тест мини-игры: найти пару."
    call memory_pairs_minigame(level="normal")
    if _return:
        "Пары собраны."
    else:
        "Выход из теста."
    return
