init -1 python:
    import copy
    import math
    import random
    import time

    CLICKER_SAVE_VERSION = 1

    CLICKER_STAGE_THRESHOLDS = [0.0, 1500.0, 12000.0, 90000.0, 650000.0, 4200000.0, 26000000.0]
    CLICKER_STAGE_NAMES = [
        "Холодный запуск",
        "Локальная сеть",
        "Орбитальная ферма",
        "Рой дронов",
        "Квантовый контур",
        "Сингулярный цикл",
        "Горизонт событий",
    ]

    CLICKER_UPGRADES = [
        {
            "id": "tap_glove",
            "name": "Кинетическая перчатка",
            "desc": "+1.0 к силе клика",
            "base": 18.0,
            "growth": 1.16,
            "max": 50,
            "unlock": 0.0,
        },
        {
            "id": "phase_knuckle",
            "name": "Фазовый привод",
            "desc": "+12% к силе клика",
            "base": 90.0,
            "growth": 1.24,
            "max": 25,
            "unlock": 150.0,
        },
        {
            "id": "drone_swarm",
            "name": "Дрон-сборщик",
            "desc": "+0.75 плазмы/с",
            "base": 45.0,
            "growth": 1.19,
            "max": 45,
            "unlock": 40.0,
        },
        {
            "id": "relay_grid",
            "name": "Релейная решетка",
            "desc": "+16% к автосбору",
            "base": 260.0,
            "growth": 1.27,
            "max": 25,
            "unlock": 500.0,
        },
        {
            "id": "critical_lens",
            "name": "Крит-линза",
            "desc": "+2.2% шанс крита",
            "base": 420.0,
            "growth": 1.29,
            "max": 20,
            "unlock": 1500.0,
        },
        {
            "id": "fracture_core",
            "name": "Матрица разлома",
            "desc": "+0.22 к множителю крита",
            "base": 900.0,
            "growth": 1.34,
            "max": 18,
            "unlock": 5000.0,
        },
        {
            "id": "rhythm_mesh",
            "name": "Ритм-сетка",
            "desc": "Усиливает синхронизацию",
            "base": 1350.0,
            "growth": 1.28,
            "max": 20,
            "unlock": 9000.0,
        },
        {
            "id": "coolant_loop",
            "name": "Охлаждающий контур",
            "desc": "Дольше буст, меньше КД",
            "base": 2100.0,
            "growth": 1.36,
            "max": 14,
            "unlock": 18000.0,
        },
        {
            "id": "quantum_core",
            "name": "Квантовое ядро",
            "desc": "+4% ко всем источникам",
            "base": 4200.0,
            "growth": 1.42,
            "max": 16,
            "unlock": 30000.0,
        },
    ]

    CLICKER_UPGRADE_MAP = dict((item["id"], item) for item in CLICKER_UPGRADES)

    def clicker_default_state():
        upgrades = {}
        for item in CLICKER_UPGRADES:
            upgrades[item["id"]] = 0

        return {
            "version": CLICKER_SAVE_VERSION,
            "points": 0.0,
            "lifetime": 0.0,
            "cores": 0,
            "best_cps": 0.0,
            "upgrades": upgrades,
        }

    def clicker_sanitize_state(raw_state):
        state = clicker_default_state()

        if not isinstance(raw_state, dict):
            return state

        state["version"] = CLICKER_SAVE_VERSION

        try:
            state["points"] = max(0.0, float(raw_state.get("points", 0.0)))
        except Exception:
            state["points"] = 0.0

        try:
            state["lifetime"] = max(0.0, float(raw_state.get("lifetime", 0.0)))
        except Exception:
            state["lifetime"] = 0.0

        try:
            state["cores"] = max(0, int(raw_state.get("cores", 0)))
        except Exception:
            state["cores"] = 0

        try:
            state["best_cps"] = max(0.0, float(raw_state.get("best_cps", 0.0)))
        except Exception:
            state["best_cps"] = 0.0

        raw_upgrades = raw_state.get("upgrades", {})
        if not isinstance(raw_upgrades, dict):
            raw_upgrades = {}

        merged_upgrades = {}
        for item in CLICKER_UPGRADES:
            uid = item["id"]
            try:
                level = int(raw_upgrades.get(uid, 0))
            except Exception:
                level = 0
            level = max(0, min(level, int(item["max"])))
            merged_upgrades[uid] = level

        state["upgrades"] = merged_upgrades
        return state

    def clicker_load_state():
        raw_state = getattr(persistent, "extra_clicker_state", None)
        return clicker_sanitize_state(raw_state)

    def clicker_save_state(state):
        persistent.extra_clicker_state = clicker_sanitize_state(copy.deepcopy(state))
        renpy.save_persistent()

    def clicker_format_number(value):
        try:
            number = float(value)
        except Exception:
            number = 0.0

        negative = number < 0
        number = abs(number)

        suffixes = ["", "K", "M", "B", "T", "Qa", "Qi"]
        suffix_index = 0

        while number >= 1000.0 and suffix_index < len(suffixes) - 1:
            number /= 1000.0
            suffix_index += 1

        if suffix_index == 0:
            text = str(int(number))
        elif number >= 100.0:
            text = "{:.0f}".format(number)
        elif number >= 10.0:
            text = "{:.1f}".format(number)
        else:
            text = "{:.2f}".format(number)

        if text.endswith(".00"):
            text = text[:-3]
        elif text.endswith("0") and "." in text:
            text = text[:-1]

        if negative:
            text = "-" + text

        return text + suffixes[suffix_index]

    def clicker_make_result(board, start_lifetime, target=0.0):
        try:
            earned = max(0.0, float(getattr(board, "lifetime", 0.0)) - float(start_lifetime))
        except Exception:
            earned = 0.0

        try:
            goal = max(0.0, float(target))
        except Exception:
            goal = 0.0

        try:
            points = max(0.0, float(getattr(board, "points", 0.0)))
        except Exception:
            points = 0.0

        try:
            lifetime = max(0.0, float(getattr(board, "lifetime", 0.0)))
        except Exception:
            lifetime = 0.0

        try:
            cores = max(0, int(getattr(board, "cores", 0)))
        except Exception:
            cores = 0

        return {
            "earned": earned,
            "target": goal,
            "hit_target": (earned >= goal) if goal > 0.0 else True,
            "points": points,
            "lifetime": lifetime,
            "cores": cores,
        }

    class ClickerGameBoard(renpy.Displayable):

        def __init__(self, width=1500, height=860, **kwargs):
            super(ClickerGameBoard, self).__init__(**kwargs)

            self.width = int(width)
            self.height = int(height)

            state = clicker_load_state()
            self.points = float(state["points"])
            self.lifetime = float(state["lifetime"])
            self.cores = int(state["cores"])
            self.best_cps = float(state["best_cps"])
            self.upgrades = dict(state["upgrades"])
            self.random = random.Random()

            self.combo = 0.0
            self.sync = 0.0
            self.last_click_time = None

            self.overdrive_timer = 0.0
            self.overdrive_cooldown_left = 0.0

            self.anomaly = None
            self.anomaly_spawn_timer = self._next_anomaly_delay()

            self.float_texts = []
            self.info_message = "Поддерживай ритм кликов: синхронизация даёт скрытый буст."
            self.info_message_timer = 4.2

            self.last_st = None
            self.save_clock = 0.0
            self.state_dirty = False

            self.button_rects = {}
            self.upgrade_rects = {}
            self.core_center = (self.width // 3, self.height // 2)
            self.core_radius = 100
            self.arena_rect = (20, 20, int(self.width * 0.60) - 30, self.height - 40)

            self.stage_index = 0
            self.stage_multiplier = 1.0
            self.click_power = 1.0
            self.auto_per_sec = 0.0
            self.crit_chance = 0.04
            self.crit_multiplier = 2.0
            self.combo_multiplier = 1.0
            self.sync_multiplier = 1.0
            self.echo_chance = 0.0
            self.echo_factor = 0.0
            self.overdrive_duration = 10.0
            self.overdrive_cooldown_total = 48.0

            self.last_stage_seen = self._stage_from_lifetime(self.lifetime)
            self._refresh_derived_stats(trigger_message=False)

        def _snapshot_state(self):
            return {
                "version": CLICKER_SAVE_VERSION,
                "points": float(self.points),
                "lifetime": float(self.lifetime),
                "cores": int(self.cores),
                "best_cps": float(self.best_cps),
                "upgrades": dict(self.upgrades),
            }

        def force_save(self):
            clicker_save_state(self._snapshot_state())
            self.state_dirty = False
            self.save_clock = 0.0

        def _touch_state(self):
            self.state_dirty = True

        def _set_message(self, message, duration=2.4):
            self.info_message = str(message)
            self.info_message_timer = max(0.6, float(duration))

        def _next_anomaly_delay(self):
            return self.random.uniform(8.5, 16.0)

        def _stage_from_lifetime(self, lifetime):
            index = 0
            for idx, threshold in enumerate(CLICKER_STAGE_THRESHOLDS):
                if lifetime >= threshold:
                    index = idx
                else:
                    break
            return index

        def _upgrade_level(self, uid):
            try:
                return int(self.upgrades.get(uid, 0))
            except Exception:
                return 0

        def _upgrade_cost(self, item):
            level = self._upgrade_level(item["id"])
            return float(item["base"]) * (float(item["growth"]) ** level)

        def _upgrade_is_unlocked(self, item):
            return self.lifetime >= float(item["unlock"])

        def _calibration_gain(self):
            potential = int(math.sqrt(max(0.0, self.lifetime) / 9000.0))
            return max(0, potential - self.cores)

        def _refresh_derived_stats(self, trigger_message=True):
            stage_now = self._stage_from_lifetime(self.lifetime)
            self.stage_index = stage_now

            if trigger_message and stage_now > self.last_stage_seen:
                self._set_message("Новый сектор: {}".format(CLICKER_STAGE_NAMES[stage_now]), duration=3.2)

            self.last_stage_seen = stage_now

            tap_glove = self._upgrade_level("tap_glove")
            phase_knuckle = self._upgrade_level("phase_knuckle")
            drone_swarm = self._upgrade_level("drone_swarm")
            relay_grid = self._upgrade_level("relay_grid")
            critical_lens = self._upgrade_level("critical_lens")
            fracture_core = self._upgrade_level("fracture_core")
            rhythm_mesh = self._upgrade_level("rhythm_mesh")
            coolant_loop = self._upgrade_level("coolant_loop")
            quantum_core = self._upgrade_level("quantum_core")

            self.combo_multiplier = 1.0 + min(45.0, self.combo) * 0.024 * (1.0 + rhythm_mesh * 0.04)
            self.sync_multiplier = 1.0 + min(1.0, self.sync) * (0.65 + rhythm_mesh * 0.02)

            core_multiplier = 1.0 + self.cores * 0.12
            self.stage_multiplier = 1.0 + self.stage_index * 0.24
            quantum_multiplier = 1.0 + quantum_core * 0.04

            overdrive_click = 2.75 if self.overdrive_timer > 0.0 else 1.0
            overdrive_auto = 2.2 if self.overdrive_timer > 0.0 else 1.0

            click_flat = 1.0 + tap_glove * 1.0
            click_mult = 1.0 + phase_knuckle * 0.12
            self.click_power = click_flat * click_mult * core_multiplier * self.stage_multiplier * quantum_multiplier
            self.click_power *= self.combo_multiplier * self.sync_multiplier * overdrive_click

            auto_flat = drone_swarm * 0.75
            auto_mult = 1.0 + relay_grid * 0.16
            self.auto_per_sec = auto_flat * auto_mult * core_multiplier * self.stage_multiplier * quantum_multiplier
            self.auto_per_sec *= (1.0 + self.sync * 0.22) * overdrive_auto

            self.crit_chance = min(0.70, 0.04 + critical_lens * 0.022)
            self.crit_multiplier = 2.0 + fracture_core * 0.22

            self.echo_chance = min(0.55, 0.06 + rhythm_mesh * 0.011 + self.sync * 0.12)
            self.echo_factor = 0.65 + rhythm_mesh * 0.06

            self.overdrive_duration = 10.0 * (1.0 + coolant_loop * 0.03)
            cooldown_reduction = min(0.68, coolant_loop * 0.04)
            self.overdrive_cooldown_total = max(14.0, 48.0 * (1.0 - cooldown_reduction))

            self.best_cps = max(self.best_cps, self.auto_per_sec)

        def _add_points(self, value):
            try:
                amount = float(value)
            except Exception:
                amount = 0.0

            if amount <= 0.0:
                return

            self.points += amount
            self.lifetime += amount
            self._touch_state()

        def _spawn_float(self, text, x, y, color="#eaf6ff", size=24, ttl=1.0):
            self.float_texts.append(
                {
                    "text": str(text),
                    "x": float(x),
                    "y": float(y),
                    "color": str(color),
                    "size": int(size),
                    "time": float(ttl),
                    "ttl": float(ttl),
                }
            )

        def _spawn_anomaly(self):
            x0, y0, w0, h0 = self.arena_rect
            margin = 90

            min_x = int(x0 + margin)
            max_x = int(x0 + w0 - margin)
            min_y = int(y0 + 120)
            max_y = int(y0 + h0 - margin)

            if max_x <= min_x:
                max_x = min_x + 1
            if max_y <= min_y:
                max_y = min_y + 1

            self.anomaly = {
                "x": self.random.randint(min_x, max_x),
                "y": self.random.randint(min_y, max_y),
                "r": self.random.randint(18, 28),
                "time": self.random.uniform(3.4, 4.6),
                "quality": self.random.uniform(0.92, 1.42),
            }

        def _collect_anomaly_if_hit(self, x, y):
            if not self.anomaly:
                return False

            dx = float(x) - float(self.anomaly["x"])
            dy = float(y) - float(self.anomaly["y"])
            radius = float(self.anomaly["r"]) + 8.0

            if dx * dx + dy * dy > radius * radius:
                return False

            reward = max(150.0, self.click_power * 7.0 + self.auto_per_sec * 14.0)
            reward *= (1.0 + self.stage_index * 0.30) * float(self.anomaly["quality"])

            self._add_points(reward)
            self.combo = min(60.0, self.combo + 2.0)
            self.sync = min(1.0, self.sync + 0.18)

            self._spawn_float("Аномалия +{}".format(clicker_format_number(reward)), x, y - 16, "#ffe38a", 30, 1.35)
            self._set_message("Аномалия поймана. Синхронизация ускорена.")

            self.anomaly = None
            self.anomaly_spawn_timer = self._next_anomaly_delay()
            return True

        def _is_core_hit(self, x, y):
            dx = float(x) - float(self.core_center[0])
            dy = float(y) - float(self.core_center[1])
            return dx * dx + dy * dy <= float(self.core_radius * self.core_radius)

        def _handle_core_click(self, x, y):
            now = time.monotonic()
            interval = None if self.last_click_time is None else max(0.0, now - self.last_click_time)
            self.last_click_time = now

            rhythm_mesh = self._upgrade_level("rhythm_mesh")

            if interval is None:
                self.combo = min(60.0, self.combo + 0.9)
            elif 0.15 <= interval <= 0.50:
                self.combo = min(60.0, self.combo + 1.0 + rhythm_mesh * 0.06)
                self.sync = min(1.0, self.sync + 0.11 + rhythm_mesh * 0.01)
            elif interval <= 1.10:
                self.combo = min(60.0, self.combo + 0.35)
                self.sync = min(1.0, self.sync + 0.03)
            else:
                self.combo *= 0.55
                self.sync *= 0.85

            value = self.click_power
            critical = self.random.random() < self.crit_chance

            if critical:
                value *= self.crit_multiplier

            if self.random.random() < self.echo_chance:
                echo_bonus = max(self.click_power * 0.35, self.auto_per_sec * self.echo_factor)
                value += echo_bonus
                self._spawn_float("Эхо +{}".format(clicker_format_number(echo_bonus)), x + self.random.randint(-20, 20), y - 32, "#7be7ff", 24, 0.95)

            self._add_points(value)

            if critical:
                self._spawn_float("КРИТ x{:.2f}".format(self.crit_multiplier), x, y - 52, "#ffb0b0", 24, 0.9)
                self._spawn_float("+{}".format(clicker_format_number(value)), x, y - 18, "#ffd6d6", 28, 1.1)
            else:
                self._spawn_float("+{}".format(clicker_format_number(value)), x, y - 10, "#eaf6ff", 26, 1.0)

        def _try_activate_overdrive(self):
            if self.overdrive_timer > 0.0:
                self._set_message("Овердрайв уже активен.", duration=1.5)
                return False

            if self.overdrive_cooldown_left > 0.0:
                self._set_message("Овердрайв перезаряжается.", duration=1.5)
                return False

            self.overdrive_timer = self.overdrive_duration
            self.overdrive_cooldown_left = self.overdrive_cooldown_total
            self._set_message("Овердрайв активирован: пик добычи на короткое время.", duration=2.4)
            self._touch_state()
            return True

        def _try_buy_upgrade(self, upgrade_id):
            item = CLICKER_UPGRADE_MAP.get(str(upgrade_id))
            if item is None:
                return False

            level = self._upgrade_level(item["id"])
            max_level = int(item["max"])

            if level >= max_level:
                self._set_message("{} уже на максимуме.".format(item["name"]), duration=1.5)
                return False

            if not self._upgrade_is_unlocked(item):
                unlock_value = clicker_format_number(item["unlock"])
                self._set_message("{} откроется после total {}.".format(item["name"], unlock_value), duration=1.8)
                return False

            cost = self._upgrade_cost(item)
            if self.points < cost:
                self._set_message("Не хватает плазмы для {}.".format(item["name"]), duration=1.6)
                return False

            self.points -= cost
            self.upgrades[item["id"]] = level + 1
            self._touch_state()

            rect = self.upgrade_rects.get(item["id"])
            if rect:
                x0, y0, w0, _h0 = rect
                self._spawn_float("-{}".format(clicker_format_number(cost)), x0 + w0 - 58, y0 + 12, "#ff9f9f", 20, 0.8)

            self._set_message("{} улучшен до уровня {}.".format(item["name"], level + 1), duration=1.8)
            return True

        def _perform_calibration(self):
            gain = self._calibration_gain()
            if gain <= 0:
                need_total = clicker_format_number((self.cores + 1) * (self.cores + 1) * 9000)
                self._set_message("Для калибровки нужно больше total (цель: {}).".format(need_total), duration=2.0)
                return False

            self.cores += gain
            self.points = 0.0

            for item in CLICKER_UPGRADES:
                self.upgrades[item["id"]] = 0

            self.combo = 0.0
            self.sync = 0.0
            self.last_click_time = None
            self.overdrive_timer = 0.0
            self.overdrive_cooldown_left = 0.0

            self.anomaly = None
            self.anomaly_spawn_timer = self._next_anomaly_delay()

            self._touch_state()
            self._set_message("Калибровка завершена: +{} ядер.".format(gain), duration=3.0)
            self._spawn_float("+{} ядер".format(gain), self.width * 0.50, self.height * 0.50, "#ffe08a", 34, 1.6)
            return True

        def _rect_contains(self, rect, x, y):
            if rect is None:
                return False
            x0, y0, w0, h0 = rect
            return x0 <= x <= x0 + w0 and y0 <= y <= y0 + h0

        def _draw_text(self, render, text, x, y, size=26, color="#eaf6ff", align=0.0):
            displayable = Text(
                str(text),
                size=int(size),
                color=str(color),
                outlines=[(1, "#00000088", 0, 0)],
            )
            text_render = renpy.render(displayable, self.width, self.height, 0, 0)

            try:
                tw, _th = text_render.get_size()
            except Exception:
                tw = getattr(text_render, "width", 0)

            draw_x = int(x - tw * float(align))
            draw_y = int(y)
            render.blit(text_render, (draw_x, draw_y))

        def _draw_bar(self, canvas, rect, ratio, back, fill, border):
            x0, y0, w0, h0 = rect
            canvas.rect(back, (x0, y0, w0, h0), 0)

            value = max(0.0, min(1.0, float(ratio)))
            fill_w = int(w0 * value)
            if fill_w > 0:
                canvas.rect(fill, (x0, y0, fill_w, h0), 0)

            canvas.rect(border, (x0, y0, w0, h0), 2)

        def event(self, ev, x, y, st):
            import pygame

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if self._collect_anomaly_if_hit(x, y):
                    return

                if self._rect_contains(self.button_rects.get("overdrive"), x, y):
                    self._try_activate_overdrive()
                    return

                if self._rect_contains(self.button_rects.get("calibration"), x, y):
                    self._perform_calibration()
                    return

                for item in CLICKER_UPGRADES:
                    uid = item["id"]
                    if self._rect_contains(self.upgrade_rects.get(uid), x, y):
                        self._try_buy_upgrade(uid)
                        return

                if self._is_core_hit(x, y):
                    self._handle_core_click(x, y)
                    return

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                self._handle_core_click(self.core_center[0], self.core_center[1])

        def _tick(self, dt):
            if dt <= 0.0:
                return

            self._refresh_derived_stats(trigger_message=True)

            auto_gain = self.auto_per_sec * dt
            if auto_gain > 0.0:
                self._add_points(auto_gain)

            if self.combo > 0.0:
                self.combo = max(0.0, self.combo - dt * (0.95 + self.combo * 0.02))

            if self.sync > 0.0:
                self.sync = max(0.0, self.sync - dt * (0.06 + self.sync * 0.05))

            if self.overdrive_timer > 0.0:
                self.overdrive_timer = max(0.0, self.overdrive_timer - dt)

            if self.overdrive_cooldown_left > 0.0:
                self.overdrive_cooldown_left = max(0.0, self.overdrive_cooldown_left - dt)

            if self.anomaly is None:
                self.anomaly_spawn_timer -= dt
                if self.anomaly_spawn_timer <= 0.0:
                    self._spawn_anomaly()
            else:
                self.anomaly["time"] -= dt
                if self.anomaly["time"] <= 0.0:
                    self.anomaly = None
                    self.anomaly_spawn_timer = self._next_anomaly_delay()

            updated_texts = []
            for item in self.float_texts:
                item["time"] -= dt
                if item["time"] > 0.0:
                    t = item["time"] / max(0.001, item["ttl"])
                    item["y"] -= dt * (24.0 + (1.0 - t) * 45.0)
                    updated_texts.append(item)
            self.float_texts = updated_texts

            if self.info_message_timer > 0.0:
                self.info_message_timer = max(0.0, self.info_message_timer - dt)

            self.save_clock += dt
            if self.state_dirty and self.save_clock >= 3.0:
                clicker_save_state(self._snapshot_state())
                self.state_dirty = False
                self.save_clock = 0.0

        def render(self, width, height, st, at):
            if self.last_st is None:
                dt = 0.0
            else:
                dt = max(0.0, min(0.20, st - self.last_st))

            self.last_st = st
            self._tick(dt)
            self._refresh_derived_stats(trigger_message=False)

            render = renpy.Render(self.width, self.height)
            canvas = render.canvas()

            canvas.rect((8, 12, 20, 255), (0, 0, self.width, self.height), 0)

            panel_x = int(self.width * 0.62)
            arena_rect = (18, 18, panel_x - 36, self.height - 36)
            panel_rect = (panel_x + 8, 18, self.width - panel_x - 26, self.height - 36)

            self.arena_rect = arena_rect

            canvas.rect((10, 18, 30, 255), arena_rect, 0)
            canvas.rect((11, 16, 24, 255), panel_rect, 0)
            canvas.rect((70, 120, 165, 110), arena_rect, 2)
            canvas.rect((70, 120, 165, 110), panel_rect, 2)

            pulse = math.sin(st * 3.0) * 6.0
            if self.overdrive_timer > 0.0:
                pulse += 10.0

            core_x = int(arena_rect[0] + arena_rect[2] * 0.50)
            core_y = int(arena_rect[1] + arena_rect[3] * 0.50)
            core_radius = 96 + int(pulse)

            self.core_center = (core_x, core_y)
            self.core_radius = core_radius

            canvas.circle((15, 40, 78, 255), self.core_center, core_radius + 26, 0)
            canvas.circle((70, 140, 235, 255), self.core_center, core_radius, 0)
            canvas.circle((160, 218, 255, 255), self.core_center, int(core_radius * 0.62), 0)
            canvas.circle((232, 248, 255, 255), self.core_center, int(core_radius * 0.20), 0)

            if self.anomaly:
                alpha = 70 + int(160 * max(0.0, min(1.0, self.anomaly["time"] / 4.2)))
                halo = int(self.anomaly["r"] + 8 + math.sin(st * 6.0) * 2)
                canvas.circle((255, 196, 72, alpha), (int(self.anomaly["x"]), int(self.anomaly["y"])), halo, 2)
                canvas.circle((255, 148, 36, alpha), (int(self.anomaly["x"]), int(self.anomaly["y"])), int(self.anomaly["r"]), 0)
                self._draw_text(render, "A", self.anomaly["x"], self.anomaly["y"] - 11, 22, "#241b10", align=0.5)

            top_x = arena_rect[0] + 24
            top_y = arena_rect[1] + 18

            self._draw_text(render, "Плазма: {}".format(clicker_format_number(self.points)), top_x, top_y, 46, "#f5fbff")
            self._draw_text(render, "Total: {}".format(clicker_format_number(self.lifetime)), top_x, top_y + 52, 24, "#bee8ff")
            self._draw_text(render, "Клик: {}   Авто: {}/с".format(clicker_format_number(self.click_power), clicker_format_number(self.auto_per_sec)), top_x, top_y + 84, 22, "#9dd7ff")
            self._draw_text(render, "Крит: {:.1f}% x{:.2f}".format(self.crit_chance * 100.0, self.crit_multiplier), top_x, top_y + 112, 21, "#9dd7ff")

            combo_bar = (top_x, top_y + 150, arena_rect[2] - 54, 20)
            sync_bar = (top_x, top_y + 185, arena_rect[2] - 54, 20)

            self._draw_bar(canvas, combo_bar, self.combo / 40.0, (30, 43, 57, 255), (131, 223, 255, 255), (150, 220, 255, 170))
            self._draw_bar(canvas, sync_bar, self.sync, (30, 43, 57, 255), (255, 188, 93, 255), (255, 214, 138, 170))

            self._draw_text(render, "Комбо x{:.2f}".format(self.combo_multiplier), combo_bar[0], combo_bar[1] - 23, 20, "#a8e4ff")
            self._draw_text(render, "Синхро x{:.2f}".format(self.sync_multiplier), sync_bar[0], sync_bar[1] - 23, 20, "#ffd6a8")

            self._draw_text(render, "КЛИК", core_x, core_y - 14, 42, "#0d1a2e", align=0.5)
            self._draw_text(render, "держи ритм", core_x, core_y + 30, 20, "#143353", align=0.5)

            overdrive_rect = (arena_rect[0] + 24, arena_rect[1] + arena_rect[3] - 98, 314, 72)
            self.button_rects["overdrive"] = overdrive_rect

            overdrive_ready = self.overdrive_timer <= 0.0 and self.overdrive_cooldown_left <= 0.0
            if self.overdrive_timer > 0.0:
                od_color = (136, 222, 125, 255)
                od_text = "ОВЕРДРАЙВ {:.1f}с".format(self.overdrive_timer)
                od_note = "x2.75 к клику, x2.2 к авто"
            elif overdrive_ready:
                od_color = (114, 193, 255, 255)
                od_text = "АКТИВИРОВАТЬ ОВЕРДРАЙВ"
                od_note = "пиковый режим на короткое время"
            else:
                od_color = (60, 84, 104, 255)
                od_text = "ПЕРЕЗАРЯДКА {:.1f}с".format(self.overdrive_cooldown_left)
                od_note = "улучши Охлаждающий контур"

            canvas.rect(od_color, overdrive_rect, 0)
            canvas.rect((180, 230, 255, 220), overdrive_rect, 2)
            self._draw_text(render, od_text, overdrive_rect[0] + overdrive_rect[2] / 2, overdrive_rect[1] + 13, 23, "#081220", align=0.5)
            self._draw_text(render, od_note, overdrive_rect[0] + overdrive_rect[2] / 2, overdrive_rect[1] + 41, 18, "#102642", align=0.5)

            sector_name = CLICKER_STAGE_NAMES[self.stage_index]
            self._draw_text(render, "Сектор: {}".format(sector_name), panel_rect[0] + 18, panel_rect[1] + 16, 29, "#ffe08a")
            self._draw_text(render, "Ядра: {}   Глобал x{:.2f}".format(self.cores, (1.0 + self.cores * 0.12) * self.stage_multiplier), panel_rect[0] + 18, panel_rect[1] + 52, 21, "#f6d1ff")
            self._draw_text(render, "Лучший авто-поток: {}/с".format(clicker_format_number(self.best_cps)), panel_rect[0] + 18, panel_rect[1] + 80, 20, "#9cb8ff")

            self.upgrade_rects = {}

            upgrade_y = panel_rect[1] + 118
            row_height = 56
            row_gap = 8
            row_width = panel_rect[2] - 30

            for index, item in enumerate(CLICKER_UPGRADES):
                row_x = panel_rect[0] + 15
                row_y = upgrade_y + index * (row_height + row_gap)
                row_rect = (row_x, row_y, row_width, row_height)
                self.upgrade_rects[item["id"]] = row_rect

                level = self._upgrade_level(item["id"])
                max_level = int(item["max"])
                unlocked = self._upgrade_is_unlocked(item)
                cost = self._upgrade_cost(item)
                affordable = unlocked and level < max_level and self.points >= cost

                if level >= max_level:
                    row_color = (57, 104, 73, 255)
                elif not unlocked:
                    row_color = (46, 52, 64, 255)
                elif affordable:
                    row_color = (48, 90, 130, 255)
                else:
                    row_color = (42, 60, 84, 255)

                canvas.rect(row_color, row_rect, 0)
                canvas.rect((156, 202, 255, 150), row_rect, 2)

                line_name = "{} [{} / {}]".format(item["name"], level, max_level)
                self._draw_text(render, line_name, row_x + 12, row_y + 7, 20, "#edf7ff")
                self._draw_text(render, item["desc"], row_x + 12, row_y + 32, 17, "#b9d9ff")

                if level >= max_level:
                    price_text = "MAX"
                    price_color = "#a7ffc2"
                elif not unlocked:
                    price_text = "unlock {}".format(clicker_format_number(item["unlock"]))
                    price_color = "#8f9bb2"
                else:
                    price_text = clicker_format_number(cost)
                    price_color = "#ffd9aa" if affordable else "#b8c9db"

                self._draw_text(render, price_text, row_x + row_width - 12, row_y + 18, 21, price_color, align=1.0)

            calibration_rect = (panel_rect[0] + 15, panel_rect[1] + panel_rect[3] - 90, panel_rect[2] - 30, 64)
            self.button_rects["calibration"] = calibration_rect

            gain = self._calibration_gain()
            if gain > 0:
                cal_color = (143, 108, 226, 255)
                cal_text = "КАЛИБРОВКА +{} ЯДЕР".format(gain)
                cal_note = "Сбросит апгрейды, но даст постоянный мультипликатор"
            else:
                cal_color = (66, 58, 84, 255)
                next_target = clicker_format_number((self.cores + 1) * (self.cores + 1) * 9000)
                cal_text = "КАЛИБРОВКА НЕДОСТУПНА"
                cal_note = "Следующая цель total: {}".format(next_target)

            canvas.rect(cal_color, calibration_rect, 0)
            canvas.rect((222, 205, 255, 190), calibration_rect, 2)
            self._draw_text(render, cal_text, calibration_rect[0] + calibration_rect[2] / 2, calibration_rect[1] + 10, 21, "#f8f0ff", align=0.5)
            self._draw_text(render, cal_note, calibration_rect[0] + calibration_rect[2] / 2, calibration_rect[1] + 35, 17, "#eadcff", align=0.5)

            for item in self.float_texts:
                self._draw_text(render, item["text"], item["x"], item["y"], item["size"], item["color"], align=0.5)

            if self.info_message_timer > 0.0:
                self._draw_text(render, self.info_message, self.width * 0.50, self.height - 36, 24, "#ffdf99", align=0.5)

            renpy.redraw(self, 0.016)
            return render


default clicker_last_result = {
    "earned": 0.0,
    "target": 0.0,
    "hit_target": False,
    "points": 0.0,
    "lifetime": 0.0,
    "cores": 0,
}


screen clicker_minigame_screen(board, target=0.0, start_lifetime=0.0):
    tag clicker_minigame
    modal True
    layer "master"

    on "hide" action Function(board.force_save)

    add Solid("#02050acc")
    add board:
        xalign 0.5
        yalign 0.55

    frame:
        align (0.02, 0.02)
        background "#0d1728dd"
        padding (16, 12)
        has vbox
        spacing 6

        if float(target) > 0.0:
            text "Испытание кликера" size 33 color "#f4fbff"
            text "Цель: добыть минимум [clicker_format_number(target)] плазмы за сессию." size 21 color "#d5e9ff"
            text "Выйдите кнопкой справа, когда решите что хватит." size 19 color "#abc9eb"
        else:
            text "Кликер: свободный режим" size 33 color "#f4fbff"
            text "Это внутриигровой модуль. Пробел = клик в центр." size 21 color "#d5e9ff"

    textbutton "Завершить":
        align (0.98, 0.03)
        action Return(clicker_make_result(board, start_lifetime, target))
        text_size 38


label clicker_minigame(target=0.0):
    $ _clicker_target = max(0.0, float(target))
    $ _clicker_board = ClickerGameBoard(width=1500, height=860)
    $ _clicker_start_lifetime = float(_clicker_board.lifetime)

    call screen clicker_minigame_screen(
        _clicker_board,
        target=_clicker_target,
        start_lifetime=_clicker_start_lifetime,
    )

    $ _clicker_result = _return if isinstance(_return, dict) else clicker_make_result(_clicker_board, _clicker_start_lifetime, _clicker_target)
    $ clicker_last_result = _clicker_result

    if _clicker_target > 0.0:
        return bool(_clicker_result.get("hit_target", False))
    return _clicker_result


label test_clicker_minigame:
    scene black
    with fade
    "Тест модуля кликера."

    $ _test_clicker_goal = 12000.0
    call clicker_minigame(target=_test_clicker_goal)
    $ _test_clicker_success = bool(_return)
    $ _test_clicker_result = dict(clicker_last_result)

    if _test_clicker_success:
        "Испытание пройдено."
    else:
        "Испытание завершено без выполнения цели."

    "Добыто за сессию: [clicker_format_number(_test_clicker_result.get('earned', 0.0))]."
    "Баланс: [clicker_format_number(_test_clicker_result.get('points', 0.0))], total: [clicker_format_number(_test_clicker_result.get('lifetime', 0.0))], ядра: [int(_test_clicker_result.get('cores', 0))]."
    return
