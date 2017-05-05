#hello
import pygame
import os,sys
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("First")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250,250,250))
screen.blit(background,(0,0))
pygame.display.flip()

