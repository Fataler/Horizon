image bg_coridor_fon = "CG/CG_koridor/CG_koridor_0004_fon.png"
image bg_coridor_cherkash = "CG/CG_koridor/CG_koridor_0000_cherkash.png"
image bg_coridor_teni_1 = "CG/CG_koridor/CG_koridor_0001_teni_1.png"

image bg_coridor_teni_2:
    "CG/CG_koridor/CG_koridor_0002_teni_2.png"
    anchor(0.5, 0.5)
    
image bg_coridor_figuri = "CG/CG_koridor/CG_koridor_0003_figuri.png"

init python:
    import math
    def _circle_motion(radius, duration, start_angle_deg, clockwise, trans, st, at):
        if duration <= 0.0:
            progress = 0.0
        else:
            progress = (st % duration) / duration
        direction = -1.0 if clockwise else 1.0
        angle_rad = math.radians(start_angle_deg) + direction * (2.0 * math.pi * progress)
        trans.xoffset = radius * math.cos(angle_rad)
        trans.yoffset = radius * math.sin(angle_rad)
        return 0
    circle_motion = renpy.curry(_circle_motion)

transform move_by_circle(cx=0.5, cy=0.5, radius=100, duration=2.0, start_angle=0.0, clockwise=True):
    xpos cx
    ypos cy
    function circle_motion(radius, duration, start_angle, clockwise)
    repeat

label scene_coridor:
    scene bg_coridor_fon
    show bg_coridor_figuri
    
    show bg_coridor_teni_1
    show bg_coridor_teni_2 at move_by_circle(0.5, 0.5, 10, 2.0, 0.0, True):
        pos (0.53, 0.52)
    show bg_coridor_cherkash at soot_drift_bottom()
    pause
    return