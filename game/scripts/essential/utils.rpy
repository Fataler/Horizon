init -1 python:
    import random

    robot_char = Character("")
    
    def make_robot_bits(txt):
        # symbols = "0123456789ABCDEF"
        symbols = "01"
        
        # matrix_colors = ["#00ff00", "#00cc00", "#00ff41", "#00cc33"]
        
        robot_bits = ""
        for char in txt:
            if char != " ":
                symbol = random.choice(symbols)
                color = "#ffffff"
                robot_bits += "{color=" + color + "}" + symbol + "{/color}"
            else:
                robot_bits += char
        return robot_bits

    def robot_say(what, **kwargs):
        bits = make_robot_bits(str(what))
        
        robot_char("{font=gui/fonts/DejaVuSansMono.ttf}{cps=200}" + bits + "{/font}", interact=False)
        
        renpy.pause(0.3, hard=True)
        
        return robot_char("{font=gui/fonts/DejaVuSansMono.ttf}{cps=999}" + str(what) + "{/font}", interact=True)

# трансформ для моргания
transform parametric_blink(open_img, closed_img, min_wait=2.0, max_wait=4.0, blink_speed=0.15, double_blink_chance=0.03):
    open_img
    block:
        choice:
            pause min_wait
        choice:
            pause (min_wait + max_wait) / 2
        choice:
            pause max_wait
        closed_img
        pause 0.1
        open_img
        repeat

init python:
    eye_on = ImageDissolve("gui/masks/eye_mask.png", 0.3, 10, reverse=False)
    #eye_off = ImageDissolve("gui/masks/eye_mask.png", 0.3, 10, reverse=True)
    def eye_off(duration=0.3):
        return ImageDissolve("gui/masks/eye_mask.png", duration, 10, reverse=True)
