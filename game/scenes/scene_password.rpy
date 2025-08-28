image scene_password_cherkash = "CG/CG_password/CG_password_cherkash.png"
image scene_password_zapiska = "CG/CG_password/CG_password_Zapiska.png"

label scene_password:
    show scene_password_zapiska
    show scene_password_cherkash at soot_drift_bottom(speed=1.0, amplitude=3, x_amplitude=2), truecenter
    with dissolve

    cutscene "Констатирую смерть, время — 17:34."
    cutscene "Я вздохнул."

    hide scene_password_zapiska
    hide scene_password_cherkash
    with dissolve
    return