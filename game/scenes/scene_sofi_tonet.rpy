image scene_sofi_tonet_ruka = "CG/CG_Sofi_tonet/CG_Sofi_tonet_Ruka.png"
image scene_sofi_tonet_blik = "CG/CG_Sofi_tonet/CG_Sofi_tonet_blik.png"
image scene_sofi_tonet_cherkash = "CG/CG_Sofi_tonet/CG_Sofi_tonet_cherkash.png"
image scene_sofi_tonet_effect1 = "CG/CG_Sofi_tonet/CG_Sofi_tonet_effect1.png"
image scene_sofi_tonet_effect2 = "CG/CG_Sofi_tonet/CG_Sofi_tonet_effect2.png"
image scene_sofi_tonet_effect3 = "CG/CG_Sofi_tonet/CG_Sofi_tonet_effect3.png"
image scene_sofi_tonet_fon = "CG/CG_Sofi_tonet/CG_Sofi_tonet_fon.png"
image scene_sofi_tonet_glaza = "CG/CG_Sofi_tonet/CG_Sofi_tonet_Glaza.png"
image scene_sofi_tonet_golova = "CG/CG_Sofi_tonet/CG_Sofi_tonet_Golova.png"
image scene_sofi_tonet_red = "CG/CG_Sofi_tonet/CG_Sofi_tonet_red.png"

label scene_sofi_tonet:
    show scene_sofi_tonet_fon
    show scene_sofi_tonet_golova at soot_drift_bottom(speed=0.5, amplitude= 0.5, x_amplitude=-1)
    
    show scene_sofi_tonet_glaza at soot_drift_bottom(speed=1.0, amplitude= 0.6, x_amplitude=-1)
    show scene_sofi_tonet_ruka at soot_drift_bottom(speed=0.6, amplitude= -6, x_amplitude=-3)
    
    show scene_sofi_tonet_effect1
    show scene_sofi_tonet_effect2 at soot_drift_bottom(speed=0.8, zoom=1.01, x_amplitude=-1, amplitude=1)
    show scene_sofi_tonet_blik at soot_drift_bottom(speed=1.0, amplitude= 0.6, x_amplitude=-1)
    show scene_sofi_tonet_red at fade_in_out_blend(fade_time=1, max_alpha=0.5, min_alpha=0.2, blend_type="add")
    show scene_sofi_tonet_cherkash at soot_drift_bottom(speed=0.8, zoom=1.08, x_amplitude=10):
        anchor(0.5, 0.5)
        pos(0.5, 0.5)
    with dissolve

    pause
    
    show scene_sofi_tonet_ruka at soot_drift_bottom(speed=0.3, amplitude= -12, x_amplitude=-6)
    show scene_sofi_tonet_red at fade_in_out_blend(fade_time=1, max_alpha=0.7, min_alpha=0.4, from_zero=False, blend_type="min")
    pause

    return