import pygame

class Keyboard():
    def __init__(self):
        pass
        
    def control_arrows(self, rect, velocity, width, height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and rect.left > 0:
            rect.left -= velocity
        if keys[pygame.K_RIGHT] and rect.right < width:
            rect.right += velocity
        if keys[pygame.K_UP] and rect.top > 150:
            rect.top -= velocity
        if keys[pygame.K_DOWN] and rect.bottom < height:
            rect.bottom += velocity
        return None
    
    def control_wasd(self, rect, velocity, width, height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and rect.left > 0:
            rect.left -= velocity
        if keys[pygame.K_d] and rect.right < width:
            rect.right += velocity
        if keys[pygame.K_w] and rect.top > 150:
            rect.top -= velocity
        if keys[pygame.K_s] and rect.bottom < height:
            rect.bottom += velocity
        return None