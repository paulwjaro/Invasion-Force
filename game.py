from input import InputHandler
from misc import *
from levels import ObjectHandler


FPS = 60
clock = time.Clock()
game_input = InputHandler()


class Game:
    def __init__(self, _screen):
        self.screen = _screen
        self.running = True
        self.object_handler = ObjectHandler(self.screen)
        self.score = 0
        self.pt = time.get_ticks()
        self.game_levels = []
        self.current_level = 0

    def main(self, _screen):
        # Set Up Delta Time
        dt = time.get_ticks() - self.pt
        dt *= FPS
        self.pt = time.get_ticks()

        # Run Game
        game_input.game_input()
        self.input_checks(_screen)
        self.object_handler.object_handler(self.screen)

        # Set FPS
        clock.tick(FPS)

    # Game Functions
    def create_game(self):
        self.object_handler.create()

    def input_checks(self, _screen):
        if game_input.quit:
            self.running = False
        if self.object_handler.player is not None:
            self.object_handler.player.right_axis = game_input.key_d
            self.object_handler.player.left_axis = game_input.key_a

            if game_input.key_space:
                if not self.object_handler.player.fired:
                    new_bullet = self.object_handler.player.fire(_screen, 'projectile', ['enemies'])
                    self.object_handler.active_objects.append(new_bullet)
            else:
                self.object_handler.player.fired = False

        if game_input.key_enter:
            pass
    





