import pygame

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

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    display.fill(BLACK)
    pygame.display.update()

pygame.quit()
exit()

