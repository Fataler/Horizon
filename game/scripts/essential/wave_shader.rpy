init -1 python:
    from renpy.uguu import GL_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT, GL_REPEAT

    renpy.register_shader(
        "watt.wave",
        variables="""
        uniform float u_shader_time;
        uniform vec2 u_wave_period;   // radians factor per axis
        uniform vec2 u_wave_amp;      // amplitude in percents of UV (scaled by 0.01)
        uniform vec2 u_wave_speed;    // time multiplier per axis
        uniform float u_direction;    // 0 both, 1 horizontal(X by Y), 2 vertical(Y by X), <0 off
        uniform vec2 u_damp;          // pow base per-line damping (X by y, Y by x)
        uniform float u_double_use;   // 0.0 off, >0.0 on
        uniform float u_double_mix;   // mix factor for second sample

        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
        """,
        vertex_200="""
        v_coords = a_tex_coord;
        """,
        fragment_300="""
        vec2 damp = vec2(1.0, 1.0);

        if (u_damp.x != 1.0) {
            damp.x = pow(max(u_damp.x, 0.00001), v_coords.y * u_model_size.y);
        }
        if (u_damp.y != 1.0) {
            damp.y = pow(max(u_damp.y, 0.00001), v_coords.x * u_model_size.x);
        }

        vec2 wave_offset = vec2(0.0);
        if (u_direction < 2.0) {
            wave_offset.x = sin(u_wave_period.x * (v_coords.y + u_shader_time * u_wave_speed.x)) * u_wave_amp.x * 0.01 * damp.x;
        }
        if (u_direction < 1.0 || u_direction >= 2.0) {
            wave_offset.y = sin(u_wave_period.y * (v_coords.x + u_shader_time * u_wave_speed.y)) * u_wave_amp.y * 0.01 * damp.y;
        }

        vec2 pos0 = v_coords + wave_offset;
        vec4 col0 = texture2D(tex0, pos0);

        if (u_double_use <= 0.0) {
            gl_FragColor = col0;
        } else {
            vec2 pos1 = v_coords - wave_offset; // opposite sample for subtle ghost
            vec4 col1 = texture2D(tex0, pos1);
            gl_FragColor = mix(col0, col1, clamp(u_double_mix, 0.0, 1.0));
        }
        """
    )

    def advance_shader_time(trans, st, at):
        trans.u_shader_time = at
        return 0

    class WaveShader(object):
        def __init__(
            self,
            amp=12.0,
            period=20.0,
            speed=1.0,
            direction="both",
            damp=1.0,
            double=None,
            double_mix=0.5,
            repeat=None,
        ):
            direction_map = {
                "both": 0.0,
                "horizontal": 1.0, "x": 1.0,
                "vertical": 2.0,   "y": 2.0,
                None: -1.0,
            }
            wrap_map = {
                "clamp": GL_CLAMP_TO_EDGE,
                "mirrored": GL_MIRRORED_REPEAT,
                "mirror": GL_MIRRORED_REPEAT,
                "repeat": GL_REPEAT,
            }

            def to_vec2(value):
                if isinstance(value, (int, float)):
                    return (float(value), float(value))
                return (float(value[0]), float(value[1]))

            self.period = to_vec2(period)
            self.amp = to_vec2(amp)
            self.speed = to_vec2(speed)
            if isinstance(direction, str):
                self.dir = direction_map.get(direction.lower(), 0.0)
            else:
                self.dir = float(direction) if direction is not None else 0.0
            self.damp = to_vec2(damp)

            self.double_use = 1.0 if double is not None and double is not False else 0.0
            self.double_mix = float(double_mix)

            self.repeat = None
            if isinstance(repeat, str):
                w = wrap_map.get(repeat)
                if w is not None:
                    self.repeat = (w, w)
            elif isinstance(repeat, tuple) and len(repeat) == 2:
                w0 = wrap_map.get(repeat[0])
                w1 = wrap_map.get(repeat[1])
                if w0 is not None and w1 is not None:
                    self.repeat = (w0, w1)

            self.first_time = True

        def __call__(self, trans, st, at):
            if self.first_time or trans.shader != "watt.wave":
                trans.shader = "watt.wave"
                trans.mesh = True
                trans.u_shader_time = 0.0
                trans.u_wave_period = self.period
                trans.u_wave_amp = self.amp
                trans.u_wave_speed = self.speed
                trans.u_direction = self.dir
                trans.u_damp = self.damp
                trans.u_double_use = self.double_use
                trans.u_double_mix = self.double_mix
                if self.repeat is not None:
                    trans.gl_texture_wrap = self.repeat
                self.first_time = False
            return advance_shader_time(trans, st, at)

