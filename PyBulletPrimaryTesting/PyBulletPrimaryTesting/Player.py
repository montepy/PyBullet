import pygame
import pBullet
class Player(pygame.sprite.DirtySprite):
    def __init__(self,left,top,width,height,r_g_b):
        pygame.sprite.DirtySprite.__init__(self)
        self.image =pygame.Surface([width,height])
        self.image.fill(r_g_b)
        self.rect = pygame.rect.Rect(left,top,width,height)
        self.vvelocity = 0
        self.hvelocity = 0
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
        print("Hello")
    def update(self):
        mult = 1
        if self.focused:
            mult = 2
        self.rect.x += self.hvelocity/mult
        self.rect.y += self.vvelocity/mult

    def draw(self, background):
        pygame.draw.rect(background,self.color,self)

    def focus(self,bool):
        self.focused = bool

    def shoot(self):
        bullet = pBullet.pBullet(self.rect.x +self.rect.width/3,self.rect.y,self.rect.width/6,self.rect.height/2,True,0,-16,(0,182,255))
        return bullet

