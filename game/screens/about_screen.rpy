## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

screen about():

    tag menu

    ## Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
    ## включён в порт просмотра внутри экрана игрового меню.
    use game_menu(_("Об игре"), scroll="viewport"):

        style_prefix "about"

        vbox:

            text "[config.name!t]"
            text _("Версия [config.version!t]\n")

            ## gui.about обычно установлено в options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Сделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

    add "den_shadow":
        anchor (0.5, 0.5)   
        pos (1590, 530)
        at delay_appear(0.3)

    add Parallax("denis", 0.2):
        anchor (0.5, 0.5)
        at move_appear(1370,762, 1548)

    add "den_chirkash":
        anchor (0.5, 0.5)  
        pos (1590, 530)
        at delay_appear(0.3)

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is text

style about_label_text:
    size gui.label_text_size
