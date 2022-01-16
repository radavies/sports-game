import time
import random
from game.teams_and_players.team_manager import TeamManager
from game.match_simulation.match_update import MatchUpdate
from game.match_simulation.match_result import MatchResult
from game.match_simulation.dialog import Dialog
from game.enums.misc import Misc
from game.enums.dialog_enum import DialogEnum


class MatchSimulator:

    # TODO The actual simulation
    # TODO Add more "dialog" options for the events

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

        self.home_team_manager = TeamManager(self.home_team)
        self.away_team_manager = TeamManager(self.away_team)
        self.home_squad = self.home_team_manager.build_match_squad()
        self.away_squad = self.away_team_manager.build_match_squad()

        self.home_scored = 0
        self.away_scored = 0
        self.match_complete = False
        self.mins_to_play = 90
        self.half_time_at = 45
        self.mins_played = 0
        self.result = MatchResult(home_team, away_team)
        self.dialog = Dialog()

    def quick_sim(self):
        # TODO The actual simulation
        while not self.match_complete:
            self.step(False)
        return self.result

    def step(self, do_pause):
        events = []

        # DO SIM
        update = MatchUpdate(self.home_scored, self.away_scored, self.mins_played)
        for event in events:
            update.add_event(event)

        if self.mins_played == 0:
            update.add_event(
                [Misc.KickOff.value, self.dialog.get_random_option_for_group(
                    DialogEnum.GroupKickOff,
                    None,
                    self.home_team,
                    self.away_team,
                    self.home_scored,
                    self.away_scored
                )]
            )
            self.mins_played += 1
        if self.mins_played == self.half_time_at:
            update.add_event(
                [Misc.FortyFiveMins.value, self.dialog.get_random_option_for_group(
                    DialogEnum.GroupFirstHalfEnd,
                    None,
                    self.home_team,
                    self.away_team,
                    self.home_scored,
                    self.away_scored
                )]
            )
            self.mins_played += 1
        elif self.mins_played == self.half_time_at + 1:
            update.add_event(
                [Misc.FortyFiveMins.value, self.dialog.get_random_option_for_group(
                    DialogEnum.GroupSecondHalfStart,
                    None,
                    self.home_team,
                    self.away_team,
                    self.home_scored,
                    self.away_scored
                )]
            )
            self.mins_played += 1
        elif self.mins_played == self.mins_to_play:
            update.add_event(
                    [Misc.NintyMins.value, self.dialog.get_random_option_for_group(
                        DialogEnum.GroupGameEnd,
                        None,
                        self.home_team,
                        self.away_team,
                        self.home_scored,
                        self.away_scored
                    )]
            )
            self.result.home_scored = self.home_scored
            self.result.away_scored = self.away_scored
            self.match_complete = True
        else:
            self.mins_played += 1

        if do_pause:
            time.sleep(Misc.SimPauseBetweenSteps.value)

        return update
