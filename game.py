import pygame
import random
from load_sprites import Sprites
from load_text import Strings

pygame.init()

# Dimensions
HEIGHT = 750
WIDTH = 480

# Title Game
TITLE = "Catcher Game"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Stats Game
BASKET_STATING_LIVES = 5
BASKET_VELOCITY = 15
APPLE_STARTING_VELOCITY = 5
APPLE_ACCELERATION = 0.5
BASKET_ACCELERATION = 0.5

# FPS
FPS = 60

# Difficulty
# Options: HARD, MEDIUM, EASY
HARD = 3
MEDIUM = 2
EASY = 1

difficulty = MEDIUM

# Clock
clock = pygame.time.Clock()

# Score
score_value = 0
player_lives = BASKET_STATING_LIVES
apple_velocity = APPLE_STARTING_VELOCITY
basket_velocity = BASKET_VELOCITY

# Load Text
strings = Strings(WIDTH, HEIGHT, pygame, WHITE, BLACK)

gameover_title = strings.gameover_title()
gameover_text = strings.gameover_text()
lives = strings.lives_text(player_lives)
score = strings.score_text(score_value)
title = strings.title(TITLE)

# Load Sprites
sprites = Sprites(WIDTH, HEIGHT, pygame)
basket_sprite = sprites.basket(difficulty)
apple_sprite = sprites.apple()

# Display
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Keyboard by arrows
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_sprite["rect"].left > 0:
        basket_sprite["rect"].left -= basket_velocity
    if keys[pygame.K_RIGHT] and basket_sprite["rect"].right < WIDTH:
        basket_sprite["rect"].right += basket_velocity
    if keys[pygame.K_UP] and basket_sprite["rect"].top > 150:
        basket_sprite["rect"].top -= basket_velocity
    if keys[pygame.K_DOWN] and basket_sprite["rect"].bottom < HEIGHT:
        basket_sprite["rect"].bottom += basket_velocity

    # Keyboard by wasd
    if keys[pygame.K_a] and basket_sprite["rect"].left > 0:
        basket_sprite["rect"].left -= basket_velocity
    if keys[pygame.K_d] and basket_sprite["rect"].right < WIDTH:
        basket_sprite["rect"].right += basket_velocity
    if keys[pygame.K_w] and basket_sprite["rect"].top > 150:
        basket_sprite["rect"].top -= basket_velocity
    if keys[pygame.K_s] and basket_sprite["rect"].bottom < HEIGHT:
        basket_sprite["rect"].bottom += basket_velocity

    # Apple
    if apple_sprite["rect"].y > HEIGHT:
        apple_sprite["rect"].x = random.randint(0, WIDTH - 64)
        apple_sprite["rect"].y = 140
        player_lives -= 1
    else:
        apple_sprite["rect"].y += apple_velocity

    # Collision
    if basket_sprite["rect"].colliderect(apple_sprite["rect"]):
        apple_sprite["rect"].x = random.randint(0, WIDTH - 64)
        apple_sprite["rect"].y = 100
        apple_velocity += APPLE_ACCELERATION
        score_value += 1
        basket_velocity += BASKET_ACCELERATION

    # Score and Lives
    score["text"] = strings.score_text(score_value)["text"]
    lives["text"] = strings.lives_text(player_lives)["text"]

    display.fill(BLACK)

    display.blit(title["text"], title["rect"])
    display.blit(score["text"], score["rect"])
    display.blit(lives["text"], lives["rect"])

    pygame.draw.line(display, WHITE, (0, 140), (WIDTH, 140), 3)

    display.blit(apple_sprite["image"],apple_sprite["rect"])
    display.blit(basket_sprite["image"],basket_sprite["rect"])
    
    if player_lives == 0:
        display.blit(gameover_title["text"], gameover_title["rect"])
        display.blit(gameover_text["text"], gameover_text["rect"])
        pygame.display.update()
        pygame.time.wait(2000)
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    is_paused = False
                    score_value = 0
                    player_lives = BASKET_STATING_LIVES
                    apple_velocity = APPLE_STARTING_VELOCITY
                    basket_velocity = BASKET_VELOCITY

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
exit()

