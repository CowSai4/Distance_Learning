import pygame

white = ( 255, 255, 255)
black = ( 0, 0, 0)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super(Car,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill(white)
        self.rect = self.surf.get_rect()   