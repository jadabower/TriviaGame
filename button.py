import pygame
import constants

black = constants.BLACK

class Button():
		
	#colors for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = black
	width = 180
	height = 70

	def __init__(self, x, y, text, screen):
		self.x = x
		self.y = y
		self.text = text
		self.screen = screen

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
				pygame.draw.rect(self.screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(self.screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(self.screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(self.screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(self.screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(self.screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(self.screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		self.screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action


#button class
#class Button():
#	def __init__(self, x, y, text, display):
#		width = 200
#		height = 100
#		self.text = text 
#		
#		# self.rect = self.image.get_rect()
#		self.rect = pygame.Rect(100, 50, 600, 150)
#		self.rect.topleft = (x, y)
#		self.clicked = False
#
#	def draw(self, surface):
#		action = False
#		#get mouse position
#		pos = pygame.mouse.get_pos()
#		
#		# text_box = pygame.Rect(100, 50, 600, 150)
#		pygame.draw.rect(self.display, (255,0,0), text_box)
#
#		#check mouseover and clicked conditions
#		if self.rect.collidepoint(pos):
#			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
#				self.clicked = True
#				action = True
#
#		if pygame.mouse.get_pressed()[0] == 0:
#			self.clicked = False
#
#		#draw button on self.screen
#		surface.blit(self.rect, (self.rect.x, self.rect.y))
#
#		return action