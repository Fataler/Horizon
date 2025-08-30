image ending_bad = "CG/CG_ending/CG_ending_bad.png"

image ending_good = "CG/CG_ending/CG_ending_good.png"

image ending_norm = "CG/CG_ending/CG_ending_norm.png"

screen screen_final_choise():
    layer "master"

    default hover_good = False
    default hover_bad = False

    showif not hover_good and not hover_bad:
        add "ending_norm" at screen_fade_effect(2.5)

    showif hover_good:
        add "ending_good" at screen_fade_effect_in_out(2.0, start_alpha=0.75, end_alpha=1.0, initial_alpha=0.0)

    showif hover_bad:
        add "ending_bad" at screen_fade_effect_in_out(2.0, start_alpha=0.75, end_alpha=1.0, initial_alpha=0.0)

    button:
        background None#"#07b4e974"
        xpos 0.45
        anchor (0.5, 0.0)
        ypos 0.0
        xsize 1530
        ysize 430
        hovered SetScreenVariable("hover_good", True)
        unhovered SetScreenVariable("hover_good", False)
        action Return(True)
        #hover_sound Null()

    button:
        background None#"#e9d20774"
        xpos 0.5
        ypos 1.0
        anchor (0.5, 1.0)
        xsize 1530
        ysize 460
        hovered SetScreenVariable("hover_bad", True)
        unhovered SetScreenVariable("hover_bad", False)
        action Return(False)
        #hover_sound Null()

    text "поверить спасителю" style "final_choise_text":
        pos (350, 100) 
        xsize 800
        ysize 460
        underline (True if hover_good else False)

    text "и возобновить контакт" style "final_choise_text":
        pos (1500, 100) 
        xsize 800
        ysize 460
        underline (True if hover_good else False)

    text "не идти на поводу" style "final_choise_text":
        pos (450, 1000) 
        xsize 800
        ysize 460
        color "#000000"
        underline (True if hover_bad else False)

    text "у подозрительного голоса" style "final_choise_text":
        pos (1500, 1000) 
        xsize 800
        ysize 460
        color "#000000"
        underline (True if hover_bad else False)

style final_choise_text is text:
    subpixel True
    anchor (0.5, 0.5)
    font gui.interface_text_font
    size 50
    color "#ffffff"

label scene_final_choise:
    call screen screen_final_choise

    stop music fadeout 1.0
    pause
    return
    
