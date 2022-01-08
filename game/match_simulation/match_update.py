class MatchUpdate:

    def __init__(self, home_scored, away_scored, mins_played):
        self.home_scored = home_scored
        self.away_scored = away_scored
        self.mins_played = mins_played
        self.new_events = []

    def add_event(self, event):
        self.new_events.append(event)
