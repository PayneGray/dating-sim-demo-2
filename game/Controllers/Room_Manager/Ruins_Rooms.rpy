init:
#flowerbed
    image background ruins_caveroom = "backgrounds/ruins/background-ruins-flowerpatch.png"
    image background ruins_floweyroom = "backgrounds/ruins/background-ruins-floweyroom.png"

#the ruins
    image background ruins_outside_house = "backgrounds/ruins/background-ruins-blacktree.png"
    image background ruins_froggit_room = "backgrounds/ruins/background-ruins-froggitroom.png"
    image background ruins_first_entrance = "backgrounds/ruins/background-ruins-firstentrance.png"
    image background ruins_toy_knife_room = "backgrounds/ruins/background-ruins-toykniferoom.png"
    image background ruins_spider_bakery = "backgrounds/ruins/background-ruins-spiderbakery.png"


init -1 python:
    
    random_rooms = []
    class ruins_caveroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Cave Room"
            self.x = 10
            self.y = 0
            self.desc = "The large cavern you are in is lit by the light coming from far above, shining into the corners of the cave and illuminating the path of flowers that broke your fall. There is one exit from the cavern, a large, ornate doorway leading to another cave."
            self.bg = "background ruins_caveroom"

    class ruins_grassroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Grass Room"
            self.x = 9
            self.y = 0
            self.desc = "The large cavern you are in is lit by the light coming from far above, shining into the corners of the cave and illuminating the path of flowers that broke your fall. There is one exit from the cavern, a large, ornate doorway leading to another cave."
            self.bg = "background ruins_caveroom"

    class ruins_ruinsentrance(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Ruins Entrance"
            self.x = 9
            self.y = 1
            self.desc = "The large cavern you are in is lit by the light coming from far above, shining into the corners of the cave and illuminating the path of flowers that broke your fall. There is one exit from the cavern, a large, ornate doorway leading to another cave."
            self.bg = "background ruins_caveroom"

    class ruins_tunnels(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Tunnels"
            self.x = 9
            self.y = 2
            self.desc = "The large cavern you are in is lit by the light coming from far above, shining into the corners of the cave and illuminating the path of flowers that broke your fall. There is one exit from the cavern, a large, ornate doorway leading to another cave."
            self.bg = "background ruins_caveroom"


    
    room_manager.add_room(ruins_caveroom())
    room_manager.add_room(ruins_grassroom())
    room_manager.add_room(ruins_ruinsentrance())
    room_manager.add_room(ruins_tunnels())

    room_manager.current_room = room_manager.rooms[0]


    

    
