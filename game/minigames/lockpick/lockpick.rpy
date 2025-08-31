init -1 python:
    LOCK_CHANNEL_MOVE = "Lock_Move"
    LOCK_CHANNEL_CLICK = "Lock_Click"

    SFX_UNLOCK = "audio/lock_unlock.mp3"
    SFX_MOVE = "audio/lock_moving.mp3"
    SFX_MOVE_BACK = "audio/lock_moving_back.mp3"
    SFX_BREAK = "audio/lock_pick_break.mp3"

    UI_TEXT_OPENED = "Отлично!"
    UI_TEXT_BROKE = "Черт, сломалась. Возьму другую!"

    NOTIFICATIONS_ENABLED = "lockpick_notifications_enabled"

    UI_DEBUG_COLOR = "#09c"

    renpy.music.register_channel(LOCK_CHANNEL_MOVE, mixer= "sfx", loop=True)
    renpy.music.register_channel(LOCK_CHANNEL_CLICK, mixer= "sfx", loop=False, tight=True)

    class Lock(renpy.Displayable):

        MIN_CYLINDER = 0
        MAX_CYLINDER = 90
        PICK_MIN = 0
        PICK_MAX = 180
        PICK_DEFAULT = 90

        def __init__(self, difficulty, loot, resize=1920, **kwargs):
            super(Lock, self).__init__(**kwargs)

            self.width = resize
            self.lock_plate_image = im.Scale(store.lockpick_images["plate"], resize, resize)
            self.lock_cylinder_image = im.Scale(store.lockpick_images["cylinder"], resize, resize)
            self.lock_tension_image = im.Scale(store.lockpick_images["tension"], resize, resize)
            self.lock_pick_image = im.Scale(store.lockpick_images["pick"], resize, resize)
            self.offset = (resize*2**0.5-resize)/2

            self.cylinder_min = self.MIN_CYLINDER
            self.cylinder_max = self.MAX_CYLINDER
            self.cylinder_pos = 0
            self.cylinder_try_rotate = False
            self.cylinder_can_rotate = False
            self.cylinder_released = False

            self.pick_min = self.PICK_MIN
            self.pick_max = self.PICK_MAX
            self.pick_pos = self.PICK_DEFAULT
            self.pick_can_rotate = True
            self.pick_broke = False

            self.sweet_spot = renpy.random.randint(0, self.PICK_MAX)
            self.difficulty = difficulty
            self.breakage = (difficulty/7 + 0.75)

            self.loot = loot
            self.victory = False

        def event(self, ev, x, y, st):
            import pygame
            LEFT = 1
            RIGHT = 3

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT:
                self.cylinder_try_rotate = True
                self.cylinder_released = False
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == LEFT:
                renpy.sound.stop(channel=LOCK_CHANNEL_MOVE)
                self.cylinder_try_rotate = False
                self.cylinder_released = True
                self.pick_can_rotate = True
                self.pick_broke = False
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == RIGHT:
                renpy.end_interaction(False)

        def _clamp_difficulty(self):
            if self.difficulty > 29:
                self.difficulty = 29
            elif self.difficulty < 1:
                self.difficulty = 1

        def _update_pick_angle_from_mouse(self):
            x, y = renpy.get_mouse_pos()
            self.pick_pos = x / (self.width / 360.0) - 90
            if self.pick_pos > self.PICK_MAX:
                self.pick_pos = self.PICK_MAX
            elif self.pick_pos < self.PICK_MIN:
                self.pick_pos = self.PICK_MIN

        def _update_cylinder_limit(self):
            delta = abs(self.pick_pos - self.sweet_spot)
            self.cylinder_can_rotate = True
            if delta < self.difficulty:
                self.cylinder_max = self.MAX_CYLINDER
            else:
                self.cylinder_max = self.MAX_CYLINDER - (delta * (30/self.difficulty))
                if self.cylinder_max < 0:
                    self.cylinder_max = 0

        def _make_pick_transform(self):
            if self.pick_broke:
                return Transform(child=None)
            return Transform(child=self.lock_pick_image, rotate=self.pick_pos, subpixel=True)

        def _make_rot_transforms(self, rotation):
            cylinder = Transform(child=self.lock_cylinder_image, rotate=rotation, subpixel=True)
            tension = Transform(child=self.lock_tension_image, rotate=rotation, subpixel=True)
            return cylinder, tension

        def _jitter_transforms(self):
            angle1 = self.cylinder_pos + renpy.random.randint(-2,2)
            angle2 = self.cylinder_pos + renpy.random.randint(-4,4)
            cylinder = Transform(child=self.lock_cylinder_image, subpixel=True, rotate=angle1)
            tension = Transform(child=self.lock_tension_image, subpixel=True, rotate=angle2)
            return cylinder, tension

        def _maybe_break_pick(self, pygame, at, pick):
            global lockpicks
            global set_timers
            global timers
            if set_timers == False:
                timers = at
                set_timers = True
            if set_timers == True:
                if at > timers + self.breakage:
                    renpy.sound.stop(channel=LOCK_CHANNEL_MOVE)
                    renpy.sound.play(SFX_BREAK, channel=LOCK_CHANNEL_CLICK)
                    if store.lockpick_notifications_enabled:
                        renpy.notify(UI_TEXT_BROKE)
                    mispick = renpy.random.randint(-30, 30)
                    pick = Transform(child=self.lock_pick_image, rotate=self.pick_pos + (2*mispick), subpixel=True)
                    self.pick_can_rotate = False
                    pygame.time.wait(200)
                    self.pick_broke = True
                    self.cylinder_try_rotate = False
                    timers = 0
                    set_timers = False
                    if lockpicks != -1:
                        lockpicks -= 1
                        if lockpicks <= 0:
                            renpy.end_interaction(False)
                    pygame.mouse.set_pos([self.width/2, self.width/4])
                    pygame.time.wait(100)
            return pick

        def _handle_victory(self, pygame):
            renpy.sound.stop(channel=LOCK_CHANNEL_MOVE)
            renpy.sound.play(SFX_UNLOCK, channel=LOCK_CHANNEL_CLICK)
            if store.lockpick_notifications_enabled:
                renpy.notify(UI_TEXT_OPENED)
            self.cylinder_max = self.MAX_CYLINDER
            self.cylinder_pos = self.MAX_CYLINDER
            global set_timers
            global timers
            timers = 0
            set_timers = False
            pygame.time.wait(150)
            self.cylinder_can_rotate = False
            self.victory = True
            renpy.end_interaction(True)

        def _on_release_step(self, pygame, st, at):
            if self.cylinder_pos > 15:
                renpy.sound.play(SFX_MOVE_BACK, channel=LOCK_CHANNEL_CLICK)
            self.pick_can_rotate = True
            self.cylinder_pos -= (5*st)/(at+1)
            if self.cylinder_pos < self.cylinder_min:
                self.cylinder_pos = self.cylinder_min
                self.cylinder_released = False
                renpy.sound.stop(channel=LOCK_CHANNEL_CLICK)
            return self._make_rot_transforms(self.cylinder_pos)

        def render(self, width, height, st, at):
            import pygame

            self._clamp_difficulty()

            if self.pick_can_rotate:
                self._update_pick_angle_from_mouse()
                self._update_cylinder_limit()

            pick = self._make_pick_transform()

            global display_pos
            display_pos = self.pick_pos

            global display_spot
            display_spot = self.sweet_spot

            if self.cylinder_try_rotate:
                if self.cylinder_can_rotate:
                    self.cylinder_pos += (2*st)/(at+1)
                    cylinder, tension = self._make_rot_transforms(self.cylinder_pos)
                    if self.cylinder_pos > self.cylinder_max:
                        self.cylinder_pos = self.cylinder_max
                        if self.cylinder_pos == self.MAX_CYLINDER:
                            self._handle_victory(pygame)
                        else:
                            if renpy.sound.is_playing != True:
                                renpy.sound.play(SFX_MOVE, channel=LOCK_CHANNEL_MOVE)
                            cylinder, tension = self._jitter_transforms()
                            self.pick_can_rotate = False
                            pick = self._maybe_break_pick(pygame, at, pick)
                else:
                    if renpy.sound.is_playing != True:
                        renpy.sound.play(SFX_MOVE, loop=True, channel=LOCK_CHANNEL_MOVE)
                    cylinder, tension = self._jitter_transforms()
                    self.pick_can_rotate = False
                    pick = self._maybe_break_pick(pygame, at, pick)
            else:
                if self.cylinder_released:
                    cylinder, tension = self._on_release_step(pygame, st, at)
                else:
                    cylinder, tension = self._make_rot_transforms(self.cylinder_pos)

            lock_plate_render = renpy.render(self.lock_plate_image, width, height, st, at)
            lock_cylinder_render = renpy.render(cylinder, width, height, st, at)
            lock_tension_render = renpy.render(tension, width, height, st, at)
            lock_pick_render = renpy.render(pick, width, height, st, at)

            render = renpy.Render(self.width, self.width)

            render.blit(lock_plate_render, (0, 0))
            render.blit(lock_cylinder_render, (-self.offset, -self.offset))
            render.blit(lock_tension_render, (-self.offset, -self.offset))
            render.blit(lock_pick_render, (-self.offset, -self.offset))

            renpy.redraw(self, 0)
            return render

        def reset(self):
            self.cylinder_min = self.MIN_CYLINDER
            self.cylinder_max = self.MAX_CYLINDER
            self.cylinder_pos = 0
            self.cylinder_try_rotate = False
            self.cylinder_can_rotate = False
            self.pick_min = self.PICK_MIN
            self.pick_max = self.PICK_MAX
            self.pick_pos = self.PICK_DEFAULT
            self.sweet_spot = renpy.random.randint(0, self.PICK_MAX)
 
init python:
    def counter(st, at):
 
        f = 0.0
 
        if hasattr(store, 'display_pos'):
            f = store.display_pos
 
        return Text("%.1f" % f, color=UI_DEBUG_COLOR, size=30), .1
    def counter2(st, at):
 
        f = 0.0
 
        if hasattr(store, 'display_spot'):
            f = store.display_spot
 
        return Text("%.1f" % f, color=UI_DEBUG_COLOR, size=30), .1
 
image counter = DynamicDisplayable(counter)
image counter2 = DynamicDisplayable(counter2)
 
default display_pos = 0
default display_spot = 0
default timers = 0
default set_timers = 0

default lockpick_difficulty = 22
default lockpick_resize = 1920
default lockpick_initial_picks = -1
default lockpick_debug_enabled = False
default lockpick_notifications_enabled = True
default lockpick_images = {
    "plate": "minigames/lockpick/lock_plate.png",
    "cylinder": "minigames/lockpick/lock_cylinder.png",
    "tension": "minigames/lockpick/lock_tension.png",
    "pick": "minigames/lockpick/lock_pick.png",
}
 
image lock_dark = Solid("#000c")
 
 
default lockpicks = 25
 
 
screen lockpicking(lock):
    layer "master"

    add "lock_dark"
    add lock:
        xalign 0.5
        yalign 0.5

    

    vbox:
        hbox:
            if lockpicks != -1:
                label "Lockpicks: " + str(lockpicks)

                

    textbutton "Уйти" style "lockpick_button":
        action Return(False)
        align (0.5, 0.95)
        text_size 55

    if lockpick_debug_enabled:
        vbox:
            xalign 0.02
            yalign 0.05
            spacing 6
            hbox:
                label "Сейчас: "
                add "counter"
            hbox:
                label "Необходимо: "
                add "counter2"
            hbox:
                spacing 12
                textbutton "Авто":
                    action Return(True)
                textbutton "Сброс":
                    action [Function(lock.reset), SetVariable("lockpicks", lockpick_initial_picks)]

style lockpick_button is gui_button

label lockpick_game:
    call lockpick_start
    if _return:
        "Открылся"
    else:
        "Попробую потом"
    return

label lockpick_start:
    $ lockpicks = lockpick_initial_picks
    $ _lock_obj = Lock(lockpick_difficulty, 0, resize=lockpick_resize)
    call screen lockpicking(_lock_obj)
    return _return