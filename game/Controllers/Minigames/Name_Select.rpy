label Name_Select:

    python:
        ui.add(Name_Select())
        name = ui.interact(suppress_overlay=True, suppress_underlay=True)
    if name != 'quit':
        "Hello [name]!"
    return

init python:
    import math
    import pygame

    class quit_button():
        def __init__(self,x = 0, y = 0):
            self.x = x
            self.y = y
            self.text = Text("Quit")
            self.rect = pygame.Rect(x,y,self.text.size()[0],self.text.size()[1])
            
    class click_letter():
        def __init__(self,let = 'a',x = 0,y = 0):
            self.let = let
            self.origx = x
            self.origy = y

            self.timer = 0

            self.x = x
            self.y = y

        def set_pos(self,x,y):
            self.jigglex = (renpy.random.randint(0,2) - 1) + x
            self.jiggley = (renpy.random.randint(0,2) - 1) + y
            self.origx = x
            self.origy = y

        def update(self):
            self.jigglex = (renpy.random.randint(0,2) - 1) + self.x
            self.jiggley = (renpy.random.randint(0,2) - 1) + self.y

            self.timer += 1
            if self.timer <= 3:
                self.x = self.origx
                self.y = self.origy
            else:
                self.x = self.jigglex
                self.y = self.jiggley

            if self.timer > 5:
                self.timer = 0
                

    class Name_Select(renpy.Displayable):

        def __init__(self):
           
            renpy.Displayable.__init__(self)
            self.name = ""

            #are we done with the naming period
            self.done = False
            #show the confirm screen
            self.confirm = False

            self.oldst = 0

            self.quit= False

            self.title = Text("Name the fallen human.")
            self.quitb = Text("Quit")
            self.backspace = Text("Backspace")
            self.doneb = Text("Done")
            self.pname = Text(self.name)



            #game width and height, probably need to figure out how to make this dynamic
            self.WIDTH = 800
            self.HEIGHT = 600 

            self.lower_letters = [click_letter('a'),click_letter('b'),click_letter('c'),click_letter('d'),click_letter('e'),click_letter('f'),click_letter('g'),click_letter('h'),click_letter('i'),click_letter('j'),click_letter('k'),click_letter('l'),click_letter('m'),click_letter('n'),click_letter('o'),click_letter('p'),click_letter('q'),click_letter('r'),click_letter('s'),click_letter('t'),click_letter('u'),click_letter('v'),click_letter('w'),click_letter('x'),click_letter('y'),click_letter('z')]   
            self.upper_letters = [click_letter('A'),click_letter('B'),click_letter('C'),click_letter('D'),click_letter('E'),click_letter('F'),click_letter('G'),click_letter('H'),click_letter('I'),click_letter('J'),click_letter('K'),click_letter('L'),click_letter('M'),click_letter('N'),click_letter('O'),click_letter('P'),click_letter('Q'),click_letter('R'),click_letter('S'),click_letter('T'),click_letter('U'),click_letter('V'),click_letter('W'),click_letter('X'),click_letter('Y'),click_letter('Z')]

            row_count = 0

            #math!
            #there is a margin to the left and right, giving us a width of WIDTH - margin*2
            side_margin = 150
            top_margin = 100
            text_width = self.WIDTH - side_margin*2

            #there are 7 letters in a row, with the first being at margin, then the other 6 being spaced equally
            #so space is text_width / (row_count-1)
            text_space = text_width / (6)

            x = side_margin
            y = top_margin
            for l in self.upper_letters:
                l.set_pos(x,y)

                row_count+=1

                if row_count > 6:
                    row_count = 0
                    x = side_margin
                    y += 40
                else:
                    x += text_space

            x = side_margin
            y += 100
            row_count = 0
            for l in self.lower_letters:
                l.set_pos(x,y)

                row_count+=1

                if row_count > 6:
                    row_count = 0
                    x = side_margin
                    y += 40
                else:
                    x += text_space

        def interact(self):
            
            evt = ui.interact()
            rv = False

            if self.done:
                return self.name
            elif self.quit:
                return 'quit'
            else:
                return False

        # #not sure what this does but you have to put all children in here
        # def visit(self):            
        #     return False

        #handles all of the clicking
        def event(self, ev, x, y, st):

            if ev.type == pygame.MOUSEBUTTONDOWN:
                for l in self.lower_letters:
                    if pygame.Rect(l.x,l.y,Text(l.let).size()[0],Text(l.let).size()[1]).collidepoint(x,y):
                        self.name += l.let
                for l in self.upper_letters:
                    if pygame.Rect(l.x,l.y,Text(l.let).size()[0],Text(l.let).size()[1]).collidepoint(x,y):
                        self.name += l.let
                if pygame.Rect(172,530,55,40).collidepoint(x,y):
                    #quit
                    self.quit = True
                    return
                if pygame.Rect(320,530,150,40).collidepoint(x,y):
                    #backspace
                    if len(self.name) > 0:
                        self.name = self.name[:-1]
                    return
                if pygame.Rect(560,530,80,40).collidepoint(x,y):
                    #done
                    self.confirm = True
                    return

                
            # if self.score >= cap:
            #     self.turn_off_music()
            #     return "win"
            # else:
            if self.done:
                return self.name
            elif self.quit:
                return 'quit'
            else:
                raise renpy.IgnoreEvent()

        def render(self, width, height, st, at):
             
            #render object we will draw into
            r = renpy.Render(width, height)
            
            #figure out the time since last frame
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            if not self.confirm:
                for l in self.lower_letters:
                    l.update()
                    r.blit(renpy.render(Text(l.let),width,height,st,at),(l.x,l.y))
                for l in self.upper_letters:
                    l.update()
                    r.blit(renpy.render(Text(l.let),width,height,st,at),(l.x,l.y))
                self.pname = Text(self.name)
                r.blit(renpy.render(self.title,width,height,st,at),(width/2 - self.title.size()[0]/2,10))
                r.blit(renpy.render(self.pname,width,height,st,at),(width/2 - self.pname.size()[0]/2,50))
                r.blit(renpy.render(self.quitb,width,height,st,at),(width*.25 - self.quitb.size()[0]/2,height * .9))
                r.blit(renpy.render(self.backspace,width,height,st,at),(width * .5 - self.backspace.size()[0]/2,height * .9))
                r.blit(renpy.render(self.doneb,width,height,st,at),(width * .75 - self.doneb.size()[0]/2,height * .9))
            
            else:
                r.blit(renpy.render(self.pname,width,height,st,at),(width/2 - self.pname.size()[0]/2,height/2 - self.pname.size()[1]/2))
                r.blit
            
            # text_render = renpy.render(self.scoretext,width,height,st,at)
            # r.blit(text_render,(0.1,0.1))

            #redraw the frames    
            renpy.redraw(self, 0)
            #return the render
            return r