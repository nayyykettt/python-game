from config import *
import pygame


class Essence(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Player(Essence):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.speed = 5

    def updata(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y += self.speed
        if keys[pygame.K_s]:
            self.y -= self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
