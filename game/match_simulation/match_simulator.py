import time
from game.match_simulation.match_update import MatchUpdate


class MatchSimulator:

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0
        self.match_complete = False
        self.mins_to_play = 90
        self.half_time_at = 45
        self.mins_played = 0

    def step(self):
        # TODO Add more "dialog" options for the events
        # TODO Add icons to the events for the event type
        events = []
        # SOME FAKE EVENT STUFF TO TEST
        if self.mins_played == 10:
            self.home_score += 1
            events.append("Raymond scores a cracker")
        elif self.mins_played == 22:
            self.away_score += 1
            events.append("The away team evens up the scores")
        elif self.mins_played == 36:
            self.home_score += 1
            events.append("They've pulled ahead again, just before the break")
        elif self.mins_played == 51:
            self.home_score += 1
            events.append("The home team put another goal on the score sheet")
        elif self.mins_played == 66:
            events.append("He's been sent off!")
        elif self.mins_played == 73:
            self.away_score += 1
            events.append("The away team claw one back")
        elif self.mins_played == 84:
            self.home_score += 1
            events.append("That should put this game to bed")

        update = MatchUpdate(self.home_score, self.away_score, self.mins_played)
        for event in events:
            update.add_event(event)

        if self.mins_played == self.half_time_at:
            update.add_event("The players leave the pitch for half time.")
            self.mins_played += 1
            time.sleep(0.5)
        elif self.mins_played == self.half_time_at + 1:
            update.add_event("The players return for the second half.")
            self.mins_played += 1
            time.sleep(0.5)
        elif self.mins_played == self.mins_to_play:
            update.add_event("It's all over, the game ends {} {}, {} {}".format(
                self.home_team.name,
                self.home_score,
                self.away_team.name,
                self.away_score
            ))
            self.match_complete = True
        else:
            self.mins_played += 1
            time.sleep(0.5)

        return update
