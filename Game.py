import pygame
from Player import *
from Plateform import *
from random import randint

pygame.init()

font = pygame.font.Font("freesansbold.ttf", 16)
timer = pygame.time.Clock()
backround = (255,255,255)
score = 0
hightScore = 0
gameOver = False

screen = pygame.display.set_mode([400, 500]) #setup de la taille de l'écran
pygame.display.set_caption("Doodle qui Jump") #nom de la fenêtre de jeu
player = Player()
plateforms = [Plateform(), Plateform(randint(0, 330), randint(300, 400), 0), Plateform(randint(0, 330), randint(250, 350), 0), Plateform(randint(0, 330), randint(180, 280), 0),Plateform(randint(0, 330), randint(100, 200), 0)]

pygame.mixer.music.load("Glorious Morning 2.mp3")
pygame.mixer.music.play(-1, 0.0)

running = True
while running:
    timer.tick(60) #setup des fps
    screen.fill(backround)
    screen.blit(player.sprite, (player.x, player.y))
    scoreText = font.render("Score: " + str(score), True, (120,120,120), backround)
    screen.blit(scoreText, (320, 20))
    blocks = []

    for i in range(len(plateforms)):
        block = pygame.draw.rect(screen, (0, 0, 0), plateforms[i].co, plateforms[i].type, 4)
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                player.speed = -5
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                player.speed = 0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.speed = 0

    player.move()
    player.turning()
    player.onGround(blocks)
    player.updateY()

    #on vérifie la hauteur du joueur, puis on bouge les plateformes si nécessaire
    if player.y < 200 and player.yChange < 0:
        for i in range(len(plateforms)):
            plateforms[i].affichage(player.yChange)
            if plateforms[i].affichage(player.yChange): #ici on remplace la plateforme si elle sort par une nouvelle en haut de l'écran et on ajout +1 au score
                plateforms[i] = Plateform(randint(0, 330), randint(-30, 10), 0)
                score += 1

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()