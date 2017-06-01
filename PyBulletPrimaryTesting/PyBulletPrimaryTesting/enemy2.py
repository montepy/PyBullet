import pygame
import pBullet
class enemy2(pygame.sprite.Sprite):
    
    def __init__(self,left,top):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([40,40])
        self.rect = pygame.rect.Rect(left,top,40,40)
        self.image.fill((0,255,255))
        self.health = 5
        self.hasHit = False
        self.hitWait = 5
        print("Spawned e2")
        
    def whenHit(self):
        self.hasHit = True
        self.health -= 1
    def update(self):
        
        if self.hasHit and self.hitWait >0:
            self.image.fill((255,0,0))
            self.hitWait -= 1
        else:
            self.hasHit = False
            self.hitWait = 5
            
        if self.health == 0:
            self.kill()
        self.rect.y += 10


    def shoot(self):
        
        bullet = pBullet.pBullet(self.rect.x +self.rect.width/3,self.rect.y-40,self.rect.width/6,self.rect.height/2,True,0,20,(0,182,255))
        return bullet

