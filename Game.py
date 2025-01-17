import pygame
from Player import *

pygame.init()

font = pygame.font.Font("freesansbold.ttf", 16)
timer = pygame.time.Clock()
backround = (255,255,255)

screen = pygame.display.set_mode([400, 500]) #setup de la taille de l'écran
pygame.display.set_caption("Doodle qui Jump") #nom de la fenêtre de jeu
player = Player()

running = True
while running:
    timer.tick(60) #setup des fps
    screen.fill(backround)
    screen.blit(player.sprite, (player.x, player.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()


pygame.quit()