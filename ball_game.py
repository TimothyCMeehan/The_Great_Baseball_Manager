class Ball_game:
    def __init__(self, home_team, away_team):
        self.__innings = []
        self.__base_path = []
        self.__home_team = home_team
        self.__home_on_deck = None
        self.__away_team = away_team
        self.__away_on_deck = None
