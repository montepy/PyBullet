import pygame

class pBullet(pygame.rect.Rect):
    """description of class"""
    def __init__(self,x,y,width,height,isPlayers,hvelocity,vvelocity,r_g_b):
        pygame.Rect.__init__(self,x,y,width,height)
        self.isPlayers = isPlayers
        self.hvelocity = hvelocity
        self.vvelocity = vvelocity
        self.color = r_g_b

    def update(self):
        self.x += self.hvelocity
        self.y += self.vvelocity

    def draw(self,background):
        pygame.draw.rect(background,self.color,self)


