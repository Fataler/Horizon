#images 

## Определения фоновых изображений
# Фоны из папки Backgrounds
image bg_amusement_park = "images/Backgrounds/Amusement Park.jpg"
image bg_backyard = "images/Backgrounds/Backyard.jpg"
image bg_class_room = "images/Backgrounds/Class Room.jpg"
image bg_garage_dirty = "images/Backgrounds/Garage Durty.jpg"
image bg_garage = "images/Backgrounds/Garage.jpg"
image bg_living_room = "images/Backgrounds/Living Room.jpg"
image bg_monitor = "images/Backgrounds/Monitor.jpg"
image bg_near_home = "images/Backgrounds/Near Home.jpg"
image bg_near_school = "images/Backgrounds/Near School.jpg"
image bg_robo_class_room = "images/Backgrounds/Robo-class Room.jpg"
image bg_school_entrance = "images/Backgrounds/School Entrance.jpg"
image bg_square = "images/Backgrounds/Square.jpg"


# credits images
image credits_img_1:
    "images/Credits/1.png"
image credits_img_2:
    "images/Credits/2.png"
image credits_img_3:
    "images/Credits/3.png"
image credits_img_4:
    "images/Credits/4.png"
image credits_img_5:
    "images/Credits/5.png"
image credits_img_6:
    "images/Credits/6.png"
image credits_img_7:
    "images/Credits/7.png"

## Общие изображения
image bg_black = Solid("#000")
image bg_white = Solid("#fff")
image bg_paper = Solid("#FFE7CE")

image bg_black_t_10 = Solid("#0000001a")
image bg_black_t_20 = Solid("#00000033")
image bg_black_t_30 = Solid("#0000004d")
image bg_black_t_40 = Solid("#00000066")
image bg_black_t_50 = Solid("#00000080")
image bg_black_t_60 = Solid("#00000099")
image bg_black_t_70 = Solid("#000000b3")
image bg_black_t_80 = Solid("#000000cc")
image bg_black_t_90 = Solid("#000000e6")

## цгшки
image suhariki:
    "images/Prochee/emelyan.png"
    anchor (0.5, 0.5)

image energy_drink:
    "images/Prochee/imba.png"
    anchor (0.5, 0.5)

image pizza:
    "images/Prochee/pizza.png"
    anchor (0.5, 0.5)

image umi_on_floor:
    "images/CG/Robo-class Room.png"

image guitar_solo:
    "images/CG/Garage.png"

image squid:
    "images/CG/Square.png"

image all_shocked:
    "images/CG/CG RGG.png"

image novel_end:
    "images/CG/cg_novel_end_stars-.png"

image novel_end_stars:
    "images/CG/cg_novel_end_stars+.png"

image bush1:
    "images/Prochee/Kust.png"

image bush2:
    "images/Prochee/Kust2.png"

image bush3:
    "images/Prochee/Kust3.png"

image bush4:
    "images/Prochee/Kust5.png"

image bg_menu_main = "gui/menu/bg.png"

init:
    image avatar_circle = AlphaMask("gui/menu/avatar_square.jpg", im.Scale("gui/menu/alpha_mask.png", 320, 320))


## Эффекты
transform darken:
    matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

transform lighten:
    matrixcolor TintMatrix("#ffffff") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

# Анимированное затемнение
transform fade_to_dark:
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.0)
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

# Анимированное осветление
transform fade_to_light:
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.0)


