import pygame
pygame.init()

black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

screen = pygame.display.set_mode(700,500)
pygame.display.set_caption('First Game')

carryOn = True

clock = pygame.time.Clock()

while carryOn == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False 

     screen.fill(WHITE)

     pygame.display.flip()
     
     clock.tick(60)

pygame.quit()