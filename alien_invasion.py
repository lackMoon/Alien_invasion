import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from game_functions import *
def run_game():
    pygame.init()
    game_settings=Settings()
    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats=GameStats(game_settings)
    board=Scoreboard(screen,game_settings,stats)
    play_button=Button(screen,game_settings,"Play")
    ship=Ship(screen,game_settings)
    aliens=Group()
    bullets=Group()
    create_aliens(screen,game_settings,aliens)
    while True:
        check_events(game_settings,screen,stats,board,ship,bullets,aliens,play_button)
        if stats.game_active:
            ship.update()
            update_bullets(bullets,aliens)
            bullet_collision(screen,game_settings,stats,bullets,aliens,board)
            update_aliens(screen, game_settings, stats,board, bullets, ship, aliens)
        check_high_score(stats,board)
        update_screen(game_settings,screen,stats,board,ship,aliens,bullets,play_button)

if __name__ == '__main__':
    run_game()