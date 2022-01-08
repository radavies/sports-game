class LeagueTableRow:

    def __init__(self, team, played, won, drawn, lost, goals_for, goals_against):
        self.team = team
        self.played = played
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.goals_for = goals_for
        self.goals_against = goals_against

    def points(self):
        return (3 * self.won) + (1 * self.drawn)

    def goal_difference(self):
        return self.goals_for - self.goals_against

    def __lt__(self, other):
        if self.points() == other.points():
            if self.goal_difference() == other.goal_difference():
                if self.goals_for == other.goals_for:
                    if self.won == other.won:
                        return self.team.name < other.team.name
                    return self.won > other.won
                return self.goals_for > other.goals_for
            return self.goal_difference() > other.goal_difference()
        return self.points() > other.points()
