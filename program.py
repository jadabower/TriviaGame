import pygame
from questionHandler import QuestionHandler
from pygame.locals import *
from textWrap import renderTextCenteredAt
import webbrowser

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Trivia Game')

font = pygame.font.Font('font\SourceCodePro-VariableFont_wght.ttf', 20)

link_font = pygame.font.SysFont('Consolas', 25)
link_color = (0, 0, 0)

#define colors
bg = (6, 81, 67)
teal = (88, 173, 159)
black = (0, 0, 0)
white = (255, 255, 255)

#define global variable
clicked = False
gradeSelected = 'K'
subjectSelected = 'Math'
points = 0

#define screen options
mainMenu = True
gradeSelectorScreen = False
subjectSelectorScreen = False
level = False

class button():
		
	# colors for button and text
	button_col = (88, 173, 159)
	hover_col = (75, 147, 136)
	click_col = (48, 95, 88)
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.textY = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		# If the text has to be split into two lines, it moves the text up slightly so it's still centered
		if len(self.text) > 14:
			self.textY -= 10
			print(self.text)

		# We got rid of this so that we could center the text on the button:
		# text_img = font.render(self.text, True, black)
		# text_len = text_img.get_width()
		# screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.textY + 25))
		
		# Centers the text on the button. If it is too long, it sends it to the next line
		renderTextCenteredAt(self.text, font, black, self.x + 90, self.textY, screen, self.width - 2)
		return action

# Main Menu Button
buttonStartGame = button(210, 105, "Play")
buttonOptions = button(210, 245, "Options")

# Grade selector buttons
buttonK = button(80, 105, 'Kindergarten')
button1 = button(320, 105, '1st')
button2 = button(80, 245, '2nd')
button3 = button(320, 245, '3rd')
buttonToSubject = button(300, 400, "Subject")

# Menu button for both options screens
buttonBackToMenu = button(100, 400, "Menu")

# Subject selector buttons
buttonMath = button(80, 105, 'Math')
buttonScience = button(320, 105, 'Science')
buttonHistory = button(80, 245, 'History')
buttonELA = button(320, 245, 'ELA')
buttonToGrade = button(300, 400, "Grade")

# Buttons A,B,C,D when user presses play
buttona = button(80, 150, 'A')
buttonb = button(320, 150, 'B')
buttonc = button(80, 245, 'C')
buttond = button(320, 245, 'D')

# Creates a question Handler
questionHand = QuestionHandler()

# Game loop, replayed constantly until exited
run = True
while run:
	screen.fill(bg)	
	points_img = font.render("Points: " + str(points), True, teal)
	# GRADE SELECTOR MENU
	if gradeSelectorScreen:
		gradeSelected_img = font.render("Grade selected: " + gradeSelected, True, teal)
		screen.blit(gradeSelected_img, (175, 350))
		# Different grade selections
		if buttonK.draw_button():
			print('K')
			gradeSelected = 'K'
		if button1.draw_button():
			print('1')
			gradeSelected = '1'
		if button2.draw_button():
			print('2')
			gradeSelected = '2'
		if button3.draw_button():
			print('3')
			gradeSelected = '3'
		# Main Menu button pressed
		if buttonBackToMenu.draw_button():
			print('Back to Menu')
			gradeSelectorScreen = False
			mainMenu = True
		# Subject button pressed
		if buttonToSubject.draw_button():
			print("Grade selected: " + gradeSelected)
			gradeSelectorScreen = False
			subjectSelectorScreen = True
	# SUBJECT SELECTOR MENU
	elif subjectSelectorScreen:
		subjectSelected_img = font.render("Subject selected: " + subjectSelected, True, teal)
		screen.blit(subjectSelected_img, (150, 350))
		# Different subject selections
		if buttonMath.draw_button():
			print('Math')
			subjectSelected = 'Math'
		if buttonScience.draw_button():
			print('Science')
			subjectSelected = 'Science'
		if buttonHistory.draw_button():
			print('History')
			subjectSelected = 'History'
		if buttonELA.draw_button():
			print('ELA')
			subjectSelected = 'ELA'
		# Main Menu button pressed
		if buttonBackToMenu.draw_button():
			print('Back to Menu')
			subjectSelectorScreen = False
			mainMenu = True
		# Grade button pressed
		if buttonToGrade.draw_button():
			print("Subject selected: " + subjectSelected)
			subjectSelectorScreen = False
			gradeSelectorScreen = True
	# MAIN MENU
	elif mainMenu:
		screen.blit(points_img, (25, 25))
		# Start button pressed
		if buttonStartGame.draw_button():
			questionHand.createQuestionPool(gradeSelected, subjectSelected)
			print(f'Start level ({gradeSelected}, {subjectSelected})')
			mainMenu = False
			level = True
		# Options button pressed
		elif buttonOptions.draw_button():
			print('Go to options')
			mainMenu = False
			gradeSelectorScreen = True

		link = screen.blit(link_font.render("Web App", True, link_color), (490, 570))
	# LEVEL
	elif level:
		currentQuestion = questionHand.getQuestion()
		# Shows the points
		screen.blit(points_img, (25, 550))
		# Shows the question (centered on the x-axis)
		x_test = 100
		y_test = 30
		renderTextCenteredAt(currentQuestion.getText(), font, teal, screen_width/2, y_test, screen, screen_width * .6)
		# Shows the four options
		buttonA = button(80, 175, str(currentQuestion.getA()))
		buttonB = button(320, 175, str(currentQuestion.getB()))
		buttonC = button(80, 345, str(currentQuestion.getC()))
		buttonD = button(320, 345, str(currentQuestion.getD()))

		# Draws the buttons. If one is clicked, it checks whether it's correct and deals with the answer accordingly
		if buttonA.draw_button():
			print('A')
			questionHand.checkAnswer('A')
			points = questionHand.points
		if buttonB.draw_button():
			print('B')
			questionHand.checkAnswer('B')
			points = questionHand.points
		if buttonC.draw_button():
			print('C')
			questionHand.checkAnswer('C')
			points = questionHand.points
		if buttonD.draw_button():
			print('D')
			questionHand.checkAnswer('D')
			points = questionHand.points
			
		# Creates a question handler (with a question pool from the JSON file based on the options picked)
		if len(questionHand.questionPool) <= 0:
			print('Back to Menu')
			level = False
			mainMenu = True
			
	# Checks that the program has not been exited
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = event.pos
			if link.collidepoint(pos):
				webbrowser.open(r"https://master.d2jir32rtcjasl.amplifyapp.com/")

		if link.collidepoint(pygame.mouse.get_pos()):
			link_color = (70, 29, 219)

		else:
			link_color = (0, 0, 0)

		if event.type == pygame.QUIT:
			run = False	
	
	# Updates the screen (happens very often)
	pygame.display.update()

pygame.quit()