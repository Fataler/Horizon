image arrow_0_0 = "CG/CG_Clock/Arrow (11).png"

image arrow_0_5 = "CG/CG_Clock/Arrow (12).png"

image arrow_1_0 = "CG/CG_Clock/Arrow (13).png"

image arrow_1_5 = "CG/CG_Clock/Arrow (14).png"

image arrow_2_0 = "CG/CG_Clock/Arrow (15).png"

image arrow_2_5 = "CG/CG_Clock/Arrow (16).png"

image arrow_3_0 = "CG/CG_Clock/Arrow (17).png"

image arrow_3_5 = "CG/CG_Clock/Arrow (18).png"

image arrow_4_0 = "CG/CG_Clock/Arrow (19).png"

image arrow_4_5 = "CG/CG_Clock/Arrow (20).png"

image arrow_5_0 = "CG/CG_Clock/Arrow (21).png"

image arrow_5_5 = "CG/CG_Clock/Arrow (22).png"

image arrow_6_0 = "CG/CG_Clock/Arrow (23).png"

image arrow_6_5 = "CG/CG_Clock/Arrow (24).png"

image arrow_7_0 = "CG/CG_Clock/Arrow (1).png"
    
image arrow_7_5 = "CG/CG_Clock/Arrow (2).png"

image arrow_8_0 = "CG/CG_Clock/Arrow (3).png"

image arrow_8_5 = "CG/CG_Clock/Arrow (4).png"

image arrow_9_0 = "CG/CG_Clock/Arrow (5).png"

image arrow_9_5 = "CG/CG_Clock/Arrow (6).png"

image arrow_10_0 = "CG/CG_Clock/Arrow (7).png"

image arrow_10_5 = "CG/CG_Clock/Arrow (8).png"

image arrow_11_0 = "CG/CG_Clock/Arrow (9).png"

image arrow_11_5 = "CG/CG_Clock/Arrow (10).png"

image cklock_cherkash = At("CG/CG_Clock/cherkash.png", soot_drift_bottom(speed=0.8, amplitude= -2, x_amplitude=2, zoom=1.01))

image cklock_effect = At("CG/CG_Clock/effect.png", soot_drift_bottom(speed=0.8, amplitude= 2, x_amplitude=-2, zoom=1.01))

image cklock_fon = "CG/CG_Clock/fon.png"
image clock_base = "CG/CG_Clock/clock_bg.png"

image cklock_black_arrow = "CG/CG_Clock/Black_arrow.png"


init python:
    def normalize_hour(hour):
        try:
            return int(hour) % 12
        except Exception:
            return 0

    def minute_to_half_and_carry(minute):
        try:
            m = int(minute)
        except Exception:
            m = 0
        m = m % 60
        if m < 15:
            return 0, 0
        elif m < 45:
            return 5, 0
        else:
            return 0, 1

    def minute_to_half(minute):
        half, _ = minute_to_half_and_carry(minute)
        return half

    try:
        string_types = (basestring,)
    except NameError:
        string_types = (str,)

    def parse_clock_time(value):
        if isinstance(value, (tuple, list)) and len(value) == 2:
            hour = normalize_hour(value[0])
            half, carry = minute_to_half_and_carry(value[1])
            hour = normalize_hour(hour + carry)
            return hour, half
        if isinstance(value, int):
            return normalize_hour(value), 0
        if isinstance(value, string_types):
            text = value.strip()
            if ":" in text:
                parts = text.split(":", 1)
                hour = normalize_hour(parts[0])
                try:
                    minute = int(parts[1])
                except Exception:
                    minute = 0
                half, carry = minute_to_half_and_carry(minute)
                hour = normalize_hour(hour + carry)
                return hour, half
            return normalize_hour(text), 0
        return 0, 0

    def clock_index(hour, half):
        hour = normalize_hour(hour)
        return hour * 2 + (1 if half == 5 else 0)

    def index_to_image_name(index24):
        idx = int(index24) % 24
        hour = idx // 2
        half = 5 if (idx % 2) == 1 else 0
        return "arrow_%d_%d" % (hour, half)

    def build_clock_sequence(from_value, to_value, include_end=True, clockwise=True):
        from_hour, from_half = parse_clock_time(from_value)
        to_hour, to_half = parse_clock_time(to_value)
        start = clock_index(from_hour, from_half)
        end = clock_index(to_hour, to_half)

        if clockwise:
            step = 1
            distance = (end - start) % 24
        else:
            step = -1
            distance = (start - end) % 24

        steps = distance + (1 if include_end else 0)
        sequence = []
        current = start
        for s in range(steps):
            sequence.append(index_to_image_name(current))
            current = (current + step) % 24
        return sequence

    def build_clock_sequence_by_hours(start_value, hours_to_move, include_end=True):
        start_hour, start_half = parse_clock_time(start_value)
        start_idx = clock_index(start_hour, start_half)
        try:
            delta_hours = float(hours_to_move)
        except Exception:
            delta_hours = 0.0
        steps = int(round(delta_hours * 2.0))
        if steps == 0:
            return [index_to_image_name(start_idx)] if include_end else []
        direction = 1 if steps > 0 else -1
        steps_abs = abs(steps)
        sequence = []
        current = start_idx
        total_frames = steps_abs + 1 if include_end else steps_abs
        for i in range(total_frames):
            sequence.append(index_to_image_name(current))
            current = (current + direction) % 24
        return sequence


label scene_clock:
    show screen clock_screen() onlayer master
    with dissolve

    
    cutscene "Но движутся… В обратную сторону?"
    hide screen clock_screen
    with dissolve
    pause 1.0
    return


transform clock_screen_fade(fade_in=0.3, fade_out=0.3):
    on show:
        alpha 0.0
        linear fade_in alpha 1.0
    on hide:
        linear fade_out alpha 0.0


screen clock_screen(from_time=(18, 0), 
                    hours_to_move=-12, 
                    delay=0.8, 
                    include_end=True,
                    auto_hide=False,
                    loop=False
):
    layer "master"
    tag clock_screen

    default seq = build_clock_sequence_by_hours(from_time, hours_to_move, include_end=include_end)
    default step_index = 0
    default finished = False

    fixed at clock_screen_fade(0.3, 0.3):
        add "cklock_fon"
        add "cklock_effect" at truecenter
        add "clock_base"
        add "cklock_black_arrow"
        add "cklock_cherkash" at truecenter

        if seq:
            add seq[step_index]

    if seq and not finished:
        timer delay repeat True action If(
            loop or step_index < len(seq) - 1,
            true=SetScreenVariable("step_index", (step_index + 1) % len(seq) if loop else step_index + 1),
            false=[SetScreenVariable("finished", True), If(auto_hide, true=[Hide("clock_screen"), Return(True)], false=Return(True))])