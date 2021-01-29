import pygame


class InputHandler:
    def __init__(self):
        self.quit = False
        self.key_a = False
        self.key_d = False
        self.key_space = False
        self.key_enter = False
        self.enter_pressed = False

    def game_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.key_d = True
                if event.key == pygame.K_a:
                    self.key_a = True
                if event.key == pygame.K_SPACE:
                    self.key_space = True
                if event.key == pygame.K_RETURN:
                    self.key_enter = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.key_d = False
                if event.key == pygame.K_a:
                    self.key_a = False
                if event.key == pygame.K_SPACE:
                    self.key_space = False
                if event.key == pygame.K_RETURN:
                    self.key_enter = False
                    self.enter_pressed = False
