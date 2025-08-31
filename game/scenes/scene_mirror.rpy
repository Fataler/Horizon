image scene_mirror_water = "CG/CG_mirror/CG_mirror_water.png"

image scene_mirror_cherk = At("CG/CG_mirror/CG_cherk.png", soot_drift_bottom)

image scene_mirror = "CG/CG_mirror/CG_mirror.png"
image scene_mirror_dark = "CG/CG_mirror/CG_mirror_dark.png"
image scene_mirror_red = "CG/CG_mirror/CG_mirror_red.png"
image scene_mirror_beard = "CG/CG_mirror/CG_mirror_beard.png"

label scene_mirror:
    show scene_mirror
    show scene_mirror_cherk
    with dissolve

    return

label scene_mirror_water:
    show scene_mirror_water
    show scene_mirror_cherk
    with dissolve

    return

label scene_mirror_dark:
    show scene_mirror_dark
    show scene_mirror_cherk
    with dissolve

    return

label scene_mirror_red:
    show scene_mirror_red
    show scene_mirror_cherk

    return

label scene_mirror_beard:
    show scene_mirror_beard
    with dissolve

    return