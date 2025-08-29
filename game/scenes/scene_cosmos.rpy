define COSMOS_FRAME_PAUSE = 0.2
define PATH_TO_COSMOS_IMAGES = "images/CG/CG_fon_cosmos/{image_number}_{frame_number}.png"
define COSMOS_ZOOM = 1

image cosmos_fon_1 = At("images/CG/CG_fon_cosmos/fon/potato/CG_fon_cosmos_potato_0000s_0000_4.png", fade_in_out(delay=1, fade_time=3.0))
image cosmos_fon_2 = At("images/CG/CG_fon_cosmos/fon/potato/CG_fon_cosmos_potato_0000s_0001_3.png", fade_in_out(delay=2, fade_time=3.0))
image cosmos_fon_3 = At("images/CG/CG_fon_cosmos/fon/potato/CG_fon_cosmos_potato_0000s_0002_2.png", fade_in_out(delay=3, fade_time=3.0))
image cosmos_fon_4 = "images/CG/CG_fon_cosmos/fon/potato/CG_fon_cosmos_potato_0000s_0003_1.png"


label show_cosmos_background(image_number, frame_count=2):
    $ show_scene_cosmos(image_name=image_number, frame_count=frame_count)

    pause

    $ hide_scene_cosmos()
    return

label test_cosmos:
    scene bg_black

    $ show_scene_cosmos("2")
    cutscene "tes"

    cutscene "tessss"

    $ hide_scene_cosmos()
    $ show_scene_cosmos("3")
    cutscene "tessss"

    pause
    return

screen cosmos_background_screen(image_name, frame_count=2):
    zorder 0

    fixed:
        add "cosmos_fon_4"
        add "cosmos_fon_3"
        add "cosmos_fon_2"
        add "cosmos_fon_1"

        default current_frame = 1
        
        for frame_num in range(1, frame_count + 1):
            if current_frame == frame_num:
                add PATH_TO_COSMOS_IMAGES.format(image_number=image_name, frame_number=frame_num)
                if current_frame == frame_count:
                    timer COSMOS_FRAME_PAUSE action SetScreenVariable("current_frame", 1) repeat True
                else:
                    timer COSMOS_FRAME_PAUSE action SetScreenVariable("current_frame", current_frame + 1) repeat False

init -1 python:
    def show_scene_cosmos(img, tr=None):
        renpy.show_screen("cosmos_background_screen", img, _layer="master")
        if tr is None:
            tr = Dissolve(0.5)
        renpy.with_statement(tr)

    def hide_scene_cosmos(tr=None):
        renpy.hide_screen("cosmos_background_screen")
        if tr is None:
            tr = Dissolve(0.5)
        renpy.with_statement(tr)