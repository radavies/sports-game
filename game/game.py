import sys
import ctypes
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from pathlib import Path
from game.enums.misc import Misc
from game.interface.start_window import StartWindow
from game.interface.loading_window import LoadingWindow
from game.interface.select_team_window import SelectTeamWindow
from game.interface.initialise_new_game_task import InitialiseNewGameTask
from game.interface.intro_window import IntroWindow
from game.interface.main_window import MainWindow


class Game:

    def __init__(self, debug):
        self.debug = debug
        self.places = None
        self.leagues = None
        self.selected_team = None

        # UI Windows
        self.start_window = None
        self.loading_window = None
        self.select_team_window = None
        self.intro_window = None
        self.main_window = None

        # Threads & Worker Tasks
        self.game_set_up_thread = None
        self.new_game_task = None

    def start_game(self):
        app = QApplication(sys.argv)
        app.setApplicationName(Misc.GameName.value)

        folder = Path(Misc.DataFolderPath.value)
        icon_file = folder / Misc.IconFileName.value
        app.setWindowIcon(QIcon(str(icon_file)))

        if hasattr(ctypes, 'windll'):
            app_id = "sports-game"
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

        css_file = folder / Misc.CSSFileName.value
        app.setStyleSheet(open(css_file).read())

        if not self.debug:
            self.start_window = StartWindow(self.new_game_button_event)
            self.start_window.show()
        else:
            self.debug_jumper()

        sys.exit(app.exec())

    def new_game_button_event(self):
        self.start_window.close()
        self.loading_window = LoadingWindow()
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

    def after_game_set_up(self):
        self.loading_window.close()
        self.select_team_window = SelectTeamWindow(self.leagues, self.team_selected)
        self.select_team_window.show()

    def team_selected(self, team_name):
        self.selected_team = team_name
        self.select_team_window.close()
        team = self.leagues.find_team(team_name)
        self.intro_window = IntroWindow(team.name, team.current_league_name, self.intro_continue)
        self.intro_window.show()

    def intro_continue(self):
        self.main_window = MainWindow()
        self.main_window.showMaximized()

    def debug_jumper(self):
        # DEBUG METHOD TO JUMP TO SPECIFIC POINTS
        self.intro_continue()
