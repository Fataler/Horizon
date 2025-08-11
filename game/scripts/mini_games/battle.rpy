label start_pokemon_battle:
    window hide
    
    play music music_rock
    # play music "audio/bg/battle_theme.ogg" fadein 1.0
    
    call screen pokemon_battle with Dissolve(1.0)
    window show
    
    "Ну что ж, битва завершена..."
    
    stop music fadeout 1.0
    return