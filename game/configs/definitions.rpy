#constants
default persistent.first_start = True
default persistent.game_completed = False
define URL_JAM = "https://vk.com/jamof100flowers"

#screens
default MAIN_MENU_SCREEN = "main_menu"
default PAUSE_MENU_SCREEN = "pause_menu"

define splash_enabled = True

default textbox_style = "gui/textbox.png"
default came_from_pause_menu = False

init python:    
    def set_character(mouse, current_character, textbox_style_image):
        global textbox_style, character, default_mouse
        character = current_character
        textbox_style = textbox_style_image
        default_mouse  = mouse
        renpy.restart_interaction()
    
    def set_textbox_custom(path):
        global textbox_style
        textbox_style = path
        renpy.restart_interaction()