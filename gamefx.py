import pygame
import game_assets


class CustomSprite:
    def __init__(self, img=str, scale=int):
        self.source = pygame.image.load(img)
        self.sprite = pygame.transform.scale(self.source, (scale, scale))

