#hello
import pygame
import os,sys
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("First")
background = pygame.Surface(screen.get_size())
background = background.convert()
dis = pygame.Rect(25,25,25,25)
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(30)
    dis.right += 1;
    background.fill((250,250,250))
    pygame.draw.rect(background,pygame.color.Color(50,200,50),dis)
    screen.blit(background,(0,0))

    pygame.display.flip()
    if dis.right>=100:
        done = True

pygame.quit()