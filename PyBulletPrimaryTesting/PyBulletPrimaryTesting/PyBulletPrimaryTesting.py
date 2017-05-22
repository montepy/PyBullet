import pygame
import os,sys
import Player
import pBullet

SCREENHEIGHT = 480
SCREENWIDTH = 640
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Bullets")
pygame.key.set_repeat(100,100)
background = pygame.Surface(screen.get_size())
background = background.convert()
player = Player.Player(310,240,30,30,(0,0,255))
friendly = pygame.sprite.Group(player)
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
                    player.focus(True)
                if event.key == pygame.K_UP:
                    player.moveV(-4)
                if event.key == pygame.K_DOWN:
                    player.moveV(4)
                if event.key == pygame.K_RIGHT:
                    player.moveH(4)
                if event.key == pygame.K_LEFT:
                    player.moveH(-4)
            elif event.type == pygame.KEYUP:
                if not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN]:
                    player.moveV(0)
                if not pygame.key.get_pressed()[pygame.K_RIGHT] and not pygame.key.get_pressed()[pygame.K_LEFT]:
                    player.moveH(0)
                if event.key == pygame.K_LSHIFT:
                    player.focus(False)
    
    if pygame.key.get_pressed()[pygame.K_SPACE] and lastFiring > 100:
        friendly.add(player.shoot())
        lastFiring = 0
    background.fill((250,250,250))
    friendly.update()
    friendly.draw(background)
    
    screen.blit(background,(0,0))
    clock.tick(30)
    lastFiring += clock.get_time()
    
    #drawnRects.draw(background)
    
    pygame.display.flip()

pygame.quit()
                         