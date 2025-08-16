#region characters
define R = Character("Райан")
define I = Character("Ирис")
define V = Character("Виктор")
define D = Character("Дэвид")
define S = Character("Софи")
define N = Character("Неизвестный голос")
define story_teller = Character(None, kind=nvl, color="#1a1a1f")

#универсальный перс
init python:
    def speak_as(name, text, color="#232324"):
        Character(name, color=color)(text)

#endregion

