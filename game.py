import pygame
import random

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

APPLE_WITH, APPLE_HEIGHT = 50, 50
BASKET_WIDTH, BASKET_HEIGHT = 120, 120

# FPS
FPS = 60

# Clock
clock = pygame.time.Clock()

# Score
score = 0
player_lives = BASKET_STATING_LIVES
apple_velocity = APPLE_STARTING_VELOCITY
basket_velocity = BASKET_VELOCITY

# Fonts
font_title_32 = pygame.font.Font("fonts/spenbeb.otf", 32)
font_title_42 = pygame.font.Font("fonts/spenbeb.otf", 42)
font_text = pygame.font.Font("fonts/spenbeb.otf", 24)

# Score
score_text = font_text.render(f"Score: {score}", True, WHITE, BLACK)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 98)

# Set Title
title_text = font_title_42.render(TITLE, True, WHITE, BLACK)
title_rect = title_text.get_rect()
title_rect.centerx = (WIDTH // 2)
title_rect.y = 15

# Set Lives
lives_text = font_text.render(f"Lives: {player_lives}", True, WHITE, BLACK)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WIDTH - 10, 90)

# Game Over Title
gameover_title = font_title_42.render("Game Over", True, WHITE, BLACK)
gameover_title_rect = gameover_title.get_rect()
gameover_title_rect.center = (WIDTH // 2, HEIGHT // 2)

# Game Over Text
gameover_text = font_text.render("Press any key to play again", True, WHITE, BLACK)
gameover_text_rect = gameover_text.get_rect()
gameover_text_rect.center = (WIDTH // 2, (HEIGHT // 2) + 60)

# Sprite basket
basket_image = pygame.image.load("sprites/basket.png")
basket_image = pygame.transform.smoothscale(basket_image, (BASKET_WIDTH, BASKET_HEIGHT))
basket_rect = basket_image.get_rect()
basket_rect.left = 10
basket_rect.bottom = HEIGHT - 10

# Sprite apple
apple_image = pygame.image.load("sprites/apple.png")
apple_image = pygame.transform.smoothscale(apple_image, (APPLE_WITH, APPLE_HEIGHT))
apple_rect = apple_image.get_rect()
apple_rect.left = random.randint(0, WIDTH - 64)
apple_rect.bottom = HEIGHT // 2 - 175

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
        score += 1
        basket_velocity += BASKET_ACCELERATION

    # Score
    score_text = font_text.render(f"Score: {score}", True, WHITE, BLACK)
    lives_text = font_text.render(f"Lives: {player_lives}", True, WHITE, BLACK)

    display.fill(BLACK)

    display.blit(title_text, title_rect)
    display.blit(score_text, score_rect)
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
                    score = 0
                    player_lives = BASKET_STATING_LIVES
                    apple_velocity = APPLE_STARTING_VELOCITY
                    basket_velocity = BASKET_VELOCITY

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
exit()

