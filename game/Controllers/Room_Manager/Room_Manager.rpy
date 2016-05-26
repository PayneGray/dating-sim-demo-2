init -1 python:
    class Room():
        def __init__(self,name = 'default', x, y , desc = 'default'):
            self.name = name
            self.x = x
            self.y = y
            self.desc = desc

    class Room_Manager():
        def __init__(self):
            self.rooms = []
            add_room(Room('se',1,0,'south east'))
            add_room(Room('sw',0,0,'south west'))
            add_room(Room('nw',0,1,'north west'))
            add_room(Room('ne',1,1,'north east'))
            self.current_room = self.rooms[0]
        
        def add_room(self,room):
            self.rooms.add(room)

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

        def cr_get_neighbors(self):
            dirs = []

            for r in self.rooms:
                if r.x == self.current_room.x and r.y = self.current_room.y+1:
                    dirs.append('north')
                    continue
                if r.x == self.current_room.x and r.y = self.current_room.y-1:
                    dirs.append('south')
                    continue
                if r.x == self.current_room.x+1 and r.y = self.current_room.y:
                    dirs.append('east')
                    continue
                if r.x == self.current_room.x-1 and r.y = self.current_room.y:
                    dirs.append('west')

            return dirs

    
    room_manager = Room_manager()

screen navigation_buttons:
    
    textbutton "north"
    textbutton "south"
    textbutton "east"
    textbutton "west"