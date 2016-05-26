label initialize:
    #papyrus
    image papyrus normal = "characters/Character-Papyrus-Normal.png"
    image papyrus bigsmile = "characters/Character-Papyrus-BigSmile.png"
    image papyrus disgust = "characters/Character-Papyrus-disgust.png"
    image papyrus frown = "characters/Character-Papyrus-frown.png"
    image papyrus nervoussmile = "characters/Character-Papyrus-nervoussmile.png"
    image papyrus reassuringsmile = "characters/Character-Papyrus-reassuringsmile.png"
    image papyrus Sad = "characters/Character-Papyrus-Sad.png"
    image papyrus sheepish = "characters/Character-Papyrus-sheepish.png"
    image papyrus shock = "characters/Character-Papyrus-Shock.png"
    image papyrus surprised = "characters/Character-Papyrus-Surprised.png"
    image papyrus suspicious = "characters/Character-Papyrus-suspicious.png"
    image papyrus unsure = "characters/Character-Papyrus-unsure.png"
    #sans
    image sans normal = "characters/sans-normal.png"
    image sans glance = "characters/sans-normal-glance.png"
    image sans sad = "characters/sans-sad.png"
    image sans silhouette = "characters/sans-shakemyhand.png"
    image sans shakehand = "characters/sans-shakemyhand2.png"
    #flowey
    image flowey placeholder = "characters/flowey_ph.png"
    #toriel
    image toriel placeholder = "characters/toriel_ph.png"
    #background-images

    #snowdin
    image background snowdin = "backgrounds/snowdincropped.jpg"
    image background papyrus_room = "backgrounds/Background-PapyrusRoom.jpg"
    image background snowdin_bridge = "backgrounds/Background-Snowdin-Bridge-cropped.jpg"
    image background snowdin_forest = "backgrounds/Background-Snowdin-Gate2.jpg"
    image background snowdin_icegolf = "backgrounds/Background-Snowdin-Icegolf.png"
    image background snowdin_intersection = "backgrounds/Background-Snowdin-Intersection.png"
    image background snowdin_snowman = "backgrounds/Background-Snowdin-Snowman.png"

    image background papyrus_number = "characters/Papyrus-number.png"

    #prologue
    image background prologue1 = "backgrounds/prologue.jpg"
    image background intro = "backgrounds/background-intro.png"

    #flowerbed
    image background flowerfall = "backgrounds/background-ruins-flowerpatch.png"
    image background floweyroom = "backgrounds/background-ruins-floweyroom.png"

    #the ruins
    image background ruins_outside_house = "backgrounds/background-ruins-blacktree.png"
    image background ruins_froggit_room = "backgrounds/background-ruins-froggitroom.png"
    image background ruins_first_entrance = "backgrounds/background-ruins-firstentrance.png"
    image background ruins_toy_knife_room = "backgrounds/background-ruins-toykniferoom.png"
    image background ruins_spider_bakery = "backgrounds/background-ruins-spiderbakery.png"


    #toriel house
    image background toriel_house_corridor = "backgrounds/background-ruins-corridor.png"
    image background toriel_house_frisk_room = "backgrounds/background-ruins-friskroom.png"
    image background toriel_house_kitchen = "backgrounds/background-ruins-kitchen.png"
    image background toriel_house_livingroom = "backgrounds/background-ruins-livingroom.png"
    image background toriel_house_staircase = "backgrounds/background-ruins-staircase.png"
    image background toriel_house_toriel_room = "backgrounds/background-ruins-torielroom.png"
    image background toriel_house_your_room = "backgrounds/background-ruins-yourroom.png"
    image background toriel_house_corridor = "backgrounds/background-ruins-corridor.png"


    #character-settings
    #character settings
    define diary = ('Diary')
    define frisk = ('Frisk')
    define xxxfrisk = ('XXX')
    define toriel = ('Toriel')
    define narration = Character(kind=nvl)
    define system = Character('', color="#FFFFFF")
    define papyrusChar = Character('Papyrus', color="#FFFFFF", what_prefix='{font=font/Parchment-MF.ttf}{size=40}', what_suffix='{/size}{/font}')
    define xxxpapyrus = Character('xxx', color="#FFFFFF", what_prefix='{font=font/Parchment-MF.ttf}{size=40}', what_suffix='{/size}{/font}')
    define xxxsans = Character('xxx', color="#FFFFFF", what_prefix='{font=font/ComicRelief.ttf}{size=20}', what_suffix='{/size}{/font}')
    define sans = Character('Sans', color="#FFFFFF", what_prefix='{font=font/ComicRelief.ttf}{size=20}', what_suffix='{/size}{/font}')
    define floweyChar = Character('Flowey', color="#FFFFFF")
    define torielChar = Character('Toriel', color="#FFFFFF")
    define wilsonChar = Character('Wilson', color="#FFFFFF")
    #sprite positions
    init:
        $ left = Position(xpos = 0.25, xanchor = 'left')
        $ center = Position(xpos = 0.5, xanchor = 'center')
        $ right = Position(xpos = 0.75, xanchor = 'right')

    init python:
        # Wrapper to capitalize Papyrus' text
        def papyrus(text, *args, **kwargs):
            papyrusChar(text, *args, **kwargs)
        def flowey(text, *args, **kwargs):
            floweyChar(text, *args, **kwargs)
        def toriel(text, *args, **kwargs):
            torielChar(text, *args, **kwargs)
        def wilson(text, *args, **kwargs):
            wilsonChar(text, *args, **kwargs)

    #default-font
    init python:
        style.default.font = "font/DTM-Mono.otf"

    #global variables
    init python:
        #init the player
        player = Player()
        day = 0
        menu_state = "stats"
        
