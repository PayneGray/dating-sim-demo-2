init -1 python:
    class Room():
        def __init__(self,name = 'default', x = 0, y=0 , desc = 'default'):
            self.name = name
            self.x = x
            self.y = y
            self.desc = desc
            self.scene = "test_label"

    class Room_Manager():
        def __init__(self):
            self.rooms = []
            self.add_room(Room('se',1,0,'south east'))
            self.add_room(Room('sw',0,0,'south west'))
            self.add_room(Room('nw',0,1,'north west'))
            self.add_room(Room('ne',1,1,'north east'))
            self.current_room = self.rooms[0]
        
        def add_room(self,room):
            self.rooms.append(room)

        def move_dir(self,direction):
            dirx = self.current_room.x
            diry = self.current_room.y

            if direction == 'north':
                diry += 1
            if direction == 'east':
                dirx += 1
            if direction == 'south':
                diry -= 1
            if direction == 'west':
                dirx -= 1

            for room in self.rooms:
                if room.x == dirx and room.y == diry:
                    self.current_room = room
                    renpy.jump(room.scene)

        def cr_get_neighbors(self):
            dirs = []

            for r in self.rooms:
                if r.x == self.current_room.x and r.y == self.current_room.y+1:
                    dirs.append('north')
                    continue
                if r.x == self.current_room.x and r.y == self.current_room.y-1:
                    dirs.append('south')
                    continue
                if r.x == self.current_room.x+1 and r.y == self.current_room.y:
                    dirs.append('east')
                    continue
                if r.x == self.current_room.x-1 and r.y == self.current_room.y:
                    dirs.append('west')

            return dirs

    
    room_manager = Room_Manager()


screen show_nav_button:
    textbutton "Show Nav" action [Play ("sound", "audio/click.wav"), Show("navigation_buttons"), Hide("show_nav_button")] align(.95,.1) background Frame("text-box3.png",50, 21)

screen navigation_buttons:
    add "#0008"
    modal True

    $dirs = room_manager.cr_get_neighbors()

    textbutton "Hide Nav" action [Play ("sound", "audio/click.wav"),Hide("navigation_buttons"),Show('show_nav_button')] align(.95,.1) background Frame("text-box3.png",50, 21)
    
    if dirs.count('north') > 0:
        textbutton "north" background Frame("text-box3.png",50, 21) align(0.5,0.0) action[Play ("sound", "audio/click.wav"),Function(room_manager.move_dir,'north'),Hide("navigation_buttons"),Show('show_nav_button')]
    if dirs.count('south') > 0:
        textbutton "south" background Frame("text-box3.png",50, 21) align(0.5,1.0) action[Play ("sound", "audio/click.wav"),Function(room_manager.move_dir,'south'),Hide("navigation_buttons"),Show('show_nav_button')]
    if dirs.count('east') > 0:
        textbutton "east" background Frame("text-box3.png",50, 21) align(1.0,0.5)  action[Play ("sound", "audio/click.wav"),Function(room_manager.move_dir,'east'),Hide("navigation_buttons"),Show('show_nav_button')]
    if dirs.count('west') > 0:
        textbutton "west" background Frame("text-box3.png",50, 21) align(0.00,0.5) action[Play ("sound", "audio/click.wav"),Function(room_manager.move_dir,'west'),Hide("navigation_buttons"),Show('show_nav_button')]

    text '[room_manager.current_room.name]' align(0.5,0.5)

label test_label:
    scene background flowerfall
    with slideup
    "[room_manager.current_room.scene]"
    return