from config import *
import pygame
from essence import Player, Enemy
import random

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Gameme")
clock = pygame.time.Clock()
screen.fill(BLACK)
running = True
all_sprites = pygame.sprite.Group()

player = Player(WIDTH // 2 - 25, HEIGHT // 2 - 25)

all_sprites.add(player)

for i in range(100):
    enemy = Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    all_sprites.add(enemy)


while running:
    health_bar = pygame.Rect(10, 10, (WIDTH - 20) * (player.current_health // 100), 20)
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.draw.rect(screen, RED, health_bar)
    pygame.display.flip()
