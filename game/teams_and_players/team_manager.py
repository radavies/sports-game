from game.enums.positions import Positions
from game.teams_and_players.formations import Formations


class TeamManager:

    def __init__(self, team):
        self.defenders = []
        self.midfielders = []
        self.forwards = []
        self.gks = []

        self.formations = Formations()

        for player in team.players:
            if player.position == Positions.GK:
                self.gks.append(player)
            elif player.position == Positions.Defender:
                self.defenders.append(player)
            elif player.position == Positions.Midfielder:
                self.midfielders.append(player)
            elif player.position == Positions.Forward:
                self.forwards.append(player)

        # Sort them best at the end as we pop them off later
        self.defenders.sort()
        self.midfielders.sort()
        self.forwards.sort()
        self.gks.sort()

        self.positions = {
            Positions.Defender.value: self.defenders,
            Positions.Midfielder.value: self.midfielders,
            Positions.Forward.value: self.forwards,
            Positions.GK.value: self.gks
        }

        self.viable_formations = self.get_viable_formations()

    def build_match_squad(self):
        # TODO what happens if we can't build a squad for some reason?
        gk = self.select_gk()


    def select_gk(self):
        if len(self.gks) > 0:
            return self.gks.pop()
        else:
            # Take the worst player from the position with most players left
            position = self.get_position_with_most_players()
            if position is not None:
                return position.pop(0)
            else:
                return None

    def get_position_with_most_players(self):
        longest = None
        length = 0
        for key in self.positions:
            if len(self.positions[key]) > length:
                longest = key
                length = len(self.positions[key])

        if longest is not None:
            return self.positions[longest]
        else:
            return None

    def get_viable_formations(self):
        viable_formations = {
            "full_match": [],
            "part_match": []
        }

        for formation_key in self.formations.formations:
            formation = self.formations.formations[formation_key]
            matches = 0
            for position_key in formation:
                if len(self.positions[position_key]) >= formation[position_key]:
                    matches += 1

            if matches == 3:
                viable_formations["full_match"].append(formation_key)
            elif matches > 0:
                viable_formations["part_match"].append(formation_key)

        return viable_formations
