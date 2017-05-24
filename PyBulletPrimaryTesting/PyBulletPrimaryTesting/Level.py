import pygame
import enemy1
import enemy2
import enemy3

class Level(object):
    """description of class"""
    def __init__(self,code,terminator,SCREENHEIGHT,SCREENWIDTH):
        self.enemygroup = pygame.sprite.Group()
        self.counter = 0
        self.codecounter = 0
        self.code = code
        self.terminator = terminator
        self.SCREENHEIGHT= SCREENHEIGHT
        self.SCREENWIDTH = SCREENWIDTH
        self.screenRect = pygame.rect.Rect(0,0,SCREENWIDTH,SCREENHEIGHT)
        self.player = Player.Player(310,240,30,30,(0,0,255))
        self.fbullet = pygame.sprite.Group()
        self.collective = pygame.sprite.Group(enemygroup).add(fbullet)
        self.collective.add(player)
        

    def update(self):
        self.counter += 2
        if self.counter%100 == 0:
            mod = self.code[self.codecounter+1]
            if self.code[self.codecounter] == "A":
                for i in len(range(mod)):
                    self.enemygroup.add(enemy1.enemy1(i*self.SCREENWIDTH/mod+20),-40)
            elif self.code[self.codecounter] == "B":
                for i in len(range(mod)):
                    self.enemygroup.add(enemy2.enemy2(i*self.SCREENWIDTH/mod+20),-40)
            elif self.code[self.codecounter] == "C":
                self.enemygroup.add(enemy3())
        if  self.counter >= terminator:
            return True
        self.codecounter +=2
        denemy = pygame.sprite.groupcollide(self.fbullet,self.enemygroup,1,0)
        for i in denemy:
            i.whenHit()
        if pygame.sprite.spritecollideany(self.player,self.enemygroup):
            self.player.whenHit()
        for i in self.collective:
            if not self.screenRect.contains(i):
                i.kill()
    def draw(self,surface):
        self.collective.draw(surface)

