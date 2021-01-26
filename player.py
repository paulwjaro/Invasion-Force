from game_objects import GameObject
from gamefx import CustomSprite
from projectiles import Projectile


class Player(GameObject):
    def __init__(self, _screen, _x_pos, _y_pos, c_width, c_height, _spd, _collision_mask, _collision_layer,
                 _sprite=CustomSprite):
        super().__init__(_screen, _spd, _collision_mask, _collision_layer, c_width, c_height,
                         _x_pos=_x_pos, _y_pos=_y_pos, _sprite=_sprite)
        self.health = 10
        self.fired = False
        self.right_axis = 0
        self.left_axis = 0

    def step(self):
        GameObject.step(self)
        self.move(self.right_axis, self.left_axis)

    def fire(self, _screen, _collision_layer, _mask_list):
        self.fired = True
        bullet = Projectile(self.screen, -1, self.x_pos, self.y_pos, 7, 'projectiles', ['enemies'], 32, 32,
                            _sprite=CustomSprite('Assets/Beam_Green.png', 32))
        return bullet

    def move(self, _r_axis, _l_axis):
        axis = _r_axis - _l_axis
        self.x_pos += axis * self.spd
