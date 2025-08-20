#region characters
define r = Character("Райан", image="r", callback=speaker('r'))
define r_t = Character(None, image="r")
define r_f = Character("Райан", image="r_f", callback=speaker('r_f'))
define i = Character("Ирис", image="i", callback=speaker('i'))
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
    
    group emotion if_any "crazy":
        attribute mnogo:
            "images/Rayan/Rayan_crazy_mnogo.png"
        attribute nemnogo:
            "images/Rayan/Rayan_crazy_nemnogo.png"
        attribute pizdec:
            "images/Rayan/Rayan_crazy_pizdec.png"

    group mouth if_any "serious" if_not "fainting_blood":
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
layeredimage i:
    yoffset 2
    at auto_flip("i")

    group pose:
        attribute normal default:
            Null()
        attribute pen:
            Null()
        attribute profile:
            Null()
        attribute smoke:
            Null()

    group emotion if_any "normal":
        attribute angry:
            "images/Iris/Iris_neutral_angry.png"
        attribute bychit:
            "images/Iris/Iris_neutral_bychit.png"
        attribute crazy:
            "images/Iris/Iris_neutral_crazy.png"
        attribute neutral_happy:
            "images/Iris/Iris_neutral_neutral_happy.png"
        attribute neutral default:
            "images/Iris/Iris_neutral_neutral.png"
        attribute ridicule:
            "images/Iris/Iris_neutral_ridicule.png"

    group emotion if_any "pen":
        attribute nervous_laughter:
            "images/Iris/Iris_pen_nervous_laughter.png"
        attribute nervous:
            "images/Iris/Iris_pen_nervous.png"
        attribute neutral default:
            "images/Iris/Iris_pen_neutral.png"
        attribute ozadachen:
            "images/Iris/Iris_pen_ozadachen.png"
        attribute sad:
            "images/Iris/Iris_pen_sad.png"

    group emotion if_any "profile":
        attribute ahui:
            "images/Iris/Iris_profile_ahui.png"
        attribute angry:
            "images/Iris/Iris_profile_angry.png"
        attribute neutral default:
            "images/Iris/Iris_profile_neutral.png"
        attribute oooops:
            "images/Iris/Iris_profile_oooops.png"
        attribute osharashen:
            "images/Iris/Iris_profile_osharashen.png"
        attribute tricky:
            "images/Iris/Iris_profile_tricky.png"

    group emotion if_any "smoke":
        attribute calm default:
            "images/Iris/Iris_smoke_calm.png"
        attribute cry:
            "images/Iris/Iris_smoke_cry.png"
        attribute happy:
            "images/Iris/Iris_smoke_happy.png"
        attribute puzzled:
            "images/Iris/Iris_smoke_puzzled.png"
        attribute surprised:
            "images/Iris/Iris_smoke_surprised.png"
        attribute tricky:
            "images/Iris/Iris_smoke_tricky.png"

    group mouth if_any "normal":
        attribute talk:
            Null()

    group mouth if_any "pen":
        attribute talk:
            Null()

    group mouth if_any "profile":
        attribute talk:
            Null()

    group mouth if_any "smoke":
        attribute talk:
            Null()
#endregion

#region Victor
#endregion

#region David
#endregion

#region Sophie
layeredimage s:
    at auto_flip("s")

    group pose:
        attribute profile default:
            Null()
        attribute ruki:
            Null()
        attribute shy:
            Null()

    group emotion if_any "profile":
        attribute annoyed:
            "images/Sofi/Sofi_profile_annoyed.png"
        attribute cry:
            "images/Sofi/Sofi_profile_cry.png"
        attribute despair:
            "images/Sofi/Sofi_profile_despair.png"
        attribute fainting:
            "images/Sofi/Sofi_profile_fainting.png"
        attribute happy:
            "images/Sofi/Sofi_profile_happy.png"
        attribute neutral default:
            "images/Sofi/Sofi_profile_neutral.png"
        attribute sad:
            "images/Sofi/Sofi_profile_sad.png"

    group emotion if_any "ruki":
        attribute calm default:
            "images/Sofi/Sofi_ruki_calm.png"
        attribute crazy:
            "images/Sofi/Sofi_ruki_crazy.png"
        attribute cry:
            "images/Sofi/Sofi_ruki_cry.png"
        attribute happy:
            "images/Sofi/Sofi_ruki_happy.png"
        attribute hurt:
            "images/Sofi/Sofi_ruki_hurt.png"
        attribute neutral:
            "images/Sofi/Sofi_ruki_neutral.png"
        attribute ozadachen:
            "images/Sofi/Sofi_ruki_ozadachen.png"

    group emotion if_any "shy":
        attribute angry:
            "images/Sofi/Sofi_shy_angry.png"
        attribute fainting:
            "images/Sofi/Sofi_shy_fainting.png"
        attribute happy:
            "images/Sofi/Sofi_shy_happy.png"
        attribute nedovolen:
            "images/Sofi/Sofi_shy_nedovolen.png"
        attribute neutral default:
            "images/Sofi/Sofi_shy_neutral.png"
        attribute surprised:
            "images/Sofi/Sofi_shy_surprised.png"
        attribute worried:
            "images/Sofi/Sofi_shy_worried.png"
    
    group mouth if_any "profile":
        attribute talk:
            Null()
            
    group mouth if_any "ruki":
        attribute talk:
            Null()

    group mouth if_any "shy":
        attribute talk:
            Null()
#endregion



