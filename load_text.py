import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "fonts")
FONT_SPENBEB = os.path.join(FONTS_DIR, "spenbeb.otf")

class Strings():

    def __init__(self, width, height, pygame, color, background):
        self.width = width
        self.height = height
        self.pygame = pygame
        self.font_text = self.get_fonts()
        self.color = color
        self.background = background
    
    def get_fonts(self):
        font_32 = self.pygame.font.Font(FONT_SPENBEB, 32)
        font_42 = self.pygame.font.Font(FONT_SPENBEB, 42)
        font_24 = self.pygame.font.Font(FONT_SPENBEB, 24)
        return { "32": font_32, "42": font_42, "24": font_24 }
    
    def gameover_title(self):
        gameover_title = self.font_text["42"].render("Game Over", True, self.color, self.background)
        gameover_title_rect = gameover_title.get_rect()
        gameover_title_rect.center = (self.width // 2, self.height // 2)
        return { "text": gameover_title, "rect": gameover_title_rect }
    
    def gameover_text(self):
        gameover_text = self.font_text["24"].render("Press any key to continue", True, self.color, self.background)
        gameover_text_rect = gameover_text.get_rect()
        gameover_text_rect.center = (self.width // 2, self.height // 2 + 60)
        return { "text": gameover_text, "rect": gameover_text_rect }
    
    def lives_text(self, lives):
        lives_text = self.font_text["24"].render(f"Lives: {lives}", True, self.color, self.background)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (self.width - 10, 90)
        return { "text": lives_text, "rect": lives_rect }
    
    def score_text(self, score):
        score_text = self.font_text["24"].render(f"Score: {score}", True, self.color, self.background)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 90)
        return { "text": score_text, "rect": score_rect }
    
    def title(self, title):
        title_text = self.font_text["42"].render(title, True, self.color, self.background)
        title_rect = title_text.get_rect()
        title_rect.centerx = (self.width // 2)
        title_rect.y = 15
        return { "text": title_text, "rect": title_rect }