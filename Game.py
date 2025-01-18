import pygame
from Player import *
from Plateform import *
from random import randint

def play(running):
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

    while running:
        timer.tick(60) #setup des fps
        screen.fill(backround)
        screen.blit(player.sprite, (player.x, player.y))
        scoreText = font.render("Score: " + str(score), True, (120,120,120), backround)
        screen.blit(scoreText, (0, 12))
        hightScoreText = font.render("Hight Score: " + str(score), True, (120,120,120), backround)
        screen.blit(hightScoreText, (260, 12))
        blocks = []

        for i in range(len(plateforms)):
            block = pygame.draw.rect(screen, (0, 0, 0), plateforms[i].co, plateforms[i].type, 4)
            blocks.append(block)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and not gameOver:
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
                    if score > hightScore:
                        hightScore = score
        
        if player.y > 435:
            gameOver = True
            player.yChange = 0
        
        if gameOver:
            pygame.mixer.music.stop()
            screen.fill(backround)
            running = False

        pygame.display.flip()

pygame.init()
font = pygame.font.Font("freesansbold.ttf", 16)
screen = pygame.display.set_mode([500, 500]) #setup de la taille de l'écran
pygame.display.set_caption("Menu Doodle") #nom de la fenêtre de jeu
timer = pygame.time.Clock()
pygame.mixer.music.load("Musique du oui (corobizar  Musique dattente).mp3")
pygame.mixer.music.play(-1, 0.0)
inGame = True

while inGame:
    
    timer.tick(60)
    screen.fill((220, 220, 220))
    menuText = font.render("Bienvenue dans Doodle qui Jump !", True, (80,80,80), (220,220,220))
    screen.blit(menuText, (110, 150))
    menuText2 = font.render("Appuyez sur \"Espace\" pour lancer une nouvelle partie", True, (80,80,80), (220,220,220))
    screen.blit(menuText2, (40, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
                play(True)
                screen = pygame.display.set_mode([500, 500]) #setup de la taille de l'écran
                pygame.display.set_caption("Menu Doodle") #nom de la fenêtre de jeu
                pygame.mixer.music.load("Musique du oui (corobizar  Musique dattente).mp3")
                pygame.mixer.music.play(-1, 0.0)
    pygame.display.flip()
        
pygame.quit()