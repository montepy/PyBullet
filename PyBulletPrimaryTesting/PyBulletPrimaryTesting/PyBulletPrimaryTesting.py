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
levels = [Level.Level("A8B4C4D6",650,SCREENHEIGHT,SCREENWIDTH,1),Level.Level("C4A2B3D1D2D3D4D5",1100,SCREENHEIGHT,SCREENWIDTH,2)]
activelevel = 0
#player = Player.Player(310,240,30,30,(0,0,255))
#fbullet = pygame.sprite.Group()
lastFiring = 0
clock = pygame.time.Clock()
won = False
score = [0]
scorefont = pygame.font.Font(None,40)

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
                    levels[activelevel].player.moveV(-6)
                if event.key == pygame.K_DOWN:
                    levels[activelevel].player.moveV(6)
                if event.key == pygame.K_RIGHT:
                    levels[activelevel].player.moveH(6)
                if event.key == pygame.K_LEFT:
                    levels[activelevel].player.moveH(-6)
            elif event.type == pygame.KEYUP:
                if not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN]:
                    levels[activelevel].player.moveV(0)
                if not pygame.key.get_pressed()[pygame.K_RIGHT] and not pygame.key.get_pressed()[pygame.K_LEFT]:
                    levels[activelevel].player.moveH(0)
                if event.key == pygame.K_LSHIFT:
                    levels[activelevel].player.focus(False)
    
    if pygame.key.get_pressed()[pygame.K_SPACE] and lastFiring > 200:
        bullet = levels[activelevel].player.shoot()
        levels[activelevel].collective.add(bullet)
        levels[activelevel].fbullet.add(bullet)
        lastFiring = 0
    background.fill(levels[activelevel].levelcolor)
    levels[activelevel].draw(background)
    screen.blit(background,(0,0))
    
    screen.blit(scorefont.render("Score " + str(score[0]),0,(0,0,0)),(SCREENWIDTH/2-20,0))
    
    if levels[activelevel].update(score):
        activelevel += 1
    if activelevel >= len(levels):
        done = True
        won = True
    
    clock.tick(30)
    lastFiring += clock.get_time()
    
    #drawnRects.draw(background)
    
    pygame.display.flip()

#endloop
while won:
    
    if pygame.event.peek():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                won = False;
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    won = False
    background.fill((255,255,255))
    screen.blit(background,(0,0))
    screen.blit(scorefont.render("Your final score was " + str(score[0]),1,(0,0,0)),(SCREENWIDTH/2-150,SCREENHEIGHT/2 -60))
    screen.blit(scorefont.render("YOU WIN!",1,(0,0,0)),(SCREENWIDTH/2-100,0))
    screen.blit(scorefont.render("Press ESC to end", 1,(0,0,0)),(SCREENWIDTH/2-100,400))
    pygame.display.flip()


pygame.quit()
                         