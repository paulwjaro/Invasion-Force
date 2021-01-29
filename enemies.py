from game_objects import GameObject
from gamefx import CustomSprite
import pygame


class Enemy(GameObject):
    def __init__(self, _screen, _spd, _collision_layer, _mask_list, c_width, c_height, _path, _points, _sprite=CustomSprite, _strand=None, _object_handler=None):
        super().__init__(_screen, _spd, _collision_layer, _mask_list, c_width, c_height, _sprite=_sprite)
        self.path = _path
        self.current_node = _path[0]
        self.x_pos = self.current_node.x_pos
        self.y_pos = self.current_node.y_pos
        self.screen = _screen
        self.strand = _strand
        self.handler = _object_handler
        self.points = _points
        self.x_dir = 1
        self.y_dir = 1
        self.health = 2

    def step(self):
        self.move()
        if self.health <= 0:
            self.strand.enemy_list.pop(self.strand.enemy_list.index(self))
            self.destroyed = True
            self.strand.enemies_left -= 1

    def move(self):
        if self.x_pos <= self.current_node.x_pos - self.spd:
            self.x_dir = 1
        elif self.x_pos >= self.current_node.x_pos + self.spd:
            self.x_dir = -1
        else:
            self.x_dir = 0
        if self.y_pos <= self.current_node.y_pos - self.spd:
            self.y_dir = 1
        elif self.y_pos >= self.current_node.y_pos + self.spd:
            self.y_dir = -1
        else:
            self.y_dir = 0

        if self.x_dir == 0 and self.y_dir == 0:
            if self.current_node != self.path[-1]:
                self.current_node = self.path[self.path.index(self.current_node) + 1]
            else:
                self.strand.enemy_list.pop(self.strand.enemy_list.index(self))
                self.handler.active_objects.pop(self.handler.active_objects.index(self))
                # self.x_pos = -64
                # self.y_pos = 32
                # self.current_node = self.path[0]

        self.x_pos += self.x_dir * self.spd
        self.y_pos += self.y_dir * self.spd

    def hit(self):
        self.health -= 1


class Paths:
    def __init__(self):
        self.path_list = []

    def create_path(self, path, _screen=None):
        new_path = []
        for coords in path:
            new_node = Node(coords[0], coords[1])
            new_path.append(new_node)
        self.path_list.append(new_path)


class Node:
    def __init__(self, _x, _y, _screen=None):
        self.screen = _screen
        self.x_pos = _x
        self.y_pos = _y

    # noinspection PyTypeChecker
    def draw_node(self):
        if self.screen is not None:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.x_pos, self.y_pos, 10, 10))


enemies_data = {
    'Drone_1': {
        'spd': 2,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 64,
        'c_height': 64,
        'sprite': CustomSprite('Assets/Drone_1.png', 64),
        'points': 100
    },
    'Drone_2': {
            'spd': 2,
            'collision_layer': 'enemies',
            'collision_mask': ['player', 'projectiles'],
            "c_width": 64,
            'c_height': 64,
            'sprite': CustomSprite('Assets/Drone_2.png', 64),
            'points': 100
    },
    'Bot_1': {
        'spd': 2.5,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 60,
        'c_height': 32,
        'sprite': CustomSprite('Assets/Bot_1.png', 64),
        'points': 200
    },
    'Bot_2': {
        'spd': 2.5,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 60,
        'c_height': 32,
        'sprite': CustomSprite('Assets/Bot_2.png', 64),
        'points': 200
    },
    'Ship_1': {
        'spd': 3,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 64,
        'c_height': 64,
        'sprite': CustomSprite('Assets/Ship_1.png', 64),
        'points': 300
    },
    'Ship_2': {
        'spd': 3,
        'collision_layer': 'enemies',
        'collision_mask': ['player', 'projectiles'],
        "c_width": 64,
        'c_height': 64,
        'sprite': CustomSprite('Assets/Ship_2.png', 64),
        'points': 300
    }
}
