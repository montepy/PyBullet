import pygame
class enemy2(pygame.sprite.Sprite):
    
    def __init__(self,left,top):
        self.image = pygame.surface.Surface([40,40])
        self.rect = pygame.rect.Rect(left,top,40,40)
        self.image.fill((0,255,255))
        self.health = 5
        self.hasHit = False
        self.hitWait = 5

    def update(self):
        
        if self.hasHit and self.hitWait >0:
            self.image.fill(255,0,0)
            hitWait -= 1
        else:
            self.hasHit = False
            self.hitWait = 5
        self.rect.y += 10

    def shoot(self):
        
        bullet = pBullet.pBullet(self.rect.x +self.rect.width/3,self.rect.y-30,self.rect.width/6,self.rect.height/2,True,0,16,(0,182,255))
        return bullet
