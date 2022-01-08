class MatchResult:

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_scored = 0
        self.away_scored = 0

        self.goals = []
        self.events = []

    def add_goal(self, scorer, team, mins):
        self.goals.append({
            "scorer": scorer,
            "team": team,
            "mins": mins
        })

    def add_event(self, stuff):
        raise NotImplemented("Not Implemented Yet")
