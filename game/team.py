class Team:

    def __init__(self, name, place, squad):
        self.name = name
        self.place = place
        self.players = squad

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name

