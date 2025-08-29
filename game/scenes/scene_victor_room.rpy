image scene_victor_room_1 = "CG/CG_Victor_room/cg_Room Viktor1.png"
image scene_victor_room_2 = "CG/CG_Victor_room/cg_Room Viktor2.jpg"
image scene_victor_room_3 = "CG/CG_Victor_room/cg_Room Viktor3.jpg"

label scene_victor_room:
    show scene_victor_room_1
    with dissolve
    pause 1.0

    show scene_victor_room_2
    with dissolve
    pause 1.0

    show scene_victor_room_3
    with dissolve
    pause

    return
