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

    if not hasattr(persistent, 'igroteka_progress'):
        persistent.igroteka_progress = {}

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
define ACHIEVEMENT_GAME_SPECIALIST = "game_specialist"

init python:
    class Achievement(object):
        def __init__(self, id, name, description, hidden=False, icon="images/achievements/achievement.png"):
            self.id = id
            self.name = name
            self.description = description
            self.hidden = hidden
            self.icon = icon
            
            self.lock_icon = "gui/achievements/lock.png"#Transform(self.icon, matrixcolor=SaturationMatrix(0.1))
            
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
            "gui/achievements/prologue.png"
        ),
        ACHIEVEMENT_ATTACK: Achievement(
            ACHIEVEMENT_ATTACK,
            "Лучшая защита - нападение",
            "Выстрелить в Виктора",
            True,
            "gui/achievements/shot.png"
        ),
        ACHIEVEMENT_PEACEMAKER: Achievement(
            ACHIEVEMENT_PEACEMAKER,
            "Миротворец",
            "Не стрелять в Виктора",
            True,
            "gui/achievements/peacemaker.png"
        ),
        ACHIEVEMENT_ELECTRIC: Achievement(
            ACHIEVEMENT_ELECTRIC,
            "Электрический ток",
            "Умереть в 1 день",
            True,
            "gui/achievements/electricity.png"
        ),
        ACHIEVEMENT_HELL: Achievement(
            ACHIEVEMENT_HELL,
            "Я в аду?",
            "Умереть во 2 день",
            True,
            "gui/achievements/hell.png"
        ),
        ACHIEVEMENT_SHERLOCK: Achievement(
            ACHIEVEMENT_SHERLOCK,
            "Шерлок Холмс",
            "Разгадать загадку в сейфе",
            True,
            "gui/achievements/sherlock.png"
        ),
        ACHIEVEMENT_OMLET: Achievement(
            ACHIEVEMENT_OMLET,
            "Омлет был несвежим",
            "Умереть в 3 день",
            True,
            "gui/achievements/omlet.png"
        ),
        ACHIEVEMENT_HACKER: Achievement(
            ACHIEVEMENT_HACKER,
            "Хакер",
            "Взломать дверь лазарета",
            True,
            "gui/achievements/hacker.png"
        ),
        ACHIEVEMENT_DYSPNEA: Achievement(
            ACHIEVEMENT_DYSPNEA,
            "Одышка",
            "Умереть в 4 день",
            True,
            "gui/achievements/dyspnea.png"
        ),
        ACHIEVEMENT_CHANCE: Achievement(
            ACHIEVEMENT_CHANCE,
            "У меня есть шанс?",
            "Поверить голосу",
            True,
            "gui/achievements/chance.png"
        ),
        ACHIEVEMENT_CRITICAL_MIND: Achievement(
            ACHIEVEMENT_CRITICAL_MIND,
            "Критическое мышление",
            "Не поверить голосу",
            True,
            "gui/achievements/brain.png"
        ),
        ACHIEVEMENT_DREAM: Achievement(
            ACHIEVEMENT_DREAM,
            "Исполнить мечту",
            "Умереть в 5 день",
            True,
            "gui/achievements/dream.png"
        ),
        ACHIEVEMENT_CREW: Achievement(
            ACHIEVEMENT_CREW,
            "Навестить \"членов экипажа\"",
            "Вернуться домой",
            True,
            "gui/achievements/crew.png"
        ),
        ACHIEVEMENT_COMPLETE: Achievement(
            ACHIEVEMENT_COMPLETE,
            "Пройти игру",
            "",
            False,
            "gui/achievements/done.png"
        ),
        ACHIEVEMENT_GAME_SPECIALIST: Achievement(
            ACHIEVEMENT_GAME_SPECIALIST,
            "Игровой специалист",
            "Пройти все игры в игротеке",
            True,
            "gui/achievements/done.png",
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

    def mark_igroteka_completed(id):
        # Инициализируем прогресс если не существует
        if not hasattr(persistent, 'igroteka_progress') or persistent.igroteka_progress is None:
            persistent.igroteka_progress = {}

        persistent.igroteka_progress[id] = True
        renpy.save_persistent()
        if len(persistent.igroteka_progress) >= 9:
            unlock_achievement(ACHIEVEMENT_GAME_SPECIALIST)