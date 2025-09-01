define wave_color_left = "#ffffff"
define wave_color_mid = "#00d9ff"
define wave_color_right = "#0019fd"

init python:
    import math

    def hex_to_rgb(hex_code):
        hex_code = hex_code.lstrip('#')
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return (r, g, b)

    def rgb_to_hex(r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def grad_color(index, bars):
        stops = [
            (0.00, hex_to_rgb(wave_color_left)),
            (0.20, hex_to_rgb(wave_color_mid)),
            (0.40, hex_to_rgb(wave_color_right)),
            (0.60, hex_to_rgb(wave_color_right)),
            (0.80, hex_to_rgb(wave_color_mid)),
            (1.00, hex_to_rgb(wave_color_left)),
        ]
        if bars <= 1:
            x = 0.0
        else:
            x = index / float(bars - 1)

        pt, pc = stops[0]
        for t, c in stops[1:]:
            if x <= t:
                k = 0 if t == pt else (x - pt) / (t - pt)
                r = int(pc[0] + (c[0] - pc[0]) * k)
                g = int(pc[1] + (c[1] - pc[1]) * k)
                b = int(pc[2] + (c[2] - pc[2]) * k)
                return rgb_to_hex(r, g, b)
            pt, pc = t, c
        r, g, b = stops[-1][1]
        return rgb_to_hex(r, g, b)

    def hash01(i, j, seed):
        x = (i * 19940609) ^ (j * 19970215) ^ (seed * 19940708)
        x = (x ^ (x >> 13)) * 20250901
        x = (x ^ (x >> 16)) & 0xFFFFFFFF
        return (x % 10000) / 10000.0

    def wave_height(index, time_sec, bars, base, max_height, bpm, seed):
        center = (bars - 1) / 2.0
        d = abs(index - center) / (center if center else 1.0)
        envelope = max(0.0, 1.0 - d**1.7)

        v1 = 0.55 * (math.sin(time_sec * 2.2 + index * 0.23) * 0.5 + 0.5)
        v2 = 0.30 * (math.sin(time_sec * 1.3 - index * 0.37) * 0.5 + 0.5)
        v3 = 0.15 * (math.sin(time_sec * 3.7 + index * 0.11) * 0.5 + 0.5)
        v = v1 + v2 + v3

        step = int(time_sec * 4.0)
        v = min(1.0, v + hash01(index, step, seed) * 0.25)

        if bpm:
            beat_hz = bpm / 60.0
            beat_phase = (time_sec * beat_hz) % 1.0
            pulse_width = 0.15
            pulse = max(0.0, 1.0 - abs(d - beat_phase) / pulse_width)
            v = v * 0.75 + pulse * 0.9

        h = base + envelope * max_height * max(0.0, min(1.0, v))
        return max(1, int(h))

screen waveform_show(
    bars=104,
    width=None,
    height=360,
    bar_w=9,
    gap=6,
    base=10,
    max_h=220,
    bpm=0,
    speed=3.0,
    glow_px=10,
    seed=1,
    yalign_val=0.5
):
    layer "master"
    zorder 10
    
    default viewport_w = width if width is not None else config.screen_width
    default time_sec = 0.0
    
    timer 0.016 repeat True action SetScreenVariable("time_sec", time_sec + 0.016 * speed)


    $ total_w = bars * bar_w + (bars - 1) * gap
    $ x0 = (viewport_w - total_w) / 2.0

    fixed:
        xysize (viewport_w, height)
        align (0.5, yalign_val)

        for index in range(bars):
            $ h = wave_height(index, time_sec, bars, base, max_h, bpm, seed)
            $ col = grad_color(index, bars)
            $ x = int(x0 + index * (bar_w + gap))
            $ y = int((height - h) / 2)

            if glow_px > 0:
                add Solid(col + "40") xysize (bar_w + glow_px, h) xpos (x - glow_px // 2) ypos y
            add Solid(col) xysize (bar_w, h) xpos x ypos y

label wave_demo:
    show screen waveform_show()
    "Пу-пу-пу"
    hide screen waveform_show
    return
