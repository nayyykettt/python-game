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
        self.image.fill(RED)
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
        self.last_move = pygame.time.get_ticks()
        self.movedelay = 500

    def updata(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move > self.movedelay:
            direction = random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up':
                self.rect.y -= 20
            if direction == 'down':
                self.rect.y += 20
            if direction == 'left':
                self.rect.x -= 20
            if direction == 'right':
                self.rect.x += 20
            self.last_move = current_time
        if self.x > WIDTH:
            self.x = 0
        if self.y > HEIGHT:
            self.y = 0
        if self.x < 0:
            self.x = WIDTH
        if self.y < 0:
            self.y = HEIGHT
