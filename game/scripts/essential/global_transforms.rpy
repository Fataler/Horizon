transform g_appear(time = 1.0, delay = 0.0):
    alpha 0
    pause delay
    linear time alpha 1

transform _disappear(time = 1.0, delay = 0.0):
    alpha 1
    pause delay
    linear time alpha 0

transform _shake(time = 1.0, delay = 0.0):
    xoffset 0
    yoffset 0
    parallel:
        linear 0.1 xoffset 10
        pause 0.1
        linear 0.1 xoffset -10
        pause 0.1
        linear 0.1 xoffset 10
        pause 0.1
        linear 0.1 xoffset 0

transform crt:
    parallel:
        function WaveShader(amp=0.05, period=17.219, speed=4, direction="horizontal", damp=(0.999,0.043))

transform dizzy:
    parallel:
        function WaveShader(amp=(1,1), period=(1,2), speed=(1.5,1.5), direction="horizontal", damp=(1,0), double="horizontal")

transform crt_effects:
    parallel:
        blend "multiply" alpha 0.5
    parallel:
        function WaveShader(amp=0.05, period=17.219, speed=4, direction="vertical", damp=(0.043,1.0))

image crt = At("crt.png", crt_effects)

transform hover_effect(opac=0.3):
    on show:
        alpha 0.0
    on hover:
        ease 0.15 alpha opac
    on idle:
        ease 0.05 alpha 0.0 blend "add"