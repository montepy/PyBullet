import pygame
class enemy3(pygame.sprite.Sprite):
    """description of class"""
    def __init__(self,left,top):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([40,40])
        self.rect = pygame.rect.Rect(left,top,40,40)
        self.image.fill((106,255,76))
        self.health = 10
        self.hasHit = False
        self.hitWait = 5
        self.vvelocity = 10
        self.hvelocity = 8
        self.rangle = 0
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
            
        if self.health == 0:
            self.kill()
            return True
        self.rangle += 1
        self.hvelocity -= 1
        self.rect.y += self.vvelocity
        self.rect.x += self.hvelocity

    def draw(self,surface):
        surface.blit(pygame.transform.rotate(self.image,self.rangle),self.rect)

