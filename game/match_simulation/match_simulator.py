import time
from game.match_simulation.match_update import MatchUpdate
from game.match_simulation.match_result import MatchResult


class MatchSimulator:

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_scored = 0
        self.away_scored = 0
        self.match_complete = False
        self.mins_to_play = 90
        self.half_time_at = 45
        self.mins_played = 0
        self.result = MatchResult(home_team, away_team)

    def quick_sim(self):
        # TODO The actual simulation
        import random
        self.home_scored = random.randint(0, 5)
        self.away_scored = random.randint(0, 5)
        self.result.home_scored = self.home_scored
        self.result.away_scored = self.away_scored
        return self.result

    def step(self):
        # TODO The actual simulation
        # TODO Add more "dialog" options for the events
        # TODO Add icons to the events for the event type
        events = []
        # SOME FAKE EVENT STUFF TO TEST
        if self.mins_played == 10:
            self.home_scored += 1
            events.append("Raymond scores a cracker")
            self.result.add_goal(self.home_team.players[0], self.home_team, self.mins_played)
        elif self.mins_played == 22:
            self.away_scored += 1
            events.append("The away team evens up the scores")
            self.result.add_goal(self.away_team.players[0], self.away_team, self.mins_played)
        elif self.mins_played == 36:
            self.home_scored += 1
            events.append("They've pulled ahead again, just before the break")
            self.result.add_goal(self.home_team.players[0], self.home_team, self.mins_played)
        elif self.mins_played == 51:
            self.home_scored += 1
            events.append("The home team put another goal on the score sheet")
            self.result.add_goal(self.home_team.players[0], self.home_team, self.mins_played)
        elif self.mins_played == 66:
            events.append("He's been sent off!")
        elif self.mins_played == 73:
            self.away_scored += 1
            events.append("The away team claw one back")
            self.result.add_goal(self.away_team.players[0], self.away_team, self.mins_played)
        elif self.mins_played == 84:
            self.home_scored += 1
            events.append("That should put this game to bed")
            self.result.add_goal(self.home_team.players[0], self.home_team, self.mins_played)

        update = MatchUpdate(self.home_scored, self.away_scored, self.mins_played)
        for event in events:
            update.add_event(event)

        if self.mins_played == self.half_time_at:
            update.add_event("The players leave the pitch for half time.")
            self.mins_played += 1
        elif self.mins_played == self.half_time_at + 1:
            update.add_event("The players return for the second half.")
            self.mins_played += 1
        elif self.mins_played == self.mins_to_play:
            update.add_event("It's all over, the game ends {} {}, {} {}".format(
                self.home_team.name,
                self.home_scored,
                self.away_team.name,
                self.away_scored
            ))
            self.result.home_scored = self.home_scored
            self.result.away_scored = self.away_scored
            self.match_complete = True
        else:
            self.mins_played += 1

        time.sleep(0.2)

        return update
