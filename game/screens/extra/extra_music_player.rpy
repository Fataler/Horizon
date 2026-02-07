default extra_music_index = 0
default extra_music_is_playing = False
default extra_music_paused = False
default extra_music_last_pos = 0.0
default extra_music_start_offset = 0.0
default extra_music_clock_anchor = 0.0
default extra_music_duck_active = False
default extra_music_prev_paused = False
default extra_music_prev_playing = False
default extra_music_prev_track = None
default extra_music_prev_pos = 0.0

define EXTRA_MUSIC_CHANNEL = "music_player"
define EXTRA_MUSIC_MIXER = "music_player_mixer"

init python:
    import time

    def _extra_track(title, subtitle, file_path, duration, palette, pulse, viz_dense, viz_wide):
        return {
            "title": title,
            "subtitle": subtitle,
            "file": file_path,
            "duration": float(duration),
            "palette": palette,
            "pulse": pulse,
            "viz_dense": viz_dense,
            "viz_wide": viz_wide,
        }

    try:
        renpy.music.register_channel(
            EXTRA_MUSIC_CHANNEL,
            mixer=EXTRA_MUSIC_MIXER,
            loop=False,
            stop_on_mute=True,
            tight=True,
            buffer_queue=True,
        )
    except Exception:
        pass

    extra_music_tracks = [
        _extra_track(
            "Alone in the Space", "Тема главного меню", "audio/bg/Menu/Alone_in_the_space_edit.mp3", 259.272,
            [(0.0, "#ffd166"), (0.55, "#ff6b35"), (1.0, "#ff0033")], "#ff6b3520",
            {"bands": 64, "smoothing": 0.30, "gamma": 0.34, "glow_px": 10},
            {"bands": 20, "smoothing": 0.58, "gamma": 0.52, "glow_px": 14},
        ),
        _extra_track(
            "Theme 5 Day", "Финальный день", "audio/bg/Theme_5day.mp3", 46.704,
            [(0.0, "#a7f3ff"), (0.5, "#5bbcff"), (1.0, "#1d4ed8")], "#5bbcff24",
            {"bands": 62, "smoothing": 0.26, "gamma": 0.32, "glow_px": 11},
            {"bands": 18, "smoothing": 0.52, "gamma": 0.48, "glow_px": 15},
        ),
        _extra_track(
            "Solar System", "Главная тема", "audio/bg/Main_Themes/SolarSystem.mp3", 391.632,
            [(0.0, "#fef08a"), (0.5, "#f97316"), (1.0, "#ef4444")], "#f9731624",
            {"bands": 66, "smoothing": 0.28, "gamma": 0.33, "glow_px": 10},
            {"bands": 22, "smoothing": 0.56, "gamma": 0.50, "glow_px": 14},
        ),
        _extra_track(
            "In the Mirror", "Сомнения и тревога", "audio/bg/Main_Themes/In_the_mirror.mp3", 312.168,
            [(0.0, "#c7f9cc"), (0.5, "#38b000"), (1.0, "#14532d")], "#38b00024",
            {"bands": 64, "smoothing": 0.34, "gamma": 0.36, "glow_px": 9},
            {"bands": 18, "smoothing": 0.60, "gamma": 0.54, "glow_px": 13},
        ),
        _extra_track(
            "Daily", "Повседневный ритм", "audio/bg/Main_Themes/Daily.mp3", 183.144,
            [(0.0, "#e9d5ff"), (0.5, "#a855f7"), (1.0, "#6d28d9")], "#a855f724",
            {"bands": 60, "smoothing": 0.27, "gamma": 0.31, "glow_px": 10},
            {"bands": 18, "smoothing": 0.50, "gamma": 0.46, "glow_px": 14},
        ),
        _extra_track(
            "Light", "Редкий свет", "audio/bg/Main_Themes/Light.mp3", 57.720,
            [(0.0, "#fef9c3"), (0.5, "#facc15"), (1.0, "#f59e0b")], "#facc1520",
            {"bands": 58, "smoothing": 0.25, "gamma": 0.30, "glow_px": 11},
            {"bands": 16, "smoothing": 0.48, "gamma": 0.44, "glow_px": 15},
        ),
        _extra_track(
            "Reflections", "Внутренний монолог", "audio/bg/Anxiety/reflections.mp3", 303.792,
            [(0.0, "#bae6fd"), (0.5, "#0ea5e9"), (1.0, "#1e3a8a")], "#0ea5e924",
            {"bands": 64, "smoothing": 0.33, "gamma": 0.35, "glow_px": 9},
            {"bands": 20, "smoothing": 0.57, "gamma": 0.51, "glow_px": 13},
        ),
        _extra_track(
            "Make This Right", "Точка выбора", "audio/bg/Choices/Make_this_right.mp3", 11.664,
            [(0.0, "#fecaca"), (0.5, "#f87171"), (1.0, "#b91c1c")], "#f8717128",
            {"bands": 54, "smoothing": 0.22, "gamma": 0.28, "glow_px": 12},
            {"bands": 14, "smoothing": 0.44, "gamma": 0.42, "glow_px": 16},
        ),
        _extra_track(
            "Escape Room Full", "Побег", "audio/bg/Escape_room/Escape_room_full.mp3", 300.663,
            [(0.0, "#bbf7d0"), (0.5, "#22c55e"), (1.0, "#166534")], "#22c55e24",
            {"bands": 68, "smoothing": 0.31, "gamma": 0.34, "glow_px": 10},
            {"bands": 22, "smoothing": 0.58, "gamma": 0.53, "glow_px": 13},
        ),
        _extra_track(
            "Fight", "Столкновение", "audio/bg/Action/Fight.mp3", 151.128,
            [(0.0, "#fde68a"), (0.5, "#f97316"), (1.0, "#dc2626")], "#f9731628",
            {"bands": 70, "smoothing": 0.24, "gamma": 0.30, "glow_px": 12},
            {"bands": 24, "smoothing": 0.50, "gamma": 0.45, "glow_px": 16},
        ),
        _extra_track(
            "Theme Cosmos", "Космос", "audio/bg/CG_cosmos/Theme_cosmos.mp3", 172.080,
            [(0.0, "#e0e7ff"), (0.5, "#60a5fa"), (1.0, "#1d4ed8")], "#60a5fa22",
            {"bands": 66, "smoothing": 0.29, "gamma": 0.33, "glow_px": 10},
            {"bands": 20, "smoothing": 0.55, "gamma": 0.49, "glow_px": 14},
        ),
        _extra_track(
            "Epilogue", "Эпилог", "audio/bg/Endings/Epilogue.mp3", 245.088,
            [(0.0, "#f5d0fe"), (0.5, "#e879f9"), (1.0, "#db2777")], "#e879f922",
            {"bands": 62, "smoothing": 0.32, "gamma": 0.35, "glow_px": 9},
            {"bands": 18, "smoothing": 0.60, "gamma": 0.54, "glow_px": 13},
        ),
    ]

    def extra_normalize_audio_id(audio_id):
        if isinstance(audio_id, (list, tuple)):
            return audio_id[0] if audio_id else None
        return audio_id

    def extra_track_data(index=None):
        if not extra_music_tracks:
            return None
        if index is None:
            index = extra_music_index
        index = max(0, min(index, len(extra_music_tracks) - 1))
        return extra_music_tracks[index]

    def extra_track_duration(track=None):
        if track is None:
            track = extra_track_data()
        if not track:
            return 0.0
        try:
            return max(0.0, float(track.get("duration", 0.0)))
        except Exception:
            return 0.0

    def extra_format_time(seconds):
        seconds = int(max(0.0, float(seconds)))
        return "{:02d}:{:02d}".format(seconds // 60, seconds % 60)

    def extra_total_time_text(track=None):
        duration = extra_track_duration(track)
        if duration <= 0.0:
            return "--:--"
        return extra_format_time(duration)

    def extra_with_offset(path, offset):
        if not isinstance(path, str):
            return path
        if path.lstrip().startswith("<"):
            return path
        if offset <= 0.02:
            return path
        return "<from {:.3f}>{}".format(offset, path)

    def extra_sync_position():
        global extra_music_last_pos, extra_music_clock_anchor
        if extra_music_is_playing and (not extra_music_paused):
            if extra_music_clock_anchor <= 0.0:
                extra_music_clock_anchor = time.monotonic()
            elapsed = max(0.0, time.monotonic() - float(extra_music_clock_anchor))
            pos = float(extra_music_start_offset) + elapsed
            duration = extra_track_duration()
            if duration > 0.0:
                pos = pos % duration
            extra_music_last_pos = max(0.0, pos)
        return extra_music_last_pos

    def extra_select_track(index, refresh=True):
        global extra_music_index, extra_music_last_pos, extra_music_start_offset
        if not extra_music_tracks:
            return
        extra_music_index = max(0, min(index, len(extra_music_tracks) - 1))
        if (not extra_music_is_playing) and (not extra_music_paused):
            extra_music_last_pos = 0.0
            extra_music_start_offset = 0.0
        if refresh:
            renpy.restart_interaction()

    def extra_play_selected(start_pos=0.0, refresh=True, keep_paused=False):
        global extra_music_is_playing, extra_music_paused, extra_music_last_pos, extra_music_start_offset
        global extra_music_clock_anchor
        track = extra_track_data()
        if track is None:
            return

        start_pos = max(0.0, float(start_pos))
        duration = extra_track_duration(track)
        if duration > 0.0:
            start_pos = min(start_pos, duration)

        play_arg = extra_with_offset(track["file"], start_pos)
        renpy.music.play(play_arg, channel=EXTRA_MUSIC_CHANNEL, loop=True, fadein=0.12)

        extra_music_is_playing = True
        extra_music_paused = False
        extra_music_start_offset = start_pos
        extra_music_last_pos = start_pos
        extra_music_clock_anchor = time.monotonic()

        if keep_paused:
            try:
                renpy.music.set_pause(True, channel=EXTRA_MUSIC_CHANNEL)
                extra_music_paused = True
                extra_music_last_pos = start_pos
            except Exception:
                pass

        extra_update_background_duck()

        if refresh:
            renpy.restart_interaction()

    def extra_play_track(index):
        extra_select_track(index, refresh=False)
        extra_play_selected(start_pos=0.0)

    def extra_prev_track():
        if not extra_music_tracks:
            return
        next_index = (extra_music_index - 1) % len(extra_music_tracks)
        was_active = extra_music_is_playing or extra_music_paused
        was_paused = extra_music_paused
        extra_select_track(next_index, refresh=False)
        if was_active:
            extra_play_selected(start_pos=0.0, keep_paused=was_paused)
        else:
            renpy.restart_interaction()

    def extra_next_track():
        if not extra_music_tracks:
            return
        next_index = (extra_music_index + 1) % len(extra_music_tracks)
        was_active = extra_music_is_playing or extra_music_paused
        was_paused = extra_music_paused
        extra_select_track(next_index, refresh=False)
        if was_active:
            extra_play_selected(start_pos=0.0, keep_paused=was_paused)
        else:
            renpy.restart_interaction()

    def extra_toggle_playback():
        global extra_music_paused, extra_music_start_offset, extra_music_clock_anchor
        if not extra_music_is_playing:
            extra_play_selected(start_pos=extra_music_last_pos)
            return

        if extra_music_paused:
            renpy.music.set_pause(False, channel=EXTRA_MUSIC_CHANNEL)
            extra_music_start_offset = extra_music_last_pos
            extra_music_clock_anchor = time.monotonic()
            extra_music_paused = False
        else:
            extra_sync_position()
            renpy.music.set_pause(True, channel=EXTRA_MUSIC_CHANNEL)
            extra_music_paused = True

        extra_update_background_duck()
        renpy.restart_interaction()

    def extra_clamp_seek_target(target):
        target = max(0.0, float(target))
        duration = extra_track_duration()
        if duration > 0.0:
            target = min(target, duration)
        return target

    def extra_seek_absolute(target):
        global extra_music_last_pos, extra_music_start_offset, extra_music_clock_anchor
        target = extra_clamp_seek_target(target)
        was_paused = extra_music_paused

        if extra_music_is_playing or extra_music_paused:
            extra_play_selected(start_pos=target, refresh=False, keep_paused=was_paused)
        else:
            extra_music_last_pos = target
            extra_music_start_offset = target
            extra_music_clock_anchor = time.monotonic()

        renpy.restart_interaction()

    def extra_seek_relative(delta):
        base = extra_sync_position()
        extra_seek_absolute(base + float(delta))

    def extra_stop_music(refresh=True):
        global extra_music_is_playing, extra_music_paused, extra_music_last_pos, extra_music_start_offset
        global extra_music_clock_anchor
        renpy.music.stop(channel=EXTRA_MUSIC_CHANNEL, fadeout=0.15)
        extra_music_is_playing = False
        extra_music_paused = False
        extra_music_last_pos = 0.0
        extra_music_start_offset = 0.0
        extra_music_clock_anchor = 0.0
        extra_update_background_duck()
        if refresh:
            renpy.restart_interaction()

    def extra_reset_duck_snapshot():
        global extra_music_duck_active
        global extra_music_prev_playing, extra_music_prev_paused
        global extra_music_prev_track, extra_music_prev_pos

        extra_music_duck_active = False
        extra_music_prev_playing = False
        extra_music_prev_paused = False
        extra_music_prev_track = None
        extra_music_prev_pos = 0.0

    def extra_duck_background_music():
        global extra_music_duck_active
        global extra_music_prev_paused, extra_music_prev_playing
        global extra_music_prev_track, extra_music_prev_pos

        if extra_music_duck_active:
            return

        current_track = extra_normalize_audio_id(renpy.music.get_playing("music"))
        extra_music_prev_playing = bool(current_track)
        current_pos = renpy.music.get_pos("music")
        if current_pos is None or current_pos < 0:
            current_pos = 0.0

        extra_music_prev_track = current_track
        extra_music_prev_pos = float(current_pos)

        try:
            extra_music_prev_paused = renpy.music.get_pause(channel="music")
        except Exception:
            extra_music_prev_paused = False

        if extra_music_prev_playing:
            try:
                renpy.music.set_pause(True, channel="music")
            except Exception:
                pass

        extra_music_duck_active = True

    def extra_restore_background_music():
        global extra_music_prev_playing, extra_music_prev_track, extra_music_prev_pos

        if not extra_music_duck_active:
            return

        try:
            if extra_music_prev_playing:
                current_track = extra_normalize_audio_id(renpy.music.get_playing("music"))
                if (current_track is None) and extra_music_prev_track:
                    resumed = extra_with_offset(extra_music_prev_track, extra_music_prev_pos)
                    try:
                        renpy.music.play(resumed, channel="music", fadein=0.15)
                    except Exception:
                        pass

                try:
                    renpy.music.set_pause(extra_music_prev_paused, channel="music")
                except Exception:
                    pass
        finally:
            extra_reset_duck_snapshot()

    def extra_player_is_audible():
        if extra_music_paused or (not extra_music_is_playing):
            return False
        try:
            return renpy.music.is_playing(channel=EXTRA_MUSIC_CHANNEL)
        except Exception:
            return False

    def extra_update_background_duck():
        if extra_player_is_audible():
            extra_duck_background_music()
        else:
            extra_restore_background_music()


screen extra_music_player_tab(content_width=1740):
    timer 0.12 repeat True action Function(extra_update_background_duck)

    $ selected_track = extra_track_data()
    $ channel_playing = renpy.music.is_playing(channel=EXTRA_MUSIC_CHANNEL)
    if extra_music_is_playing and not channel_playing and not extra_music_paused:
        $ extra_music_is_playing = False
        $ extra_update_background_duck()

    $ playlist_width = 420 if content_width >= 1500 else 360
    $ visualizer_width = max(360, int(content_width - playlist_width - 110))
    $ visualizer_width_small = max(300, int(visualizer_width * 0.78))
    $ playlist_view_height = max(300, int(config.screen_height * 0.50))
    $ compact_controls = content_width < 1260
    $ now_height = 180 if content_width >= 1200 else 156
    $ visualizer_height = max(170, int(config.screen_height * 0.22))

    $ dense = selected_track.get("viz_dense", {}) if selected_track else {}
    $ wide = selected_track.get("viz_wide", {}) if selected_track else {}
    $ palette_points = selected_track.get("palette") if selected_track else None
    $ pulse_color = selected_track.get("pulse", "#ff000012") if selected_track else "#ff000012"

    $ playback_text = "Пауза" if channel_playing and not extra_music_paused else ("Продолжить" if extra_music_paused else "Играть")
    $ track_pos = extra_sync_position()
    $ track_duration = extra_track_duration(selected_track)
    if track_duration > 0.0:
        $ track_pos = min(track_duration, track_pos)
    $ track_time = extra_format_time(track_pos)
    $ total_time = extra_total_time_text(selected_track)
    $ track_has_duration = track_duration > 0.0
    $ track_range = track_duration if track_has_duration else 1.0
    if track_pos > track_range:
        $ track_pos = track_range
    $ track_progress = (track_pos / track_duration) if track_has_duration else 0.0
    $ track_progress_percent = int(track_progress * 100.0)
    $ bg_state_text = "Фон: приглушён" if extra_music_duck_active else "Фон: активен"

    hbox:
        spacing 18
        xfill True
        yfill True

        frame at extra_music_panel_intro:
            style "extra_playlist_frame"
            xsize playlist_width
            yfill True

            vbox:
                spacing 12
                xfill True
                text "AUDIO CONSOLE" style "extra_music_kicker"
                text "Плейлист" style "extra_music_panel_title"
                text "Выберите трек и управляйте воспроизведением в реальном времени." style "extra_music_subtle"

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_yfill False
                    xfill True
                    ysize playlist_view_height

                    vbox:
                        spacing 8
                        xfill True

                        for i, track in enumerate(extra_music_tracks):
                            textbutton ("%02d  %s\n{size=22}%s{/size}" % (i + 1, track["title"], track["subtitle"])):
                                style "extra_track_button"
                                action Function(extra_play_track, i)
                                selected i == extra_music_index

        frame at extra_music_panel_intro:
            style "extra_music_stack_frame"
            xfill True
            yfill True

            vbox:
                spacing 10
                xfill True
                yfill True

                frame:
                    style "extra_now_frame"
                    xfill True
                    ysize now_height

                    fixed:
                        xfill True
                        yfill True

                        add Solid("#8ec9ff10")
                        add Solid("#ff7a1812") at extra_music_scanline
                        add Solid(pulse_color) at extra_now_glow

                        hbox:
                            spacing 30
                            xfill True

                            vbox:
                                spacing 4
                                text "NOW STREAMING" style "extra_now_label"
                                if selected_track:
                                    text selected_track["title"] style "extra_now_title"
                                    text selected_track["subtitle"] style "extra_now_subtitle"
                                else:
                                    text "Трек не выбран" style "extra_now_title"

                            vbox:
                                spacing 2
                                xalign 1.0
                                text ("Статус: " + ("Играет" if channel_playing else ("Пауза" if extra_music_paused else "Остановлен"))) style "extra_now_meta"
                                text "Время: [track_time] / [total_time]" style "extra_now_meta"
                                text "Прогресс: [track_progress_percent]%" style "extra_now_meta"
                                text "[bg_state_text]" style "extra_now_meta"

                frame:
                    style "extra_progress_frame"
                    xfill True

                    vbox:
                        spacing 8
                        xfill True

                        text "ПОЗИЦИЯ ТРЕКА" style "extra_music_kicker"

                        if track_has_duration:
                            bar:
                                style "extra_progress_bar"
                                value track_pos
                                range track_range
                                changed extra_seek_absolute
                                xfill True
                        else:
                            bar:
                                style "extra_progress_bar"
                                value 0.0
                                range 1.0
                                xfill True

                        hbox:
                            xfill True
                            text "[track_time]" style "extra_progress_text"
                            text "[track_progress_percent]%" style "extra_progress_text":
                                xalign 0.5
                            text "[total_time]" style "extra_progress_text":
                                xalign 1.0

                        text ("Кликните и тяните полосу для перемотки" if track_has_duration else "Перемотка недоступна: нет длительности трека") style "extra_progress_hint"

                frame:
                    style "extra_music_controls_frame"
                    xfill True

                    if compact_controls:
                        vbox:
                            spacing 8
                            xalign 0.5

                            hbox:
                                spacing 10
                                xalign 0.5

                                textbutton "⏪ 10с":
                                    style "extra_control_button"
                                    action Function(extra_seek_relative, -10.0)
                                    sensitive track_has_duration

                                textbutton "[playback_text]":
                                    style "extra_control_button"
                                    action Function(extra_toggle_playback)

                                textbutton "10с ⏩":
                                    style "extra_control_button"
                                    action Function(extra_seek_relative, 10.0)
                                    sensitive track_has_duration

                            hbox:
                                spacing 10
                                xalign 0.5

                                textbutton "◀ Пред":
                                    style "extra_control_button"
                                    action Function(extra_prev_track)

                                textbutton "След ▶":
                                    style "extra_control_button"
                                    action Function(extra_next_track)

                                textbutton "■ Стоп":
                                    style "extra_control_button"
                                    action Function(extra_stop_music)
                    else:
                        hbox:
                            spacing 10
                            xalign 0.5

                            textbutton "⏪ 10с":
                                style "extra_control_button"
                                action Function(extra_seek_relative, -10.0)
                                sensitive track_has_duration

                            textbutton "◀ Пред":
                                style "extra_control_button"
                                action Function(extra_prev_track)

                            textbutton "[playback_text]":
                                style "extra_control_button"
                                action Function(extra_toggle_playback)

                            textbutton "След ▶":
                                style "extra_control_button"
                                action Function(extra_next_track)

                            textbutton "10с ⏩":
                                style "extra_control_button"
                                action Function(extra_seek_relative, 10.0)
                                sensitive track_has_duration

                            textbutton "■ Стоп":
                                style "extra_control_button"
                                action Function(extra_stop_music)

                frame:
                    style "extra_visualizer_frame"
                    xfill True
                    yfill True
                    yminimum visualizer_height

                    fixed:
                        xfill True
                        yfill True

                        add Solid("#180000AA")
                        add Solid(pulse_color) at extra_vis_pulse
                        add Solid("#8ec9ff2f"):
                            xsize 3
                            ysize max(180, visualizer_height)
                            at extra_music_sweep_line

                        use music_visualizer(
                            channel=EXTRA_MUSIC_CHANNEL,
                            bands=dense.get("bands", 64),
                            width=visualizer_width,
                            height=visualizer_height,
                            bar_w=7,
                            gap=4,
                            max_h=max(105, visualizer_height - 56),
                            glow_px=dense.get("glow_px", 10),
                            smoothing=dense.get("smoothing", 0.30),
                            gamma=dense.get("gamma", 0.34),
                            palette_points=palette_points,
                        )

                        fixed:
                            at extra_vis_layer
                            xfill True
                            yfill True
                            use music_visualizer(
                                channel=EXTRA_MUSIC_CHANNEL,
                                bands=wide.get("bands", 20),
                                width=visualizer_width_small,
                                height=max(145, visualizer_height - 24),
                                bar_w=15,
                                gap=30,
                                max_h=max(80, int(visualizer_height * 0.42)),
                                glow_px=wide.get("glow_px", 14),
                                smoothing=wide.get("smoothing", 0.58),
                                gamma=wide.get("gamma", 0.52),
                                palette_points=palette_points,
                            )


style extra_playlist_frame:
    background "#0c1219D6"
    padding (16, 16)
    outlines [(1, "#8ec9ff40", 0, 0)]

style extra_music_kicker is gui_text:
    color "#8ec9ff"
    size 22

style extra_music_panel_title is gui_text:
    color "#ff7a18"
    size 44

style extra_music_subtle is gui_text:
    color "#c7dfff9a"
    size 21

style extra_music_stack_frame:
    background "#0b1219D6"
    padding (0, 0)
    outlines [(1, "#8ec9ff38", 0, 0)]

style extra_track_button is button:
    background "#8ec9ff12"
    hover_background "#8ec9ff24"
    selected_background "#ff7a1842"
    outlines [(1, "#8ec9ff36", 0, 0)]
    padding (12, 10)
    xfill True

style extra_track_button_text is button_text:
    color gui.interface_text_color
    hover_color gui.hover_color
    selected_color gui.accent_color
    size 24
    text_align 0.0
    xalign 0.0

style extra_now_frame:
    background "#0c1219D6"
    padding (18, 16)
    outlines [(1, "#8ec9ff40", 0, 0)]

style extra_now_label is gui_text:
    color "#8ec9ff"
    size 24

style extra_now_title is gui_text:
    color gui.interface_text_color
    size 38

style extra_now_subtitle is gui_text:
    color "#c9dfffca"
    size 22

style extra_now_meta is gui_text:
    color "#dce9f3"
    size 21
    xalign 1.0
    text_align 1.0

style extra_visualizer_frame:
    background "#0a1118E0"
    padding (14, 14)
    outlines [(1, "#8ec9ff38", 0, 0)]

style extra_progress_frame:
    background "#0c1219D6"
    padding (14, 12)
    outlines [(1, "#8ec9ff38", 0, 0)]

style extra_progress_bar:
    ysize 24
    left_bar Frame("gui/slider/horizontal_hover_bar.png", 10, 10)
    right_bar Frame("gui/slider/horizontal_idle_bar.png", 10, 10)
    thumb "gui/slider/horizontal_hover_thumb.png"
    thumb_offset 0

style extra_progress_text is gui_text:
    color "#dce9f3"
    size 21

style extra_progress_hint is gui_text:
    color "#b9d4ee9d"
    size 19

style extra_music_controls_frame:
    background "#0c1219D6"
    padding (10, 12)
    outlines [(1, "#8ec9ff38", 0, 0)]

style extra_control_button is button:
    background "#8ec9ff18"
    hover_background "#8ec9ff2b"
    selected_background "#ff7a1842"
    outlines [(1, "#8ec9ff44", 0, 0)]
    padding (12, 8)
    xminimum 96

style extra_control_button_text is button_text:
    font gui.interface_text_font
    size 24
    color "#f2f8ff"
    hover_color "#ffd3b2"

transform extra_music_scanline:
    alpha 0.14
    yoffset 0
    linear 1.6 yoffset 85 alpha 0.03
    linear 0.2 alpha 0.14
    repeat

transform extra_music_panel_intro:
    alpha 0.0
    yoffset 12
    ease 0.2 alpha 1.0 yoffset 0

transform extra_now_glow:
    alpha 0.14
    linear 1.4 alpha 0.30
    linear 1.4 alpha 0.14
    repeat

transform extra_vis_pulse:
    alpha 0.24
    linear 1.3 alpha 0.52
    linear 1.3 alpha 0.24
    repeat

transform extra_vis_layer:
    alpha 0.5

transform extra_music_sweep_line:
    xoffset -12
    alpha 0.0
    linear 0.6 alpha 0.82
    linear 2.0 xoffset 860 alpha 0.0
    repeat
