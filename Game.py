import pygame
from Player import *
from Plateform import *

pygame.init()

font = pygame.font.Font("freesansbold.ttf", 16)
timer = pygame.time.Clock()
backround = (255,255,255)

screen = pygame.display.set_mode([400, 500]) #setup de la taille de l'écran
pygame.display.set_caption("Doodle qui Jump") #nom de la fenêtre de jeu
player = Player()
plateforms = [Plateform()]


running = True
while running:
    timer.tick(60) #setup des fps
    screen.fill(backround)
    screen.blit(player.sprite, (player.x, player.y))
    blocks = []

    for i in range(len(plateforms)):
        block = pygame.draw.rect(screen, (0, 0, 0), plateforms[i].co, plateforms[i].type, 4)
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.updateY()
    player.onGround(blocks)
    
    pygame.display.flip()


pygame.quit()