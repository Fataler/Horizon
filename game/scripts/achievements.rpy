init -2 python:
    ACHIEVEMENTS_VERSION = 2

    if not hasattr(persistent, '_achievements_version') or persistent._achievements_version != ACHIEVEMENTS_VERSION:
        persistent._achievements_version = ACHIEVEMENTS_VERSION
        persistent._achievement_unlocked = {}

init -1 python:
    if not hasattr(persistent, '_achievement_unlocked'):
        persistent._achievement_unlocked = {}
    elif persistent._achievement_unlocked is None:
        persistent._achievement_unlocked = {}

# ID достижений
define ACHIEVEMENT_PROLOGUE = "prologue"
define ACHIEVEMENT_ATTACK = "attack"
define ACHIEVEMENT_PEACEMAKER = "peacemaker"
define ACHIEVEMENT_ELECTRIC = "electric"
define ACHIEVEMENT_HELL = "hell"
define ACHIEVEMENT_SHERLOCK = "sherlock"
define ACHIEVEMENT_OMLET = "omlet"
define ACHIEVEMENT_HACKER = "hacker"
define ACHIEVEMENT_DYSPNEA = "dyspnea"
define ACHIEVEMENT_CHANCE = "chance"
define ACHIEVEMENT_CRITICAL_MIND = "critical"
define ACHIEVEMENT_DREAM = "dream"
define ACHIEVEMENT_CREW = "crew"
define ACHIEVEMENT_COMPLETE = "complete"

init python:
    class Achievement(object):
        def __init__(self, id, name, description, hidden=False, icon="images/achievements/achievement.png"):
            self.id = id
            self.name = name
            self.description = description
            self.hidden = hidden
            self.icon = icon
            
            self.gray_icon = Transform(self.icon, matrixcolor=SaturationMatrix(0.1))
            
        @property
        def unlocked(self):
            return self.id in persistent._achievement_unlocked and persistent._achievement_unlocked[self.id]
            
        def unlock(self):
            if not self.unlocked:
                persistent._achievement_unlocked[self.id] = True
                renpy.play(sfx_ui_achieve, channel="ui")
                renpy.show_screen("achievement_popup", achievement=self)
                renpy.restart_interaction()

    ACHIEVEMENT_ICON_SIZE = 96
    ACHIEVEMENT_POPUP_ICON_SIZE = 64

    # Список достижений
    achievements = {
        ACHIEVEMENT_PROLOGUE: Achievement(
            ACHIEVEMENT_PROLOGUE,
            "Пройти Пролог",
            "Пройти Пролог",
            False,
            "gui/achievements/1.png"
        ),
        ACHIEVEMENT_ATTACK: Achievement(
            ACHIEVEMENT_ATTACK,
            "Лучшая защита - нападение",
            "Выстрелить в Виктора",
            True,
            "gui/achievements/2.png"
        ),
        ACHIEVEMENT_PEACEMAKER: Achievement(
            ACHIEVEMENT_PEACEMAKER,
            "Миротворец",
            "Не выстрелить в Виктора",
            True,
            "gui/achievements/3.png"
        ),
        ACHIEVEMENT_ELECTRIC: Achievement(
            ACHIEVEMENT_ELECTRIC,
            "Электрический ток",
            "Умереть в 1 день",
            True,
            "gui/achievements/4.png"
        ),
        ACHIEVEMENT_HELL: Achievement(
            ACHIEVEMENT_HELL,
            "Я в аду?",
            "Умереть во 2 день",
            True,
            "gui/achievements/5.png"
        ),
        ACHIEVEMENT_SHERLOCK: Achievement(
            ACHIEVEMENT_SHERLOCK,
            "Шерлок Холмс",
            "Разгадать загадку в сейфе",
            True,
            "gui/achievements/6.png"
        ),
        ACHIEVEMENT_OMLET: Achievement(
            ACHIEVEMENT_OMLET,
            "Омлет был несвежим",
            "Умереть в 3 день",
            True,
            "gui/achievements/7.png"
        ),
        ACHIEVEMENT_HACKER: Achievement(
            ACHIEVEMENT_HACKER,
            "Хакер",
            "Взломать дверь лазарета",
            True,
            "gui/achievements/8.png"
        ),
        ACHIEVEMENT_DYSPNEA: Achievement(
            ACHIEVEMENT_DYSPNEA,
            "Одышка",
            "Умереть в 4 день",
            True,
            "gui/achievements/9.png"
        ),
        ACHIEVEMENT_CHANCE: Achievement(
            ACHIEVEMENT_CHANCE,
            "У меня есть шанс?",
            "Поверить голосу",
            True,
            "gui/achievements/10.png"
        ),
        ACHIEVEMENT_CRITICAL_MIND: Achievement(
            ACHIEVEMENT_CRITICAL_MIND,
            "Критическое мышление",
            "Не поверить голосу",
            True,
            "gui/achievements/11.png"
        ),
        ACHIEVEMENT_DREAM: Achievement(
            ACHIEVEMENT_DREAM,
            "Исполнить мечту",
            "Умереть в 5 день",
            True,
            "gui/achievements/12.png"
        ),
        ACHIEVEMENT_CREW: Achievement(
            ACHIEVEMENT_CREW,
            "Навестить \"членов экипажа\"",
            "Вернуться домой",
            True,
            "gui/achievements/13.png"
        ),
        ACHIEVEMENT_COMPLETE: Achievement(
            ACHIEVEMENT_COMPLETE,
            "Пройти игру",
            "",
            False,
            "gui/achievements/Heart.png"
        ),
    }

    def unlock_achievement(id):
        if id in achievements:
            achievements[id].unlock()
            
    def reset_achievements():
        """Сброс всех достижений"""
        persistent._achievement_unlocked.clear()
        renpy.save_persistent()
        renpy.restart_interaction()

    def unlock_all_achievements():
        for ach in achievements.values():
            ach.unlock()