import pygame
from sys import exit
import button
import questionHandler

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

GRID_SIZE = 50 # this is for debugging purposes in setting the placement of assets



# define colors
WHITE = (255,255,255)
TEAL = (6, 81, 67)



class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('menu')
        self.menu = Menu(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)
        
        self.quesHandKMath = questionHandler.QuestionHandler("K", "Math")
        self.quesHandKMath.getRandomQuestion()

        self.states = {
            'menu': self.menu,
            'level': self.level
        }
        
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.states[self.gameStateManager.getState()].run()

            pygame.display.update()
            self.clock.tick(FPS)


class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # Create multiple choice buttons
        self.button1 = button.Button(SCREEN_WIDTH*.1 , SCREEN_HEIGHT*.25, pygame.image.load('graphics/play_button.png').convert_alpha(), .25)
        self.button2 = button.Button(SCREEN_WIDTH*.6 , SCREEN_HEIGHT*.25, pygame.image.load('graphics/play_button.png').convert_alpha(), .25)
        self.button3 = button.Button(SCREEN_WIDTH*.1 , SCREEN_HEIGHT*.5, pygame.image.load('graphics/play_button.png').convert_alpha(), .25)
        self.button4 = button.Button(SCREEN_WIDTH*.6 , SCREEN_HEIGHT*.5, pygame.image.load('graphics/play_button.png').convert_alpha(), .25)


    def run(self):
        screen =pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.display.fill(WHITE)

        # draw grid for debugging and asset placement
        # for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        #     pygame.draw.line(self.display, TEAL, (x, 0), (x, SCREEN_HEIGHT))
        # for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        #     pygame.draw.line(self.display, TEAL, (0, y), (SCREEN_WIDTH, y))
        
        # draws text and text box on screen for Question
        text = "hit the bottom right button to go back to menu"
        font = pygame.font.Font(None, 32)
        text_surface = font.render(text, True, WHITE)
        text_box = pygame.Rect(100, 50, 600, 150)

        pygame.draw.rect(self.display, TEAL, text_box)
        screen.blit(text_surface, (text_box.x + 10, text_box.y + 10))
        

        if self.button1.draw(self.display): # We need to still go into the button and see if we can change the text, play button works for now. Also need to figure randomizing the answers
            print("Button 1 Works")
        if self.button2.draw(self.display):
            print("Button 2 Works")
        if self.button3.draw(self.display):
            print("Button 3 Works")
        if self.button4.draw(self.display):
            print("Button 4 Works")
            self.gameStateManager.setState('menu')

        

class Menu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # create button images
        self.play_img = pygame.image.load('graphics/play_button.png').convert_alpha()

        # create button instances
        self.play_button = button.Button(SCREEN_WIDTH*.1 , SCREEN_HEIGHT*.10, self.play_img, .25)

    def run(self):
        self.display.fill(TEAL)
        
        if self.play_button.draw(self.display):
            self.gameStateManager.setState('level')
            print("Menu Button Works")

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    
    def getState(self):
        return self.currentState

    def setState(self, newState):
        print("change of state")
        self.currentState = newState
    


if __name__ == "__main__":
    game = Game()
    game.run()

