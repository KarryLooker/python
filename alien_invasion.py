import sys
import pygame
def run_game():
    # init game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("alien invasion")
    # set background color
    bg_color = (130, 30, 90)
    # start the main loop of the game
    while True:
        # lisening the event of keyboard and mouse
        # draw the screen since the loop runs
        screen.fill(bg_color)
        # show the latest screen
        pygame.display.flip()

run_game()
