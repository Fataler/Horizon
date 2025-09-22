init -1 python:
    import functools as ft
    import time
    from renpy.curry import curry
    
    talk_key = 'talk_'
    speaking = None
    MINIMUM_SPEAK_TIME = 0.8
    _speaking_start_times = {}
    _speaking_min_end_times = {}

    def _mark_speaking_start(character_name, now):
        _speaking_start_times[character_name] = now
        _speaking_min_end_times.pop(character_name, None)

    def _mark_speaking_end(character_name, now):
        start = _speaking_start_times.get(character_name)
        if start is None:
            return

        if preferences.text_cps > 0:
            _speaking_start_times.pop(character_name, None)
            _speaking_min_end_times.pop(character_name, None)
            return

        min_end = start + MINIMUM_SPEAK_TIME
        if now >= min_end:
            _speaking_start_times.pop(character_name, None)
            _speaking_min_end_times.pop(character_name, None)
            return

        _speaking_min_end_times[character_name] = min_end

    def _current_time():
        return time.monotonic()

    def while_speaking(character_name, speak_d, done_d, st, at):
        now = _current_time()
        min_end = _speaking_min_end_times.get(character_name, 0.0)

        if speaking == character_name:
            start = _speaking_start_times.get(character_name, now)
            if start is None:
                _mark_speaking_start(character_name, now)
                start = now

            if preferences.text_cps <= 0:
                desired_end = start + MINIMUM_SPEAK_TIME
                if desired_end > min_end:
                    _speaking_min_end_times[character_name] = desired_end

            return speak_d, .1

        if now < min_end:
            return speak_d, .1

        _speaking_start_times.pop(character_name, None)
        _speaking_min_end_times.pop(character_name, None)
        return done_d, None

    curried_while_speaking = curry(while_speaking)

    def WhileSpeaking(character_name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(character_name, speaking_d, done_d))

    def speaker_callback(character_name, event, **kwargs):        
        global speaking
        
        now = _current_time()

        if event == "show" or event == "begin":
            speaking = character_name
            _mark_speaking_start(character_name, now)
        elif event == 'slow_done' or event == "end":
            _mark_speaking_end(character_name, now)

            if speaking == character_name:
                speaking = None

    speaker = curry(speaker_callback)

