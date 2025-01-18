import pygame

class Player:
    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load("doodle.png"), (70,70))
        self.x = 170
        self.y = 400
        self.jump = False
        self.yChange = 0
        self.speed = 0
    
    #gère le saut
    def updateY(self):
        if self.jump:
            self.yChange = -15 #hauteur du saut
            self.jump = False
        self.y += self.yChange
        self.yChange += .5 #l'effet de gravité
    
    #gère la collision avec les plateformes
    def onGround(self, blocks):
        for i in range(len(blocks)):
            if blocks[i].colliderect([self.x +20, self.y + 60, 35, 5]) and self.jump == False and self.yChange > 0: #on vérifie qu'on touche une plateforme pendant la redescente
                self.jump = True
    
    def move(self):
        self.x += self.speed