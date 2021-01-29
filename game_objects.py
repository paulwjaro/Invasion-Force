import pygame
from misc import Timer


class GameObject:
    def __init__(self, _screen, _spd, _collision_layer, _mask_list, c_width, c_height,
                 _x_pos=0, _y_pos=0, _sprite=None, _owner=None):
        self.screen = _screen
        self.x_pos = _x_pos
        self.y_pos = _y_pos
        self.sprite = _sprite
        self.spd = _spd
        self.destroyed = False
        self.collision_size = (c_width, c_height)
        self.collision_layer = _collision_layer
        self.collision_mask = _mask_list
        self.owner = _owner
        self.collision_shape = tuple
        self.rect = pygame.Rect((self.x_pos, self.y_pos, 0, 0))
        self.timers = []

    def create(self):
        self.destroyed = False

    def step(self):
        pass

    def draw(self, _screen):
        if self.sprite is not None:
            if self.collision_layer != 'none':
                self.update_collision(self.collision_size[0], self.collision_size[1], self.screen)
            _screen.blit(self.sprite.sprite, (self.x_pos - self.sprite.x_offset, self.y_pos - self.sprite.y_offset))

    def hit(self):
        return None

    def play(self):
        self.run_timers()
        self.step()
        if self.sprite is not None:
            self.draw(self.screen)

    def update_collision(self, collision_x, collision_y, _screen):
        collision_variance_x = self.sprite.sprite.get_rect().width - collision_x
        collision_variance_y = self.sprite.sprite.get_rect().height - collision_y
        self.collision_shape = (self.x_pos - self.sprite.x_offset + collision_variance_x/2, self.y_pos - self.sprite.y_offset + collision_variance_y/2, collision_x, collision_y)
        self.rect = pygame.Rect(self.collision_shape)
        # pygame.draw.rect(_screen, (255, 255, 255), self.collision_shape)

    def create_timer(self, _func=None):
        new_timer = Timer(func=_func)
        self.timers.append(new_timer)

    def run_timers(self):
        if len(self.timers) > 0:
            for t in self.timers:
                t.run_timer()
