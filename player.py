import game
from game_objects import GameObject
from projectiles import *


class Player(GameObject):
    def __init__(self, _screen, _x_pos, _y_pos, c_width, c_height, _spd, _collision_mask, _collision_layer,
                 _sprite=CustomSprite):
        super().__init__(_screen, _spd, _collision_mask, _collision_layer, c_width, c_height,
                         _x_pos=_x_pos, _y_pos=_y_pos, _sprite=_sprite)
        self.health = 10
        self.fired = False
        self.right_axis = 0
        self.left_axis = 0
        self.game_started = False

    def step(self):
        self.move(self.right_axis, self.left_axis)

    def play(self):
        if self.game_started:
            GameObject.play(self)

    def fire(self, _screen, _collision_layer, _mask_list):
        self.fired = True
        bullet_data = projectile_data['Beam_Green']
        bullet = Projectile(self.screen, -1, self.x_pos - bullet_data['c_width'], self.y_pos - bullet_data['c_height'],
                            bullet_data['spd'], bullet_data['collision_layer'], bullet_data['collision_mask'],
                            bullet_data['c_width'], bullet_data['c_height'],
                            _sprite=bullet_data['sprite'], _owner=self)
        return bullet

    def move(self, _r_axis, _l_axis):
        axis = _r_axis - _l_axis
        self.x_pos += axis * self.spd


player_data = {
    "sprites": {
        '0': {
            'c_width': 48,
            'c_height': 48,
            'collision_layer': 'player',
            'collision_mask': ['enemies', 'projectiles'],
            'spd': 3,
            'sprite': CustomSprite('Assets/Player_1.png', 64)
        }
    }
}
