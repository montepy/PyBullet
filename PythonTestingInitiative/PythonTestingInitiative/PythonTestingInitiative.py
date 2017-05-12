#hello
import pygame
import os,sys
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("First")
background = pygame.Surface(screen.get_size())
background = background.convert()
class Controllable(pygame.Rect):
    def __init__(self,left,top,width,height,hvelocity = 0,vvelocity = 0):
        pygame.Rect.__init__(self,left,top,width,height)
        self.hvelocity = hvelocity
        self.vvelocity = vvelocity
        self.can_jump = False
    def jump(self):
        if self.can_jump:
            self.can_jump = False
            self.vvelocity = -20

    def gravity(self):
        self.vvelocity += 1

    def update(self):
        self.gravity()
        dis.x += self.hvelocity
        dis.y += self.vvelocity

    def collisionTest(self,rect):
        if self.colliderect(rect):
            self.y = rect.y - self.height
            if self.vvelocity > 0:
                self.vvelocity = 0
            self.can_jump = True

floor = pygame.Rect(0,400,480,1)
dis = Controllable(25,25,50,50)
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
            if event.key == pygame.K_SPACE:
                dis.jump()
            elif event.key == pygame.K_RIGHT:
                 dis.hvelocity = 4
            elif event.key == pygame.K_LEFT:
                dis.hvelocity = -4

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                dis.hvelocity = 0
            elif event.key == pygame.K_LEFT:
                dis.hvelocity = 0
    dis.update()
    dis.collisionTest(floor)
    clock.tick(30)
    background.fill((250,250,250))
    pygame.draw.rect(background,pygame.color.Color(50,200,50),dis)
    screen.blit(background,(0,0))

    pygame.display.flip()

pygame.quit()