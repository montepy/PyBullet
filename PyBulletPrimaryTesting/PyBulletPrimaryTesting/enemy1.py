import pygame
class enemy1(pygame.sprite.Sprite):
    """description of class"""
    def __init__(self,left,top):
        self.image = pygame.surface.Surface([40,40])
        self.rect = pygame.rect.Rect(left,top,40,40)
        self.image.fill((190,100,190))
        self.health = 5
        self.hasHit = False
        self.hitWait = 5
        
    def whenHit(self):
        self.hasHit = True
        self.health -= 1
    def update(self):
        if self.hasHit and self.hitWait >0:
            self.image.fill(255,0,0)
            hitWait -= 1
        else:
            self.hasHit = False
            self.hitWait = 5
        self.rect.y += 10




