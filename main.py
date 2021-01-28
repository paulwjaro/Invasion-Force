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
font = pygame.font.Font('Assets/ChakraPetch-Light.ttf', 24)

score_text = font.render("Score: 100", True, (255, 255, 255))


current_game = game.Game(screen)
current_game.create_game()



while current_game.running:
    score_text = font.render(f"Score: {current_game.score}", True, (255, 255, 255))
    screen.fill((19, 12, 30))

    current_game.main(screen)
    screen.blit(score_text, (450, 32))

    pygame.display.update()
