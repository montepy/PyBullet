import pygame
import random
import enemy1
import enemy2
import enemy3
import enemy3mirror
import enemy4
import Player
pygame.init()
class Level(object):
    """description of class"""
    def __init__(self,code,terminator,SCREENHEIGHT,SCREENWIDTH,levelnum):
        self.font = pygame.font.Font(None,50)
        self.levelcolor = (255,255,255)
        self.leveltext = "Level " + str(levelnum)
        self.textloc = (0,0)
        self.levelnum = levelnum
        self.enemygroup = pygame.sprite.Group()
        self.counter = 0
        self.codecounter = 0
        self.code = code
        self.terminator = terminator
        self.SCREENHEIGHT= SCREENHEIGHT
        self.SCREENWIDTH = SCREENWIDTH
        self.screenRect = pygame.rect.Rect(-60,-60,SCREENWIDTH+120,SCREENHEIGHT+120)
        self.player = Player.Player(310,240,20,20,(0,0,255))
        self.fbullet = pygame.sprite.Group()
        self.ebullet = pygame.sprite.Group()
        self.collective = pygame.sprite.Group(self.enemygroup)
        self.collective.add(self.fbullet)
        self.collective.add(self.player)
        self.enemyshoot = pygame.sprite.Group()
        

    def update(self,score):
        self.counter += 2
        if self.counter%100 == 0:
            
            if self.codecounter+2 > len(self.code):
                pass
            else:
                mod = int(self.code[self.codecounter+1])
                if self.code[self.codecounter] == "A":
                    for i in list(range(mod)):
                        enemy = enemy1.enemy1((i+1)*self.SCREENWIDTH/(mod+1),-40)
                        self.enemygroup.add(enemy)
                        self.collective.add(enemy)
                elif self.code[self.codecounter] == "B":
                    for i in list(range(mod)):
                        enemy = enemy2.enemy2((i+1)*self.SCREENWIDTH/(mod+1),-40)
                        self.enemygroup.add(enemy)
                        self.enemyshoot.add(enemy)
                        self.collective.add(enemy)
                elif self.code[self.codecounter] == "C":
                    for i in list(range(mod)):
                        enemy = enemy3.enemy3((i+1)*self.SCREENWIDTH/(mod+1) + 20,-40)
                        self.enemygroup.add(enemy)
                        self.collective.add(enemy)
                    for i in list(range(mod)):
                        enemy = enemy3mirror.enemy3mirror(-(i+1)*self.SCREENWIDTH/(mod+1) + 460,-40)
                        self.enemygroup.add(enemy)  
                        self.collective.add(enemy)
                elif self.code[self.codecounter] == "D":
                    for i in list(range(mod)):
                        enemy = enemy4.enemy4((i+1)*self.SCREENWIDTH/(mod+1),-40)
                        self.enemygroup.add(enemy)
                        self.enemyshoot.add(enemy)
                        self.collective.add(enemy)
                self.codecounter +=2
        for i in self.enemyshoot:
            if random.random() >= 0.97:
                bullet = i.shoot(self.player)
                self.collective.add(bullet)
                self.ebullet.add(bullet)
        if  self.counter >= self.terminator:
            return True

        self.collective.update()

        #denemy = pygame.sprite.groupcollide(self.fbullet,self.enemygroup,1,0)
        for i in self.fbullet:
            collided = pygame.sprite.spritecollideany(i,self.enemygroup)
            if collided:
                collided.whenHit()
                i.kill()
                score[0] += 50
        if pygame.sprite.spritecollideany(self.player,self.enemygroup):
            pygame.sprite.spritecollideany(self.player,self.enemygroup).kill()
            self.player.whenHit()
        if pygame.sprite.spritecollideany(self.player,self.ebullet):
            pygame.sprite.spritecollideany(self.player,self.ebullet).kill()
            self.player.whenHit()
        for i in self.enemygroup.sprites():
            if i.health ==0:
                i.kill()
                score[0] += 200
        if self.player.health == 0:
            self.player.kill()
            self.ebullet.empty()
            self.fbullet.empty()
            self.collective.empty()
            self.leveltext = "You Lost"
            self.textloc = (self.SCREENWIDTH/2-60,self.SCREENHEIGHT/2-30)
            self.levelcolor = (0,125,0)
            self.counter = 0
        else:
            score[0] += 2

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
        surface.blit(self.font.render(self.leveltext,0,(0,0,0)),self.textloc)
        self.collective.draw(surface)
        for i in list(range(self.player.health)):
            surface.blit(self.player.image,(i*30+20,450))


