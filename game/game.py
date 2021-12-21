from utils import get_place_data_from_file
from game.generators.league_generator import LeagueGenerator
from game.places import Places


class Game:

    def __init__(self):

        self.places = Places(get_place_data_from_file())
        league_gen = LeagueGenerator()
        self.leagues = league_gen.create_leagues(self.places)

        print("bla")

    def start_game(self):
        print("go")
