class Settings():
    def __init__(self):
        self.screen_width=800
        self.screen_height=600
        self.bg_color=(230,230,230)
        self.point=50
        self.point_scale=25
        self.ship_speed=1.5
        self.bullet_speed=2.3
        self.alien_speed=1.0
        self.speed_scale=0.2
        self.alien_drop_speed=6.0
        self.ship_limit=3
        self.bullet_width=4
        self.bullet_height=13
        self.bullet_color=(60,60,60)
        self.alien_level_direction=1
        self.alien_vert_direction=1
    def initialize(self):
        self.alien_speed=1.0
        self.alien_level_direction=1
    def increase_speed(self):
        self.ship_speed+=self.speed_scale
        self.alien_speed+=self.speed_scale
        self.alien_drop_speed+=self.speed_scale
        self.point+=self.point_scale