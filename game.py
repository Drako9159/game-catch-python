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

# Clock
clock = pygame.time.Clock()

# Score
score_value = 0
player_lives = BASKET_STATING_LIVES
apple_velocity = APPLE_STARTING_VELOCITY
basket_velocity = BASKET_VELOCITY

# Load Text
strings = Strings(WIDTH, HEIGHT, pygame, WHITE, BLACK)
gameover_title, gameover_title_rect = strings.gameover_title()
gameover_text, gameover_text_rect = strings.gameover_text()
font_title_32, font_title_42, font_text = strings.get_fonts()
lives_text, lives_rect = strings.lives_text(player_lives)
score = strings.score_text(score_value)
title = strings.title(TITLE)

# Load Sprites
sprites = Sprites(WIDTH, HEIGHT, pygame)
basket_image, basket_rect = sprites.basket()
apple_image, apple_rect = sprites.apple()

# Display
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_rect.left > 0:
        basket_rect.left -= basket_velocity
    if keys[pygame.K_RIGHT] and basket_rect.right < WIDTH:
        basket_rect.right += basket_velocity
    if keys[pygame.K_UP] and basket_rect.top > 150:
        basket_rect.top -= basket_velocity
    if keys[pygame.K_DOWN] and basket_rect.bottom < HEIGHT:
        basket_rect.bottom += basket_velocity

    # Apple
    if apple_rect.y > HEIGHT:
        apple_rect.x = random.randint(0, WIDTH - 64)
        apple_rect.y = 140
        player_lives -= 1
    else:
        apple_rect.y += apple_velocity

    # Collision
    if basket_rect.colliderect(apple_rect):
        apple_rect.x = random.randint(0, WIDTH - 64)
        apple_rect.y = 100
        apple_velocity += APPLE_ACCELERATION
        score_value += 1
        basket_velocity += BASKET_ACCELERATION

    # Score
    score["text"] = font_text.render(f"Score: {score_value}", True, WHITE, BLACK)
    lives_text = font_text.render(f"Lives: {player_lives}", True, WHITE, BLACK)

    display.fill(BLACK)

    display.blit(title["text"], title["rect"])
    display.blit(score["text"], score["rect"])
    display.blit(lives_text, lives_rect)

    pygame.draw.line(display, WHITE, (0, 140), (WIDTH, 140), 3)

    display.blit(apple_image,apple_rect)
    display.blit(basket_image,basket_rect)
    
    if player_lives == 0:
        display.blit(gameover_title, gameover_title_rect)
        display.blit(gameover_text, gameover_text_rect)
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

