init -1 python:

    class th_staircase(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Staircase"
            self.x = 100
            self.y = 100
            self.desc = "There is a stairway here."
            self.scene = "toriel_house_staircase"

    class th_corridor(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Corridor"
            self.x = 101
            self.y = 100
            self.desc = "This is the hallway."
            self.scene = "toriel_house_corridor"

    class th_kitchen(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Kitchen"
            self.x = 99
            self.y = 101
            self.desc = "This is the kitchen."
            self.scene = "toriel_house_kitchen"

    class th_living_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Living Room"
            self.x = 99
            self.y = 100
            self.desc = "This is the living room."
            self.scene = "toriel_house_living_room"

    class th_frisk_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Frisk's Room"
            self.x = 101
            self.y = 101
            self.desc = "This is Frisk's room."
            self.scene = "toriel_house_frisk_room"
            self.locked = True

    class th_your_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Your Room"
            self.x = 101
            self.y = 101
            self.desc = "This is your room."
            self.scene = "toriel_house_your_room"
            self.locked = True

    class th_toriel_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Toriel's Room"
            self.x = 101
            self.y = 101
            self.desc = "This is toriel's room."
            self.scene = "toriel_house_toriel_room"
            self.locked = True
    
    room_manager.add_room(th_staircase())
    room_manager.add_room(th_kitchen())
    room_manager.add_room(th_living_room())
    room_manager.add_room(th_corridor())
    room_manager.add_room(th_your_room())
    room_manager.add_room(th_frisk_room())
    room_manager.add_room(th_toriel_room())
    
    room_manager.current_room = room_manager.rooms[0]

label toriel_house_corridor:
    scene background toriel_house_corridor
    while True:
        '[room_manager.current_room.desc]'
        menu:
            "There are three doors here."
            "Frisk":
                jump toriel_house_frisk_room
            "Toriel":
                jump toriel_house_toriel_room
            "Your":
                jump toriel_house_your_room
    return

    

label toriel_house_kitchen:
    scene background toriel_house_kitchen
    $ chance = room_manager.get_random_scene()
    if chance:
        $ renpy.call_in_new_context(chance)
    while True:
        "[room_manager.current_room.desc]"
    return
    
label toriel_house_living_room:
    scene background toriel_house_livingroom
    $ chance = room_manager.get_random_scene()
    if chance:
        $ renpy.call_in_new_context(chance)
    while True:
        "[room_manager.current_room.desc]"
    return
    
label toriel_house_staircase :
    scene background toriel_house_staircase

    while True:
        "[room_manager.current_room.desc]"
    return
    
label toriel_house_toriel_room:
    $ room_manager.move_to_room("Toriel's Room") 
    scene background toriel_house_toriel_room
    
    $ chance = room_manager.get_random_scene()
    if chance:
        $ renpy.call_in_new_context(chance)

    while True:
        "[room_manager.current_room.desc]"
    return
    
label toriel_house_your_room:
    $ room_manager.move_to_room("Your Room") 
    scene background toriel_house_your_room
    $ chance = room_manager.get_random_scene()
    if chance:
        $ renpy.call_in_new_context(chance)
    while True:
        "[room_manager.current_room.desc]"
    return

label toriel_house_frisk_room:
    $ room_manager.move_to_room("Frisk's Room") 
    scene background toriel_house_frisk_room
    $ chance = room_manager.get_random_scene()
    if chance:
        $ renpy.call_in_new_context(chance)
    while True:
        "[room_manager.current_room.desc]"
    return
    


label toriel_random:
    show toriel placeholder
    with moveinbottom
    toriel "BOO"
    toriel "This is a random scene!"
    hide toriel ph
    with moveoutbottom
    return

label flowey_random:
    show flowey placeholder
    with moveinbottom
    flowey "HOWDY"
    flowey "Getting tired of these yet?"
    hide flowey ph
    with moveoutbottom
    return

label papyrus_random:
    show papyrus surprised
    with moveinbottom
    papyrus "....."
    papyrus "Spaghetti?"
    hide papyrus surprised
    with moveoutbottom
    return

label sans_random:
    show sans normal
    with moveinbottom
    sans "Brah"
    sans "Help"
    sans "Me."
    hide sans normal
    with moveoutbottom
    return
