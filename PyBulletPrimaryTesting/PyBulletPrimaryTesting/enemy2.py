import pygame
import pBullet
class enemy2(pygame.sprite.Sprite):
    
    def __init__(self,left,top):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([40,40])
        self.rect = pygame.rect.Rect(left,top,40,40)
        self.defcolor = (0,255,255)
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
            self.image.fill(self.defcolor)
            
        if self.health == 0:
            self.kill()
            return True
        self.rect.y += 5


    def shoot(self,player):
        
        bullet = pBullet.pBullet(self.rect.x +self.rect.width/3,self.rect.y-40,10,10,True,0,20,(0,0,0))
        return bullet

