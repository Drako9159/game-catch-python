import random

# Dimensions Sprites
APPLE_WITH, APPLE_HEIGHT = 50, 50
BASKET_WIDTH, BASKET_HEIGHT = 120, 120
    
class Sprites():
    def __init__(self, width, height, pygame):
        self.width = width
        self.height = height
        self.pygame = pygame
    
    def apple(self):
        apple_image = self.pygame.image.load("sprites/apple.png")
        apple_image = self.pygame.transform.smoothscale(apple_image, (APPLE_WITH, APPLE_HEIGHT))
        apple_rect = apple_image.get_rect()
        apple_rect.left = random.randint(0, self.width - 64)
        apple_rect.bottom = self.height // 2 - 175
        return apple_image, apple_rect
    
    def basket(self):
        basket_image = self.pygame.image.load("sprites/basket.png")
        basket_image = self.pygame.transform.smoothscale(basket_image, (BASKET_WIDTH, BASKET_HEIGHT))
        basket_rect = basket_image.get_rect()
        basket_rect.left = 10
        basket_rect.bottom = self.height - 10
        return basket_image, basket_rect
    
