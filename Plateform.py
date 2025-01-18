import pygame

class Plateform:
    def __init__(self, coX = 165, coY = 480, type = 0):
        self.co = [coX, coY, 70, 11]
        self.type = type