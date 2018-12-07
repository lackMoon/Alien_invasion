class GameStats():
    def __init__(self,game_settings):
        self.game_settings=game_settings
        self.ships_left = self.game_settings.ship_limit
        self.game_active=False
        self.score=0
        self.high_score=0

    def reset_stats(self):
        self.ships_left=self.game_settings.ship_limit
        self.score=0