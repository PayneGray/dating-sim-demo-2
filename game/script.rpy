
#This takes place after the MC has heard about Frisk from Toriel.
label start:
    stop music
    call initialize
    jump dev_label
    #jump frisk_start




label dev_label:
    # show screen show_menu_button
    # show screen show_nav_button
    play music 'audio/Intro_1-2.MP3'
    jump Name_Select
    while True:
        "?"
        menu:
            "Where would you like to go?"
            "Undersnail":
                jump demo_undersnail
            "Prologue":
                jump prologue
            "Name Select":
                jump name_select
            "The Fall":
                jump the_fall
            "Random Encounters":
                menu:
                    "Vegetoid":
                        jump vegetoid_start
                    "Whimsun":
                        jump whimsun_start
            "Frisk":
                jump frisk_start
label demo_end:
    "This demo ends here. Thanks for playing!"
    "Stay determined..."

label the_end:
return