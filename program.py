import pygame
from sys import exit
import button

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Variables 
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Trivia Game')


# test_surf = pygame.image.load('graphics/start.png').convert_alpha()
# test_rect = test_surf.get_rect(center = (400,200))

# Game Variables
game_active = False
menu_active = True

# create button images
play_img = pygame.image.load('graphics/play_button.png').convert_alpha()

# create button instances
play_button = button.Button(SCREEN_WIDTH*.1 , SCREEN_HEIGHT*.10, play_img, .25)



# define fonts
font = pygame.font.SysFont('Futura',30)

# define colors
WHITE = (255,255,255)
TEAL = (6, 81, 67)

# define functions
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))

# Game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:
        pygame.quit()
        exit()
    else:
        screen.fill((TEAL))
        # screen.blit(test_surf,test_rect)
        if menu_active:
            if play_button.draw(screen):
                menu_active = False
                print("Menu Button Works")
        else: 
            draw_text("hello word", font, WHITE, 160, 250)
        pygame.display.update()