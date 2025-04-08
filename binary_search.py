import pygame

# constants
WIDTH, HEIGHT = 1024, 768
BACKGROUND_COLOR = (255, 255, 255)
ARRAY_SIZE = 16
BLOCK_SIZE = 40
FONT_SIZE = 24

# game stats
GAME_MENU = 0
GAME_INPUT = 1
GAME_PLAYING = 2
GAME_WON = 3
GAME_NOT_FOUND = 4

# initialize pygame
pygame.init()
font = pygame.font.SysFont('Arial', FONT_SIZE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binary Search Visualizer")