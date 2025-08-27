transform screen_shaking(dx=5, dy=3, t=0.04):
    xoffset 0 yoffset 0
    linear t xoffset dx
    linear t yoffset dy
    linear t xoffset -dx
    linear t yoffset -dy
    repeat

label scene_earthquake:
    show layer master at screen_shaking
    return

label scene_earthquake_hard:
    show layer master at screen_shaking(dx=10, dy=5, t=0.02)
    return