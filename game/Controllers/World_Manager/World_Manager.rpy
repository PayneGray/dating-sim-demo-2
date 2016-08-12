label default_event:
    "You shouldn't see this.  Its the default. Tell Wilson."
    return

init -10 python:
    import random
    class Area():

        def __init__(self,name):
            self.rooms = []
            self.currentRoom = False
            self.name = name
            self.random_areas = []
            self.random_monsters = []
            #self.random_scenes = ['papyrus_random','sans_random','toriel_random','flowey_random']
        
        def add_room(self,room):
            self.rooms.append(room)

        def move_to_room(self,name):
            for r in self.rooms:
                if r.name == name:
                    self.currentRoom = r
                    renpy.jump("load_room")
                    break

        def move_dir(self,direction):
            dirx = self.currentRoom.x
            diry = self.currentRoom.y

            if direction == 'north':
                diry += 1
            if direction == 'east':
                dirx += 1
            if direction == 'south':
                diry -= 1
            if direction == 'west':
                dirx -= 1

            for room in self.rooms:
                if not room.locked:
                    if room.x == dirx and room.y == diry:

                        self.currentRoom = room
                        renpy.jump("load_room")

        def get_random_monster(self,name):
            for x in self.random_monsters:
                if x.name == name:
                    return x

            return False


        def cr_get_neighbors(self):
            dirs = []

            for r in self.rooms:
                if r.x == self.currentRoom.x and r.y == self.currentRoom.y+1 and not r.locked and not r.locksouth:
                    dirs.append('north')
                    continue
                if r.x == self.currentRoom.x and r.y == self.currentRoom.y-1 and not r.locked and not r.locknorth:
                    dirs.append('south')
                    continue
                if r.x == self.currentRoom.x+1 and r.y == self.currentRoom.y and not r.locked and not r.lockwest:
                    dirs.append('east')
                    continue
                if r.x == self.currentRoom.x-1 and r.y == self.currentRoom.y and not r.locked and not r.lockeast:
                    dirs.append('west')

            return dirs

        def get_random_scene(self):
            
            s = False
            if len(self.random_scenes) > 0:
                if renpy.random.randint(0,100) < 101:
                    s = self.random_scenes[renpy.random.randint(0,len(self.random_scenes)-1)]
                        #remove so it doesn't happen again
                    self.random_scenes.remove(s)
                    if len(self.random_scenes) == 0 and wilson_locked:
                        renpy.call_in_new_context("wilson_unlock")
                    return s
            
            return s

    class Room():
        def __init__(self,name = 'default', x = 0, y=0 , desc = 'default',locked = False, bg = 'nothing'):
            self.name = name
            self.x = x
            self.y = y
            self.desc = desc
            self.visited = False
            #place holder to stop people from moving into the room.
            self.locked = locked
            self.bg = bg

            #stop people from leaving room in wrong direction
            self.locksouth = False
            self.locknorth = False
            self.lockeast = False
            self.lockwest = False
            self.events = []
            self.monsters = []
            self.current_monster = False


        #First check to see if the room itself has an event to do
        #Then check to see if the room has a monster event to do
        def get_event(self):

            for e in self.events:
                if e.completed == False:
                    return e
            for m in self.monsters:
                for e in m.specialEvents:
                    if e.completed == False:
                        self.current_monster = m
                        return e

                if m.get_current_event():
                    if m.get_current_event().completed == False:
                        self.current_monster = m
                        return m.get_current_event()

            return False

        def add_monster(self,Monster):
            Monster.currentRoom = self
            self.monsters.append(Monster)

        def remove_monster(self,Monster):
            self.monsters.remove(Monster)


    class Event():
        def __init__(self,label = "flowey_hangout",perm = False,arg = False):
            self.completed = False
            self.label = label
            self.owner = False
            self.permanent = perm
            self.arg = arg


        def call_event(self):
            if self.arg:
                renpy.call_in_new_context(self.label,self.arg)
            else:
                renpy.call_in_new_context(self.label)
            if self.permanent == False:
                self.completed = True

    class World():

    
        def __init__(self):
            self.name = "Underground"
            self.areas = []
            self.currentArea = False
            self.maxTime = 1440
            self.currentTime = 0
            self.day = 1
            self.timeZones = {"Night":0,"Morning":480,"Day":720,"Afternoon":960,"Evening":1200}
            self.generate_ruins()

        def get_current_timezone(self):
            
            timezone = "Night"
            for t,z in self.timeZones.iteritems():
                if self.currentTime > z and self.timeZones[timezone] <= z:
                    timezone = t

            return timezone

        #this function should be called at the beginning of every day.
        #it will update all of the areas for whatever we need.
        def update_day(self):
            self.seed_random_monsters()


        #this function will seed all of the random monsters to the various rooms they can be in.
        #rooms with events already in them should be ignored.
        def seed_random_monsters(self):
            for a in self.areas:
                #we need to add each random monster to a different room

                #first we get a list of all the rooms in the area
                room_list = list(a.rooms)
                #now we remove every room that has an event, or another monster in it
                for r in room_list:
                    if len(r.monsters) > 0 or len(r.events) > 0:
                        room_list.remove(r)

                #now we seed the monsters into random rooms in the list, removing each room as we do it.
                #we will do this until we run out of rooms
                random.shuffle(a.random_monsters)
                random.shuffle(room_list)
                for m in a.random_monsters:
                    if len(room_list) > 0:
                        m.move_to_room(room_list[0].name)
                        room_list.remove(room_list[0])

            return

        def update_world(self,update_day = False):

            timezone = self.get_current_timezone()
            renpy.notify(timezone)
            for a in self.areas:
                for r in a.rooms:
                    for m in r.monsters:
                        if m.schedule:
                            if timezone in m.schedule:
                                for x,t in m.schedule[timezone].iteritems():
                                    m.move_to_room(x)

            if update_day:
                self.update_day()

            return

        def get_current_time(self):
            seconds = self.currentTime * 60
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return "%d:%02d" % (h, m)

        #sets the current time
        def set_current_time(self,time,update_day = False):

            if time > 1440 or time < 0:
                renpy.notify("Time too high or negative for set_current_time.")
                return

            if update_day:
                if self.currentTime > time:
                    self.day += 1


            self.currenttime = time


            self.update_world(update_day)


        #Adds minutes to the current time
        #Updates current day if time goes over
        def update_current_time(self,amount):

            #check to see if we added more than one day

            new_time = self.currentTime + amount
            update_day_check = False

            if new_time > self.maxTime:
                self.day += 1
                new_time -= self.maxTime
                update_day_check = True
            if new_time < 0:
                self.day -= 1
                new_time += self.maxTime
                update_day_check = True

            self.currentTime = new_time
            self.update_world(update_day_check)
            renpy.call("load_room")

        def add_monster(self,monster):
            if isinstance(monster,Monster):
                self.monsters.append()
            else:
                renpy.notify("Illegal Type: not a Monster")

        def add_area(self,area):
            if isinstance(area,Area):
                self.areas.append(area)
            else:
                renpy.notify("Illegal Type: not an Area")

        def generate_ruins(self):
            self.add_area(TheRuins())
            self.currentArea = self.areas[0]
            self.currentArea.currentRoom = self.currentArea.rooms[0]



label test_label:
    "Awesome, it worked."
    return
#This is the label that handles the loading
#shows the current background, if the room hasn't been visited shows the description, sets visited to True, then Pauses to allow player to do things
label load_room:
    $ renpy.scene()
    
    $ renpy.show(world.currentArea.currentRoom.bg)
    
    with fade
    if not world.currentArea.currentRoom.visited:
        "[world.currentArea.currentRoom.desc]"
    $ world.currentArea.currentRoom.visited = True

    $ temp_event = world.currentArea.currentRoom.get_event()

    while temp_event:
        $ temp_event.call_event()
        $ temp_event = world.currentArea.currentRoom.get_event()
    
    while True:
        call show_buttons
        pause
    return



#until we find a way to figure out what order the files are loaded in, all the rooms have to go in here.





