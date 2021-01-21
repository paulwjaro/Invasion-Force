from pygame import time
from input import InputHandler
from player import Player
from misc import Timer
from enemies import Enemy

FPS = 60
collision_types = ['player', 'projectile', 'enemy']
clock = time.Clock()
player = Player(320, 400, 3, collision_types[0], collision_types[2])
game_input = InputHandler()


class Game:
    def __init__(self, _screen):
        self.screen = _screen
        self.running = True
        self.score = 0
        self.screens = ['start', 'level', 'end']
        self.level = 1
        self.active_objects = [player]
        self.timer_list = []
        self.pt = time.get_ticks()
        self.level_started = False
        self.wave_length = 20


    def main(self, _screen):
        dt = time.get_ticks() - self.pt
        dt *= FPS
        self.pt = time.get_ticks()
        game_input.game_input()
        self.input_checks(_screen)
        self.object_handler(_screen)
        self.game_timers()

        clock.tick(FPS)

    def input_checks(self, _screen):
        if game_input.quit:
            self.running = False

        player.right_axis = game_input.key_d
        player.left_axis = game_input.key_a

        if game_input.key_space:
            if not player.fired:
                self.active_objects.append(player.fire(_screen, collision_types[1], collision_types[2]))
                new_timer = Timer()
                self.timer_list.append(new_timer)
        else:
            player.fired = False

        if game_input.key_enter:
            if not self.level_started:
                self.control_waves()
                self.level_started = True
    
    def object_handler(self, _screen):
        if len(self.active_objects) > 0:
            for _object in self.active_objects:
                if _object.destroyed:
                    self.active_objects.pop(self.active_objects.index(_object))
                else:
                    for collisions in self.active_objects:
                        if _object != collisions:
                            if _object.rect.colliderect(collisions.rect):
                                if _object.collision_type in collisions.can_hit:
                                    _object.hit()
                                    collisions.hit()
                    _object.play(_screen)
    
    def game_timers(self):
        if len(self.timer_list) > 0:
            for timer in self.timer_list:
                if timer.timer_ring:
                    self.timer_list.pop(self.timer_list.index(timer))
                else:
                    timer.run_timer()

    def spawn_enemy(self):
        new_enemy = Enemy(self.screen, 0, 32, 2, collision_types[2], collision_types[1:])
        self.active_objects.append(new_enemy)

    def control_waves(self):
        if self.wave_length > 0:
            self.spawn_enemy()
            new_timer = Timer(func=self.control_waves)
            self.timer_list.append(new_timer)
            self.wave_length -= 1
