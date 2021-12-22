import names, random
from game.enums.positions import Positions
from game.player import Player
from game.player_stats import PlayerStats
from game.enums.stats_player import StatsPlayer

class PlayerGenerator:

    def generate_initial_squad_for_team(self, league_rank):
        players = []

        # Generate Forwards
        for counter in range(0, 2):
            players.append(self.generate_player(Positions.Forward, league_rank))
        # Generate Mid
        for counter in range(0, 5):
            players.append(self.generate_player(Positions.Midfielder, league_rank))
        # Generate Def
        for counter in range(0, 5):
            players.append(self.generate_player(Positions.Defender, league_rank))
        # Generate GKs
        for counter in range(0, 2):
            players.append(self.generate_player(Positions.GK, league_rank))
        # Generate random subs
        for counter in range(0, 3):
            players.append(self.generate_player(None, league_rank))

        return players

    def generate_player(self, position, league_rank):
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

        return Player(name_parts[0], name_last, position, self.generate_random_stats(position, league_rank))

    def generate_random_stats(self, position, league_rank):
        age = random.randint(16, 30)

        if position.GK:
            return self.generate_random_gk_stats(age, league_rank)
        else:
            return self.generate_random_outfield_stats(age, position, league_rank)

    def generate_random_gk_stats(self, age, league_rank):
        new_player = PlayerStats(age)

        for stat in new_player.base_stats[StatsPlayer.GroupGK]:
            # TODO - base stat range based on league rank
            # TODO - Also set up the modifiers based on age
            stat_score = random.randint()
            new_player.base_stats[StatsPlayer.GroupGK][stat] =

    def generate_random_outfield_stats(self, age, position, league_rank):
        return PlayerStats(age)
