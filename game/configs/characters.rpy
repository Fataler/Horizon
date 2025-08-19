#region characters
define r_f = Character("Райан", image="r", callback=speaker('r_f'))
define r_t = Character(None, image="r")
define i = Character("Ирис")
define v = Character("Виктор")
define d = Character("Дэвид")
define s = Character("Софи")
define n = Character("Неизвестный голос")
define story_teller = Character(None, kind=nvl, color="#1a1a1f")

#универсальный перс
init python:
    def speak_as(name, text, color="#232324"):
        Character(name, color=color)(text)

#endregion

#region Ryan

image side r = LayeredImageProxy("r_f", Transform(crop=(0, 0, 640, 460), xoffset=-80))

layeredimage r_f:
    at auto_flip("r_f")

    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute serious default:
            Null()
        attribute thinking:
            Null()
        attribute ear:
            Null()
        attribute crazy:
            Null()

    group emotion if_any "serious":
        attribute think default:
            "images/Rayan/Rayan_seryoznii_thinking.png"
        attribute angry:
            "images/Rayan/Rayan_seryoznii_angry.png"
        attribute very_angry:
            "images/Rayan/Rayan_seryoznii_very_angry.png"
        attribute fainting:
            "images/Rayan/Rayan_seryoznii_fainting.png"
        attribute fainting_blood:
            "images/Rayan/Rayan_seryoznii_fainting_blood.png"

    group emotion if_any "thinking":
        attribute neutral default:
            "images/Rayan/Rayan_thinking_calm.png"
        attribute not_sure:
            "images/Rayan/Rayan_thinking_interrogative.png"
        attribute ne_ponyal:
            "images/Rayan/Rayan_thinking_ne_ponyal.png"
        attribute osharashen:
            "images/Rayan/Rayan_thinking_osharashen.png"
        attribute suspicious:
            "images/Rayan/Rayan_thinking_suspicious.png"

    group emotion if_any "ear":
        attribute neutral default:
            "images/Rayan/Rayan_yxo_neutral.png"
        attribute dissatisfied:
            "images/Rayan/Rayan_yxo_dissatisfied.png"
        attribute hehe:
            "images/Rayan/Rayan_yxo_hehe.png"
        attribute sick:
            "images/Rayan/Rayan_yxo_sick.png"
        attribute surprised:
            "images/Rayan/Rayan_yxo_surprised.png"
    
    group crazy:
        attribute mnogo:
            "images/Rayan/Rayan_crazy_mnogo.png"
        attribute nemnogo:
            "images/Rayan/Rayan_crazy_nemnogo.png"
        attribute pizdec:
            "images/Rayan/Rayan_crazy_pizdec.png"

    group mouth if_any "serious":
        attribute talk:
            WhileSpeaking('r_f', 'rayan_talk_seryoznii', Null())

    group mouth if_any "thinking":
        attribute talk:
            WhileSpeaking('r_f', 'rayan_talk_thinking', Null())

    group mouth if_any "ear":
        attribute talk:
            WhileSpeaking('r_f', 'rayan_talk_ear', Null())

    group mouth if_any "crazy":
        attribute talk:
            Null()

image rayan_talk_seryoznii:
    'images/Rayan/Rayan_seryoznii_rot1.png'
    pause 0.1
    'images/Rayan/Rayan_seryoznii_rot2.png'
    pause 0.1
    'images/Rayan/Rayan_seryoznii_rot3.png'
    repeat

image rayan_talk_thinking:
    'images/Rayan/Rayan_thinking_rot1.png'
    pause 0.1
    'images/Rayan/Rayan_thinking_rot2.png'
    pause 0.1
    'images/Rayan/Rayan_thinking_rot3.png'
    repeat

image rayan_talk_ear:
    'images/Rayan/Rayan_yxo_rot1.png'
    pause 0.1
    'images/Rayan/Rayan_yxo_rot2.png'
    pause 0.1
    'images/Rayan/Rayan_yxo_rot3.png'
    repeat

#endregion

#region Iris
#endregion

#region Victor
#endregion

#region David
#endregion

#region Sophie
#endregion



