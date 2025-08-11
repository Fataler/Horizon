init -2 python:
    ACHIEVEMENTS_VERSION = 1

    if not hasattr(persistent, '_achievements_version') or persistent._achievements_version != ACHIEVEMENTS_VERSION:
        persistent._achievements_version = ACHIEVEMENTS_VERSION
        persistent._achievement_unlocked = {}

init -1 python:
    if not hasattr(persistent, '_achievement_unlocked'):
        persistent._achievement_unlocked = {}
    elif persistent._achievement_unlocked is None:
        persistent._achievement_unlocked = {}

# ID достижений
define ACHIEVEMENT_FUTURE_HISTORIAN = "future_historian" #
define ACHIEVEMENT_MAX_DAMAGE = "max_damage" #
define ACHIEVEMENT_STRATEGIST = "strategist" #
define ACHIEVEMENT_PIG_SLAYER = "pig_slayer" #
define ACHIEVEMENT_GENIUS = "genius" #
define ACHIEVEMENT_FIRST_CHAPTER = "first_chapter" #
define ACHIEVEMENT_SECOND_CHAPTER = "second_chapter" #
define ACHIEVEMENT_THIRD_CHAPTER = "third_chapter" #
define ACHIEVEMENT_THANK_YOU = "thank_you" #

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
        ACHIEVEMENT_FIRST_CHAPTER: Achievement(
            ACHIEVEMENT_FIRST_CHAPTER,
            "Пройти 1 акт",
            "",
            False,
            "gui/menu/Achievements/1.png"
        ),
        ACHIEVEMENT_SECOND_CHAPTER: Achievement(
            ACHIEVEMENT_SECOND_CHAPTER,
            "Пройти 2 акт",
            "",
            False,
            "gui/menu/Achievements/2.png"
        ),
        ACHIEVEMENT_THIRD_CHAPTER: Achievement(
            ACHIEVEMENT_THIRD_CHAPTER,
            "Пройти 3 акт",
            "",
            False,
            "gui/menu/Achievements/3.png"
        ),
        ACHIEVEMENT_THANK_YOU: Achievement(
            ACHIEVEMENT_THANK_YOU,
            "Спасибо, что прошёл игру. От всего сердца :)",
            "Пройти игру",
            False,
            "gui/menu/Achievements/Heart.png"
        ),
        ACHIEVEMENT_FUTURE_HISTORIAN: Achievement(
            ACHIEVEMENT_FUTURE_HISTORIAN,
            "Историк будущего",
            "Добро пожаловать в эпоху Эдо 2.0 — теперь с киберимплантами и корпоративным сёгунатом",
            True,
            "gui/menu/Achievements/Samurai.png"
        ),
        ACHIEVEMENT_MAX_DAMAGE: Achievement(
            ACHIEVEMENT_MAX_DAMAGE,
            "Почти получилось, ты просто поддавался",
            "Нанести Дзиндзо максимальное количество урона",
            True,
            "gui/menu/Achievements/Pokeball.png"
        ),
        ACHIEVEMENT_STRATEGIST: Achievement(
            ACHIEVEMENT_STRATEGIST,
            "Трус? Нет, стратег",
            "Попытаться сбежать из боя",
            True,
            "gui/menu/Achievements/Chess.png"
        ),
        ACHIEVEMENT_PIG_SLAYER: Achievement(
            ACHIEVEMENT_PIG_SLAYER,
            "Кабанье проклятье",
            "Одержи победу над Ужасным Вепрем",
            True,
            "gui/menu/Achievements/Pig.png"
        ),
        ACHIEVEMENT_GENIUS: Achievement(
            ACHIEVEMENT_GENIUS,
            "Гений поневоле",
            "Ты ответил правильно на всё. Системе не оставили выбора. Тебе — тоже",
            True,
            "gui/menu/Achievements/Gears.png"
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