import  pygame
from  pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,screen,game_settings):
        super(Ship,self).__init__()
        self.screen=screen
        self.game_settings=game_settings
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
        self.rect.bottom=self.screen_rect.bottom
        self.moving_up=False
        self.moving_down=False
        self.moving_right=False
        self.moving_left=False
        self.rect.centerx=float(self.rect.centerx)
        self.rect.centery = float(self.rect.centery)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=self.game_settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.rect.centerx-=self.game_settings.ship_speed
        if self.moving_up and self.rect.top>0:
            self.rect.centery-=self.game_settings.ship_speed
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery+=self.game_settings.ship_speed