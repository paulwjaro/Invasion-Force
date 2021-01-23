from input import InputHandler
from player import Player
from misc import *
from movement_entities import collision_types
from levels import Level

FPS = 60
clock = time.Clock()
game_input = InputHandler()


class Game:
    def __init__(self, _screen):
        self.screen = _screen
        self.running = True
        self.score = 0
        self.screens = ['start', 'level', 'end']
        self.level = Level(self.screen)
        self.player = None
        self.active_objects = []
        self.collision_objects = []
        self.pt = time.get_ticks()
        self.game_levels = []
        self.current_level = 0

    def main(self, _screen):
        # Set Up Delta Time
        dt = time.get_ticks() - self.pt
        dt *= FPS
        self.pt = time.get_ticks()

        # Run Game
        self.level.run()
        if len(self.level.add_list) > 0:
            self.add_object_to_game(self.level.add_list[0])
        game_input.game_input()
        self.input_checks(_screen)
        self.object_handler(_screen)
        game_timers()

        # Set FPS
        clock.tick(FPS)

    # Game Functions
    def create_game(self):
        player = Player(320, 400, 3, collision_types[0], collision_types[2])
        self.player = player
        self.add_object_to_game(player)

    def input_checks(self, _screen):
        if game_input.quit:
            self.running = False
        if self.player is not None:
            self.player.right_axis = game_input.key_d
            self.player.left_axis = game_input.key_a

            if game_input.key_space:
                if not self.player.fired:
                    new_bullet = self.player.fire(_screen, collision_types[1], collision_types[2])
                    self.active_objects.append(new_bullet)
                    self.collision_objects.append(new_bullet)
            else:
                self.player.fired = False

        if game_input.key_enter:
            self.level.start()
    
    def object_handler(self, _screen):
        if len(self.active_objects) > 0:
            for _object in self.active_objects:
                if _object.destroyed:
                    self.active_objects.pop(self.active_objects.index(_object))

                else:
                    _object.play(_screen)

        if len(self.collision_objects) > 0:
            for _object in self.collision_objects:
                if _object.destroyed:
                    self.collision_objects.pop(self.collision_objects.index(_object))
                else:
                    for collisions in self.collision_objects:
                        if _object != collisions:
                            if _object.rect.colliderect(collisions.rect):
                                if _object.collision_type in collisions.can_hit:
                                    _object.hit()
                                    collisions.hit()

    def add_object_to_game(self, _object, _collision_object=True):
        if _collision_object:
            self.collision_objects.append(_object)
        self.active_objects.append(_object)


