import pygame.font
from  pygame.sprite import Group
from ship import Ship
class Scoreboard():
    def __init__(self,screen,game_settings,stats):
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.game_settings=game_settings
        self.stats=stats
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()
    def prep_score(self):
        score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.game_settings.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def prep_high_score(self):
        high_score=str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score, True, self.text_color, self.game_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=20

    def prep_ships(self):
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.screen,self.game_settings)
            ship.rect.x=ship_number*ship.rect.width+10
            ship.rect.y=10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.ships.draw(self.screen)