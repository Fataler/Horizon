transform fade_in_out(fade_time=2.0):
    alpha 0.0
    linear fade_time alpha 1.0
    linear fade_time alpha 0.0
    repeat

layeredimage viktor_scene:
    always:
        "images/CG/CG Victor shooting/2.png"
    always:
        "images/CG/CG Victor shooting/1.png"
        at fade_in_out(0.5)

label viktor_scene:
    show viktor_scene
    with dissolve
    pause
    return
