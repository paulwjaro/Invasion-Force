import pygame
import game
from level_data import levels
from gui import GameGUI
pygame.init()

# Initialize Game Screen
screen = pygame.display.set_mode((640, 480))
logo_img = pygame.image.load('Assets/Player_1.png')
logo_sprite = pygame.transform.scale(logo_img, (32, 32))
pygame.display.set_icon(logo_sprite)
pygame.display.set_caption('Invasion Force')

# Create Game Instance
current_game = game.Game(screen)
current_game.create_game()

game_gui = GameGUI(screen)

print(len(levels))

# Game Loop
while current_game.running:
    game_gui.score_text = game_gui.font.render(f"Score: {current_game.score}", True, (255, 255, 255))
    game_gui.level_text = game_gui.font.render(f"Level: {current_game.current_level + 1}", True, (255, 255, 255))
    try:
        game_gui.wave_text = game_gui.font.render(f"Wave: {current_game.game_levels[current_game.current_level].current_wave}", True, (255, 255, 255))
    except IndexError:
        pass
    screen.fill((19, 12, 30))

    game_gui.draw_gui(current_game)

    current_game.main(screen)
    pygame.display.update()
