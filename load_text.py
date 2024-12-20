import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "fonts")
FONT_SPENBEB = os.path.join(FONTS_DIR, "spenbeb.otf")

class Strings():

    def __init__(self, width, height, pygame, color, background):
        self.width = width
        self.height = height
        self.pygame = pygame
        self.font_title_32, self.font_title_42, self.font_text = self.get_fonts()
        self.color = color
        self.background = background
    
    def get_fonts(self):
        font_title_32 = self.pygame.font.Font(FONT_SPENBEB, 32)
        font_title_42 = self.pygame.font.Font(FONT_SPENBEB, 42)
        font_text = self.pygame.font.Font(FONT_SPENBEB, 24)
        return font_title_32, font_title_42, font_text
    
    def gameover_title(self):
        gameover_title = self.font_title_42.render("Game Over", True, self.color, self.background)
        gameover_title_rect = gameover_title.get_rect()
        gameover_title_rect.center = (self.width // 2, self.height // 2)
        return gameover_title, gameover_title_rect
    
    def gameover_text(self):
        gameover_text = self.font_text.render("Press any key to continue", True, self.color, self.background)
        gameover_text_rect = gameover_text.get_rect()
        gameover_text_rect.center = (self.width // 2, self.height // 2 + 60)
        return gameover_text, gameover_text_rect
    
    def lives_text(self, lives):
        lives_text = self.font_text.render(f"Lives: {lives}", True, self.color, self.background)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (self.width - 10, 90)
        return lives_text, lives_rect
    
    def score_text(self, score):
        score_text = self.font_text.render(f"Score: {score}", True, self.color, self.background)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 90)
        return { "text": score_text, "rect": score_rect }
    
    def title(self, title):
        title_text = self.font_title_42.render(title, True, self.color, self.background)
        title_rect = title_text.get_rect()
        title_rect.centerx = (self.width // 2)
        title_rect.y = 15
        return { "text": title_text, "rect": title_rect }