init -2 python:
    import datetime

    def time_to_digits(t):
        if t is None:
            now = datetime.datetime.now()
            h, m, s = now.hour, now.minute, now.second
        elif isinstance(t, (tuple, list)) and len(t) == 3:
            h, m, s = map(int, t)
        elif isinstance(t, str):
            parts = t.strip().split(":")
            if len(parts) != 3:
                raise Exception("time must be 'HH:MM:SS'")
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
            parts = t.strip().split(":")
            if len(parts) != 3:
                raise Exception("time must be 'HH:MM:SS'")
            h, m, s = map(int, parts)
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
    function fn

transform rolltick(y0=0, y1=0, dur=0.2):
    yoffset y0
    linear dur yoffset y1

screen rolling_clock(
        start_time=None,
        end_time=None,
        direction="forward",
        duration=3.0,
        delay=0.0,
        size=(80, 90),
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

    $ repeat_cycles = 40
    $ digits_total = repeat_cycles * 10

    default state = {"acc": 0.0, "p": 0.0, "tsec": time_to_seconds(end_time if end_time is not None else start_time), "prev": end_digits}

    if state["p"] < 1.0:
        timer 0.02 repeat True action Function(tick_progress, state, duration, delay, 0.02)

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

            hbox:
                spacing gap

                for i in range(6):
                    $ sd = start_digits[i]
                    $ ed = end_digits[i]
                    $ diff = ((ed - sd) % 10) if direction == "forward" else ((sd - ed) % 10)
                    $ steps_total = diff
                    $ base_index = (digits_total // 2) + (sd if not in_live else state["prev"][i])
                    $ y0 = -base_index * digit_h

                    fixed:
                        xsize digit_w
                        ysize digit_h
                        clipping True

                        if not in_live:
                            $ pw = float(powers[i]) if isinstance(powers, (list, tuple)) else (
                                4.0 if i==0 else 3.0 if i==1 else 2.5 if i==2 else 2.0 if i==3 else 1.5 if i==4 else 1.0)
                            $ fn = make_progress_fn(state, y0, steps_total, digit_h, direction, pw)
                            vbox at odom(fn):
                                spacing 0
                                for cycle_idx in range(repeat_cycles):
                                    for val in range(10):
                                        frame:
                                            xsize digit_w
                                            ysize digit_h
                                            background None
                                            text str(val) size font_size color color xalign 0.5 yalign 0.5
                        else:
                            $ curr = digits_from_seconds(state["tsec"])
                            $ d = (curr[i] - state["prev"][i]) % 10
                            $ y1 = - (base_index + d) * digit_h
                            vbox at rolltick(y0, y1, tick_anim):
                                spacing 0
                                for cycle_idx in range(repeat_cycles):
                                    for val in range(10):
                                        frame:
                                            xsize digit_w
                                            ysize digit_h
                                            background None
                                            text str(val) size font_size color color xalign 0.5 yalign 0.5

                    if colons and (i == 1 or i == 3):
                        fixed:
                            xsize colon_w
                            ysize digit_h
                            text ":" size colon_size color color xalign 0.5 yalign 0.5

screen hud_with_clock():
    use rolling_clock(
        start_time="22:43:56",
        end_time="08:39:57",
        direction="backward",
        duration=2,
        delay=0.0
    )

label test_clock:
    scene black
    show screen hud_with_clock
    "Часеки"
    pause
    return
