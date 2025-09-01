image scene_talk_in_end_1 = At("CG/CG_talk_in_the_end/1.png", fade_on_show)
image scene_talk_in_end_2 = At("CG/CG_talk_in_the_end/2.png", fade_on_show)
image scene_talk_in_end_3 = At("CG/CG_talk_in_the_end/3.png", fade_on_show)
image scene_talk_in_end_4 = At("CG/CG_talk_in_the_end/4.png", fade_on_show)
image scene_talk_in_end_5 = At("CG/CG_talk_in_the_end/5.png", fade_on_show)
image scene_talk_in_end_6 = At("CG/CG_talk_in_the_end/6.png", fade_on_show)
image scene_talk_in_end_7 = At("CG/CG_talk_in_the_end/7.png", fade_on_show)
image scene_talk_in_end_8 = At("CG/CG_talk_in_the_end/8.png", fade_on_show)
image scene_talk_in_end_9 = At("CG/CG_talk_in_the_end/9.png", fade_on_show)
image scene_talk_in_end_10 = At("CG/CG_talk_in_the_end/10.png", fade_on_show)
image scene_talk_in_end_11 = At("CG/CG_talk_in_the_end/11.png", fade_on_show)
image scene_talk_in_end_12 = At("CG/CG_talk_in_the_end/12.png", fade_on_show)
image scene_talk_in_end_13 = At("CG/CG_talk_in_the_end/13.png", fade_on_show)
image scene_talk_in_end_14 = At("CG/CG_talk_in_the_end/14.png", fade_on_show)
image scene_talk_in_end_15 = At("CG/CG_talk_in_the_end/15.png", fade_on_show)
image scene_talk_in_end_16 = At("CG/CG_talk_in_the_end/16.png", fade_on_show)
image scene_talk_in_end_17 = At("CG/CG_talk_in_the_end/17.png", fade_on_show)
image scene_talk_in_end_18 = At("CG/CG_talk_in_the_end/18.png", fade_on_show)
image scene_talk_in_end_19 = At("CG/CG_talk_in_the_end/19.png", fade_on_show)
image scene_talk_in_end_cherk = At("CG/CG_talk_in_the_end/cherk.png", soot_drift_bottom(speed=0.5, amplitude= 1, x_amplitude=-1, zoom=1.001), fade_on_show)

label scene_elis:
    show scene_talk_in_end_cherk at truecenter zorder 10:
        anchor(0.5, 0.5)
        pos(0.5, 0.5)
    return

label test_elis:
    scene bg_white
    pause 3.0
    show scene_talk_in_end_19
    show scene_talk_in_end_cherk
    "..."
    show scene_talk_in_end_10
    pause
    return

label scene_talk_in_end:
    play music music_bad_end_after_talk fadein 1.0 loop
    show scene_talk_in_end_1
    show scene_talk_in_end_cherk at soot_drift_bottom(speed=0.5, amplitude= 1, x_amplitude=-1, zoom=1.001), truecenter zorder 10
    with dissolve
    pause
    show scene_talk_in_end_2
    with dissolve
    pause
    show scene_talk_in_end_3
    with dissolve
    pause
    show scene_talk_in_end_4
    with dissolve
    pause
    show scene_talk_in_end_5
    with dissolve
    pause
    show scene_talk_in_end_6
    with dissolve
    pause
    show scene_talk_in_end_7
    with dissolve
    pause
    show scene_talk_in_end_8
    with dissolve
    pause
    show scene_talk_in_end_9
    with dissolve
    pause
    show scene_talk_in_end_10
    with dissolve
    pause
    show scene_talk_in_end_11
    with dissolve
    pause
    show scene_talk_in_end_12
    with dissolve
    pause
    show scene_talk_in_end_13
    with dissolve
    pause
    show scene_talk_in_end_14
    with dissolve
    pause
    show scene_talk_in_end_15
    with dissolve
    pause
    show scene_talk_in_end_16
    with dissolve
    pause
    show scene_talk_in_end_17
    with dissolve
    pause
    show scene_talk_in_end_18
    with dissolve
    pause
    show scene_talk_in_end_19
    with dissolve
    pause

    stop music fadeout 1.0
    pause
    return
