init python:
    import copy
    import math

    REPAIR_MATRIX_DEFAULT_SHAPES = {
        "square": [(0, 0), (1, 0), (0, 1), (1, 1)],
        "line4": [(0, 0), (1, 0), (2, 0), (3, 0)],
        "l4": [(0, 0), (0, 1), (0, 2), (1, 2)],
        "z4": [(0, 0), (1, 0), (1, 1), (2, 1)],
        "t4": [(0, 1), (1, 0), (1, 1), (2, 1)],
        "line3": [(0, 0), (1, 0), (2, 0)],
        "l3": [(0, 0), (0, 1), (1, 1)],
        "domino": [(0, 0), (1, 0)],
    }

    REPAIR_MATRIX_DEFAULT_BLOCKS = [
        {"id": "A", "shape": "square", "color": "#5898E3"},
        {"id": "B", "shape": "line4", "color": "#EE9361"},
        {"id": "C", "shape": "l4", "color": "#7FCDA1"},
        {"id": "D", "shape": "z4", "color": "#DF78AD"},
        {"id": "E", "shape": "t4", "color": "#DBC272"},
        {"id": "F", "shape": "line3", "color": "#A796EC"},
        {"id": "G", "shape": "l3", "color": "#66D0D6"},
        {"id": "H", "shape": "domino", "color": "#EB7A7A"},
    ]

    REPAIR_MATRIX_DEFAULT_SOLUTION = [
        {"block": 0, "rot": 0, "x": 0, "y": 0},
        {"block": 1, "rot": 0, "x": 2, "y": 0},
        {"block": 2, "rot": 0, "x": 5, "y": 1},
        {"block": 3, "rot": 0, "x": 1, "y": 2},
        {"block": 4, "rot": 0, "x": 0, "y": 4},
        {"block": 5, "rot": 1, "x": 4, "y": 4},
        {"block": 6, "rot": 2, "x": 2, "y": 4},
        {"block": 7, "rot": 1, "x": 6, "y": 4},
    ]

    REPAIR_MATRIX_LEVELS = {
        "standard": {
            "width": 7,
            "height": 7,
            "cell": 62,
            "shapes": REPAIR_MATRIX_DEFAULT_SHAPES,
            "blocks": REPAIR_MATRIX_DEFAULT_BLOCKS,
            "solution": REPAIR_MATRIX_DEFAULT_SOLUTION,
            "require_all_blocks": True,
        },
        "compact_demo": {
            "width": 6,
            "height": 6,
            "cell": 64,
            "shapes": REPAIR_MATRIX_DEFAULT_SHAPES,
            "blocks": [
                {"id": "A", "shape": "square", "color": "#5898E3"},
                {"id": "B", "shape": "line4", "color": "#EE9361"},
                {"id": "C", "shape": "l4", "color": "#7FCDA1"},
                {"id": "D", "shape": "z4", "color": "#DF78AD"},
                {"id": "E", "shape": "line3", "color": "#A796EC"},
                {"id": "F", "shape": "domino", "color": "#EB7A7A"},
            ],
            "target_rows": [4, 3, 4, 2, 3, 1],
            "target_cols": [3, 4, 3, 2, 3, 2],
            "require_all_blocks": False,
        },
    }


    def repair_matrix_parse_color(value):
        if isinstance(value, (list, tuple)) and len(value) >= 3:
            r = max(0, min(255, int(value[0])))
            g = max(0, min(255, int(value[1])))
            b = max(0, min(255, int(value[2])))
            a = max(0, min(255, int(value[3]))) if len(value) > 3 else 255
            return (r, g, b, a)

        if isinstance(value, str):
            raw = value.strip()
            if raw.startswith("#"):
                hx = raw[1:]
                if len(hx) == 6:
                    return (int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16), 255)
                if len(hx) == 8:
                    return (int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16), int(hx[6:8], 16))

        return (120, 170, 220, 255)


    def _repair_norm_shapes(raw_shapes):
        if not isinstance(raw_shapes, dict):
            return copy.deepcopy(REPAIR_MATRIX_DEFAULT_SHAPES)

        out = {}
        for key, pts in raw_shapes.items():
            if not isinstance(pts, (list, tuple)):
                continue
            normalized = []
            for pt in pts:
                if not isinstance(pt, (list, tuple)) or len(pt) < 2:
                    continue
                normalized.append((int(pt[0]), int(pt[1])))
            if normalized:
                out[str(key)] = normalized

        if not out:
            return copy.deepcopy(REPAIR_MATRIX_DEFAULT_SHAPES)
        return out


    def _repair_norm_blocks(raw_blocks, shapes):
        if not isinstance(raw_blocks, (list, tuple)) or len(raw_blocks) == 0:
            raw_blocks = REPAIR_MATRIX_DEFAULT_BLOCKS

        default_shape = list(shapes.keys())[0]
        out = []
        for i, item in enumerate(raw_blocks):
            if not isinstance(item, dict):
                continue
            shape_name = str(item.get("shape", default_shape))
            if shape_name not in shapes:
                shape_name = default_shape
            out.append({
                "id": str(item.get("id", chr(ord("A") + (i % 26)))),
                "shape": shape_name,
                "color": repair_matrix_parse_color(item.get("color", "#78AADC")),
            })

        if not out:
            out = copy.deepcopy(REPAIR_MATRIX_DEFAULT_BLOCKS)
            for item in out:
                item["color"] = repair_matrix_parse_color(item.get("color"))

        return out


    def _repair_norm_solution(raw_solution, blocks_count):
        if not isinstance(raw_solution, (list, tuple)):
            return []

        out = []
        for item in raw_solution:
            if not isinstance(item, dict):
                continue
            b = int(item.get("block", -1))
            if b < 0 or b >= blocks_count:
                continue
            out.append({
                "block": b,
                "rot": int(item.get("rot", 0)) % 4,
                "x": int(item.get("x", 0)),
                "y": int(item.get("y", 0)),
            })
        return out


    def _repair_norm_line(raw_line):
        if not isinstance(raw_line, (list, tuple)):
            return None
        return [max(0, int(v)) for v in raw_line]


    def repair_matrix_resolve_level(
        level=None,
        width=None,
        height=None,
        shapes=None,
        blocks=None,
        solution=None,
        target_rows=None,
        target_cols=None,
        cell=None,
        require_all_blocks=None,
    ):
        cfg = copy.deepcopy(REPAIR_MATRIX_LEVELS["standard"])
        level_id = "standard"

        if isinstance(level, str):
            if level in REPAIR_MATRIX_LEVELS:
                cfg = copy.deepcopy(REPAIR_MATRIX_LEVELS[level])
                level_id = str(level)
        elif isinstance(level, dict):
            preset = level.get("preset")
            if isinstance(preset, str) and preset in REPAIR_MATRIX_LEVELS:
                cfg = copy.deepcopy(REPAIR_MATRIX_LEVELS[preset])
                level_id = str(preset)
            for key, val in level.items():
                if key in ("preset",):
                    continue
                cfg[key] = copy.deepcopy(val)
            level_id = str(level.get("id", level_id if level_id else "custom"))

        if width is not None:
            cfg["width"] = width
        if height is not None:
            cfg["height"] = height
        if shapes is not None:
            cfg["shapes"] = shapes
        if blocks is not None:
            cfg["blocks"] = blocks
        if solution is not None:
            cfg["solution"] = solution
        if target_rows is not None:
            cfg["target_rows"] = target_rows
        if target_cols is not None:
            cfg["target_cols"] = target_cols
        if cell is not None:
            cfg["cell"] = cell
        if require_all_blocks is not None:
            cfg["require_all_blocks"] = require_all_blocks

        cfg["shapes"] = _repair_norm_shapes(cfg.get("shapes"))
        cfg["blocks"] = _repair_norm_blocks(cfg.get("blocks"), cfg["shapes"])

        cfg["width"] = max(4, int(cfg.get("width", 7)))
        cfg["height"] = max(4, int(cfg.get("height", 7)))
        cfg["cell"] = max(36, int(cfg.get("cell", 62)))

        cfg["target_rows"] = _repair_norm_line(cfg.get("target_rows"))
        cfg["target_cols"] = _repair_norm_line(cfg.get("target_cols"))

        if cfg["target_rows"] is not None:
            cfg["height"] = len(cfg["target_rows"])
        if cfg["target_cols"] is not None:
            cfg["width"] = len(cfg["target_cols"])

        cfg["solution"] = _repair_norm_solution(cfg.get("solution"), len(cfg["blocks"]))
        cfg["require_all_blocks"] = bool(cfg.get("require_all_blocks", True))
        cfg["level_id"] = level_id
        return cfg


    class RepairMatrixGame(object):
        def __init__(
            self,
            width=7,
            height=7,
            shapes=None,
            blocks=None,
            solution=None,
            target_rows=None,
            target_cols=None,
            cell=62,
            require_all_blocks=True,
            level_id="custom",
        ):
            self.width = max(4, int(width))
            self.height = max(4, int(height))
            self.cell_size = max(36, int(cell))
            self.level_id = str(level_id)
            self.require_all_blocks = bool(require_all_blocks)

            self.SHAPES = _repair_norm_shapes(shapes)
            self.BLOCKS = _repair_norm_blocks(blocks, self.SHAPES)
            self.SOLUTION = _repair_norm_solution(solution, len(self.BLOCKS))

            self.target_rows = _repair_norm_line(target_rows)
            self.target_cols = _repair_norm_line(target_cols)

            if self.target_rows is not None:
                self.height = len(self.target_rows)
            if self.target_cols is not None:
                self.width = len(self.target_cols)

            self.grid = [[-1 for _x in range(self.width)] for _y in range(self.height)]
            self.placements = [None for _ in self.BLOCKS]
            self.rotations = [0 for _ in self.BLOCKS]

            self.moves = 0
            self.completed = False
            self.message = "Перетащите блоки на матрицу."

            if self.target_rows is None or self.target_cols is None:
                self.target_rows, self.target_cols = self._build_targets_from_solution()

            self._config = {
                "width": self.width,
                "height": self.height,
                "shapes": copy.deepcopy(self.SHAPES),
                "blocks": copy.deepcopy(self.BLOCKS),
                "solution": copy.deepcopy(self.SOLUTION),
                "target_rows": copy.deepcopy(self.target_rows),
                "target_cols": copy.deepcopy(self.target_cols),
                "cell": self.cell_size,
                "require_all_blocks": self.require_all_blocks,
                "level_id": self.level_id,
            }

            self._refresh_completion()

        def _rotated_shape(self, shape_name, rot):
            coords = list(self.SHAPES[str(shape_name)])
            rot = int(rot) % 4

            for _i in range(rot):
                coords = [(y, -x) for (x, y) in coords]

            min_x = min(x for x, _y in coords)
            min_y = min(y for _x, y in coords)
            return [(x - min_x, y - min_y) for (x, y) in coords]

        def _cells_for(self, block_index, x, y, rot=None):
            idx = int(block_index)
            if rot is None:
                rot = self.rotations[idx]
            shape = self._rotated_shape(self.BLOCKS[idx]["shape"], rot)
            return [(int(x) + sx, int(y) + sy) for (sx, sy) in shape]

        def _in_bounds(self, x, y):
            return 0 <= x < self.width and 0 <= y < self.height

        def _build_targets_from_solution(self):
            temp = [[0 for _x in range(self.width)] for _y in range(self.height)]

            for item in self.SOLUTION:
                cells = self._cells_for(item["block"], item["x"], item["y"], item["rot"])
                for x, y in cells:
                    if self._in_bounds(x, y):
                        temp[y][x] = 1

            rows = [sum(temp[y][x] for x in range(self.width)) for y in range(self.height)]
            cols = [sum(temp[y][x] for y in range(self.height)) for x in range(self.width)]
            return rows, cols

        def current_rows(self):
            return [sum(1 for x in range(self.width) if self.grid[y][x] >= 0) for y in range(self.height)]

        def current_cols(self):
            return [sum(1 for y in range(self.height) if self.grid[y][x] >= 0) for x in range(self.width)]

        def _can_place_cells(self, cells):
            for x, y in cells:
                if not self._in_bounds(x, y):
                    return False
                if self.grid[y][x] >= 0:
                    return False
            return True

        def _place_cells(self, block_index, cells, x, y):
            idx = int(block_index)
            for cx, cy in cells:
                self.grid[cy][cx] = idx
            self.placements[idx] = {
                "x": int(x),
                "y": int(y),
                "rot": int(self.rotations[idx]) % 4,
                "cells": list(cells),
            }

        def remove_block(self, block_index, count_move=False, refresh=True):
            idx = int(block_index)
            placement = self.placements[idx]
            if placement is None:
                return None

            saved = {
                "x": placement["x"],
                "y": placement["y"],
                "rot": placement["rot"],
                "cells": list(placement["cells"]),
            }

            for x, y in placement["cells"]:
                if self._in_bounds(x, y) and self.grid[y][x] == idx:
                    self.grid[y][x] = -1

            self.placements[idx] = None
            if count_move:
                self.moves += 1

            if refresh:
                self._refresh_completion()

            return saved

        def restore_block(self, block_index, placement, refresh=True):
            idx = int(block_index)
            if not placement:
                if refresh:
                    self._refresh_completion()
                return False

            self.rotations[idx] = int(placement["rot"]) % 4
            cells = self._cells_for(idx, placement["x"], placement["y"], self.rotations[idx])
            if not self._can_place_cells(cells):
                if refresh:
                    self._refresh_completion()
                return False

            self._place_cells(idx, cells, placement["x"], placement["y"])
            if refresh:
                self._refresh_completion()
            return True

        def try_place_removed(self, block_index, x, y, count_move=True):
            idx = int(block_index)
            cells = self._cells_for(idx, x, y)

            if not self._can_place_cells(cells):
                return False

            self._place_cells(idx, cells, x, y)
            if count_move:
                self.moves += 1
            self._refresh_completion()
            return True

        def rotate_block(self, block_index):
            idx = int(block_index)
            old_rot = int(self.rotations[idx]) % 4
            new_rot = (old_rot + 1) % 4

            placement = self.placements[idx]
            if placement is None:
                self.rotations[idx] = new_rot
                self.message = "Блок %s повернут." % self.BLOCKS[idx]["id"]
                self._refresh_completion()
                return True

            old_place = self.remove_block(idx, count_move=False, refresh=False)
            self.rotations[idx] = new_rot

            if self.try_place_removed(idx, old_place["x"], old_place["y"], count_move=False):
                self.message = "Блок %s повернут." % self.BLOCKS[idx]["id"]
                return True

            self.rotations[idx] = old_rot
            self.restore_block(idx, old_place, refresh=True)
            self.message = "Поворот не помещается."
            return False

        def _refresh_completion(self):
            rows = self.current_rows()
            cols = self.current_cols()

            if self.require_all_blocks:
                placement_gate = all(p is not None for p in self.placements)
            else:
                placement_gate = True

            self.completed = placement_gate and rows == self.target_rows and cols == self.target_cols
            if self.completed:
                self.message = "Контур отремонтирован."

        def reset(self):
            self.__init__(**copy.deepcopy(self._config))


    class RepairMatrixBoard(renpy.Displayable):
        def __init__(self, game, **kwargs):
            super(RepairMatrixBoard, self).__init__(**kwargs)
            self.game = game

            self.cell = int(self.game.cell_size)
            self.board_x = 128
            self.board_y = 176
            self.board_w = self.game.width * self.cell
            self.board_h = self.game.height * self.cell

            self.tray_cols = 2
            self.slot_w = 285
            self.slot_h = max(98, int(self.cell * 1.55))

            self.tray_x = self.board_x + self.board_w + 96
            self.tray_y = self.board_y
            self.tray_w = self.tray_cols * self.slot_w + (self.tray_cols - 1) * 20

            self.slots = {}
            for i in range(len(self.game.BLOCKS)):
                col = i % self.tray_cols
                row = i // self.tray_cols
                sx = self.tray_x + col * (self.slot_w + 20)
                sy = self.tray_y + row * (self.slot_h + 14)
                self.slots[i] = (sx, sy, self.slot_w, self.slot_h)

            tray_rows = int(math.ceil(float(max(1, len(self.game.BLOCKS))) / float(self.tray_cols)))
            self.tray_panel_h = tray_rows * (self.slot_h + 14) + 24

            self.width = max(1520, self.tray_x + self.tray_w + 80)
            self.height = max(820, self.board_y + self.board_h + 140, self.tray_y - 22 + self.tray_panel_h + 120)

            self.z_order = [i for i in range(len(self.game.BLOCKS))]

            self.selected_idx = 0
            self.drag_idx = None
            self.drag_origin = None
            self.drag_px = 0.0
            self.drag_py = 0.0
            self.drag_off_x = 0.0
            self.drag_off_y = 0.0

            self.pointer_down_idx = None
            self.pointer_down_x = 0.0
            self.pointer_down_y = 0.0

            self.drag_start_threshold = 10.0
            self.last_click_idx = None
            self.last_click_st = -99.0
            self.last_click_x = 0.0
            self.last_click_y = 0.0

        def _draw_text(self, render, text, x, y, size=22, color="#f2f9ff", align=0.0):
            d = Text(str(text), size=int(size), color=str(color), outlines=[(1, "#00000099", 0, 0)])
            tr = renpy.render(d, self.width, self.height, 0, 0)
            tw, _th = tr.get_size()
            render.blit(tr, (int(x - tw * align), int(y)))

        def _shape_dims(self, block_index, rot=None):
            idx = int(block_index)
            if rot is None:
                rot = self.game.rotations[idx]
            shape = self.game._rotated_shape(self.game.BLOCKS[idx]["shape"], rot)
            max_x = max(x for x, _y in shape)
            max_y = max(y for _x, y in shape)
            return (max_x + 1, max_y + 1)

        def _piece_top_left(self, block_index):
            idx = int(block_index)

            if self.drag_idx == idx:
                return (self.drag_px, self.drag_py)

            placement = self.game.placements[idx]
            if placement is not None:
                return (
                    self.board_x + placement["x"] * self.cell,
                    self.board_y + placement["y"] * self.cell,
                )

            sx, sy, sw, sh = self.slots[idx]
            w, h = self._shape_dims(idx)
            pw = w * self.cell
            ph = h * self.cell
            return (sx + (sw - pw) / 2.0, sy + (sh - ph) / 2.0)

        def _piece_rects(self, block_index, top_left=None):
            idx = int(block_index)
            if top_left is None:
                top_left = self._piece_top_left(idx)

            px, py = top_left
            shape = self.game._rotated_shape(self.game.BLOCKS[idx]["shape"], self.game.rotations[idx])
            rects = []
            for sx, sy in shape:
                rects.append((
                    int(px + sx * self.cell),
                    int(py + sy * self.cell),
                    self.cell,
                    self.cell,
                ))
            return rects

        def _piece_at(self, x, y):
            candidates = list(self.z_order)
            candidates.reverse()
            for idx in candidates:
                if self.drag_idx == idx:
                    continue
                for rx, ry, rw, rh in self._piece_rects(idx):
                    if rx <= x <= rx + rw and ry <= y <= ry + rh:
                        return idx
            return None

        def _set_selected(self, idx):
            if idx is None:
                return
            self.selected_idx = int(idx)
            if self.selected_idx in self.z_order:
                self.z_order.remove(self.selected_idx)
                self.z_order.append(self.selected_idx)

        def _start_drag(self, idx, x, y):
            idx = int(idx)
            self._set_selected(idx)

            current_top_left = self._piece_top_left(idx)
            self.drag_idx = idx
            self.drag_origin = self.game.remove_block(idx, count_move=False, refresh=False)

            self.drag_px = float(current_top_left[0])
            self.drag_py = float(current_top_left[1])
            self.drag_off_x = float(x) - self.drag_px
            self.drag_off_y = float(y) - self.drag_py

            self.game.message = "Перетащите блок %s на матрицу." % self.game.BLOCKS[idx]["id"]
            self.game._refresh_completion()

        def _drop_drag(self):
            if self.drag_idx is None:
                return

            idx = int(self.drag_idx)
            gx = int(round((self.drag_px - self.board_x) / float(self.cell)))
            gy = int(round((self.drag_py - self.board_y) / float(self.cell)))

            placed = self.game.try_place_removed(idx, gx, gy, count_move=True)
            if placed:
                self.game.message = "Блок %s установлен." % self.game.BLOCKS[idx]["id"]
            else:
                if self.drag_origin is not None:
                    self.game.restore_block(idx, self.drag_origin, refresh=True)
                    self.game.message = "Блок %s возвращен на прежнее место." % self.game.BLOCKS[idx]["id"]
                else:
                    self.game._refresh_completion()
                    self.game.message = "Блок сюда не помещается."

            self.drag_idx = None
            self.drag_origin = None
            self.drag_off_x = 0.0
            self.drag_off_y = 0.0
            self.pointer_down_idx = None

        def _rotate_selected(self):
            idx = self.drag_idx if self.drag_idx is not None else self.selected_idx
            if idx is None:
                return

            idx = int(idx)
            self.game.rotate_block(idx)

        def event(self, ev, x, y, st):
            import pygame

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                idx = self._piece_at(x, y)
                if idx is not None:
                    self._set_selected(idx)
                    self.pointer_down_idx = int(idx)
                    self.pointer_down_x = float(x)
                    self.pointer_down_y = float(y)
                else:
                    self.pointer_down_idx = None

            elif ev.type == pygame.MOUSEMOTION:
                if self.drag_idx is not None:
                    self.drag_px = float(x) - self.drag_off_x
                    self.drag_py = float(y) - self.drag_off_y
                elif self.pointer_down_idx is not None:
                    dx = float(x) - self.pointer_down_x
                    dy = float(y) - self.pointer_down_y
                    if (dx * dx + dy * dy) >= (self.drag_start_threshold * self.drag_start_threshold):
                        self._start_drag(self.pointer_down_idx, self.pointer_down_x, self.pointer_down_y)
                        self.pointer_down_idx = None
                        if self.drag_idx is not None:
                            self.drag_px = float(x) - self.drag_off_x
                            self.drag_py = float(y) - self.drag_off_y

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                if self.drag_idx is not None:
                    self._drop_drag()
                elif self.pointer_down_idx is not None:
                    idx = int(self.pointer_down_idx)
                    dt = float(st) - self.last_click_st
                    dx = float(x) - self.last_click_x
                    dy = float(y) - self.last_click_y
                    is_double_click = (
                        self.last_click_idx == idx and
                        dt <= 0.34 and
                        (dx * dx + dy * dy) <= (18.0 * 18.0)
                    )

                    if is_double_click:
                        self._set_selected(idx)
                        self.game.rotate_block(idx)
                        self.last_click_idx = None
                        self.last_click_st = -99.0
                    else:
                        self._set_selected(idx)
                        self.game.message = "Блок %s выбран. Двойной клик для поворота." % self.game.BLOCKS[idx]["id"]
                        self.last_click_idx = idx
                        self.last_click_st = float(st)
                        self.last_click_x = float(x)
                        self.last_click_y = float(y)
                    self.pointer_down_idx = None

            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_r:
                self._rotate_selected()

        def _ghost_preview(self):
            if self.drag_idx is None:
                return None

            idx = int(self.drag_idx)
            gx = int(round((self.drag_px - self.board_x) / float(self.cell)))
            gy = int(round((self.drag_py - self.board_y) / float(self.cell)))
            cells = self.game._cells_for(idx, gx, gy)

            valid = True
            for cx, cy in cells:
                if not self.game._in_bounds(cx, cy):
                    valid = False
                    break
                if self.game.grid[cy][cx] >= 0:
                    valid = False
                    break

            return (cells, valid)

        def _draw_piece(self, canvas, render, idx, top_left, alpha_mul=1.0):
            block = self.game.BLOCKS[idx]
            color = block["color"]
            shade = (
                int(color[0] * 0.62),
                int(color[1] * 0.62),
                int(color[2] * 0.62),
                int(color[3] * alpha_mul),
            )
            fill = (
                int(color[0]),
                int(color[1]),
                int(color[2]),
                int(color[3] * alpha_mul),
            )

            rects = self._piece_rects(idx, top_left=top_left)
            for rx, ry, rw, rh in rects:
                canvas.rect(shade, (rx + 3, ry + 3, rw - 6, rh - 6), 0)
                canvas.rect(fill, (rx + 1, ry + 1, rw - 2, rh - 2), 0)
                canvas.rect((240, 246, 255, int(180 * alpha_mul)), (rx + 1, ry + 1, rw - 2, rh - 2), 2)

            if rects:
                cx = rects[0][0] + rects[0][2] // 2
                cy = rects[0][1] + rects[0][3] // 2 - 13
                self._draw_text(render, block["id"], cx, cy, 24, "#f8fbff", 0.5)

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            canvas = render.canvas()

            canvas.rect((10, 16, 26, 255), (0, 0, self.width, self.height), 0)

            panel = (66, 96, 620, max(640, self.board_h + 170))
            canvas.rect((18, 30, 48, 255), panel, 0)
            canvas.rect((88, 126, 162, 190), panel, 2)

            tray_panel = (self.tray_x - 18, self.tray_y - 22, self.tray_w + 36, self.tray_panel_h)
            canvas.rect((17, 29, 45, 255), tray_panel, 0)
            canvas.rect((88, 126, 162, 140), tray_panel, 2)

            self._draw_text(render, "РЕМОНТ МАТРИЦЫ", panel[0], 40, 52, "#f7fbff", 0.0)
            self._draw_text(render, "Уровень: %s" % self.game.level_id, panel[0], 86, 20, "#93b8dc", 0.0)
            self._draw_text(render, "LMB: перетаскивание | двойной LMB или R: поворот", panel[0], 110, 22, "#c7ddf4", 0.0)
            self._draw_text(render, "Ходы: %s" % self.game.moves, panel[0], 138, 24, "#ffd7a8", 0.0)
            self._draw_text(render, self.game.message, panel[0], 166, 21, "#ffe9a9", 0.0)

            current_cols = self.game.current_cols()
            for x in range(self.game.width):
                now = current_cols[x]
                target = self.game.target_cols[x]
                ok = now == target
                bx = self.board_x + x * self.cell
                by = self.board_y - 44
                canvas.rect((28, 44, 64, 255), (bx + 2, by + 2, self.cell - 4, 32), 0)
                border = (130, 221, 151, 210) if ok else (221, 140, 140, 210)
                canvas.rect(border, (bx + 2, by + 2, self.cell - 4, 32), 2)
                self._draw_text(render, "%s/%s" % (now, target), bx + self.cell / 2.0, by + 6, 16, "#edf7ff", 0.5)

            current_rows = self.game.current_rows()
            for y in range(self.game.height):
                now = current_rows[y]
                target = self.game.target_rows[y]
                ok = now == target
                bx = self.board_x - 70
                by = self.board_y + y * self.cell
                canvas.rect((28, 44, 64, 255), (bx + 2, by + 2, 62, self.cell - 4), 0)
                border = (130, 221, 151, 210) if ok else (221, 140, 140, 210)
                canvas.rect(border, (bx + 2, by + 2, 62, self.cell - 4), 2)
                self._draw_text(render, "%s/%s" % (now, target), bx + 33, by + 18, 16, "#edf7ff", 0.5)

            for y in range(self.game.height):
                for x in range(self.game.width):
                    rx = self.board_x + x * self.cell
                    ry = self.board_y + y * self.cell
                    cell_bg = (24, 38, 56, 255)
                    owner = self.game.grid[y][x]
                    if owner >= 0:
                        c = self.game.BLOCKS[owner]["color"]
                        cell_bg = (int(c[0] * 0.45), int(c[1] * 0.45), int(c[2] * 0.45), 255)

                    canvas.rect(cell_bg, (rx + 2, ry + 2, self.cell - 4, self.cell - 4), 0)
                    canvas.rect((92, 128, 160, 120), (rx + 1, ry + 1, self.cell - 2, self.cell - 2), 1)

            preview = self._ghost_preview()
            if preview is not None:
                cells, valid = preview
                ghost = (114, 206, 133, 130) if valid else (220, 116, 116, 130)
                for cx, cy in cells:
                    if self.game._in_bounds(cx, cy):
                        gx = self.board_x + cx * self.cell
                        gy = self.board_y + cy * self.cell
                        canvas.rect(ghost, (gx + 5, gy + 5, self.cell - 10, self.cell - 10), 0)

            for idx in self.z_order:
                if idx == self.drag_idx:
                    continue
                top_left = self._piece_top_left(idx)
                self._draw_piece(canvas, render, idx, top_left)

            if self.drag_idx is not None:
                self._draw_piece(canvas, render, int(self.drag_idx), (self.drag_px, self.drag_py), alpha_mul=0.95)

            for idx in range(len(self.game.BLOCKS)):
                sx, sy, sw, sh = self.slots[idx]
                selected = idx == self.selected_idx
                has_place = self.game.placements[idx] is not None
                border = (88, 126, 162, 110)
                if has_place:
                    border = (120, 203, 144, 170)
                if selected:
                    border = (120, 194, 255, 220)
                canvas.rect(border, (sx, sy, sw, sh), 2)

            if self.game.completed:
                self._draw_text(render, "КОНТУР ОТРЕМОНТИРОВАН", panel[0], min(self.height - 70, panel[1] + panel[3] + 10), 42, "#b6ffbe", 0.0)

            renpy.redraw(self, 0.016)
            return render


screen repair_matrix_screen(game):
    modal True
    tag repair_matrix

    default board = RepairMatrixBoard(game)

    add Solid("#070c13f0")

    fixed:
        add board:
            xalign 0.5
            yalign 0.5

        hbox:
            spacing 12
            align (0.97, 0.96)

            textbutton "Сброс":
                action Function(game.reset)
                text_size 34

            if game.completed:
                textbutton "Готово":
                    action Return(True)
                    text_size 34
            else:
                textbutton "Уйти":
                    action Return(False)
                    text_size 34


label repair_matrix_minigame(
    level=None,
    width=None,
    height=None,
    shapes=None,
    blocks=None,
    solution=None,
    target_rows=None,
    target_cols=None,
    cell=None,
    require_all_blocks=None,
):
    $ _repair_cfg = repair_matrix_resolve_level(
        level=level,
        width=width,
        height=height,
        shapes=shapes,
        blocks=blocks,
        solution=solution,
        target_rows=target_rows,
        target_cols=target_cols,
        cell=cell,
        require_all_blocks=require_all_blocks,
    )
    $ _repair_game = RepairMatrixGame(**_repair_cfg)
    call screen repair_matrix_screen(_repair_game)
    return _return


label test_repair_matrix_minigame:
    scene black
    with fade
    "Тест мини-игры: ремонт матрицы."
    call repair_matrix_minigame(level="standard")
    if _return:
        "Матрица восстановлена."
    else:
        "Выход из теста."
    return
