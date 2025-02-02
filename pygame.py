import pygame
import random 

pygame.init()
winHeight = 480
winWidth = 700
win=pygame.display.set_mode((winWidth,winHeight))
#---------------------------------------#
# initialize global variables/constants #
#---------------------------------------#
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

btn_font = pygame.font.SysFont("ariel", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('ariel', 45)
word = ''
buttons = []
guessed = []
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.]

limbs = 0


def redraw_game_window():
	global guessed 
	global hangmanPics
	global limbs 
	win.fill(GREEN)