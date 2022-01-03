import unittest
from game.player_stats import PlayerStats
from game.enums.stats_player import StatsPlayer
from game.enums.positions import Positions


class PlayerStatsTests(unittest.TestCase):

    def setUp(self):
        self.gk_stats = PlayerStats(20)
        self.gk_stats_with_modifiers = PlayerStats(20)

        self.outfield_stats = PlayerStats(20)
        self.outfield_stats_with_modifiers = PlayerStats(20)

        self.setup_gk(self.gk_stats)
        self.setup_gk(self.gk_stats_with_modifiers)
        self.add_gk_modifiers(self.gk_stats_with_modifiers)

        self.setup_outfield(self.outfield_stats)
        self.setup_outfield(self.outfield_stats_with_modifiers)
        self.add_outfield_modifiers(self.outfield_stats_with_modifiers)

    @staticmethod
    def setup_gk(stats):
        for stat_group in stats.base_stats:
            stat_score = 5
            if stat_group is StatsPlayer.GroupGK:
                stat_score = 10
            for stat in stats.base_stats[stat_group]:
                stats.base_stats[stat_group][stat] = stat_score

    @staticmethod
    def add_gk_modifiers(stats):
        for stat_group in stats.stat_modifiers:
            if stat_group is StatsPlayer.GroupGK:
                for stat in stats.stat_modifiers[stat_group]:
                    stats.stat_modifiers[stat_group][stat][StatsPlayer.ModifierAge] = -5

    @staticmethod
    def setup_outfield(stats):
        for stat_group in stats.base_stats:
            stat_score = 10
            if stat_group is StatsPlayer.GroupGK:
                stat_score = 5
            for stat in stats.base_stats[stat_group]:
                stats.base_stats[stat_group][stat] = stat_score

    @staticmethod
    def add_outfield_modifiers(stats):
        for stat_group in stats.stat_modifiers:
            if stat_group is not StatsPlayer.GroupGK:
                for stat in stats.stat_modifiers[stat_group]:
                    stats.stat_modifiers[stat_group][stat][StatsPlayer.ModifierAge] = -5

    def test_get_overall_score_gk_no_modifiers(self):
        self.assertEqual(10, self.gk_stats.get_overall_score(Positions.GK))

    def test_get_overall_score_outfield_no_modifiers(self):
        self.assertEqual(10, self.outfield_stats.get_overall_score(Positions.Forward))

    def test_get_overall_score_gk_with_modifiers(self):
        self.assertEqual(5, self.gk_stats_with_modifiers.get_overall_score(Positions.GK))

    def test_get_overall_score_outfield_with_modifiers(self):
        self.assertEqual(5, self.outfield_stats_with_modifiers.get_overall_score(Positions.Forward))


if __name__ == '__main__':
    unittest.main()
