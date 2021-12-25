import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from pathlib import Path
from game.enums.misc import Misc
from game.interface.start_window import StartWindow
from game.interface.loading_window import LoadingWindow
from game.interface.select_team_window import SelectTeamWindow
from game.interface.initialise_new_game_task import InitialiseNewGameTask


class Game:

    def __init__(self, debug):
        self.debug = debug
        self.places = None
        self.leagues = None

        # UI Windows
        self.start_window = None
        self.loading_window = None
        self.select_team_window = None

        # Threads & Worker Tasks
        self.game_set_up_thread = None
        self.new_game_task = None

    def start_game(self):
        app = QApplication(sys.argv)
        app.setApplicationName(Misc.GameName.value)

        folder = Path(Misc.DataFolderPath.value)
        icon_file = folder / Misc.IconFileName.value
        app.setWindowIcon(QIcon(str(icon_file)))

        css_file = folder / Misc.CSSFileName.value
        app.setStyleSheet(open(css_file).read())

        self.loading_window = LoadingWindow()

        self.start_window = StartWindow(self.new_game_button_event)
        self.start_window.show()

        sys.exit(app.exec())

    def new_game_button_event(self):
        self.start_window.close()
        self.loading_window.show()

        self.game_set_up_thread = QtCore.QThread()
        self.new_game_task = InitialiseNewGameTask()
        self.new_game_task.moveToThread(self.game_set_up_thread)

        self.game_set_up_thread.started.connect(self.new_game_task.run)
        self.new_game_task.finished.connect(self.game_set_up_thread.quit)
        self.game_set_up_thread.finished.connect(self.after_game_set_up)

        self.new_game_task.places_signal.connect(self.update_places)
        self.new_game_task.league_signal.connect(self.update_leagues)

        self.game_set_up_thread.start()

    def update_places(self, places_in):
        self.places = places_in

    def update_leagues(self, leagues_in):
        self.leagues = leagues_in
        self.print_debug()

    def after_game_set_up(self):
        self.loading_window.close()

        self.select_team_window = SelectTeamWindow(self.leagues)
        self.select_team_window.show()

    def print_debug(self):
        for league in self.leagues.leagues["Scotland"]:
            league_stat_avg = 0
            print(league.name)
            print("")
            for team in league.teams:
                league_stat_avg += self.get_team_average_stat(team)
            print(round(league_stat_avg / len(league.teams)))
            print("")

        for league in self.leagues.leagues["England & Wales"]:
            league_stat_avg = 0
            print(league.name)
            print("")
            for team in league.teams:
                league_stat_avg += self.get_team_average_stat(team)
            print(round(league_stat_avg / len(league.teams)))
            print("")

        for player in self.leagues.leagues["Scotland"][0].teams[0].players:
            print("{} - {} ({})".format(player, player.position.value, player.overall_stat_total()))

    @staticmethod
    def get_team_average_stat(team):
        total = 0
        for player in team.players:
            total += player.overall_stat_total()
        return round(total / len(team.players))
