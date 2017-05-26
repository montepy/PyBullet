import pygame
import enemy1
import enemy2
import enemy3
import enemy3mirror
import Player

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
        self.screenRect = pygame.rect.Rect(-60,-60,SCREENWIDTH+60,SCREENHEIGHT+60)
        self.player = Player.Player(310,240,30,30,(0,0,255))
        self.fbullet = pygame.sprite.Group()
        self.collective = pygame.sprite.Group(self.enemygroup)
        self.collective.add(self.fbullet)
        self.collective.add(self.player)
        

    def update(self):
        self.counter += 2
        if self.counter%100 == 0:
            mod = int(self.code[self.codecounter+1])
            if self.code[self.codecounter] == "A":
                for i in list(range(mod)):
                    enemy = enemy1.enemy1(i*self.SCREENWIDTH/mod+20,-40)
                    self.enemygroup.add(enemy)
                    self.collective.add(enemy)
            elif self.code[self.codecounter] == "B":
                for i in list(range(mod)):
                    enemy = enemy2.enemy2(i*self.SCREENWIDTH/mod+20,-40)
                    self.enemygroup.add(enemy)
                    self.collective.add(enemy)
            elif self.code[self.codecounter] == "C":
                for i in list(range(mod)):
                    enemy = enemy3.enemy3(i*self.SCREENWIDTH/mod + 20,-40)
                    self.enemygroup.add(enemy)
                    self.collective.add(enemy)
                for i in list(range(mod)):
                    enemy = enemy3mirror.enemy3mirror(-i*self.SCREENWIDTH/mod + 460,-40)
                    self.enemygroup.add(enemy)  
                    self.collective.add(enemy)
            self.codecounter +=2
        if  self.counter >= self.terminator:
            return True

        self.collective.update()

        #denemy = pygame.sprite.groupcollide(self.fbullet,self.enemygroup,1,0)
        for i in self.fbullet:
            collided = pygame.sprite.spritecollideany(i,self.enemygroup)
            if collided:
                collided.whenHit()
                i.kill()
        if pygame.sprite.spritecollideany(self.player,self.enemygroup):
            self.player.whenHit()
        if self.player.rect.x <0:
            self.player.x == 0
        if self.player.rect.y <0:
            self.player.y == 0
        if self.player.rect.y > self.SCREENHEIGHT - self.player.rect.height:
            self.player.rect.y = self.SCREENHEIGHT - self.player.rect.height
        if self.player.rect.x > self.SCREENWIDTH - self.player.rect.width:
            self.player.rect.x = self.SCREENWIDTH - self.player.rect.width
        for i in self.collective:
            if not self.screenRect.contains(i):
                i.kill()
    def draw(self,surface):
        self.collective.draw(surface)

