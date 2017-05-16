import pygame
import os,sys
pygame.init()

SCREENHEIGHT = 480
SCREENWIDTH = 640
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Testing text")
background = pygame.Surface(screen.get_size())
background = background.convert()
Fonz = pygame.font.Font(None,40)
count = 0
done = False
clock = pygame.time.Clock()
while not done:
    clock.tick(30)
    background.fill((255,255,255))
    
    screen.blit(background,(0,0))
    count += 1
    screen.blit(Fonz.render("Hello",True,(0,0,0),(150,255,255)),(count,20))
    pygame.display.flip()

pygame.quit()