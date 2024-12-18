import pygame

pygame.init()

# Dimensions
HEIGHT = 750
WIDTH = 480

# Version
VERSION = "1.0.0"

# Title Game
TITLE = "Catcher Game " + VERSION

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# FPS
FPS = 60

# Sprites
apple_image = pygame.image.load("sprites/apple.png")
basket_image = pygame.image.load("sprites/basket.png")

# Minimal rectangle
apple_rect = apple_image.get_rect()
basket_rect = basket_image.get_rect()

apple_rect.center = (WIDTH // 2, HEIGHT // 2)

apple_rect.size = (WIDTH // 10, HEIGHT // 10)




apple_rect.left = 10
apple_rect.bottom = HEIGHT - 10


basket_rect.center = (WIDTH // 2, HEIGHT // 2)




display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    display.fill(BLACK)

    display.blit(apple_image,apple_rect)
    display.blit(basket_image,basket_rect)
    
    pygame.display.update()
   

pygame.quit()
exit()

