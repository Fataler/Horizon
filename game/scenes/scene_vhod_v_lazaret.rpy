image scene_vhod_v_lazaret_fon = "CG/CG_vhod_v_lazaret/CG_vhod_v_lazaret_0004_fon.png"
image scene_vhod_v_lazaret_figures = "CG/CG_vhod_v_lazaret/CG_vhod_v_lazaret_0000_figures.png"
image scene_vhod_v_lazaret_dver = "CG/CG_vhod_v_lazaret/CG_vhod_v_lazaret_0001_dver.png"
image scene_vhod_v_lazaret_cherkash = "CG/CG_vhod_v_lazaret/CG_vhod_v_lazaret_0002_cherkash.png"
image scene_vhod_v_lazaret_bryzgash = "CG/CG_vhod_v_lazaret/CG_vhod_v_lazaret_0003_bryzgash.png"

transform door_effect:
    subpixel True
    parallel:
        block:
            easein 2.0 zoom 1.02
            easeout 2.0 zoom 1.00
            repeat
    parallel:
        block:
            linear 0.5 alpha 0.8
            linear 0.5 alpha 1.0
            repeat

label scene_vhod_v_lazaret:
    show scene_vhod_v_lazaret_fon
    
    show scene_vhod_v_lazaret_dver at door_effect:
        anchor(0.5, 0.5)
        pos(0.5, 0.5)
    
    show scene_vhod_v_lazaret_bryzgash at fade_in_out(fade_time=1.5, max_alpha=0.6, min_alpha=0.2)
    
    show scene_vhod_v_lazaret_figures at soot_drift_bottom(speed=0.6, amplitude=2, x_amplitude=1)
    show scene_vhod_v_lazaret_cherkash at soot_drift_bottom(speed=0.8, amplitude=2, x_amplitude=-1)
    with dissolve

    cutscene "Софи и Ирис испуганно взглянули на меня."
    cutscene "Уверенности нам всем не добавляло то, что я стоял с горсткой металлических игл в руке."
    return
