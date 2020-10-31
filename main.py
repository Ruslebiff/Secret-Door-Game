import pygame
import os
from Players.Player import Player


pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 480

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Secret Door Game")
bg = pygame.image.load(os.path.join('resources', 'bg.jpg'))
char = pygame.image.load(os.path.join('resources', 'player_standing.png'))

font = pygame.font.SysFont('comicsans', 30, True, False)
clock = pygame.time.Clock()

player1 = Player(300, 410, 64, 64)


def redrawGameWindow():
    win.blit(bg, (0, 0))  # background

    pygame.display.update()


""" main loop """
run = True
while run:
    clock.tick(27)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()

""" main loop end """
pygame.quit()
