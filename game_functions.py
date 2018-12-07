import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien
def check_events(game_settings,screen,stats,board,ship,bullets,aliens,button):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,game_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN and not stats.game_active:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play(screen,game_settings,button,ship,bullets,aliens,stats,board,mouse_x,mouse_y)

def check_play(screen,game_settings,button,ship,bullets,aliens,stats,board,mouse_x,mouse_y):
    if button.rect.collidepoint(mouse_x,mouse_y):
        stats.reset_stats()
        board.prep_score()
        board.prep_high_score()
        board.prep_ships()
        game_settings.initialize()
        stats.game_active=True
        pygame.mouse.set_visible(False)
        clear_screen(screen, game_settings, bullets, ship, aliens)

def check_keydown_events(event,game_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key==pygame.K_UP:
        ship.moving_up=True
    elif event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key==pygame.K_SPACE:
        fire(game_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False

def update_screen(game_settings,screen,stats,board,ship,aliens,bullets,button):
    screen.fill(game_settings.bg_color)  #重绘屏幕
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    board.prep_score()
    board.prep_high_score()
    board.prep_ships()
    board.show_score()
    if not stats.game_active:
        button.draw_button()
    pygame.display.flip()    #绘制屏幕可见

def update_bullets(bullets,aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

def fire(game_settings,screen,ship,bullets):
    new_bullet = Bullet(game_settings, screen, ship)
    bullets.add(new_bullet)

def create_aliens(screen,game_settings,aliens):
    alien=Alien(screen,game_settings)
    alien_width=alien.rect.width
    avail_spacex=game_settings.screen_width-2*alien_width
    alien_numbers=int(avail_spacex/(2*alien_width))
    for alien_number in range(alien_numbers):
        new_alien=Alien(screen,game_settings)
        new_alien.rect.x=alien_width+2*alien_width*alien_number
        aliens.add(new_alien)

def update_aliens(screen, game_settings, stats,board, bullets, ship, aliens):
    screen_rect = screen.get_rect()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_collision(screen, game_settings, stats,board,bullets, ship, aliens)
    for alien in aliens.sprites():
        if game_settings.alien_level_direction==1 and alien.rect.right<=alien.screen_rect.right:
            alien.rect.x+=game_settings.alien_level_direction*game_settings.alien_speed
        elif game_settings.alien_level_direction==-1 and alien.rect.left>=0:
            alien.rect.x+=game_settings.alien_level_direction*game_settings.alien_speed
        elif alien.rect.bottom>=screen_rect.bottom:
            ship_collision(screen, game_settings, stats, bullets, ship, aliens)
            break
        else:
            for alien in aliens.sprites():
                alien.rect.y+=game_settings.alien_vert_direction*game_settings.alien_drop_speed
            game_settings.alien_level_direction*=-1

def bullet_collision(screen,game_settings,stats,bullets,aliens,board):
    collision=pygame.sprite.groupcollide(bullets, aliens, True, True)  # bullets 和 aliens两个的rect重叠时，删除发生碰撞的两个元素
    if collision:
        for alien in collision.values():
            stats.score+=game_settings.point*len(alien)
            board.prep_score()
    if len(aliens) == 0:
        game_settings.increase_speed()
        create_aliens(screen, game_settings, aliens)

def ship_collision(screen, game_settings, stats,board,bullets, ship, aliens):
    if stats.ships_left>=1:
        stats.ships_left-=1
        board.prep_ships()
        clear_screen(screen, game_settings, bullets, ship, aliens)
        game_settings.initialize()
        sleep(0.8)
    else:
        stats.game_active=False
        stats.reset_stats()
        clear_screen(screen, game_settings, bullets, ship, aliens)
        pygame.mouse.set_visible(True)

def clear_screen(screen, game_settings, bullets, ship, aliens):
    screen_rect = screen.get_rect()
    aliens.empty()
    bullets.empty()
    create_aliens(screen, game_settings, aliens)
    ship.rect.centerx = screen_rect.centerx
    ship.rect.bottom = screen_rect.bottom

def check_high_score(stats,board):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        board.prep_high_score()