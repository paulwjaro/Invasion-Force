from player import *
from enemies import Enemy
from gamefx import StarGen
import misc


class Level:
    def __init__(self, _screen, _object_handler, _level_data):
        self.screen = _screen
        self.handler = _object_handler
        self.level_data = _level_data
        self.wave_count = len(self.level_data['waves'])
        self.current_wave = 1
        self.wave_list = []
        self.timers = []
        self.level_started = False

    def create(self):
        for wave in range(len(self.level_data['waves'])):
            self.create_wave(wave)

    def run(self):
        if self.level_started:

            if self.wave_list[self.current_wave - 1].finished:
                self.current_wave += 1
            else:
                self.wave_list[self.current_wave - 1].run()

    def create_wave(self, _current_wave):
        new_wave = Wave(self.screen, self.timers, self.handler, self.level_data['waves'][str(_current_wave)], self)
        new_wave.create_strands(_current_wave)
        self.wave_list.append(new_wave)


class Wave:
    def __init__(self, _screen, _timers, _object_handler, _wave_data, _owner):
        self.screen = _screen
        self.handler = _object_handler
        self.timers = _timers
        self.wave_data = _wave_data
        self.strand_count = len(self.wave_data['strands'])
        self.strand_list = []
        self.current_strand = 0
        self.finished = False
        self.owner = _owner

    def create_strands(self, _current_wave):
        for s in range(self.strand_count):
            strand_data = self.wave_data['strands'][str(s)]
            new_strand = Strand(self.screen, self.timers, self.handler, strand_data, self)
            self.strand_list.append(new_strand)

    def run(self):
        if len(self.strand_list) > 0:
            try:
                self.strand_list[self.current_strand].run()
                if self.strand_list[self.current_strand].finished:
                    self.strand_list[self.current_strand].finished = False
                    self.current_strand += 1
            except IndexError:
                self.current_strand = 0
        else:
            self.finished = True
            self.owner.current_wave += 1


class Strand:
    def __init__(self, _screen, _timers, _object_handler, _strand_data, _wave):
        self.screen = _screen
        self.timers = _timers
        self.handler = _object_handler
        self.strand_data = _strand_data
        self.enemies_count = self.strand_data['length']
        self.enemies_left = self.enemies_count
        self.strand_enemy = self.strand_data['enemy']
        self.wave = _wave
        self.strand_started = False
        self.spawn_finished = False
        self.enemy_list = []
        self.finished = False

    def run(self):
        if len(self.timers) > 0:
            misc.run_timers(self)

        if self.enemies_count > 0:
            self.spawn_enemies()
        else:
            if not self.strand_started:
                self.wave.strand_list.pop(self.wave.strand_list.index(self))

        if self.strand_started:
            if len(self.enemy_list) > 0:
                pass
            else:
                self.finished = True
                self.strand_started = False
                self.enemies_count = self.enemies_left

    def spawn_enemies(self):
        if self.enemies_count > 0:
            if len(self.timers) == 0:
                misc.create_timer(self, _func=self.create_enemy)

    def create_enemy(self):
        enemy_data = self.strand_data['enemy']
        new_enemy = Enemy(self.screen, enemy_data['spd'], enemy_data['collision_layer'], enemy_data['collision_mask'], enemy_data['c_width'], enemy_data['c_height'], self.strand_data['path'],
                          enemy_data['points'], _sprite=enemy_data['sprite'], _strand=self, _object_handler=self.handler)
        self.handler.add_object_to_game(new_enemy)
        self.enemy_list.append(new_enemy)
        self.enemies_count -= 1
        if not self.strand_started:
            self.strand_started = True


class ObjectHandler:
    def __init__(self, _screen):
        self.screen = _screen
        self.score = 0
        self.active_objects = []
        self.player = None
        self.star_generator = StarGen(self.screen)

    def create(self):
        self.star_generator.star_scatter(50)

    def object_handler(self, _screen):
        self.star_generator.play()
        if len(self.active_objects) > 0:
            for _object in self.active_objects:
                if _object.destroyed:
                    if type(_object) == Enemy:
                        self.score += _object.points
                    self.active_objects.pop(self.active_objects.index(_object))

                else:
                    _object.play()
                    if _object.collision_layer != 'none':
                        for collisions in self.active_objects:
                            if _object != collisions:
                                if _object.rect.colliderect(collisions.rect):
                                    if collisions.collision_layer in _object.collision_mask:
                                        if type(_object) == Projectile:
                                            if _object.owner != collisions:
                                                _object.hit()
                                        else:
                                            _object.hit()

    def add_object_to_game(self, _object):
        self.active_objects.append(_object)
