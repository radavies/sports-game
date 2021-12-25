from PyQt6.QtCore import QObject, pyqtSignal
import time
from utils import get_place_data_from_file
from game.generators.league_generator import LeagueGenerator
from game.places import Places


class InitialiseNewGameTask(QObject):

    finished = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        places = Places(get_place_data_from_file())
        league_gen = LeagueGenerator()
        leagues = league_gen.create_leagues(places)
        self.finished.emit()

        #self.print_debug()


    # def print_debug(self):
    #     for league in self.leagues["Scotland"]:
    #         league_stat_avg = 0
    #         print(league.name)
    #         print("")
    #         for team in league.teams:
    #             print(team.name)
    #             league_stat_avg += self.get_team_average_stat(team)
    #         print("")
    #         print(round(league_stat_avg / len(league.teams)))
    #         print("")
    #
    #     for league in self.leagues["England & Wales"]:
    #         league_stat_avg = 0
    #         print(league.name)
    #         print("")
    #         for team in league.teams:
    #             print(team.name)
    #             league_stat_avg += self.get_team_average_stat(team)
    #         print("")
    #         print(round(league_stat_avg / len(league.teams)))
    #         print("")
    #
    #     for player in self.leagues["Scotland"][0].teams[0].players:
    #         print("{} - {} ({})".format(player, player.position.value, player.overall_stat_total()))
    #
    # @staticmethod
    # def get_team_average_stat(team):
    #     total = 0
    #     for player in team.players:
    #         total += player.overall_stat_total()
    #     return round(total / len(team.players))