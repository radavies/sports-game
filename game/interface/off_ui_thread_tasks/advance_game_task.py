from PyQt6.QtCore import QObject, pyqtSignal
from utils import get_place_data_from_file
from game.generators.league_generator import LeagueGenerator
from game.places import Places
from game.league_management.leagues import Leagues


class AdvanceGameTask(QObject):

    finished = pyqtSignal()
    # league_signal = pyqtSignal(Leagues)
    # places_signal = pyqtSignal(Places)

    def __init__(self):
        super().__init__()

    def run(self):
        print("RUN")

        # TODO write the code to sim the fixtures for one match day
        #places = Places(get_place_data_from_file())
        #self.places_signal.emit(places)

        #league_gen = LeagueGenerator()
        #leagues = Leagues(league_gen.create_leagues(places))
        #self.league_signal.emit(leagues)

        self.finished.emit()
