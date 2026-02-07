default extra_gallery_filter = "all"
default extra_gallery_only_unlocked = False
default extra_gallery_index = 0

define EXTRA_GALLERY_AUTO_BG_NAME_PREFIXES = ("bg_", "background_", "bg ", "background ")
define EXTRA_GALLERY_AUTO_BG_EXCLUDE_EXACT = (
    "bg_black",
    "bg_white",
    "bg_red",
    "bg_paper",
    "bg_menu_main",
    "bg_coridor_teni_1",
    "bg_coridor_teni_2",
    "bg_coridor_figuri",
    "bg_coridor_cherkash",
)
define EXTRA_GALLERY_AUTO_BG_EXCLUDE_PREFIXES = ("bg_black_t_",)
define EXTRA_GALLERY_AUTO_BG_NAME_CONTAINS = ("_fon", " fon", "background", "_background", "_bg")
define EXTRA_GALLERY_AUTO_BG_NAME_SUFFIXES = ("_fon", "_background", "_bg", " background")

init python:
    # Настройка пользовательских изображений галереи.
    # Поля: image (обязательно), title, thumb, description, unlock (always/seen/manual), group.
    extra_gallery_custom_entries = [
        {"image": "mirror_default", "title": "Зеркало", "description": "CG из истории.", "unlock": "seen"},
        {"image": "mirror_dark", "title": "Зеркало (тьма)", "description": "CG из истории.", "unlock": "seen"},
        {"image": "mirror_water", "title": "Зеркало (вода)", "description": "CG из истории.", "unlock": "seen"},
        {"image": "room_viktor1", "title": "Комната Виктора I", "description": "CG из истории.", "unlock": "seen"},
        {"image": "room_viktor2", "title": "Комната Виктора II", "description": "CG из истории.", "unlock": "seen"},
        {"image": "room_viktor3", "title": "Комната Виктора III", "description": "CG из истории.", "unlock": "seen"},
    ]
    extra_gallery_cached_entries = None

    if not hasattr(persistent, "extra_gallery_manual_unlocks"):
        persistent.extra_gallery_manual_unlocks = []
    if not hasattr(persistent, "extra_gallery_seen_runtime_images"):
        persistent.extra_gallery_seen_runtime_images = []

    def extra_gallery_title_from_name(raw_name):
        name = str(raw_name or "").strip()
        if not name:
            return "Без названия"
        normalized = name.replace("\\", " ").replace("/", " ").replace("-", " ").replace("_", " ")
        normalized = " ".join(normalized.split())
        if not normalized:
            return "Без названия"
        return normalized[:1].upper() + normalized[1:]

    def extra_gallery_entry(image, title=None, thumb=None, description="", unlock="always", group="custom", item_id=None):
        image_name = str(image or "").strip()
        if not image_name:
            return None

        unlock_mode = str(unlock or "always").lower()
        if unlock_mode not in ("always", "seen", "manual"):
            unlock_mode = "always"

        group_name = str(group or "custom").lower()
        if group_name not in ("custom", "background"):
            group_name = "custom"

        return {
            "id": str(item_id or ("%s::%s" % (group_name, image_name))),
            "image": image_name,
            "thumb": str(thumb or image_name).strip(),
            "title": str(title or extra_gallery_title_from_name(image_name)),
            "description": str(description or ""),
            "unlock": unlock_mode,
            "group": group_name,
        }

    def extra_gallery_add_custom(image, title=None, thumb=None, description="", unlock="always", group="custom", item_id=None):
        global extra_gallery_cached_entries
        entry = extra_gallery_entry(
            image=image,
            title=title,
            thumb=thumb,
            description=description,
            unlock=unlock,
            group=group,
            item_id=item_id,
        )
        if entry:
            extra_gallery_custom_entries.append(entry)
            extra_gallery_cached_entries = None
        return entry

    def extra_gallery_refresh_entries(restart=True):
        global extra_gallery_cached_entries
        extra_gallery_record_visible_backgrounds()
        extra_gallery_cached_entries = None
        if restart:
            renpy.restart_interaction()

    def extra_gallery_runtime_seen_list():
        seen = getattr(persistent, "extra_gallery_seen_runtime_images", [])
        if isinstance(seen, tuple):
            seen = list(seen)
        elif not isinstance(seen, list):
            seen = []
        return seen

    def extra_gallery_mark_seen_image(image_name):
        if not image_name:
            return

        value = str(image_name).strip()
        if not value:
            return

        seen = extra_gallery_runtime_seen_list()

        changed = False
        for candidate in (value, value.lower(), value.replace(" ", "_"), value.replace("_", " ")):
            key = str(candidate).strip().lower()
            if key and key not in seen:
                seen.append(key)
                changed = True

        if changed:
            persistent.extra_gallery_seen_runtime_images = seen
            renpy.save_persistent()

    def extra_gallery_record_visible_backgrounds():
        # Captures actually shown bg* images/tags during gameplay.
        try:
            tags = renpy.get_showing_tags(layer="master")
        except Exception:
            tags = []

        for tag in tags:
            tag_name = str(tag or "").strip()
            if not tag_name:
                continue

            if extra_gallery_is_auto_background(tag_name):
                extra_gallery_mark_seen_image(tag_name)

            try:
                showing_name = renpy.get_showing_image(tag_name, layer="master")
            except Exception:
                showing_name = None

            showing_text = extra_gallery_image_name_from_key(showing_name)
            if showing_text and extra_gallery_is_auto_background(showing_text):
                extra_gallery_mark_seen_image(showing_text)

    if not getattr(store, "_extra_gallery_periodic_hook_installed", False):
        _extra_gallery_old_periodic_callback = getattr(config, "periodic_callback", None)

        def _extra_gallery_periodic_callback():
            if _extra_gallery_old_periodic_callback:
                try:
                    _extra_gallery_old_periodic_callback()
                except Exception:
                    pass
            try:
                extra_gallery_record_visible_backgrounds()
            except Exception:
                pass

        config.periodic_callback = _extra_gallery_periodic_callback
        store._extra_gallery_periodic_hook_installed = True

    def extra_gallery_seen_image(image_name):
        seen_runtime = extra_gallery_runtime_seen_list()
        seen_runtime_set = set([str(raw).strip().lower() for raw in seen_runtime if str(raw).strip()])
        source_name = str(image_name or "").strip()
        if source_name and source_name.lower() in seen_runtime_set:
            return True

        candidates = [source_name]
        if source_name:
            candidates.append(source_name.replace(" ", "_"))
            candidates.append(source_name.replace("_", " "))

        for candidate in candidates:
            name = str(candidate or "").strip()
            if not name:
                continue
            if name.lower() in seen_runtime_set:
                return True
            try:
                if renpy.seen_image(name):
                    return True
            except Exception:
                pass

        try:
            return bool(renpy.seen_image(image_name))
        except Exception:
            return False

    def extra_gallery_is_unlocked(item):
        if not item:
            return False

        unlock_mode = item.get("unlock", "always")
        if unlock_mode == "always":
            return True
        if unlock_mode == "seen":
            return extra_gallery_seen_image(item.get("image", ""))
        if unlock_mode == "manual":
            item_id = item.get("id")
            manual_unlocks = getattr(persistent, "extra_gallery_manual_unlocks", [])
            try:
                return item_id in manual_unlocks
            except Exception:
                return False
        return False

    def extra_gallery_unlock(item_id):
        if not item_id:
            return

        unlocks = getattr(persistent, "extra_gallery_manual_unlocks", [])
        if isinstance(unlocks, tuple):
            unlocks = list(unlocks)
        elif not isinstance(unlocks, list):
            unlocks = []

        if item_id not in unlocks:
            unlocks.append(item_id)
            persistent.extra_gallery_manual_unlocks = unlocks
            renpy.save_persistent()

    def extra_gallery_display_text(item):
        if not item:
            return ""
        description = item.get("description", "").strip()
        if description:
            return description
        if item.get("group") == "background":
            return "Фоновое изображение, открывается автоматически после первого показа в истории."
        return "Пользовательское изображение галереи."

    def extra_gallery_status_text(item):
        if not item:
            return ""
        if extra_gallery_is_unlocked(item):
            return "Статус: открыто"
        unlock_mode = item.get("unlock", "always")
        if unlock_mode == "seen":
            return "Статус: заблокировано, покажите изображение в прохождении."
        if unlock_mode == "manual":
            return "Статус: заблокировано, требуется ручная разблокировка."
        return "Статус: заблокировано"

    def extra_gallery_image_name_from_key(key):
        if isinstance(key, tuple):
            parts = [str(part).strip() for part in key if str(part).strip()]
            return " ".join(parts).strip()
        return str(key or "").strip()

    def extra_gallery_registered_image_names():
        names = []

        try:
            listed = renpy.list_images()
        except Exception:
            listed = []

        for raw_name in listed:
            image_name = extra_gallery_image_name_from_key(raw_name)
            if image_name:
                names.append(image_name)

        if not names:
            image_store = getattr(getattr(renpy.display, "image", None), "images", None)
            if isinstance(image_store, dict):
                for key in image_store.keys():
                    image_name = extra_gallery_image_name_from_key(key)
                    if image_name:
                        names.append(image_name)

        return sorted(set(names), key=lambda value: value.lower())

    def extra_gallery_is_auto_background(image_name):
        lower_name = str(image_name or "").lower().strip()
        if not lower_name:
            return False
        if lower_name in EXTRA_GALLERY_AUTO_BG_EXCLUDE_EXACT:
            return False
        for prefix in EXTRA_GALLERY_AUTO_BG_EXCLUDE_PREFIXES:
            if lower_name.startswith(prefix):
                return False
        for prefix in EXTRA_GALLERY_AUTO_BG_NAME_PREFIXES:
            if lower_name.startswith(prefix):
                return True
        for suffix in EXTRA_GALLERY_AUTO_BG_NAME_SUFFIXES:
            if lower_name.endswith(suffix):
                return True
        for needle in EXTRA_GALLERY_AUTO_BG_NAME_CONTAINS:
            if needle in lower_name:
                return True
        return False

    def extra_gallery_build_auto_background_entries():
        entries = []
        for image_name in extra_gallery_registered_image_names():
            if not extra_gallery_is_auto_background(image_name):
                continue
            entry = extra_gallery_entry(
                image=image_name,
                title=extra_gallery_title_from_name(image_name),
                description="Фоновое изображение из прохождения.",
                unlock="seen",
                group="background",
            )
            if entry:
                entries.append(entry)
        return entries

    def extra_gallery_build_custom_entries():
        entries = []
        for raw_entry in extra_gallery_custom_entries:
            entry = None
            if isinstance(raw_entry, dict):
                entry = extra_gallery_entry(
                    image=raw_entry.get("image", ""),
                    title=raw_entry.get("title"),
                    thumb=raw_entry.get("thumb"),
                    description=raw_entry.get("description", ""),
                    unlock=raw_entry.get("unlock", "always"),
                    group=raw_entry.get("group", "custom"),
                    item_id=raw_entry.get("id"),
                )
            elif isinstance(raw_entry, str):
                entry = extra_gallery_entry(raw_entry, group="custom")

            if entry:
                entries.append(entry)
        return entries

    def extra_gallery_entries(refresh=False):
        global extra_gallery_cached_entries

        if refresh or (extra_gallery_cached_entries is None):
            merged = []
            seen_ids = set()
            for entry in extra_gallery_build_auto_background_entries() + extra_gallery_build_custom_entries():
                entry_id = entry.get("id")
                if (not entry_id) or (entry_id in seen_ids):
                    continue
                seen_ids.add(entry_id)
                merged.append(entry)
            extra_gallery_cached_entries = merged

        return list(extra_gallery_cached_entries or [])

    def extra_gallery_filter_entries(entries, selected_filter, only_unlocked=False):
        selected = []
        for entry in entries:
            if selected_filter != "all" and entry.get("group") != selected_filter:
                continue
            if only_unlocked and (not extra_gallery_is_unlocked(entry)):
                continue
            selected.append(entry)
        return selected

    def extra_gallery_clamp_index(index, items_count):
        if items_count <= 0:
            return 0
        try:
            index = int(index)
        except Exception:
            index = 0
        return max(0, min(index, items_count - 1))

    def extra_gallery_displayable_exists(source):
        source_name = str(source or "").strip()
        if not source_name:
            return False
        try:
            if renpy.has_image(source_name):
                return True
        except Exception:
            pass
        try:
            return bool(renpy.loadable(source_name))
        except Exception:
            return False

    def extra_gallery_best_thumb_source(item):
        if not item:
            return None
        thumb = item.get("thumb", "")
        if extra_gallery_displayable_exists(thumb):
            return thumb
        image = item.get("image", "")
        if extra_gallery_displayable_exists(image):
            return image
        return None


screen extra_gallery_tab(content_width=1740):
    $ extra_gallery_record_visible_backgrounds()
    $ all_items = extra_gallery_entries()
    $ unlocked_total = sum([1 for item in all_items if extra_gallery_is_unlocked(item)])
    $ filtered_items = extra_gallery_filter_entries(all_items, extra_gallery_filter, extra_gallery_only_unlocked)
    $ filtered_count = len(filtered_items)
    if filtered_count > 0:
        $ current_index = extra_gallery_clamp_index(extra_gallery_index, filtered_count)
        if current_index != extra_gallery_index:
            $ extra_gallery_index = current_index
        $ selected_item = filtered_items[current_index]
        $ selected_item_unlocked = extra_gallery_is_unlocked(selected_item)
    else:
        $ current_index = 0
        $ selected_item = None
        $ selected_item_unlocked = False

    $ preview_width = max(390, min(520, int(content_width * 0.38)))
    $ preview_image_height = min(500, max(290, int(config.screen_height * 0.38)))
    $ card_spacing = 12
    $ card_columns = 2 if content_width >= 1060 else 1
    $ grid_width = max(360, int(content_width - preview_width - 20))
    $ inner_grid_width = max(300, grid_width - 24)
    if card_columns > 1:
        $ card_width = max(170, min(300, int((inner_grid_width - card_spacing) / 2)))
    else:
        $ card_width = max(260, min(520, inner_grid_width))
    $ card_height = max(122, int(card_width * 0.58))

    vbox:
        spacing 14
        xfill True
        yfill True

        frame:
            style "extra_gallery_toolbar_frame"
            xfill True

            hbox:
                spacing 12
                xfill True
                yalign 0.5

                vbox:
                    spacing 2
                    text "GALLERY MATRIX" style "extra_gallery_kicker"
                    text "Галерея" style "extra_gallery_panel_title"

                text "Открыто: [unlocked_total] / [len(all_items)]" style "extra_gallery_meta_text"

                textbutton "Все":
                    style "extra_gallery_filter_button"
                    action [SetVariable("extra_gallery_filter", "all"), SetVariable("extra_gallery_index", 0)]
                    selected extra_gallery_filter == "all"

                textbutton "Фоны":
                    style "extra_gallery_filter_button"
                    action [SetVariable("extra_gallery_filter", "background"), SetVariable("extra_gallery_index", 0)]
                    selected extra_gallery_filter == "background"

                textbutton "Указанные":
                    style "extra_gallery_filter_button"
                    action [SetVariable("extra_gallery_filter", "custom"), SetVariable("extra_gallery_index", 0)]
                    selected extra_gallery_filter == "custom"

                textbutton ("Показать все" if extra_gallery_only_unlocked else "Скрыть закрытые"):
                    style "extra_gallery_toggle_button"
                    action [ToggleVariable("extra_gallery_only_unlocked"), SetVariable("extra_gallery_index", 0)]
                    selected extra_gallery_only_unlocked

                textbutton "Обновить":
                    style "extra_gallery_toggle_button"
                    action Function(extra_gallery_refresh_entries)

        hbox:
            spacing 20
            xfill True
            yfill True

            frame at extra_gallery_panel_intro:
                style "extra_gallery_grid_frame"
                xsize grid_width
                yfill True

                if filtered_count <= 0:
                    vbox:
                        spacing 10
                        xfill True
                        yfill True
                        yalign 0.5

                        text "Изображения не найдены." style "extra_gallery_locked_text":
                            xalign 0.5
                        text "Смените фильтр или отключите скрытие закрытых элементов." style "extra_gallery_empty_hint":
                            xalign 0.5
                else:
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable False
                        side_yfill True
                        xfill True
                        yfill True

                        vbox:
                            spacing card_spacing
                            xfill True
                            $ rows_count = (filtered_count + card_columns - 1) // card_columns

                            for row_idx in range(rows_count):
                                hbox:
                                    spacing card_spacing
                                    xfill True

                                    for col_idx in range(card_columns):
                                        $ item_idx = (row_idx * card_columns) + col_idx
                                        if item_idx < filtered_count:
                                            $ item = filtered_items[item_idx]
                                            $ item_unlocked = extra_gallery_is_unlocked(item)
                                            $ thumb_source = extra_gallery_best_thumb_source(item)

                                            button:
                                                style "extra_gallery_card_button"
                                                xsize card_width
                                                ysize card_height
                                                action SetVariable("extra_gallery_index", item_idx)
                                                selected item_idx == current_index

                                                has fixed

                                                add Solid("#080808")

                                                if item_unlocked and thumb_source:
                                                    add thumb_source:
                                                        fit "cover"
                                                        xsize card_width
                                                        ysize card_height
                                                        xalign 0.5
                                                        yalign 0.5

                                                add Solid("#00000078")
                                                if item_idx == current_index:
                                                    add Solid("#8ec9ff1c") at extra_gallery_card_pulse
                                                    add Solid("#ff7a1822") at extra_gallery_card_glint

                                                text item.get("title", "Без названия") style "extra_gallery_card_title":
                                                    xalign 0.04
                                                    yalign 0.87

                                                if not item_unlocked:
                                                    text "ЗАКРЫТО" style "extra_gallery_card_lock":
                                                        xalign 0.5
                                                        yalign 0.5
                                        elif card_columns > 1:
                                            null width card_width

            frame at extra_gallery_panel_intro:
                style "extra_gallery_preview_frame"
                xsize preview_width
                yfill True

                vbox:
                    spacing 12
                    xfill True
                    yfill True

                    frame:
                        style "extra_gallery_image_frame"
                        xfill True
                        ysize preview_image_height

                        if selected_item and selected_item_unlocked and extra_gallery_displayable_exists(selected_item.get("image")):
                            button:
                                style "extra_gallery_preview_button"
                                action Show("extra_gallery_viewer", items=filtered_items, start_index=current_index)
                                xfill True
                                yfill True

                                has fixed

                                add Solid("#040404")
                                add Solid("#8ec9ff0d")
                                add Solid("#ff7a180f") at extra_gallery_scanline
                                add selected_item.get("image"):
                                    at extra_gallery_preview_breathe
                                    fit "contain"
                                    xsize (preview_width - 34)
                                    ysize (preview_image_height - 12)
                                    xalign 0.5
                                    yalign 0.5
                        else:
                            fixed:
                                xfill True
                                yfill True

                                add Solid("#040404")
                                add Solid("#8ec9ff0d")

                                if selected_item and not selected_item_unlocked:
                                    text "ЗАБЛОКИРОВАНО" style "extra_gallery_locked_text":
                                        xalign 0.5
                                        yalign 0.5
                                elif selected_item:
                                    text "Изображение не найдено" style "extra_gallery_locked_text":
                                        xalign 0.5
                                        yalign 0.5
                                else:
                                    text "Нет изображений для выбранного фильтра" style "extra_gallery_locked_text":
                                        xalign 0.5
                                        yalign 0.5

                    if selected_item:
                        text selected_item.get("title", "Без названия") style "extra_gallery_selected_title"
                        text extra_gallery_display_text(selected_item) style "extra_gallery_selected_desc"
                        text extra_gallery_status_text(selected_item) style "extra_gallery_status_text"

                        hbox:
                            spacing 8

                            if filtered_count > 1:
                                textbutton "◀":
                                    style "extra_gallery_action_button"
                                    action SetVariable("extra_gallery_index", (current_index - 1) % filtered_count)

                                textbutton "▶":
                                    style "extra_gallery_action_button"
                                    action SetVariable("extra_gallery_index", (current_index + 1) % filtered_count)

                            if selected_item_unlocked:
                                textbutton "Открыть просмотр":
                                    style "extra_gallery_action_button"
                                    action Show("extra_gallery_viewer", items=filtered_items, start_index=current_index)

                        text "ЛКМ по карточке: выбрать. ЛКМ по предпросмотру: открыть фуллскрин. Esc/ПКМ: назад." style "extra_gallery_inline_hint"


screen extra_gallery_viewer(items=None, start_index=0):
    modal True
    zorder 120

    default viewer_items = list(items or [])
    default viewer_index = extra_gallery_clamp_index(start_index, len(viewer_items))

    key "dismiss" action [SetVariable("extra_gallery_index", viewer_index), Hide("extra_gallery_viewer")]
    key "game_menu" action [SetVariable("extra_gallery_index", viewer_index), Hide("extra_gallery_viewer")]
    key "K_ESCAPE" action [SetVariable("extra_gallery_index", viewer_index), Hide("extra_gallery_viewer")]
    key "mouseup_3" action [SetVariable("extra_gallery_index", viewer_index), Hide("extra_gallery_viewer")]

    if viewer_items and len(viewer_items) > 1:
        key "K_LEFT" action SetScreenVariable("viewer_index", (viewer_index - 1) % len(viewer_items))
        key "K_RIGHT" action SetScreenVariable("viewer_index", (viewer_index + 1) % len(viewer_items))

    if viewer_items:
        $ viewer_index = extra_gallery_clamp_index(viewer_index, len(viewer_items))
        $ viewer_item = viewer_items[viewer_index]
        $ viewer_item_unlocked = extra_gallery_is_unlocked(viewer_item)
    else:
        $ viewer_item = None
        $ viewer_item_unlocked = False

    add Solid("#000000EB")
    add Solid("#8ec9ff10")

    frame:
        style "extra_gallery_viewer_frame"
        xfill True
        yfill True

        vbox:
            spacing 12
            xfill True
            yfill True

            hbox:
                spacing 8
                xfill True

                textbutton "← Назад к галерее":
                    style "extra_gallery_close_button"
                    action [SetVariable("extra_gallery_index", viewer_index), Hide("extra_gallery_viewer")]

                if viewer_item:
                    text viewer_item.get("title", "Галерея") style "extra_gallery_viewer_title"

                if viewer_items and len(viewer_items) > 1:
                    textbutton "◀":
                        style "extra_gallery_close_button"
                        action SetScreenVariable("viewer_index", (viewer_index - 1) % len(viewer_items))

                    text "[viewer_index + 1] / [len(viewer_items)]" style "extra_gallery_counter_text"

                    textbutton "▶":
                        style "extra_gallery_close_button"
                        action SetScreenVariable("viewer_index", (viewer_index + 1) % len(viewer_items))

            frame:
                style "extra_gallery_view_image_frame"
                xfill True
                yfill True

                fixed:
                    xfill True
                    yfill True

                    add Solid("#020202")
                    add Solid("#8ec9ff0f")

                    if viewer_item and viewer_item_unlocked and extra_gallery_displayable_exists(viewer_item.get("image")):
                        add viewer_item.get("image"):
                            fit "contain"
                            xsize (config.screen_width - 120)
                            ysize (config.screen_height - 230)
                            xalign 0.5
                            yalign 0.5
                    elif viewer_item and (not viewer_item_unlocked):
                        text "Изображение закрыто" style "extra_gallery_locked_text":
                            xalign 0.5
                            yalign 0.5
                    else:
                        text "Изображение недоступно" style "extra_gallery_locked_text":
                            xalign 0.5
                            yalign 0.5

            text "Esc или ПКМ: назад в галерею" style "extra_gallery_viewer_hint"


style extra_gallery_toolbar_frame:
    background "#0b1219D8"
    padding (14, 12)
    outlines [(1, "#8ec9ff40", 0, 0)]

style extra_gallery_kicker is gui_text:
    color "#8ec9ff"
    size 22

style extra_gallery_panel_title is gui_text:
    color "#ff7a18"
    size 50

style extra_gallery_meta_text is gui_text:
    color "#d6e9ff"
    size 26

style extra_gallery_filter_button is button:
    background "#8ec9ff18"
    hover_background "#8ec9ff2a"
    selected_background "#ff7a1850"
    outlines [(1, "#8ec9ff42", 0, 0)]
    padding (12, 8)

style extra_gallery_filter_button_text is button_text:
    color "#f2f8ff"
    hover_color "#ffd9bc"
    selected_color "#ffe3cc"
    size 26

style extra_gallery_toggle_button is button:
    background "#8ec9ff14"
    hover_background "#8ec9ff26"
    selected_background "#ff7a1840"
    outlines [(1, "#8ec9ff36", 0, 0)]
    padding (12, 8)

style extra_gallery_toggle_button_text is button_text:
    color "#e8f3ff"
    hover_color "#ffd9bc"
    selected_color "#ffe3cc"
    size 25

style extra_gallery_preview_frame:
    background "#0b1219D8"
    padding (14, 14)
    outlines [(1, "#8ec9ff40", 0, 0)]

style extra_gallery_image_frame:
    background "#03080dcc"
    padding (8, 8)
    outlines [(1, "#8ec9ff33", 0, 0)]

style extra_gallery_preview_button is button:
    background None
    hover_background "#8ec9ff16"
    selected_background "#8ec9ff20"
    padding (0, 0)

style extra_gallery_locked_text is gui_text:
    color "#e1edfaab"
    size 30
    text_align 0.5
    xalign 0.5

style extra_gallery_empty_hint is gui_text:
    color "#d0dff58a"
    size 24
    text_align 0.5
    xalign 0.5

style extra_gallery_selected_title is gui_text:
    color "#f2f8ff"
    size 38

style extra_gallery_selected_desc is gui_text:
    color "#d1e4f7"
    size 24

style extra_gallery_status_text is gui_text:
    color "#8ec9ff"
    size 23

style extra_gallery_action_button is button:
    background "#8ec9ff18"
    hover_background "#8ec9ff2d"
    selected_background "#ff7a1842"
    outlines [(1, "#8ec9ff42", 0, 0)]
    padding (12, 8)

style extra_gallery_action_button_text is button_text:
    color "#eef7ff"
    hover_color "#ffd9bc"
    selected_color "#ffe3cc"
    size 25

style extra_gallery_inline_hint is gui_text:
    color "#b8cce395"
    size 20

style extra_gallery_grid_frame:
    background "#0b1219D0"
    padding (12, 12)
    outlines [(1, "#8ec9ff34", 0, 0)]

style extra_gallery_card_button is button:
    background "#8ec9ff12"
    hover_background "#8ec9ff24"
    selected_background "#ff7a1842"
    outlines [(1, "#8ec9ff2f", 0, 0)]
    padding (0, 0)

style extra_gallery_card_title is gui_text:
    color "#eef7ffeb"
    size 22

style extra_gallery_card_lock is gui_text:
    color "#ffccb3"
    size 22
    text_align 0.5
    xalign 0.5

style extra_gallery_viewer_frame:
    background None
    padding (26, 20)

style extra_gallery_view_image_frame:
    background "#050b11d9"
    padding (8, 8)
    outlines [(1, "#8ec9ff38", 0, 0)]

style extra_gallery_viewer_title is gui_text:
    color "#f2f8ff"
    size 33

style extra_gallery_counter_text is gui_text:
    color "#d8eaff"
    size 25
    xalign 1.0

style extra_gallery_close_button is button:
    background "#8ec9ff1c"
    hover_background "#8ec9ff31"
    selected_background "#ff7a1844"
    outlines [(1, "#8ec9ff44", 0, 0)]
    padding (14, 8)

style extra_gallery_close_button_text is button_text:
    color "#f2f8ff"
    hover_color "#ffd9bc"
    size 26

style extra_gallery_viewer_hint is gui_text:
    color "#c0d4eb9f"
    size 22
    xalign 0.5

transform extra_gallery_scanline:
    alpha 0.13
    yoffset 0
    linear 1.8 yoffset 92 alpha 0.03
    linear 0.25 alpha 0.13
    repeat

transform extra_gallery_panel_intro:
    alpha 0.0
    yoffset 14
    ease 0.22 alpha 1.0 yoffset 0

transform extra_gallery_card_pulse:
    alpha 0.18
    linear 1.0 alpha 0.46
    linear 1.0 alpha 0.18
    repeat

transform extra_gallery_card_glint:
    alpha 0.06
    linear 1.1 alpha 0.24
    linear 1.1 alpha 0.06
    repeat

transform extra_gallery_preview_breathe:
    zoom 1.0
    linear 3.6 zoom 1.02
    linear 3.6 zoom 1.0
    repeat
