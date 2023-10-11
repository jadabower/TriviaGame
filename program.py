import pygame
from sys import exit

# Variables
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Trivia Game')
game_active = False

test_surf = pygame.image.load('graphics/start.png').convert_alpha()
test_rect = test_surf.get_rect(center = (400,200))

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
        screen.fill('#065143')
        screen.blit(test_surf,test_rect)