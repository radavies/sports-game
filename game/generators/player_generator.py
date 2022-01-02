import names
import random
from game.enums.positions import Positions
from game.player import Player
from game.player_stats import PlayerStats
from game.enums.stats_player import StatsPlayer


class PlayerGenerator:

    def __init__(self):
        self.stat_range_low_off_stat = 10
        self.stat_range_high_off_stat = 30

        self.stat_range_low_mid_stat = 40
        self.stat_range_high_mid_stat = 75

        self.stat_range_low_good_stat = 45
        self.stat_range_high_good_stat = 100

    def generate_initial_squad_for_team(self, league_rank):
        players = []

        # Generate Forwards
        for counter in range(0, 2):
            players.append(self._generate_player(Positions.Forward, league_rank))
        # Generate Mid
        for counter in range(0, 5):
            players.append(self._generate_player(Positions.Midfielder, league_rank))
        # Generate Def
        for counter in range(0, 5):
            players.append(self._generate_player(Positions.Defender, league_rank))
        # Generate GKs
        for counter in range(0, 2):
            players.append(self._generate_player(Positions.GK, league_rank))
        # Generate random subs
        for counter in range(0, 3):
            players.append(self._generate_player(None, league_rank))

        return players

    def _generate_player(self, position, league_rank):
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

        return Player(name_parts[0], name_last, position, self._generate_random_stats(position, league_rank))

    def _generate_random_stats(self, position, league_rank):
        age = random.randint(16, 30)

        if position is Positions.GK:
            return self._generate_random_gk_stats(age, league_rank)
        else:
            return self._generate_random_outfield_stats(age, position, league_rank)

    def _generate_random_gk_stats(self, age, league_rank):
        new_player_stats = PlayerStats(age)

        league_modifier_percent = 0
        if league_rank == 1:
            league_modifier_percent = random.randint(1, 5)
        elif league_rank > 1:
            league_modifier_percent = random.randint(2, 15)

        for stat in new_player_stats.base_stats[StatsPlayer.GroupGK]:
            stat_score = self._remove_modifier_percentage_from_stat(random.randint(
                self.stat_range_low_good_stat,
                self.stat_range_high_good_stat),
                league_modifier_percent
            )
            new_player_stats.base_stats[StatsPlayer.GroupGK][stat] = stat_score

        # Other stats should have lower base range
        for stat_group in new_player_stats.base_stats:
            if stat_group is StatsPlayer.GroupGK:
                continue

            for stat in new_player_stats.base_stats[stat_group]:
                # TODO - There are some stats in here like jumping and reactions the GK should get better base for
                stat_score = self._remove_modifier_percentage_from_stat(
                    random.randint(self.stat_range_low_off_stat, self.stat_range_high_off_stat),
                    league_modifier_percent
                )
                new_player_stats.base_stats[stat_group][stat] = stat_score

        self._generate_initial_modifiers(new_player_stats)
        return new_player_stats

    def _generate_random_outfield_stats(self, age, position, league_rank):
        new_player_stats = PlayerStats(age)

        league_modifier_percent = 0
        if league_rank == 1:
            league_modifier_percent = random.randint(1, 5)
        elif league_rank > 1:
            league_modifier_percent = random.randint(2, 15)

        # Each position gets a main stat and one random other one
        # Midfield gets two random
        main_stat_group = StatsPlayer.GroupShooting
        second_stat_group = None
        if position is Positions.Forward:
            second_stat_group = self._pick_random_stat(main_stat_group)
        if position is Positions.Defender:
            main_stat_group = StatsPlayer.GroupDefence
            second_stat_group = self._pick_random_stat(main_stat_group)
        elif position is Positions.Midfielder:
            main_stat_group = self._pick_random_stat(None)
            second_stat_group = self._pick_random_stat(main_stat_group)

        for stat_group in new_player_stats.base_stats:
            stat_range_low = self.stat_range_low_mid_stat
            stat_range_high = self.stat_range_high_mid_stat
            if stat_group is main_stat_group or stat_group is second_stat_group:
                stat_range_low = self.stat_range_low_good_stat
                stat_range_high = self.stat_range_high_good_stat
            elif stat_group is StatsPlayer.GroupGK:
                stat_range_low = 1
                stat_range_high = 10

            for stat in new_player_stats.base_stats[stat_group]:
                stat_score = self._remove_modifier_percentage_from_stat(
                    random.randint(stat_range_low, stat_range_high),
                    league_modifier_percent
                )
                new_player_stats.base_stats[stat_group][stat] = stat_score

        self._generate_initial_modifiers(new_player_stats)
        return new_player_stats

    def _generate_initial_modifiers(self, new_player_stats):
        for stat_group in new_player_stats.stat_modifiers:
            for stat in new_player_stats.stat_modifiers[stat_group]:
                new_player_stats.stat_modifiers[stat_group][stat][StatsPlayer.ModifierAge] = self._get_age_modifier(
                    new_player_stats.age
                )

    @staticmethod
    def _remove_modifier_percentage_from_stat(stat, percentage):
        if percentage == 0:
            return stat
        modified = stat - (stat / 100 * percentage)
        return modified if modified > 0 else 1

    @staticmethod
    def _get_age_modifier(age):
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

    @staticmethod
    def _pick_random_stat(dont_match):
        second_stat_group_options = [
            StatsPlayer.GroupShooting, StatsPlayer.GroupDefence, StatsPlayer.GroupMental,
            StatsPlayer.GroupPassing, StatsPlayer.GroupPhysical, StatsPlayer.GroupBallSkills
        ]
        random_stat = dont_match
        while random_stat is dont_match:
            stat_choice = random.randint(0, len(second_stat_group_options) - 1)
            random_stat = second_stat_group_options[stat_choice]
        return random_stat
