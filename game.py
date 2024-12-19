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
STUDENT_STATING_LIVES = 5
STUDENT_VELOCITY = 15
APPLE_STARTING_VELOCITY = 5
APPLE_ACCELERATION = 0.5

# FPS
FPS = 60

# Clock
clock = pygame.time.Clock()

# Score
score = 0
player_lives = STUDENT_STATING_LIVES
apple_velocity = APPLE_STARTING_VELOCITY

# Fonts
font_title_32 = pygame.font.Font("fonts/super_pixel.ttf", 32)
font_title_42 = pygame.font.Font("fonts/super_pixel.ttf", 42)
font_text = pygame.font.Font("fonts/super_pixel.ttf", 24)

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
lives_rect.topright = (WIDTH - 10, 98)

# Game Over Title
game_over_title = font_title_32.render("Game Over", True, WHITE, BLACK)
game_over_rect = game_over_title.get_rect()
game_over_rect.center = (WIDTH // 2, HEIGHT // 2)

# Game Over Text
game_over_text = font_text.render("Press any key to play again", True, WHITE, BLACK)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH // 2, (HEIGHT // 2) + 60)

# Sprite basket
basket_image = pygame.image.load("sprites/basket.png")
basket_image = pygame.transform.smoothscale(basket_image, (100, 100))
basket_rect = basket_image.get_rect()
basket_rect.left = 10
basket_rect.bottom = HEIGHT - 10

# Sprite apple
apple_image = pygame.image.load("sprites/apple.png")
apple_image = pygame.transform.smoothscale(apple_image, (50, 50))
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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_rect.left > 0:
        basket_rect.left -= STUDENT_VELOCITY
    if keys[pygame.K_RIGHT] and basket_rect.right < WIDTH:
        basket_rect.right += STUDENT_VELOCITY
    if keys[pygame.K_UP] and basket_rect.top > 150:
        basket_rect.top -= STUDENT_VELOCITY
    if keys[pygame.K_DOWN] and basket_rect.bottom < HEIGHT:
        basket_rect.bottom += STUDENT_VELOCITY

    # Apple
    

    # Score
    score_text = font_text.render(f"Score: {score}", True, WHITE, BLACK)
    lives_text = font_text.render(f"Lives: {player_lives}", True, WHITE, BLACK)

    display.fill(BLACK)

    display.blit(title_text, title_rect)
    display.blit(score_text, score_rect)
    display.blit(lives_text, lives_rect)

    display.blit(apple_image,apple_rect)
    display.blit(basket_image,basket_rect)
    
    pygame.draw.line(display, WHITE, (0, 140), (WIDTH, 140), 3)
    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
exit()

