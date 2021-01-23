from movement_entities import MovementEntity
from gamefx import CustomSprite
import pygame


class Enemy(MovementEntity):
    def __init__(self, _screen, _spd, _collision_type=[], _hitlist=[], _path=[]):
        super().__init__(_spd, _collision_type, _hitlist)
        self.path = _path
        self.current_node = _path[0]
        self.x_pos = self.current_node.x_pos
        self.y_pos = self.current_node.y_pos
        self.sprite = CustomSprite('Assets/Drone_1.png', 64)
        self.screen = _screen
        self.x_dir = 1
        self.y_dir = 1
        self.health = 2


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

    def draw(self, _screen, _x_pos, _y_pos):
        _screen.blit(self.sprite.sprite, (_x_pos, _y_pos))

    def hit(self):
        self.health -= 1

    def play(self, _screen):
        self.move()
        self.check_for_collision(64, 64, _screen)
        self.draw(_screen, self.x_pos, self.y_pos)

        if self.health <= 0:
            self.destroyed = True


class Paths:
    def __init__(self):
        self.path_list = []

    def create_path(self, path_length, node_coords=[], *_screen):
        new_path = []
        for i in range(path_length):
            new_node = Node(node_coords[i][0], node_coords[i][1])
            new_path.append(new_node)
        self.path_list.append(new_path)


class Node:
    def __init__(self, _x, _y, *_screen):
        self.screen = _screen
        self.x_pos = _x
        self.y_pos = _y

    def draw_node(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x_pos, self.y_pos, 10, 10))