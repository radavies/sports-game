import time
from PyQt6.QtCore import QObject, pyqtSignal
from game.match_simulation.match_update import MatchUpdate
from game.match_simulation.match_start import MatchStart
from game.match_simulation.match_simulator import MatchSimulator


class AdvanceGameTask(QObject):

    finished = pyqtSignal()
    match_update_signal = pyqtSignal(MatchUpdate)
    match_start_signal = pyqtSignal(MatchStart)

    def __init__(self, leagues, currently_selected_team, currently_selected_league):
        super().__init__()
        self.leagues = leagues
        self.currently_selected_team = currently_selected_team
        self.currently_selected_league = currently_selected_league

    def run(self):

        for country in self.leagues.leagues:
            for league in self.leagues.leagues[country]:
                if league.name == self.currently_selected_league.name:
                    self.simulate_match_day(league.get_next_match_day(), league)
                    league.advance_to_next_match_day()

        self.finished.emit()

    def simulate_match_day(self, match_day, league):
        for fixture in match_day:
            if fixture[0] == self.currently_selected_team or fixture[1] == self.currently_selected_team:
                self.match_start_signal.emit(MatchStart(league, fixture[0], fixture[1]))
                time.sleep(0.5)
                self.fully_simulate_fixture(fixture)

    def fully_simulate_fixture(self, fixture):
        match_sim = MatchSimulator(fixture[0], fixture[1])

        while not match_sim.match_complete:
            update = match_sim.step()
            self.match_update_signal.emit(update)
