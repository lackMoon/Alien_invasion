import  pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,screen,game_settings):
        super(Alien,self).__init__()
        self.screen=screen
        self.game_settings=game_settings
        self.image=pygame.image.load('images/alien.bmp')
        self.screen_rect=self.screen.get_rect()
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.rect.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
