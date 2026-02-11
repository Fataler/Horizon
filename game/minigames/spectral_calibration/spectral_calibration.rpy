init python:
    import copy

    SPECTRAL_CALIBRATION_LEVELS = {
        "standard": {
            "harmonics": 4,
            "amp_step": 5,
            "phase_step": 15,
            "amp_tolerance": 5,
            "phase_tolerance": 15,
        },
        "hard": {
            "harmonics": 5,
            "amp_step": 5,
            "phase_step": 15,
            "amp_tolerance": 4,
            "phase_tolerance": 10,
        },
    }


    def _spectral_norm_list(raw, count, fallback, clamp_min=None, clamp_max=None, mod=None):
        out = []
        if isinstance(raw, (list, tuple)):
            for item in raw:
                try:
                    value = int(item)
                except Exception:
                    continue
                if mod is not None:
                    value %= int(mod)
                if clamp_min is not None:
                    value = max(int(clamp_min), value)
                if clamp_max is not None:
                    value = min(int(clamp_max), value)
                out.append(value)
                if len(out) >= count:
                    break

        while len(out) < count:
            out.append(int(fallback[len(out) % len(fallback)]))
        return out[:count]


    def spectral_calibration_resolve_level(
        level=None,
        harmonics=None,
        amp_step=None,
        phase_step=None,
        amp_tolerance=None,
        phase_tolerance=None,
        target_amp=None,
        target_phase=None,
        current_amp=None,
        current_phase=None,
    ):
        cfg = copy.deepcopy(SPECTRAL_CALIBRATION_LEVELS["standard"])
        level_id = "standard"

        if isinstance(level, str) and level in SPECTRAL_CALIBRATION_LEVELS:
            cfg = copy.deepcopy(SPECTRAL_CALIBRATION_LEVELS[level])
            level_id = str(level)
        elif isinstance(level, dict):
            preset = level.get("preset")
            if isinstance(preset, str) and preset in SPECTRAL_CALIBRATION_LEVELS:
                cfg = copy.deepcopy(SPECTRAL_CALIBRATION_LEVELS[preset])
                level_id = str(preset)
            for key, val in level.items():
                if key in ("id", "preset"):
                    continue
                cfg[key] = copy.deepcopy(val)
            level_id = str(level.get("id", level_id if level_id else "custom"))

        if harmonics is not None:
            cfg["harmonics"] = harmonics
        if amp_step is not None:
            cfg["amp_step"] = amp_step
        if phase_step is not None:
            cfg["phase_step"] = phase_step
        if amp_tolerance is not None:
            cfg["amp_tolerance"] = amp_tolerance
        if phase_tolerance is not None:
            cfg["phase_tolerance"] = phase_tolerance
        if target_amp is not None:
            cfg["target_amp"] = target_amp
        if target_phase is not None:
            cfg["target_phase"] = target_phase
        if current_amp is not None:
            cfg["current_amp"] = current_amp
        if current_phase is not None:
            cfg["current_phase"] = current_phase

        count = max(3, int(cfg.get("harmonics", 4)))
        cfg["harmonics"] = count
        cfg["amp_step"] = max(1, int(cfg.get("amp_step", 5)))
        cfg["phase_step"] = max(1, int(cfg.get("phase_step", 15)))
        cfg["amp_tolerance"] = max(1, int(cfg.get("amp_tolerance", 5)))
        cfg["phase_tolerance"] = max(1, int(cfg.get("phase_tolerance", 15)))

        target_amp_fallback = [35, 55, 75, 50, 65]
        target_phase_fallback = [45, 180, 300, 120, 240]
        current_amp_fallback = [60, 25, 45, 80, 30]
        current_phase_fallback = [210, 45, 120, 300, 15]

        cfg["target_amp"] = _spectral_norm_list(cfg.get("target_amp"), count, target_amp_fallback, 0, 100)
        cfg["target_phase"] = _spectral_norm_list(cfg.get("target_phase"), count, target_phase_fallback, mod=360)
        cfg["current_amp"] = _spectral_norm_list(cfg.get("current_amp"), count, current_amp_fallback, 0, 100)
        cfg["current_phase"] = _spectral_norm_list(cfg.get("current_phase"), count, current_phase_fallback, mod=360)

        return {
            "harmonics": cfg["harmonics"],
            "amp_step": cfg["amp_step"],
            "phase_step": cfg["phase_step"],
            "amp_tolerance": cfg["amp_tolerance"],
            "phase_tolerance": cfg["phase_tolerance"],
            "target_amp": cfg["target_amp"],
            "target_phase": cfg["target_phase"],
            "current_amp": cfg["current_amp"],
            "current_phase": cfg["current_phase"],
            "level_id": level_id,
        }


    class SpectralCalibrationGame(object):
        def __init__(
            self,
            harmonics=4,
            amp_step=5,
            phase_step=15,
            amp_tolerance=5,
            phase_tolerance=15,
            target_amp=None,
            target_phase=None,
            current_amp=None,
            current_phase=None,
            level_id="custom",
        ):
            self.harmonics = max(3, int(harmonics))
            self.amp_step = max(1, int(amp_step))
            self.phase_step = max(1, int(phase_step))
            self.amp_tolerance = max(1, int(amp_tolerance))
            self.phase_tolerance = max(1, int(phase_tolerance))
            self.level_id = str(level_id)

            self.target_amp = _spectral_norm_list(target_amp, self.harmonics, [35, 55, 75, 50, 65], 0, 100)
            self.target_phase = _spectral_norm_list(target_phase, self.harmonics, [45, 180, 300, 120, 240], mod=360)
            self.current_amp = _spectral_norm_list(current_amp, self.harmonics, [60, 25, 45, 80, 30], 0, 100)
            self.current_phase = _spectral_norm_list(current_phase, self.harmonics, [210, 45, 120, 300, 15], mod=360)

            self.moves = 0
            self.completed = False
            self.message = "Подстройте амплитуды и фазы к целевой волне."

            self._config = {
                "harmonics": self.harmonics,
                "amp_step": self.amp_step,
                "phase_step": self.phase_step,
                "amp_tolerance": self.amp_tolerance,
                "phase_tolerance": self.phase_tolerance,
                "target_amp": list(self.target_amp),
                "target_phase": list(self.target_phase),
                "current_amp": list(self.current_amp),
                "current_phase": list(self.current_phase),
                "level_id": self.level_id,
            }

            self._refresh_completion()

        def _phase_delta(self, current, target):
            raw = abs(int(current) - int(target)) % 360
            return min(raw, 360 - raw)

        def total_error(self):
            err = 0
            for i in range(self.harmonics):
                err += abs(self.current_amp[i] - self.target_amp[i])
                err += self._phase_delta(self.current_phase[i], self.target_phase[i])
            return err

        def adjust_amp(self, idx, delta):
            if self.completed:
                return
            i = int(idx)
            if not (0 <= i < self.harmonics):
                return
            value = self.current_amp[i] + int(delta)
            self.current_amp[i] = max(0, min(100, value))
            self.moves += 1
            self._refresh_completion()

        def adjust_phase(self, idx, delta):
            if self.completed:
                return
            i = int(idx)
            if not (0 <= i < self.harmonics):
                return
            self.current_phase[i] = (self.current_phase[i] + int(delta)) % 360
            self.moves += 1
            self._refresh_completion()

        def _refresh_completion(self):
            ok = True
            for i in range(self.harmonics):
                if abs(self.current_amp[i] - self.target_amp[i]) > self.amp_tolerance:
                    ok = False
                    break
                if self._phase_delta(self.current_phase[i], self.target_phase[i]) > self.phase_tolerance:
                    ok = False
                    break

            self.completed = ok
            if ok:
                self.message = "Спектр откалиброван."
            else:
                self.message = "Суммарная ошибка: %s." % self.total_error()

        def reset(self):
            self.__init__(**copy.deepcopy(self._config))


screen spectral_calibration_screen(game):
    modal True
    tag spectral_calibration

    add Solid("#080d14ef")

    frame:
        xalign 0.5
        yalign 0.5
        background "#0f1a29f0"
        padding (20, 18)

        vbox:
            spacing 10
            xmaximum 980

            text "Спектральная калибровка" size 50 color "#f7fbff"
            text "Уровень: [game.level_id]" size 21 color "#93b8dc"
            text "Ходы: [game.moves]" size 24 color "#b6d8f7"
            text "Точность: amp ±[game.amp_tolerance], phase ±[game.phase_tolerance]" size 21 color "#c6dffc"
            text "[game.message]" size 21 color "#ffe8a6"

            for i in range(game.harmonics):
                frame:
                    background "#13243a"
                    padding (12, 10)
                    vbox:
                        spacing 5
                        text "Гармоника [i+1]" size 24 color "#eaf4ff"
                        text "Цель: amp [game.target_amp[i]] | phase [game.target_phase[i]]" size 20 color "#b9d4ec"
                        text "Текущее: amp [game.current_amp[i]] | phase [game.current_phase[i]]" size 20 color "#ffe3b8"

                        hbox:
                            spacing 8
                            textbutton "Amp -":
                                action Function(game.adjust_amp, i, -game.amp_step)
                                sensitive (not game.completed)
                                text_size 24
                            textbutton "Amp +":
                                action Function(game.adjust_amp, i, game.amp_step)
                                sensitive (not game.completed)
                                text_size 24
                            textbutton "Phase -":
                                action Function(game.adjust_phase, i, -game.phase_step)
                                sensitive (not game.completed)
                                text_size 24
                            textbutton "Phase +":
                                action Function(game.adjust_phase, i, game.phase_step)
                                sensitive (not game.completed)
                                text_size 24

            if game.completed:
                text "Успех!" size 36 color "#b6ffbe"

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


label spectral_calibration_minigame(
    level=None,
    harmonics=None,
    amp_step=None,
    phase_step=None,
    amp_tolerance=None,
    phase_tolerance=None,
    target_amp=None,
    target_phase=None,
    current_amp=None,
    current_phase=None,
):
    $ _spectral_cfg = spectral_calibration_resolve_level(
        level=level,
        harmonics=harmonics,
        amp_step=amp_step,
        phase_step=phase_step,
        amp_tolerance=amp_tolerance,
        phase_tolerance=phase_tolerance,
        target_amp=target_amp,
        target_phase=target_phase,
        current_amp=current_amp,
        current_phase=current_phase,
    )
    $ _spectral_game = SpectralCalibrationGame(**_spectral_cfg)
    call screen spectral_calibration_screen(_spectral_game)
    return _return


label test_spectral_calibration_minigame:
    scene black
    with fade
    "Тест мини-игры: спектральная калибровка."
    call spectral_calibration_minigame(level="standard")
    if _return:
        "Калибровка выполнена."
    else:
        "Выход из теста."
    return
