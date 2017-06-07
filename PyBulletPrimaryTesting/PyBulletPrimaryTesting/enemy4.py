import pygame
import math
import pBullet
class enemy4(pygame.sprite.Sprite):
    """description of class"""
    def __init__(self,left,top):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([40,40])
        self.rect = pygame.rect.Rect(left,top,40,40)
        self.defcolor= (155,155,255)
        self.image.fill((155,155,255))
        self.health = 5
        self.hasHit = False
        self.hitWait = 5
        self.vvelocity = 5
        self.hvelocity = 0
        print("Spawned e3")
        
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
        self.rect.y += self.vvelocity
        self.rect.x += self.hvelocity
    def shoot(self,player):
        vec = math.atan2(player.rect.centery -self.rect.centery, player.rect.centerx - self.rect.centerx)
        vectop = 20*math.sin(vec)
        vecside = 20*math.cos(vec)
        bullet = pBullet.pBullet(self.rect.x +self.rect.width/3,self.rect.y-40,8,8,True,vecside,vectop,(0,0,0))
        return bullet
    def draw(self,surface):
        surface.blit(pygame.transform.rotate(self.image,self.rangle),self.rect)

