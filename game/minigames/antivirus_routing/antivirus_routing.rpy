init python:
    import copy

    ANTIVIRUS_ROUTING_LEVELS = {
        "standard": {
            "width": 6,
            "height": 6,
            "start_infected": [(2, 2), (3, 3)],
            "max_turns": 10,
            "purge_charges": 3,
            "outbreak_limit": 14,
        },
        "hard": {
            "width": 7,
            "height": 7,
            "start_infected": [(3, 3), (2, 3), (3, 2)],
            "max_turns": 10,
            "purge_charges": 2,
            "outbreak_limit": 18,
        },
    }


    def _av_norm_pos(raw):
        if isinstance(raw, (list, tuple)) and len(raw) >= 2:
            return (int(raw[0]), int(raw[1]))
        return None


    def _av_norm_positions(raw_positions, width, height):
        out = []
        if not isinstance(raw_positions, (list, tuple)):
            raw_positions = []

        used = set()
        for item in raw_positions:
            pos = _av_norm_pos(item)
            if pos is None:
                continue
            if not (0 <= pos[0] < width and 0 <= pos[1] < height):
                continue
            if pos in used:
                continue
            used.add(pos)
            out.append(pos)

        if out:
            return out

        return [(width // 2, height // 2)]


    def antivirus_routing_resolve_level(level=None, width=None, height=None, start_infected=None, max_turns=None, purge_charges=None, outbreak_limit=None):
        cfg = copy.deepcopy(ANTIVIRUS_ROUTING_LEVELS["standard"])
        level_id = "standard"

        if isinstance(level, str) and level in ANTIVIRUS_ROUTING_LEVELS:
            cfg = copy.deepcopy(ANTIVIRUS_ROUTING_LEVELS[level])
            level_id = str(level)
        elif isinstance(level, dict):
            preset = level.get("preset")
            if isinstance(preset, str) and preset in ANTIVIRUS_ROUTING_LEVELS:
                cfg = copy.deepcopy(ANTIVIRUS_ROUTING_LEVELS[preset])
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
        if start_infected is not None:
            cfg["start_infected"] = start_infected
        if max_turns is not None:
            cfg["max_turns"] = max_turns
        if purge_charges is not None:
            cfg["purge_charges"] = purge_charges
        if outbreak_limit is not None:
            cfg["outbreak_limit"] = outbreak_limit

        cfg["width"] = max(5, int(cfg.get("width", 6)))
        cfg["height"] = max(5, int(cfg.get("height", 6)))
        cfg["max_turns"] = max(4, int(cfg.get("max_turns", 10)))
        cfg["purge_charges"] = max(0, int(cfg.get("purge_charges", 3)))
        cfg["outbreak_limit"] = max(1, int(cfg.get("outbreak_limit", 14)))
        cfg["start_infected"] = _av_norm_positions(cfg.get("start_infected"), cfg["width"], cfg["height"])

        return {
            "width": cfg["width"],
            "height": cfg["height"],
            "start_infected": cfg["start_infected"],
            "max_turns": cfg["max_turns"],
            "purge_charges": cfg["purge_charges"],
            "outbreak_limit": cfg["outbreak_limit"],
            "level_id": level_id,
        }


    class AntivirusRoutingGame(object):
        def __init__(
            self,
            width=6,
            height=6,
            start_infected=None,
            max_turns=10,
            purge_charges=3,
            outbreak_limit=14,
            level_id="custom",
        ):
            self.width = max(5, int(width))
            self.height = max(5, int(height))
            self.level_id = str(level_id)

            self.infected = set(_av_norm_positions(start_infected, self.width, self.height))
            self.firewalled = set()

            self.turn = 0
            self.max_turns = max(4, int(max_turns))
            self.purge_charges = max(0, int(purge_charges))
            self.outbreak_limit = max(1, int(outbreak_limit))

            self.mode = "firewall"
            self.completed = False
            self.failed = False
            self.message = "Изолируйте заражение и удержите сеть."

            self._config = {
                "width": self.width,
                "height": self.height,
                "start_infected": list(self.infected),
                "max_turns": self.max_turns,
                "purge_charges": self.purge_charges,
                "outbreak_limit": self.outbreak_limit,
                "level_id": self.level_id,
            }

        def _in_bounds(self, x, y):
            return 0 <= x < self.width and 0 <= y < self.height

        def _neighbors(self, x, y):
            return [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

        def set_mode(self, mode):
            mode = str(mode)
            if mode in ("firewall", "purge"):
                self.mode = mode

        def click_node(self, x, y):
            if self.completed or self.failed:
                return

            x = int(x)
            y = int(y)
            if not self._in_bounds(x, y):
                return

            pos = (x, y)

            if self.mode == "firewall":
                if pos in self.infected:
                    self.message = "Нельзя ставить экран на зараженный узел."
                    return
                if pos in self.firewalled:
                    self.firewalled.remove(pos)
                    self.message = "Экран снят с узла."
                else:
                    self.firewalled.add(pos)
                    self.message = "Узел закрыт экраном."
                return

            if self.mode == "purge":
                if self.purge_charges <= 0:
                    self.message = "Импульсы очистки закончились."
                    return
                if pos not in self.infected:
                    self.message = "Этот узел не заражен."
                    return

                self.infected.remove(pos)
                self.firewalled.discard(pos)
                self.purge_charges -= 1
                self.message = "Узел очищен импульсом."
                self._refresh_state()

        def _can_spread_from(self, pos):
            x, y = pos
            for nx, ny in self._neighbors(x, y):
                npos = (nx, ny)
                if not self._in_bounds(nx, ny):
                    continue
                if npos in self.infected:
                    continue
                if npos in self.firewalled:
                    continue
                return True
            return False

        def _spread_candidates(self):
            out = set()
            for x, y in self.infected:
                for nx, ny in self._neighbors(x, y):
                    npos = (nx, ny)
                    if not self._in_bounds(nx, ny):
                        continue
                    if npos in self.infected:
                        continue
                    if npos in self.firewalled:
                        continue
                    out.add(npos)
            return out

        def _refresh_state(self):
            if len(self.infected) >= self.outbreak_limit:
                self.failed = True
                self.message = "Сеть захвачена инфекцией."
                return

            exposed = len(self._spread_candidates())
            if exposed == 0 and len(self.infected) > 0:
                self.completed = True
                self.message = "Очаг изолирован."
                return

            if self.turn >= self.max_turns:
                if exposed == 0:
                    self.completed = True
                    self.message = "Сеть удержана до конца цикла."
                else:
                    self.failed = True
                    self.message = "Время вышло, инфекция не изолирована."

        def advance_turn(self):
            if self.completed or self.failed:
                return

            new_infected = self._spread_candidates()
            self.infected.update(new_infected)
            self.turn += 1

            if new_infected:
                self.message = "Инфекция распространилась на %s узл(ов)." % len(new_infected)
            else:
                self.message = "Распространение остановлено в этот такт."

            self._refresh_state()

        def reset(self):
            self.__init__(**copy.deepcopy(self._config))


    def antivirus_node_bg(game, x, y):
        pos = (int(x), int(y))
        if pos in game.infected:
            return "#9c3c3c"
        if pos in game.firewalled:
            return "#3f6e9f"
        return "#213042"


    def antivirus_node_text(game, x, y):
        pos = (int(x), int(y))
        if pos in game.infected:
            return "V"
        if pos in game.firewalled:
            return "F"
        return ""


screen antivirus_routing_screen(game):
    modal True
    tag antivirus_routing

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
                xmaximum 440

                text "Антивирусный роутинг" size 50 color "#f7fbff"
                text "Уровень: [game.level_id]" size 21 color "#93b8dc"
                text "Такт: [game.turn]/[game.max_turns]" size 24 color "#b6d8f7"
                text "Заражено: [len(game.infected)] / лимит [game.outbreak_limit]" size 24 color "#ffccb8"
                text "Очистка: [game.purge_charges]" size 24 color "#c9dfff"
                text "[game.message]" size 21 color "#ffe8a6"

                hbox:
                    spacing 8
                    $ _fw_bg = "#6aa8dd" if game.mode == "firewall" else "#2d435d"
                    $ _pg_bg = "#df8f7c" if game.mode == "purge" else "#5a3330"
                    textbutton "Режим: Экраны":
                        action Function(game.set_mode, "firewall")
                        background _fw_bg
                        text_size 26
                    textbutton "Режим: Очистка":
                        action Function(game.set_mode, "purge")
                        background _pg_bg
                        text_size 26

                textbutton "Следующий такт":
                    action Function(game.advance_turn)
                    sensitive (not game.completed and not game.failed)
                    text_size 34

                if game.completed:
                    text "Успех!" size 38 color "#b6ffbe"
                elif game.failed:
                    text "Провал" size 38 color "#ffb8a8"

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
                        $ _cell_text = antivirus_node_text(game, gx, gy)
                        $ _cell_bg = antivirus_node_bg(game, gx, gy)
                        button:
                            xysize (58, 58)
                            background _cell_bg
                            hover_background "#6ea3d0"
                            action Function(game.click_node, gx, gy)
                            sensitive (not game.completed and not game.failed)

                            text _cell_text:
                                xalign 0.5
                                yalign 0.5
                                size 24
                                color "#eff7ff"


label antivirus_routing_minigame(level=None, width=None, height=None, start_infected=None, max_turns=None, purge_charges=None, outbreak_limit=None):
    $ _av_cfg = antivirus_routing_resolve_level(level=level, width=width, height=height, start_infected=start_infected, max_turns=max_turns, purge_charges=purge_charges, outbreak_limit=outbreak_limit)
    $ _av_game = AntivirusRoutingGame(**_av_cfg)
    call screen antivirus_routing_screen(_av_game)
    return _return


label test_antivirus_routing_minigame:
    scene black
    with fade
    "Тест мини-игры: антивирусный роутинг."
    call antivirus_routing_minigame(level="standard")
    if _return:
        "Очаг локализован."
    else:
        "Выход из теста."
    return
