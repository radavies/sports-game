import names, random
from game.enums.positions import Positions
from game.player import Player


class PlayerGenerator:

    def generate_initial_squad_for_team(self):
        players = []

        # Generate Forwards
        for counter in range(0, 2):
            players.append(self.generate_player(Positions.Forward))
        # Generate Mid
        for counter in range(0, 5):
            players.append(self.generate_player(Positions.Midfielder))
        # Generate Def
        for counter in range(0, 5):
            players.append(self.generate_player(Positions.Defender))
        # Generate GKs
        for counter in range(0, 2):
            players.append(self.generate_player(Positions.GK))
        # Generate random subs
        for counter in range(0, 3):
            players.append(self.generate_player(None))

        return players

    @staticmethod
    def generate_player(position):
        if position is None:
            choice = random.randint(0, 3)
            if choice == 0:
                position = Positions.Forward
            if choice == 1:
                position = Positions.Midfielder
            if choice == 2:
                position = Positions.Defender
            if choice == 3:
                position = Positions.GK

        # this is purely to get the name generator to give a mix of names
        gender = "male"
        if random.randint(1, 100) <= 50:
            gender = "female"

        name_parts = names.get_full_name(gender).split(' ')

        name_last = name_parts[1]
        if len(name_parts) > 2:
            for counter in range(2, len(name_parts) - 1):
                name_last += " {}".format(name_parts[counter])

        return Player(name_parts[0], name_last, position)


