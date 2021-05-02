import pygame

#Initializing the pygame
pygame.init()

#Creating the screen(simple HD resolutions)
screen = pygame.display.set_mode((1280, 720))

#setup (icon, title, etc...)

pygame.display.set_caption('2DPROJECT')
icon = pygame.image.load('2DPROJECT.png')
pygame.display.set_icon(icon)

#variables and classes
game_on = True

#gameloop
while game_on == True:

    screen.fill((0,0,0))
    pygame.display.update()