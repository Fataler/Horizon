#region characters

define story_teller = Character(None, kind=nvl, color="#1a1a1f")

#универсальный перс
init python:
    def speak_as(name, text, color="#232324"):
        Character(name, color=color)(text)

#endregion

