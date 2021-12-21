from utils import get_place_data_from_file
from game.generators.league_generator import LeagueGenerator
from game.places import Places


class Game:

    def __init__(self, debug):
        self.debug = debug
        self.places = Places(get_place_data_from_file())
        league_gen = LeagueGenerator()
        self.leagues = league_gen.create_leagues(self.places)

        if self.debug:
            for league in self.leagues["Scotland"]:
                print(league.name)
                print("")
                for team in league.teams:
                    print(team.name)
                print("")

            for league in self.leagues["England & Wales"]:
                print(league.name)
                print("")
                for team in league.teams:
                    print(team.name)
                print("")

    def start_game(self):
        print("go")
