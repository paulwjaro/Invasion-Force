from input import InputHandler
from player import Player, player_data
from misc import *
from levels import Level, ObjectHandler
from level_data import levels


FPS = 60
clock = time.Clock()
game_input = InputHandler()
GAME_STATES = ['start', 'levels', 'game_over']


class Game:
    def __init__(self, _screen):
        self.screen = _screen
        self.running = True
        self.object_handler = ObjectHandler(self.screen)
        self.score = 0
        self.pt = time.get_ticks()
        self.game_state = GAME_STATES[0]
        self.game_levels = []
        self.current_level = 0
        self.player = None

    def main(self, _screen):
        # Set Up Delta Time
        dt = time.get_ticks() - self.pt
        dt *= FPS
        self.pt = time.get_ticks()

        # Run Game
        game_input.game_input()
        self.input_checks(_screen)
        self.object_handler.object_handler(self.screen)
        if self.game_state == 'start':
            pass
        elif self.game_state == 'levels':
            try:
                self.game_levels[self.current_level].run()
                if len(self.game_levels[self.current_level].wave_list) < self.game_levels[self.current_level].current_wave:
                    self.current_level += 1
            except IndexError:
                self.player.game_started = False
                self.game_state = 'game_over'
            self.update_score()
        else:
            pass

        # Set FPS
        clock.tick(FPS)

    # Game Functions
    def create_game(self):
        self.object_handler.create()
        data = player_data['sprites']['0']
        self.player = Player(self.screen, 320, 460, data['c_width'], data['c_height'], data['spd'], data['collision_layer'], data['collision_mask'],
                             _sprite=data['sprite'])
        self.level_setup()
        self.object_handler.add_object_to_game(self.player)

    def input_checks(self, _screen):
        if game_input.quit:
            self.running = False
        if self.player is not None:
            self.player.right_axis = game_input.key_d
            self.player.left_axis = game_input.key_a

            if game_input.key_space:
                if self.player.game_started:
                    if not self.player.fired:
                        new_bullet = self.player.fire(_screen, 'projectile', ['enemies'])
                        self.object_handler.active_objects.append(new_bullet)
            else:
                self.player.fired = False

        if game_input.key_enter and not game_input.enter_pressed:
            game_input.enter_pressed = True
            if self.game_state == 'start':
                self.game_state = 'levels'
                self.player.game_started = True
            elif self.game_state == 'levels':
                self.game_levels[self.current_level].level_started = True
            elif self.game_state == 'game_over':
                self.__init__(self.screen)
                self.create_game()

    def update_score(self):
        if self.object_handler.score != 0:
            self.score += self.object_handler.score
            self.object_handler.score = 0

    def level_setup(self):
        for level in range(len(levels)):
            new_level = Level(self.screen, self.object_handler, levels[str(level + 1)])
            new_level.create()
            self.game_levels.append(new_level)
