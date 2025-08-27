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
