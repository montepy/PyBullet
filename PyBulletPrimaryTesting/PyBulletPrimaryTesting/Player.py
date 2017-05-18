import pygame

class Player(pygame.Rect):
    def __init__(self,left,top,width,height,r_g_b):
        pygame.Rect.__init__(self,left,top,width,height)
        self.vvelocity = 0
        self.hvelocity = 0
        self.color = r_g_b
        self.focused = False

    #def __init__(self,rect,color):
    #    super.__init__(rect)
    #    
    #    self.vvelocity = 0
    #    self.hvelocity = 0
    #    self.color = color

    def moveH(self,move):
        self.hvelocity = move
    def moveV(self,move):
        self.vvelocity = move
    def update(self):
        mult = 1
        if self.focused:
            mult = 2
        self.x += self.hvelocity/mult
        self.y += self.vvelocity/mult

    def draw(self, background):
        pygame.draw.rect(background,self.color,self)

    def focus(self,bool):
        self.focused = bool

