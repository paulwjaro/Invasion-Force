from movement_entities import MovementEntity
from gamefx import CustomSprite


class Enemy(MovementEntity):
    def __init__(self, _screen, _x_pos, _y_pos, _spd, _collision_type, _hitlist):
        super().__init__(_x_pos, _y_pos, _spd, _collision_type, _hitlist)
        self.sprite = CustomSprite('Assets/Drone_1.png', 64)
        self.screen = _screen
        self._dir = 1
        self.health = 2

    def move(self):
        self.x_pos += self.spd * self._dir
        if self.x_pos + self.spd + 64 >= 640:
            self._dir = -1
            self.y_pos += 64
        elif self.x_pos + self.spd <= 0:
            self._dir = 1
            self.y_pos += 64

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

