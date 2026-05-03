from config import *
import pygame
import random


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


class Enemy(Essence):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40)
        self.speed = 3

    def updata(self):
        VOV = random.randrange(0, 4)
        if VOV == 0:
            self.y += self.speed
        if VOV == 1:
            self.y -= self.speed
        if VOV == 2:
            self.x -= self.speed
        if VOV == 3:
            self.x += self.speed
        if self.x > WIDTH:
            self.x = 0
        if self.y > HEIGHT:
            self.y = 0
        if self.x < 0:
            self.x = WIDTH
        if self.y < 0:
            self.y = HEIGHT
