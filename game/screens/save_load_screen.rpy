## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

screen save():

    tag menu

    use file_slots(_("Сохранить"))


screen load():

    tag menu

    use file_slots(_("Загрузить"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Основные сохранения"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"), default=False)

    use game_menu(title):

        fixed:

            ## Это гарантирует, что ввод будет принимать enter перед остальными
            ## кнопками.
            order_reverse True

            ## Номер страницы, который может быть изменён посредством клика на
            ## кнопку.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                #action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Таблица слотов.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пусто")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Кнопки для доступа к другим страницам.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    # textbutton _("<=") action FilePagePrevious()
                    # key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}Авто") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Быстрые") action FilePage("quick")

                    ## range(1, 2) задаёт диапазон значений от 1 до 2.
                    for page in range(1, max_save_pages + 1):
                        textbutton "Основные" action FilePage(page)

                    # textbutton _("=>") action FilePageNext(max = max_save_pages)
                    # key "save_page_next" action FilePageNext(max = max_save_pages)

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Загрузить Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Скачать Sync"):
                            action DownloadSync()
                            xalign 0.5
    add "hikaru_shadow":
        anchor (0.5, 0.5)   
        pos (1610, 565)
        at delay_appear(0.3)

    add Parallax("hikaru", 0.2):
        anchor (0.5, 0.5)
        at move_appear(959,641)

    add "hikaru_chirkash":
        anchor (0.5, 0.5)  
        pos (1610, 555)
        at delay_appear(0.3)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text:
    size 40

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text:
    size 30
    #color gui.text_color
    #hover_color "#FFF"

style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")
    yoffset 20

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675