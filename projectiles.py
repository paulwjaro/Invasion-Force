from movement_entities import MovementEntity
from gamefx import CustomSprite


class Projectile(MovementEntity):
    def __init__(self, _screen, _dir, _x_pos, _y_pos, _spd, _collision_type, _hitlist):
        super().__init__(_x_pos, _y_pos, _spd, _collision_type, _hitlist)
        self.sprite = CustomSprite('Assets/Beam_Green.png', 32)
        self.direction = _dir
        self.screen = _screen

    def move(self, _dir):
        self.y_pos += _dir * self.spd
        if self.y_pos <= 20:
            self.destroyed = True

    def draw(self, _screen, _x_pos, _y_pos):
        _screen.blit(self.sprite.sprite, (_x_pos, _y_pos))

    def hit(self):
        self.destroyed = True

    def play(self, _screen):
        self.check_for_collision(32, 32, _screen)
        self.draw(_screen, self.x_pos, self.y_pos)
        self.move(self.direction)