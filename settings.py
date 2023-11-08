#Settings button
import pygame
import button
import constants

SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
TEAL = constants.TEAL
FPS = constants.FPS
WHITE = constants.WHITE

class Settings:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # Create multiple choice buttons
        self.button1 = button.Button(SCREEN_WIDTH*.1 , SCREEN_HEIGHT*.25, pygame.image.load('graphics/play_button.png').convert_alpha(), .25)
        self.button2 = button.Button(SCREEN_WIDTH*.6 , SCREEN_HEIGHT*.25, pygame.image.load('graphics/play_button.png').convert_alpha(), .25)
        self.button3 = button.Button(SCREEN_WIDTH*.1 , SCREEN_HEIGHT*.5, pygame.image.load('graphics/play_button.png').convert_alpha(), .25)
        self.button4 = button.Button(SCREEN_WIDTH*.6 , SCREEN_HEIGHT*.5, pygame.image.load('graphics/play_button.png').convert_alpha(), .25)


    def run(self):
        self.screen = self.display
        self.display.fill(WHITE)

        # draw grid for debugging and asset placement
        # for x in range(0, self.screen_WIDTH, GRID_SIZE):
        #     pygame.draw.line(self.display, TEAL, (x, 0), (x, self.screen_HEIGHT))
        # for y in range(0, self.screen_HEIGHT, GRID_SIZE):
        #     pygame.draw.line(self.display, TEAL, (0, y), (self.screen_WIDTH, y))
        
        # draws text and text box on self.screen for Question
        text = "hit the bottom right button to go back to menu"
        font = pygame.font.Font(None, 32)
        text_surface = font.render(text, True, WHITE)
        text_box = pygame.Rect(100, 50, 600, 150)

        pygame.draw.rect(self.display, TEAL, text_box)
        self.screen.blit(text_surface, (text_box.x + 10, text_box.y + 10)) # this causing bug and writting the text
        

        if self.button1.draw(self.display): # We need to still go into the button and see if we can change the text, play button works for now. Also need to figure randomizing the answers
            print("Button 1 Works")
        if self.button2.draw(self.display):
            print("Button 2 Works")
        if self.button3.draw(self.display):
            print("Button 3 Works")
        if self.button4.draw(self.display):
            print("Button 4 Works")
            self.gameStateManager.setState('menu')
