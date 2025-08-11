init python:
    class Parallax(renpy.Displayable):
        def __init__(self, image_name, movement_speed):
            super(Parallax, self).__init__()
            self.image = renpy.displayable(image_name)
            self.movement_speed = movement_speed
            self.current_x = 0
            self.current_y = 0
        
        def render(self, width, height, st, at):
            canvas = renpy.Render(width, height)
            image_render = renpy.render(self.image, width, height, st, at)
            
            mouse_x, mouse_y = renpy.get_mouse_pos()
            center_x = config.screen_width / 2
            center_y = config.screen_height / 2
            
            offset_from_center_x = mouse_x - center_x
            offset_from_center_y = mouse_y - center_y
            
            self.current_x = (width - image_render.width)/2 + offset_from_center_x * self.movement_speed / 50.0
            self.current_y = (height - image_render.height)/2 + offset_from_center_y * self.movement_speed / 50.0
            
            canvas.blit(image_render, (int(self.current_x), int(self.current_y)))
            renpy.redraw(self, 0)
            
            return canvas
        
        def event(self, ev, x, y, st):
            return None
        
        def visit(self):
            return [self.image]


screen parallax_bg(image_name, movement_speed = 10):
    zorder 0
    add Parallax(image_name, movement_speed)

label parallax_test:
    scene bg_paper
    show screen parallax_bg("images/CG RGG/cg1 b.png", 10)
    "..."
    hide screen parallax_bg
    return