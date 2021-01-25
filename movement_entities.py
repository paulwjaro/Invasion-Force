import pygame



class MovementEntity:
    def __init__(self, _spd, _collision_type, _hitlist, _x_pos=0, _y_pos=0):
        self.x_pos = _x_pos
        self.y_pos = _y_pos
        self.spd = _spd
        self.destroyed = False
        self.collision_type = _collision_type
        self.can_hit = _hitlist
        self.collision_shape = tuple
        self.rect = pygame.Rect((self.x_pos, self.y_pos, 0, 0))

    def move(self, _right, _left):
        axis = _right - _left
        self.x_pos += axis * self.spd




        


