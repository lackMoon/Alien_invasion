import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,game_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.rect.y=float(self.rect.y)
        self.color=game_settings.bullet_color
        self.speed=game_settings.bullet_speed
    def update(self):
        self.rect.y-=self.speed
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
