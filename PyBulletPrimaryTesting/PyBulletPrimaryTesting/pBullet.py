import pygame

class pBullet(pygame.sprite.DirtySprite):
    """description of class"""
    def __init__(self,x,y,width,height,isPlayers,hvelocity,vvelocity,r_g_b):
        pygame.sprite.DirtySprite.__init__(self)
        self.isPlayers = isPlayers
        self.hvelocity = hvelocity
        self.vvelocity = vvelocity
        self.image = pygame.Surface([width,height])
        self.image.fill(r_g_b)
        self.rect = pygame.rect.Rect(x,y,width,height)

    def update(self):
        self.rect.x += self.hvelocity
        self.rect.y += self.vvelocity
    def whenHit(self):
        return

    def draw(self,background):
        pygame.draw.rect(background,self.color,self)


