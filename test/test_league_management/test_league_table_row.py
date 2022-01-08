import unittest
from game.league_management.league_table_row import LeagueTableRow
from game.team import Team


class LeagueTableRowTests(unittest.TestCase):

    def setUp(self):
        self.team = Team("Test Team", None, None, None)
        self.other_team = Team("X Test", None, None, None)

    def test_points(self):
        row = LeagueTableRow(self.team, 7, 1, 2, 4, 4, 8)
        self.assertEqual(5, row.points())

    def test_goal_difference_neg(self):
        row = LeagueTableRow(self.team, 7, 1, 2, 4, 5, 8)
        self.assertEqual(-3, row.goal_difference())

    def test_goal_difference_pos(self):
        row = LeagueTableRow(self.team, 7, 1, 2, 4, 10, 4)
        self.assertEqual(6, row.goal_difference())

    def test_lt_points(self):
        row = LeagueTableRow(self.team, 2, 1, 1, 0, 4, 2)
        other = LeagueTableRow(self.other_team, 2, 0, 1, 1, 2, 4)
        self.assertTrue(row.__lt__(other))

    def test_lt_gd(self):
        row = LeagueTableRow(self.team, 2, 1, 1, 0, 4, 2)
        other = LeagueTableRow(self.other_team, 2, 1, 1, 0, 2, 4)
        self.assertTrue(row.__lt__(other))

    def test_lt_gf(self):
        row = LeagueTableRow(self.team, 2, 1, 1, 0, 10, 5)
        other = LeagueTableRow(self.other_team, 2, 1, 1, 0, 5, 0)
        self.assertTrue(row.__lt__(other))

    def test_lt_won(self):
        row = LeagueTableRow(self.team, 3, 1, 0, 2, 1, 1)
        other = LeagueTableRow(self.other_team, 3, 0, 3, 0, 1, 1)
        self.assertTrue(row.__lt__(other))

    def test_lt_alpha(self):
        row = LeagueTableRow(self.team, 3, 1, 0, 2, 1, 1)
        other = LeagueTableRow(self.other_team, 3, 1, 0, 2, 1, 1)
        self.assertTrue(row.__lt__(other))


if __name__ == '__main__':
    unittest.main()
