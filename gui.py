import pygame


class GameGUI:
    def __init__(self, _screen):
        self.screen = _screen
        # Set Fonts
        self.font = pygame.font.Font('Assets/ChakraPetch-Light.ttf', 24)
        self.title_font = pygame.font.Font('Assets/ChakraPetch-Light.ttf', 48)

        # Render Fonts
        self.score_text = self.font.render(f"Score: ", True, (255, 255, 255))
        self.wave_text = self.font.render(f"Wave: ", True, (255, 255, 255))
        self.level_text = self.font.render(f"Level: ", True, (255, 255, 255))
        self.title = self.title_font.render("Invasion Force".upper(), True, (255, 255, 255))
        self.title_width = self.title.get_rect().width
        self.title_height = self.title.get_rect().height

        self.game_over = self.title_font.render("Game Over".upper(), True, (255, 255, 255))
        self.game_over_width = self.game_over.get_rect().width
        self.game_over_height = self.game_over.get_rect().height
        self.space_options = ["Begin Game", "Start Level", "Restart Game"]
        self.space_button = self.font.render(f"Press Enter to {self.space_options[0]}", True, (255, 255, 255))
        self.space_button_width = self.space_button.get_rect().width
        self.space_button_height = self.space_button.get_rect().height

    def draw_gui(self, _game):
        if _game.game_state == 'levels':
            self.screen.blit(self.score_text, (450, 32))
            self.screen.blit(self.level_text, (32, 32))
            self.screen.blit(self.wave_text, (225, 32))
            try:
                if not _game.game_levels[_game.current_level].level_started:
                    if _game.current_level == 0:
                        instruct = self.font.render("Move with WSAD and Fire with 'Space'", True, (255, 255, 255))
                        self.screen.blit(instruct, (320 - (instruct.get_rect().width/2), 300 - (instruct.get_rect().height/2)))
                    self.space_button = self.font.render(f"Press Enter to {self.space_options[1]}", True,
                                                         (255, 255, 255))
                    self.screen.blit(self.space_button,
                                     (320 - self.space_button_width / 2, 240 - self.space_button_height / 2))
            except IndexError:
                pass
        elif _game.game_state == 'start':
            self.space_button = self.font.render(f"Press Enter to {self.space_options[0]}", True, (255, 255, 255))
            self.screen.blit(self.title, (320 - self.title_width / 2, 240 - self.title_height))
            self.screen.blit(self.space_button, (320 - self.space_button_width/2, 400 - self.space_button_height/2))
        elif _game.game_state == 'game_over':
            self.space_button = self.font.render(f"Press Enter to {self.space_options[2]}", True, (255, 255, 255))
            self.screen.blit(self.game_over, (320 - self.game_over_width / 2, 240 - self.title_height))
            self.screen.blit(self.space_button, (320 - self.space_button_width / 2, 400 - self.space_button_height / 2))
