class Team:

    def __init__(self, name, place, squad, league_name):
        self.name = name
        self.place = place
        self.players = squad
        self.current_league_name = league_name

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name
