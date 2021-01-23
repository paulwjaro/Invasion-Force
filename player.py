from movement_entities import MovementEntity
from projectiles import Projectile
from gamefx import CustomSprite


class Player(MovementEntity):
    def __init__(self, _x_pos, _y_pos, _spd, _collision_type, _hitlist):
        super().__init__(_spd, _collision_type, _hitlist, _x_pos=_x_pos, _y_pos=_y_pos)
        self.sprite = CustomSprite('Assets/Player_1.png', 64)
        self.health = 10
        self.fired = False
        self.right_axis = 0
        self.left_axis = 0

    def step(self):
        self.move(self.right_axis, self.left_axis)

    def draw(self, _screen, _x_pos, _y_pos):
        _screen.blit(self.sprite.sprite, (_x_pos, _y_pos))

    def fire(self, _screen, _collision_type, _hitlist):
        self.fired = True
        bullet = Projectile(_screen, -1, self.x_pos, self.y_pos, 10,  _collision_type, _hitlist)
        return bullet

    def play(self, _screen):
        self.check_for_collision(64, 64, _screen)
        self.draw(_screen, self.x_pos, self.y_pos)
        self.step()

