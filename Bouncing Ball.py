import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

pygame.init()
# Set the width and height of the screen [width, height]

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Here!")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

stepx= random.randint(-10, 10)
stepy = random.randint(-10, 10)
colors = [ BLACK, WHITE,  RED, BLUE, GREY ] 
shade = colors[random.randint(0,4)]
sizeThing = random.randint(20,80)
mouse_pos = list(pygame.mouse.get_pos())
           
while not done:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True   
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = list(mouse_pos)
            print ("Here!")
            shade = colors[random.randint(0,4)]
            sizeThing = random.randint(20,80)
    screen.fill(GREEN)
    pygame.draw.circle(screen, shade, mouse_pos, sizeThing )
    if mouse_pos[0] < sizeThing or mouse_pos[0] >= SCREEN_WIDTH-sizeThing:
        stepx *= -1
    if mouse_pos[1] < sizeThing or mouse_pos[1] >= SCREEN_HEIGHT-sizeThing:
        stepy *= -1
    mouse_pos[0] += stepx
    mouse_pos[1] += stepy
    pygame.display.flip()
    clock.tick(60) 
pygame.quit()
exit() 
