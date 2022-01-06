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
from game.interface.off_ui_thread_tasks.initialise_new_game_task import InitialiseNewGameTask
from game.interface.off_ui_thread_tasks.advance_game_task import AdvanceGameTask
from game.interface.intro_window import IntroWindow
from game.interface.main_window import MainWindow


class Game:

    def __init__(self, debug):

        # Main Game Objects
        self.debug = debug
        self.places = None
        self.leagues = None

        # Player Selected Game Objects
        self.current_selected_team = None
        self.current_teams_league = None

        # UI Windows
        self.start_window = None
        self.loading_window = None
        self.select_team_window = None
        self.intro_window = None
        self.main_window = None

        # Threads & Worker Tasks
        self.game_set_up_thread = None
        self.new_game_task = None

        self.advance_game_thread = None
        self.advance_game_task = None

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
        returned = self.leagues.find_team_and_league(team_name)
        self.current_selected_team = returned["team"]
        self.current_teams_league = returned["league"]

        self.leagues.generate_fixtures_for_leagues(self.current_selected_team)

        self.select_team_window.close()

        self.intro_window = IntroWindow(
            self.current_selected_team.name,
            self.current_selected_team.current_league_name,
            self.intro_continue)

        self.intro_window.show()

    def intro_continue(self):
        self.intro_window.close()
        self.main_window = MainWindow(self.current_teams_league, self.current_selected_team, self.advance_the_game)
        self.main_window.showMaximized()

    def advance_the_game(self):
        self.advance_game_thread = QtCore.QThread()
        self.advance_game_task = AdvanceGameTask()
        self.advance_game_task.moveToThread(self.advance_game_thread)

        self.advance_game_thread.started.connect(self.advance_game_task.run)
        self.advance_game_task.finished.connect(self.advance_game_thread.quit)
        self.advance_game_thread.finished.connect(self.main_window.enable_advance_button)

        # self.new_game_task.places_signal.connect(self.update_places)
        # self.new_game_task.league_signal.connect(self.update_leagues)

        self.advance_game_thread.start()

    def debug_jumper(self):
        # DEBUG METHOD TO JUMP TO SPECIFIC POINTS
        print("beep")
