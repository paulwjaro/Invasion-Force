from game_objects import GameObject
from gamefx import CustomSprite
import pygame


class Enemy(GameObject):
    def __init__(self, _screen, _spd, _collision_layer, _mask_list, c_width, c_height, _path=[], _sprite=CustomSprite):
        super().__init__(_screen, _spd, _collision_layer, _mask_list, c_width, c_height, _sprite=_sprite)
        self.path = _path
        self.current_node = _path[0]
        self.x_pos = 320
        self.y_pos = 32
        self.screen = _screen
        self.x_dir = 1
        self.y_dir = 1
        self.health = 2

    def step(self):
        GameObject.step(self)
        self.move()
        if self.health <= 0:
            self.destroyed = True

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
                self.x_pos = -64
                self.y_pos = 32
                self.current_node = self.path[0]

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
    def __init__(self, _x, _y, *_screen):
        self.screen = _screen
        self.x_pos = _x
        self.y_pos = _y

    def draw_node(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x_pos, self.y_pos, 10, 10))
