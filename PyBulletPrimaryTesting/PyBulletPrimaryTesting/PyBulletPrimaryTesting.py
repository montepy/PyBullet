import pygame
import os,sys
import Player
import pBullet
import Level
pygame.init()

SCREENHEIGHT = 480
SCREENWIDTH = 640
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Bullets")
pygame.key.set_repeat(100,100)
background = pygame.Surface(screen.get_size())
background = background.convert()
levels = [Level.Level("A4B4C4",450,SCREENHEIGHT,SCREENWIDTH,1),Level.Level("C4A2B3",450,SCREENHEIGHT,SCREENWIDTH,2)]
activelevel = 0
#player = Player.Player(310,240,30,30,(0,0,255))
#fbullet = pygame.sprite.Group()
lastFiring = 0
clock = pygame.time.Clock()

done = False
while not done:
    if pygame.event.peek():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_LSHIFT:
                    levels[activelevel].player.focus(True)
                if event.key == pygame.K_UP:
                    levels[activelevel].player.moveV(-4)
                if event.key == pygame.K_DOWN:
                    levels[activelevel].player.moveV(4)
                if event.key == pygame.K_RIGHT:
                    levels[activelevel].player.moveH(4)
                if event.key == pygame.K_LEFT:
                    levels[activelevel].player.moveH(-4)
            elif event.type == pygame.KEYUP:
                if not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN]:
                    levels[activelevel].player.moveV(0)
                if not pygame.key.get_pressed()[pygame.K_RIGHT] and not pygame.key.get_pressed()[pygame.K_LEFT]:
                    levels[activelevel].player.moveH(0)
                if event.key == pygame.K_LSHIFT:
                    levels[activelevel].player.focus(False)
    
    if pygame.key.get_pressed()[pygame.K_SPACE] and lastFiring > 100:
        bullet = levels[activelevel].player.shoot()
        levels[activelevel].collective.add(bullet)
        levels[activelevel].fbullet.add(bullet)
        lastFiring = 0
    background.fill((250,250,250))
    levels[activelevel].draw(background)
    screen.blit(background,(0,0))
    
    if levels[activelevel].update():
        activelevel += 1
    if activelevel >= len(levels):
        done = True
    
    clock.tick(30)
    lastFiring += clock.get_time()
    
    #drawnRects.draw(background)
    
    pygame.display.flip()

pygame.quit()
                         