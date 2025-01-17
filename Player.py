import pygame

class Player:
    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load("doodle.png"), (70,70))
        self.x = 170
        self.y = 400