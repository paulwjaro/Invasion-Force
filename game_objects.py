import pygame


class GameObject:
    def __init__(self, _screen, _spd, _collision_layer, _mask_list, c_width, c_height, _x_pos=0, _y_pos=0, _sprite=None):
        self.screen = _screen
        self.x_pos = _x_pos
        self.y_pos = _y_pos
        self.sprite = _sprite
        self.spd = _spd
        self.destroyed = False
        self.collision_size = (c_width, c_height)
        self.collision_layer = _collision_layer
        self.collision_mask = _mask_list
        self.collision_shape = tuple
        self.rect = pygame.Rect((self.x_pos, self.y_pos, 0, 0))

    def create(self):
        return None

    def step(self):
        if self.collision_layer != 'none':
            self.update_collision(self.collision_size[0], self.collision_size[1], self.screen)

    def draw(self, _screen):
        if self.sprite is not None:
            _screen.blit(self.sprite.sprite, (self.x_pos, self.y_pos))

    def hit(self):
        return None

    def play(self):
        self.step()
        if self.sprite is not None:
            self.draw(self.screen)

    def update_collision(self, collision_x, collision_y, _screen):
        self.collision_shape = (self.x_pos, self.y_pos, collision_x, collision_y)
        self.rect = pygame.Rect(self.collision_shape)
        # pygame.draw.rect(_screen, (255, 255, 255), self.collision_shape)