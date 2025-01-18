import pygame

class Player:
    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load("doodle.png"), (70,70))
        self.x = 170
        self.y = 400
        self.jump = False
        self.yChange = 0
    
    def updateY(self):
        if self.jump:
            self.yChange = -10
            self.jump = False
        self.y += self.yChange
        self.yChange += 1
    
    def onGround(self, blocks):
        for i in range(len(blocks)):
            if blocks[i].colliderect([self.x, self.y + 60, 90, 10]) and self.jump == False and self.yChange > 0:
                self.jump = True