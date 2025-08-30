label epilogue:
    scene bg_black
    with dissolve

    play music music_epilogue fadein 1.0 loop
    show expression Solid("#fff") as overlay_light at light_hurt
    pause 2.0
    show expression Solid("#fff") as overlay_light at alpha_mask_fade_inverse
    pause 1.0
    call scene_good_ending
    return
