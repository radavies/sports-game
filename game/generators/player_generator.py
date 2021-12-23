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
        new_player_stats = PlayerStats(age)

        league_modifier_percent = 0
        if league_rank == 1:
            league_modifier_percent = random.randint(1, 5)
        elif league_rank > 1:
            league_modifier_percent = random.randint(2, 15)

        for stat in new_player_stats.base_stats[StatsPlayer.GroupGK]:
            stat_score = self.remove_modifier_percentage_from_stat(random.randint(40, 100), league_modifier_percent)
            new_player_stats.base_stats[StatsPlayer.GroupGK][stat] = stat_score

        # Other stats should have lower base range
        for stat_group in new_player_stats.base_stats:
            if stat_group is StatsPlayer.GroupGK:
                continue

            for stat in new_player_stats.base_stats[stat_group]:
                # TODO - There are some stats in here like jumping and reactions the GK should get better base for
                stat_score = self.remove_modifier_percentage_from_stat(random.randint(10, 40), league_modifier_percent)
                new_player_stats.base_stats[StatsPlayer.GroupGK][stat] = stat_score

        self.generate_initial_modifiers(new_player_stats)
        return new_player_stats

    def generate_random_outfield_stats(self, age, position, league_rank):
        new_player_stats = PlayerStats(age)

        league_modifier_percent = 0
        if league_rank == 1:
            league_modifier_percent = random.randint(1, 5)
        elif league_rank > 1:
            league_modifier_percent = random.randint(2, 15)

        # Each position gets a main stat and one random other one
        main_stat_group = StatsPlayer.GroupShooting
        second_stat_group = None
        second_stat_group_options = [
            StatsPlayer.GroupShooting, StatsPlayer.GroupDefence, StatsPlayer.GroupMental,
            StatsPlayer.GroupPassing, StatsPlayer.GroupPhysical, StatsPlayer.GroupBallSkills
        ]

        if position is Positions.Forward:

        if position is Positions.Defender:
            main_stat_group = StatsPlayer.GroupDefence
        elif position is Positions.Midfielder:
            

        for stat in new_player_stats.base_stats[StatsPlayer.GroupGK]:
            stat_score = self.remove_modifier_percentage_from_stat(random.randint(40, 100), league_modifier_percent)
            new_player_stats.base_stats[StatsPlayer.GroupGK][stat] = stat_score

        # Other stats should have lower base range
        for stat_group in new_player_stats.base_stats:
            if stat_group is StatsPlayer.GroupGK:
                continue

            for stat in new_player_stats.base_stats[stat_group]:
                # TODO - There are some stats in here like jumping and reactions the GK should get better base for
                stat_score = self.remove_modifier_percentage_from_stat(random.randint(10, 40), league_modifier_percent)
                new_player_stats.base_stats[StatsPlayer.GroupGK][stat] = stat_score

        self.generate_initial_modifiers(new_player_stats)
        return new_player_stats

    def generate_initial_modifiers(self, new_player_stats):
        for stat_group in new_player_stats.stat_modifiers:
            for stat in new_player_stats.stat_modifiers[stat_group]:
                stat[StatsPlayer.ModifierAge] = self.get_age_modifier(new_player_stats.age)

    @staticmethod
    def remove_modifier_percentage_from_stat(stat, percentage):
        if percentage == 0:
            return stat
        modified = stat - (stat / 100 * percentage)
        return modified if modified > 0 else 1

    @staticmethod
    def get_age_modifier(age):
        if age <= 21:
            return 4
        elif 22 <= age <= 25:
            return 2
        elif 26 <= age <= 35:
            return 0
        elif 36 <= age <= 38:
            return -1
        else:
            return -2

