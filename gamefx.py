import pygame
import misc
import random as rand


class CustomSprite:
    def __init__(self, img=str, scale=int):
        self.source = pygame.image.load(img)
        self.sprite = pygame.transform.scale(self.source, (scale, scale))
        self.x_offset = self.sprite.get_rect().width
        self.y_offset = self.sprite.get_rect().height


class Star:
    def __init__(self, _screen, _x, _size):
        self.screen = _screen
        self.x_pos = _x
        self.y_pos = -5
        self.size = _size


    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x_pos, self.y_pos, self.size, self.size))

    def play(self):
        self.draw()
        self.y_pos += self.size * .25


class StarGen:
    def __init__(self, _screen):
        self.screen = _screen
        self.timer = misc.Timer(_length=500, _func=self.create_star)
        self.star_list = []

    def create_star(self):
        new_star = Star(self.screen, rand.randint(0, 640), rand.randint(1, 2))
        self.star_list.append(new_star)
        self.timer = misc.Timer(_length=500, _func=self.create_star)

    def play(self):
        self.timer.run_timer()
        if len(self.star_list) > 0:
            for star in self.star_list:
                star.play()

    def star_scatter(self, _amount):
        for i in range(_amount):
            new_star = Star(self.screen, rand.randint(0, 640), rand.randint(1, 2))
            new_star.y_pos = rand.randint(0, 480)
            self.star_list.append(new_star)
