# Import and initialize pygame library
import pygame
pygame.init() 

# RGB color combinations
WHITE = (255,255,255)
LIGHTBLUE = (0,176,240)
PURPLE = (128,0,128)

# Create a screen of size (400, 200) and name it as "screen"
screen = pygame.display.set_mode((400, 200))

# While loop
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            carryOn = False
    # Fill the screen with lightblue color. 
    # RGB for lightblue color is provided in variable "LIGHTBLUE"
    screen.fill(LIGHTBLUE)
    
    # Code to draw a white-colored straight line
    pygame.draw.line(screen, WHITE, [0, 38], [600, 38], 2)
    
    # Code to display text "Score:" with font size = 40 in purple color and at location (20,10)
    # RGB for purple color is provided in variable "PURPLE"
    font = pygame.font.Font(None, 40)
    text = font.render("Score:" , 1, PURPLE)
    screen.blit(text, (20,10))
    
    # Update the display
    pygame.display.flip()
# Close the window
pygame.quit()
    