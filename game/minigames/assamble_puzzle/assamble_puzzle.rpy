#region Constants
# Game board grid
define block_size = 80
define offset_x = 1100
define offset_y = 100

# Target shape mask (1 = must be filled)
define puzzle_mask_1 = [
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0]
]

# State
default puzzle = None
default puzzle_mask = puzzle_mask_1
default parts = []
default current_puzzle_level = 1
default puzzle_level = 1
default puzzle_win_played = False

# Color scheme for UI elements
default c1 = "#1d96db"  # Primary blue
default c2 = "#d62a2a"  # Error red
default c3 = "#454545"  # Neutral gray

#endregion

#region Images

image handle:
    Solid("#fff", xsize=block_size, ysize=block_size)
    alpha 0.6

image puzzle_borders_1 = "minigames/assamble_puzzle/bomb_borders_1.png"
image puzzle_borders_2 = "minigames/assamble_puzzle/bomb_borders_2.png"
image puzzle_borders_3 = "minigames/assamble_puzzle/bomb_borders_3.png"

# Basic shapes
image long_shape = "minigames/assamble_puzzle/long_shape.png"
image corner_shape = "minigames/assamble_puzzle/corner_shape.png"
image square_shape = "minigames/assamble_puzzle/square_shape.png"
image z_shape = "minigames/assamble_puzzle/z_shape.png"

image o_z_shape = Transform("z_shape", xzoom=-1.0)

image t_shape = "minigames/assamble_puzzle/t_shape.png"

# Extended shapes
image shape_1 = "minigames/assamble_puzzle/shape_1.png"
image shape_2 = "minigames/assamble_puzzle/shape_2.png"
image shape_3 = "minigames/assamble_puzzle/shape_3.png"
image shape_4 = "minigames/assamble_puzzle/shape_4.png"
image shape_5 = "minigames/assamble_puzzle/shape_5.png"
image shape_6 = "minigames/assamble_puzzle/shape_6.png"
image shape_7 = "minigames/assamble_puzzle/shape_7.png"
image shape_8 = "minigames/assamble_puzzle/shape_8.png"
image shape_9 = "minigames/assamble_puzzle/shape_9.png"
image shape_10 = "minigames/assamble_puzzle/shape_10.png"
image shape_11 = "minigames/assamble_puzzle/shape_11.png"
image shape_12 = "minigames/assamble_puzzle/shape_12.png"
image shape_13 = "minigames/assamble_puzzle/shape_13.png"
image shape_14 = "minigames/assamble_puzzle/shape_14.png"

# Variants used by level 2 configs
image shape_2_1 = "minigames/assamble_puzzle/shape_2_1.png"
image shape_2_2 = "minigames/assamble_puzzle/shape_2_2.png"
image shape_2_3 = "minigames/assamble_puzzle/shape_2_3.png"

#endregion
#region Shape templates

init python:
    # Basic piece masks (1 = occupied cell)
    long_shape = [
        [1, 1, 1, 1]
    ]

    corner_shape = [
        [1, 1],
        [0, 1]
    ]

    square_shape = [
        [1, 1],
        [1, 1]
    ]

    z_shape = [
        [0, 1],
        [1, 1],
        [1, 0]
    ]

    o_z_shape = [
        [1, 0],
        [1, 1],
        [0, 1]
    ]

    t_shape = [
        [1, 1, 1],
        [0, 1, 0]
    ]

    # Extended set for level 3 (distinct shapes)
    shape_1 = [
        [1, 1, 1],
        [1, 0, 0]
    ]

    shape_2 = [
        [1, 1, 1],
        [0, 0, 1]
    ]

    shape_3 = [
        [1, 1, 1],
        [0, 1, 0]
    ]

    shape_4 = [
        [0, 1, 1],
        [1, 1, 0]
    ]

    shape_5 = [
        [1, 1, 1, 1]
    ]

    shape_6 = [
        [1, 0],
        [1, 1]
    ]

    shape_7 = [
        [1],
        [1],
        [1]
    ]

    shape_8 = [
        [1, 1, 0],
        [0, 1, 1]
    ]

    shape_9 = [
        [1, 0, 1],
        [1, 1, 1]
    ]

    shape_10 = [
        [1, 0, 0],
        [1, 1, 1]
    ]

    shape_11 = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    shape_12 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]

    shape_13 = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 1]
    ]

    shape_14 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]

    # Level 2 additional shapes
    shape_2_1 = [
        [1, 1, 1]
    ]

    shape_2_2 = [
        [1, 1],
        [1, 0]
    ]

    shape_2_3 = [
        [0, 1, 0],
        [1, 1, 1]
    ]

#endregion

#region Classes

init python:

    #region Board class

    class PuzzleBoard(object):
        def __init__(self, width, height, parts, block_size=block_size, ox=offset_x, oy=offset_y, level=1, mask=None):
            self.group = DragGroup()
            self.parts = parts

            # Add all parts to the drag group
            for p in self.parts:
                p.set_group(self.group)

            self.x = width
            self.y = height
            self.ox = ox
            self.oy = oy
            self.block_size = block_size
            self.level = level
            self.mask = mask
            self.borders = "puzzle_borders_%s" % self.level

            # Initialize board grid
            self.board = []
            self.data = []

            for row in range(self.y):
                self.board.append([])
                self.data.append([])
                for col in range(self.x):
                    self.data[row].append(0)
                    # Create draggable placeholder for valid positions
                    if self.mask[row][col]:
                        drag_element = Drag(
                            Fixed("#fff",
                                    Fixed("#000", xysize=(self.block_size-2, self.block_size-2), align=(0.5, 0.5)),
                                    xysize=(self.block_size, self.block_size)),
                            pos=(self.ox + col * self.block_size, self.oy + row * self.block_size),
                            draggable=False,
                            drag_name=(col, row)
                        )
                        self.board[row].append(drag_element)
                        self.group.add(self.board[row][col])
                    else:
                        self.board[row].append(None)
        def verify(self):
            failed = False

            # Check each position on the board
            for y in range(len(self.data)):
                for x in range(len(self.data[y])):
                    # Every valid position must be filled exactly once
                    if self.mask[y][x] and self.data[y][x] != 1:
                        failed = True
                        break
                if failed:
                    break

            if failed:
                if preferences.puzzle_resets:
                    renpy.notify(_("Not a valid solution."))
                    return
                else:
                    renpy.jump("puzzle_game_over")
            else:
                store.room1["puzzle"] = "solved"
                clear_puzzle("room1_1")
                return True

        def is_solved(self):
            for y in range(len(self.data)):
                for x in range(len(self.data[y])):
                    if self.mask[y][x] and self.data[y][x] != 1:
                        return False
            return True

        def reset_drags(self):
            """
            Reset all drag elements to their initial positions.
            Used when restarting the puzzle.
            """
            # Reset all part positions
            for p in parts:
                p.display.target_at = 0.0
                for h in p.handles:
                    for d in h:
                        if d:
                            d.target_at = 0.0

            for y in puzzle.board:
                for x in y:
                    if x:
                        x.target_at = 0.0
    #endregion
    #region Part class

    default_shape = [
        [1, 1],
        [0, 1]
        ]

    class Piece(object):
        """
        Represents an individual puzzle piece that can be dragged and rotated.
        Handles all the drag-and-drop mechanics and collision detection.
        """

        def __init__(self, shape=None, bond="triple", color="#fff", pos=(600, 400), initial_rotation_degrees=0):
            """
            Initialize a puzzle piece.

            Args:
                shape: Name of the shape template to use
                bond: Connection type (unused)
                color: Hex color for the piece
                pos: Initial position (x, y)
            """

            # Load shape template from Ren'Py store or use default
            shape_template = getattr(renpy.store, "%s" % shape, None)
            if shape_template is None:
                log_debug("Warning: Shape '%s' not found in renpy.store, using default shape" % shape)
                self.shape = [row[:] for row in default_shape]
            else:
                self.shape = [row[:] for row in shape_template]
            self.shape_name = shape
            # Apply initial rotation to data shape (0/90/180/270)
            rotation_steps = int((initial_rotation_degrees // 90) % 4)
            for _ in range(rotation_steps):
                self.shape = list(zip(*self.shape[::-1]))
            self.rotation = rotation_steps

            # Position management
            self.x = pos[0]
            self.y = pos[1]
            self.bench_x = pos[0]  # Initial bench position
            self.bench_y = pos[1]  # Initial bench position

            # Visual properties
            self.color = color
            # Use the Ren'Py image with the same name as shape for visuals
            self.img = Transform(self.shape_name, matrixcolor=TintMatrix(color))
            self.last_filled = []  # Track which board positions this piece occupies

            # Drag handles for each filled cell in the shape
            self.handles = [[None for x in range(len(self.shape[0]))] for y in range(len(self.shape))]
            
            for y in range(len(self.shape)):
                for x in range(len(self.shape[0])):
                    if self.shape[y][x]:
                        self.handles[y][x] = Drag('handle',
                                                    pos=(self.x+x*block_size, self.y+y*block_size),
                                                    droppable=False,
                                                    drag_name=(self.bench_x, self.bench_y),
                                                    drag_joined=self.joined,
                                                    dragged=renpy.curry(dragged)(self),
                                                    dragging=renpy.curry(dragging)(self),
                                                    clicked=self.rotate,
                                                    alternate=renpy.curry(self.rotate)(False),
                                                    mouse_drop=True,
                                                    drag_offscreen=False)
            self.display = Drag(Transform(self.img, rotate_pad=False),
                                pos=(self.x, self.y),
                                drag_name=(self.bench_x, self.bench_y),
                                draggable=False,
                                droppable=False,
                                dragged=renpy.curry(dragged)(self),
                                dragging=renpy.curry(dragging)(self),
                                drag_joined=self.joined,
                                drag_handle=(0,0,0,0),
                                clicked=self.rotate,
                                alternate=renpy.curry(self.rotate)(False),
                                drag_offscreen=True,
                                focus_mask=True)
            # Apply initial visual rotation
            if self.rotation:
                self.display.child.rotate = self.rotation * 90
                self.display.child.update()
        
        def joined(self, drag):
            ret = [(self.display, 0, 0)]
            for y in range(len(self.shape)):
                for x in range(len(self.shape[0])):
                    if self.shape[y][x] > 0:
                        ret.append((self.handles[y][x], x*block_size, y*block_size))
            
            for t in ret:
                if t[0] == drag:
                    t[0].handle = True
                elif t[0]:
                    t[0].handle = False
            return ret
        
        def rotate(self, cw=True):
            if cw:
                self.rotation += 1
                self.rotation = 0 if self.rotation == 4 else self.rotation
                self.shape = list(zip(*self.shape[::-1]))
                self.handles = list(map(list, list(zip(*self.handles[::-1]))))
            else:
                self.rotation -= 1
                self.rotation = 3 if self.rotation == -1 else self.rotation
                self.shape = list(zip(*self.shape[::-1]))
                self.handles = list(map(list, list(zip(*self.handles[::-1]))))
                self.shape = list(zip(*self.shape[::-1]))
                self.handles = list(map(list, list(zip(*self.handles[::-1]))))
                self.shape = list(zip(*self.shape[::-1]))
                self.handles = list(map(list, list(zip(*self.handles[::-1]))))
            try:
                renpy.music.play(sfx_puzzle_click_rotate, channel="sfx")
            except Exception:
                pass

            for y in range(len(self.handles)):
                for x in range(len(self.handles[y])):
                    if self.handles[y][x]:
                        self.handles[y][x].snap(int(self.display.x+x*block_size), int(self.display.y+y*block_size))
            self.display.child.rotate = self.rotation*90
            self.display.child.update()
            ox, oy = (math.floor((self.display.x-puzzle.ox)/block_size),
                        math.floor((self.display.y-puzzle.oy)/block_size))
            if self.last_filled:
                for (x, y) in self.last_filled:
                    puzzle.data[y][x] -= 1
                    self.display.snap(int(offset_x+ox*block_size), int(offset_y+oy*block_size))
            self.last_filled = []
            not_filled = False
            for y in range(len(self.shape)):
                for x in range(len(self.shape[y])):
                    if self.shape[y][x]:
                        if not 0 <= ox+x < len(puzzle.mask[0]) or \
                            not 0 <= oy+y < len(puzzle.mask) or \
                            not puzzle.mask[oy+y][ox+x]:
                            not_filled = True
                            break
                        self.last_filled.append((ox+x, oy+y))
                if not_filled: break
            if not not_filled:
                for (x, y) in self.last_filled:
                    puzzle.data[y][x] += 1
                self.display.snap(int(offset_x+ox*block_size), int(offset_y+oy*block_size))
                for y in range(len(self.handles)):
                    for x in range(len(self.handles[y])):
                        if self.handles[y][x]:
                            pass
                            self.handles[y][x].snap(int(offset_x+ox*block_size+x*block_size),
                                                    int(offset_y+oy*block_size+y*block_size))
                try:
                    renpy.music.play(sfx_puzzle_place, channel="sfx")
                except Exception:
                    pass
            else:
                self.last_filled = []
                self.display.snap(self.display.x, self.display.y)
            attempt_auto_complete()
            # Play victory sound exactly once at the moment the puzzle becomes solved
            if puzzle.is_solved():
                on_puzzle_solved_event()
            renpy.retain_after_load()
            renpy.restart_interaction()
        
        def __eq__(self, other):
            return False
        
        def set_group(self, g):
            g.add(self.display)
            for d in [d for row in self.handles for d in row if d is not None]:
                g.add(d)

    #endregion
#endregion

    #region Functions

    def dragged(part, drags, drop):
        drag = drags[0]
        if drop:
            if drag == part.display:
                mx, my = renpy.get_mouse_pos()
                offx, offy = (int(math.floor((mx-drag.x)/block_size)),int(math.floor((my-drag.y)/block_size)))
                for py in range(len(part.handles)):
                    for px in range(len(part.handles[py])):
                        if part.handles[py][px]:
                            part.handles[py][px].handle = (px, py) == (offx, offy)
            x, y = drop.drag_name
            handle = [d for d in drags if d and d.handle]
            if handle:
                for py in range(len(part.handles)):
                    for px in range(len(part.handles[py])):
                        if part.handles[py][px] and part.handles[py][px].handle:
                            ox, oy = (px, py)
                            break
            else:
                ox, oy = (1, 1)
            filled = []
            for py in range(len(part.handles)):
                for px in range(len(part.handles[py])):
                    if part.handles[py][px]:
                        pox, poy = (x+px-ox, y+py-oy)
                        if not 0 <= pox < len(puzzle.mask[0]) or \
                        not 0 <= poy < len(puzzle.mask) or \
                        not puzzle.mask[poy][pox]:
                            return
                        filled.append((pox, poy))
            for (fx, fy) in filled:
                puzzle.data[fy][fx] += 1
            part.last_filled = filled
            for py in range(len(part.handles)):
                for px in range(len(part.handles[py])):
                    if part.handles[py][px]:
                        part.handles[py][px].snap(puzzle.ox+x*block_size+px*block_size-ox*block_size,
                                                    puzzle.oy+y*block_size+py*block_size-oy*block_size)
            part.display.snap(puzzle.ox+x*block_size-ox*block_size,
                                puzzle.oy+y*block_size-oy*block_size)
            try:
                renpy.music.play(sfx_puzzle_place, channel="sfx")
            except Exception:
                pass
        else:
            for py in range(len(part.handles)):
                for px in range(len(part.handles[py])):
                    if part.handles[py][px]:
                        part.handles[py][px].snap(part.display.x+px*block_size,
                                                    part.display.y+py*block_size)

        renpy.retain_after_load()
        # Play victory sound exactly once at the moment the puzzle becomes solved
        if puzzle.is_solved():
            on_puzzle_solved_event()
        renpy.restart_interaction()

    def dragging(part, drags):
        if part.last_filled:
            for (x, y) in part.last_filled:
                puzzle.data[y][x] -= 1
            part.last_filled = []
            renpy.retain_after_load()
            renpy.restart_interaction()

    def activated(drags):
        return



#endregion
#region Auto-complete

init python:
    def attempt_auto_complete():
        """
        Placeholder for future auto-complete logic.
        Currently a no-op to prevent NameError on rotate.
        """
        return

#endregion
#region Level configuration

# Level data for different difficulty levels
define level_configs = {
    1: {
        "parts": [
            ("long_shape", (363, 173), "#E97B9A", 90),
            ("corner_shape", (679, 171), "#00E6E3"),
            ("square_shape", (606, 246), "#52CD6A"),
            ("z_shape", (762, 251), "#E3615A"),
            ("corner_shape", (451, 249), "#0087E8"),
            ("o_z_shape", (372, 250), "#E88D26"),
            ("z_shape", (211, 252), "#51A35B")
        ],
        "mask": puzzle_mask_1
    }
}
#endregion

#region Game initialization and utility functions

init python:
    def puzzle_cleared(puzzle_id):
        """
        Check if puzzle is cleared.
        Args:
            puzzle_id: Puzzle identifier
        Returns:
            bool: True if puzzle is solved
        """
        if puzzle_id == "room1_1":
            return room1.get("puzzle") == "solved"
        return False

    def on_puzzle_solved_event():
        if not store.puzzle_win_played:
            store.puzzle_win_played = True
            try:
                renpy.music.stop(channel="sfx")
                renpy.music.play(sfx_puzzle_win, channel="sfx")
            except Exception:
                pass

    def clear_puzzle(puzzle_id):
        """
        Mark puzzle as cleared.
        Args:
            puzzle_id: Puzzle identifier to clear
        """
        if puzzle_id == "system_hacked":
            room2_data["system_hacked"] = "True"

    def init_puzzle_function(txt=None):
        """
        Initialize or reset the bomb puzzle.

        Args:
            txt: Optional notification message to display
        """
        store.parts = []
        store.puzzle_win_played = False

        config = level_configs.get(puzzle_level, level_configs[1])
        bm = config["mask"]
        renpy.log("Initializing puzzle for difficulty level: %d" % puzzle_level)
        renpy.log("Using mask with dimensions: %dx%d" % (len(bm[0]), len(bm)))

        # Create parts for this level
        for item in config["parts"]:
            # Support tuples of 3 or 4 elements: (shape, pos, color[, rotation_degrees])
            if len(item) == 4:
                shape_name, pos, color, rot = item
            else:
                shape_name, pos, color = item
                rot = 0
            renpy.log("Creating piece with shape: %s, position: %s, color: %s, rot: %s" % (shape_name, pos, color, rot))
            store.parts.append(Piece(shape_name, pos=pos, color=color, initial_rotation_degrees=rot))

        store.puzzle = PuzzleBoard(len(bm[0]), len(bm), parts, level=puzzle_level, mask=bm)
        store.current_puzzle_level = puzzle_level

        if txt:
            renpy.notify(txt)
            renpy.hide_screen("room1_puzzle")
            renpy.show_screen("room1_puzzle", puzzle)

label init_puzzle:
    $ init_puzzle_function()
    return

#endregion

#region labels

label assemble_puzzle:
    $ puzzle_level = 1
    call init_puzzle
    call screen room1_puzzle(puzzle, interactable=True)
    return _return

label test_puzzle:
    scene bg room1

    # Test menu for different difficulty levels
    menu:
        "Test Difficulty Level 1":
            $ puzzle_level = 1
            jump test_puzzle_start

        "Return to Main Menu":
            return

label test_puzzle_start:
    """
    Start the bomb puzzle test with current difficulty level.
    """
    call init_puzzle

    # Show instructions
    "Testing assembly puzzle - Level [puzzle_level]"
    "Drag and drop the pieces to fill the target shape."
    "Right-click pieces to rotate them."

    # Start the puzzle
    call screen room1_puzzle(puzzle, interactable=True)

    # Handle result
    if _return == True:
        "Puzzle solved successfully!"
    else:
        "Puzzle test completed."

    jump test_puzzle

label puzzle_game_over:
    """
    Game over label for bomb puzzle.
    Called when player fails the puzzle.
    """
    scene bg room1

    "К сожалению, пазл не был собран правильно."
    "Попробуй изменить расположение деталей."
    "Игра окончена."

    # Return to main menu or restart
    menu:
        "Попробовать снова":
            call init_puzzle
            call screen room1_puzzle(puzzle, interactable=True)

        "Вернуться в комнату":
            return


#endregion

#region UI screens


# Skip button for puzzle skipping functionality
screen skip_button(room_dict, puzzle_name, puzzle_id, yoffset=0, xalign=1.0, xoffset=0):
    """
    Skip button for puzzle games.
    Allows skipping a puzzle and marking it as solved.

    Args:
        room_dict: Dictionary containing room state (e.g., room1)
        puzzle_name: Name of the puzzle (e.g., "bomb")
        puzzle_id: Puzzle identifier (e.g., "room1_1")
        yoffset: Y offset from alignment position
        xalign: X alignment (0.0 = left, 1.0 = right)
        xoffset: X offset from alignment position
    """
    zorder 100

    # Position the button
    fixed:
        xalign xalign
        yalign 0.0
        offset (xoffset, yoffset)

        # Skip button
        textbutton "SKIP":
            style "confirm_button"
            action [
                SetDict(room_dict, puzzle_name, "True"),
                Function(clear_puzzle, puzzle_id),
                Return()
            ]
            sensitive True
            at Transform(zoom=0.75)

screen room1_puzzle(b=None, interactable=True):
    sensitive (interactable and not _menu) tag puzzle
    modal True

    layer "master"

    default completion_pending = False

    if puzzle_level != current_puzzle_level:
        timer 0.1 action Function(init_puzzle_function, None)

    frame:
        padding 20,20,40,50

        fixed:
            add puzzle.borders pos (puzzle.ox-5, puzzle.oy-5)
            add puzzle.group
            fixed:
                pos (puzzle.ox, puzzle.oy)
                for y in range(len(puzzle.data)):
                    for x in range(len(puzzle.data[0])):
                        if puzzle.data[y][x] == 1:
                            add "#ffffff55" xysize (block_size, block_size) pos (x*block_size, y*block_size)
                        elif puzzle.data[y][x] > 1:
                            add "#ff000088" xysize (block_size, block_size) pos (x*block_size, y*block_size)

        if puzzle.is_solved() and not completion_pending:
            $ completion_pending = True
            $ renpy.music.play(sfx_puzzle_win, channel="sfx")
        
        # frame:
        #     align (0.0, 1.0) padding 30,30 offset (0, 30)
        #     xsize 1000
        #     ymaximum 350
        #     has vbox spacing 20
        #     xalign 0.5
        #     label _("Instructions")
        #     text _("Assemble the bomb by placing all pieces correctly on the grid.\nRight-click pieces to rotate them.\nAll valid positions must be filled exactly once.")

        # Control buttons
        hbox xalign 1.0 yalign 1.0 spacing 30:
            textbutton "RESET" style "confirm_button" action [ SetScreenVariable("completion_pending", False), Function(init_puzzle_function, _("Restarting...")) ] xalign 0.0 yalign 0.5 sensitive interactable at Transform(zoom=0.75)
            textbutton "RETURN" style "confirm_button" action [Return(False), With(Dissolve(0.5))]

    if completion_pending:
        timer 2.0 action [Function(clear_puzzle, "room1_1"), Return(True)]

    if config.developer:
        vbox:
            textbutton _("Skip Puzzle") action [SetDict(room2_data, "system_hacked", "true"), Return()] style "confirm_button"
            textbutton _("Game Over") action [Jump("puzzle_game_over")] style "confirm_button"
#endregion