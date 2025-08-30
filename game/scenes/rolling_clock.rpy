init -2 python:
    import datetime
    DIGIT_STRINGS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    DEFAULT_POWERS = (4.0, 3.0, 2.5, 2.0, 1.5, 1.0)
    DIGITS_BY_INDEX = (
        tuple(range(0, 3)),   # h1: 0..2
        tuple(range(0, 10)),  # h2: 0..9
        tuple(range(0, 6)),   # m1: 0..5
        tuple(range(0, 10)),  # m2: 0..9
        tuple(range(0, 6)),   # s1: 0..5
        tuple(range(0, 10)),  # s2: 0..9
    )
    DIGITS_STR_BY_INDEX = tuple(tuple(DIGIT_STRINGS[v] for v in seq) for seq in DIGITS_BY_INDEX)
    DIGIT_VALUE_TO_INDEX = tuple({v: idx for idx, v in enumerate(seq)} for seq in DIGITS_BY_INDEX)

    def time_to_digits(t):
        if t is None:
            now = datetime.datetime.now()
            h, m, s = now.hour, now.minute, now.second
        elif isinstance(t, (tuple, list)) and len(t) == 3:
            h, m, s = map(int, t)
        elif isinstance(t, str):
            parts = t.strip().split("/")
            if len(parts) != 3:
                raise Exception("time must be 'HH/MM/SS'")
            h, m, s = map(int, parts)
        else:
            raise Exception("Unsupported time format")
        h = max(0, min(23, int(h)))
        m = max(0, min(59, int(m)))
        s = max(0, min(59, int(s)))
        return [h // 10, h % 10, m // 10, m % 10, s // 10, s % 10]

    def time_to_seconds(t):
        if t is None:
            now = datetime.datetime.now()
            return now.hour*3600 + now.minute*60 + now.second
        elif isinstance(t, (tuple, list)) and len(t) == 3:
            h, m, s = map(int, t)
        elif isinstance(t, str):
            if ":" in t:
                parts = t.strip().split(":")
                if len(parts) != 3:
                    raise Exception("time must be 'HH:MM:SS'")
                h, m, s = map(int, parts)
            elif "/" in t:
                parts = t.strip().split("/")
                if len(parts) != 3:
                    raise Exception("time must be 'HH/MM/SS'")
                h, m, s = map(int, parts)
            else:
                raise Exception("Unsupported time format")
        else:
            raise Exception("Unsupported time format")
        h = max(0, min(23, int(h)))
        m = max(0, min(59, int(m)))
        s = max(0, min(59, int(s)))
        return (h*3600 + m*60 + s) % 86400

    def digits_from_seconds(sec):
        sec %= 86400
        h, rem = divmod(sec, 3600)
        m, s = divmod(rem, 60)
        return [h // 10, h % 10, m // 10, m % 10, s // 10, s % 10]

    def tick_progress(state, duration, delay, step):
        acc = state.get("acc", 0.0) + float(step)
        state["acc"] = acc
        if acc < delay:
            p = 0.0
        else:
            p = (acc - delay) / float(duration)
            if p > 1.0:
                p = 1.0
        state["p"] = p

    def tick_live(state):
        tsec = state.get("tsec", 0)
        state["prev"] = digits_from_seconds(tsec)
        state["tsec"] = (tsec + 1) % 86400

    def make_progress_fn(state, y_base, steps_total, cell_h, direction="forward", power=1.0):
        sign = 1.0 if direction == "forward" else -1.0
        steps_total = float(steps_total)
        cell_h = float(cell_h)
        pw = max(0.1, float(power))
        def _fn(trans, st, at):
            u = float(state.get("p", 0.0))
            if u < 0.0:
                u = 0.0
            if u > 1.0:
                u = 1.0
            u_i = u ** pw
            trans.yoffset = y_base - sign * steps_total * u_i * cell_h
            if u >= 1.0:
                trans.yoffset = int(round(trans.yoffset / cell_h)) * cell_h
                return None
            return 0
        return _fn

transform odom(fn):
    subpixel True
    function fn

transform rolltick(y0=0, y1=0, dur=0.2):
    subpixel True
    yoffset y0
    ease dur yoffset y1

screen rolling_clock(
        start_time=None,
        end_time=None,
        direction="forward",
        duration=3.0,
        delay=0.0,
        size=(150, 160),
        gap=10,
        pad=20,
        bg="#222",
        color="#f31010",
        powers=(4.0, 3.0, 2.5, 2.0, 1.5, 1.0),
        live=True,
        tick_period=1.0,
        tick_anim=0.20,
        xalign=0.5,
        yalign=0.5,
        colons=True,
        colon_w=None,
        colon_size=None
    ):

    $ digit_w, digit_h = int(size[0]), int(size[1])
    $ font_size = int(digit_h * 0.7)

    $ start_digits = time_to_digits(start_time)
    $ end_digits = time_to_digits(end_time if end_time is not None else start_time)

    $ colon_w = int(digit_w * 0.35) if colon_w is None else int(colon_w)
    $ colon_size = int(font_size * 0.9) if colon_size is None else int(colon_size)
    $ colon_count = 2 if colons else 0

    $ clock_w = 6 * digit_w + (5 + colon_count) * gap + colon_count * colon_w + 2 * pad
    $ clock_h = digit_h + 2 * pad

    $ repeat_cycles = 4
    $ digits_len_list = [repeat_cycles * len(DIGITS_BY_INDEX[j]) for j in range(6)]
    $ digits_half_list = [l // 2 for l in digits_len_list]

    default state = {"acc": 0.0, "p": 0.0, "tsec": time_to_seconds(end_time if end_time is not None else start_time), "prev": end_digits}

    if state["p"] < 1.0:
        timer 0.016 repeat True action Function(tick_progress, state, duration, delay, 0.016)

    if live and state["p"] >= 1.0:
        timer tick_period repeat True action Function(tick_live, state)

    fixed:
        xalign xalign
        yalign yalign
        xsize clock_w
        ysize clock_h

        frame:
            xsize clock_w
            ysize clock_h
            background Solid(bg)
            padding (pad, pad, pad, pad)

            $ in_live = (live and state["p"] >= 1.0)
            $ prev_digits = state["prev"]
            $ curr_digits = digits_from_seconds(state["tsec"]) if in_live else None
            $ is_seq = isinstance(powers, (list, tuple))
            $ resolved_powers = [float(powers[j]) if is_seq else DEFAULT_POWERS[j] for j in range(6)]

            hbox:
                spacing gap

                for i in range(6):
                    $ sd = start_digits[i]
                    $ ed = end_digits[i]
                    $ steps_len = len(DIGITS_BY_INDEX[i])
                    $ sd_idx = DIGIT_VALUE_TO_INDEX[i][sd]
                    $ ed_idx = DIGIT_VALUE_TO_INDEX[i][ed]
                    $ diff = ((ed_idx - sd_idx) % steps_len) if direction == "forward" else ((sd_idx - ed_idx) % steps_len)
                    $ steps_total = diff
                    $ base_digit = sd if not in_live else prev_digits[i]
                    $ base_digit_idx = DIGIT_VALUE_TO_INDEX[i][base_digit]
                    $ base_index = digits_half_list[i] + base_digit_idx
                    $ y0 = -base_index * digit_h

                    fixed:
                        xsize digit_w
                        ysize digit_h
                        clipping True

                        if not in_live:
                            $ pw = resolved_powers[i]
                            $ fn = make_progress_fn(state, y0, steps_total, digit_h, direction, pw)
                            vbox at odom(fn):
                                spacing 0
                                for cycle_idx in range(repeat_cycles):
                                    for val_str in DIGITS_STR_BY_INDEX[i]:
                                        frame:
                                            xsize digit_w
                                            ysize digit_h
                                            background None
                                            text val_str size font_size color color xalign 0.5 yalign 0.5 font gui.interface_text_font
                        else:
                            $ d = (DIGIT_VALUE_TO_INDEX[i][curr_digits[i]] - DIGIT_VALUE_TO_INDEX[i][prev_digits[i]]) % steps_len
                            $ y1 = - (base_index + d) * digit_h
                            vbox at rolltick(y0, y1, tick_anim):
                                spacing 0
                                for cycle_idx in range(repeat_cycles):
                                    for val_str in DIGITS_STR_BY_INDEX[i]:
                                        frame:
                                            xsize digit_w
                                            ysize digit_h
                                            background None
                                            text val_str size font_size color color xalign 0.5 yalign 0.5 font gui.interface_text_font

                    if colons and (i == 1 or i == 3):
                        fixed:
                            xsize colon_w
                            ysize digit_h
                            text ":" size colon_size color color xalign 0.5 yalign 0.5 font gui.interface_text_font

screen hud_with_clock():
    use rolling_clock(
        start_time="22/43/56",
        end_time="07/59/55",
        direction="backward",
        duration=2,
        delay=0.0
    )

screen hud_with_clock1(start_time="22/43/56"):
    use rolling_clock(
        start_time=start_time,
        end_time="07/59/55",
        direction="backward",
        duration=5,
        delay=0.0
    )

label test_clock(start_time="22/43/00"):
    #scene black
    show screen hud_with_clock1(start_time=start_time)
    $ renpy.pause(6.3, hard=True)
    play sfx sfx_tik_tak loop
    $ renpy.pause(4.7, hard=True)
    stop sfx
    hide screen hud_with_clock1 with dissolve
    $ renpy.pause(0.5, hard=True)
    return
