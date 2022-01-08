class MatchUpdate:

    def __init__(self, home_score, away_score, mins_played):
        self.home_score = home_score
        self.away_score = away_score
        self.mins_played = mins_played
        self.new_events = []

    def add_event(self, event):
        self.new_events.append(event)
