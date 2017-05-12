#hello
import pygame
import os,sys
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("First")
background = pygame.Surface(screen.get_size())
background = background.convert()
class Controllable(pygame.Rect):
    def __init__(self,left,top,width,height):
        pygame.Rect.__init__(self,left,top,width,height,hvelocity = 0,vvelocity = 0)
        hvelocity = 0#edit this
        vvelocity = 0

    def update(self):
        dis.x += hvelocity
        dis.y += vvelocity

dis = Controllable(25,25,25,25)
#dis = pygame.Rect(25,25,25,25)
done = False
clock = pygame.time.Clock()

while not done:
    if pygame.event.peek():
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_UP:
                dis.vvelocity = -2
            elif event.key == pygame.K_RIGHT:
                 dis.hvelocity = 2
            elif event.key == pygame.K_DOWN:
                dis.vvelocity = 2
            elif event.key == pygame.K_LEFT:
                dis.hvelocity = -2

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                dis.vvelocity = 0
            elif event.key == pygame.K_RIGHT:
                dis.hvelocity = 0
            elif event.key == pygame.K_DOWN:
                dis.vvelocity = 0
            elif event.key == pygame.K_LEFT:
                dis.hvelocity = 0
    dis.update()
    clock.tick(30)
    background.fill((250,250,250))
    pygame.draw.rect(background,pygame.color.Color(50,200,50),dis)
    screen.blit(background,(0,0))

    pygame.display.flip()
    if dis.right>=400:
        done = True

pygame.quit()