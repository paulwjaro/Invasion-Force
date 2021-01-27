import pygame
import game
from enemies import Paths
from projectiles import *

pygame.init()

# Initialize Game Screen
screen = pygame.display.set_mode((640, 480))
logo_img = pygame.image.load('Assets/Player_1.png')
logo_sprite = pygame.transform.scale(logo_img, (32, 32))
pygame.display.set_icon(logo_sprite)
pygame.display.set_caption('Invasion Force')

current_game = game.Game(screen)
current_game.create_game()



while current_game.running:
    screen.fill((19, 12, 30))

    current_game.main(screen)

    pygame.display.update()
