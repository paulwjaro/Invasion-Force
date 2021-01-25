from game_objects import GameObject
from gamefx import CustomSprite


class Projectile(GameObject):
    def __init__(self, _screen, _dir, _x_pos, _y_pos, _spd, _collision_layer, _mask_list, c_width, c_height, _sprite=CustomSprite):
        super().__init__(_screen, _spd, _collision_layer, _mask_list, c_width, c_height, _x_pos=_x_pos, _y_pos=_y_pos, _sprite=_sprite)
        self.direction = _dir
        self.screen = _screen

    def move(self, _dir):
        self.y_pos += _dir * self.spd
        if self.y_pos <= 20:
            self.destroyed = True

    def hit(self):
        self.destroyed = True

    def step(self):
        GameObject.step(self)
        self.move(self.direction)
