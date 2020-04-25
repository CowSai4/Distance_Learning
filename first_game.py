import pygame
from car import Car
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)

pygame.init()

black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('First Game')

running = True

car = Car()

def move(self, pressed_keys):
     if pressed_keys[K_UP]:
         self.rect.move_ip(0, -5)
     if pressed_keys[K_DOWN]:
         self.rect.move_ip(0, 5)
     if pressed_keys[K_LEFT]:
         self.rect.move_ip(-5, 0)
     if pressed_keys[K_RIGHT]:
         self.rect.move_ip(5, 0)

while running == True:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
             if event.key == K_ESCAPE:
                 running = False
        if event.type == pygame.QUIT:
              running = False 
        
        pressed_keys = pygame.key.get_pressed()

        car.move(pressed_keys)

        screen.fill(black)

        screen.blit(car.surf, (350, 250))

        pygame.display.flip()


pygame.quit()