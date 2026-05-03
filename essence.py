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
        self.max_health = 100
        self.current_health = self.max_health

    def health(self, health_change):
        
        self.current_healt += health_change
        if self.current_health >= self.max_health:
            self.current_health = self.max_health
        if self.current_health <= 0:
            self.current_health = 0
            self.kill()


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH
        if self.rect.y < 0:
            self.rect.y = HEIGHT


class Enemy(Essence):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40)
        self.speed = 3
        self.last_move = pygame.time.get_ticks()
        self.movedelay = 250

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move > self.movedelay:
            direction = random.choice(["up", "down", "left", "right"])
            if direction == "up":
                self.rect.y -= 20
            if direction == "down":
                self.rect.y += 20
            if direction == "left":
                self.rect.x -= 20
            if direction == "right":
                self.rect.x += 20
            self.last_move = current_time
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH
        if self.rect.y < 0:
            self.rect.y = HEIGHT
