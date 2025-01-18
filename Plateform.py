import pygame

class Plateform:
    def __init__(self, coX = 165, coY = 480, type = 0):
        self.co = [coX, coY, 70, 11]
        self.type = type
    
    #actualise la position de la plateforme et renvoi true si elle sort de l'écran
    def affichage(self, movement):
        self.co[1] -= movement
        if self.co[1] > 500:
            return True
        else:
            return False