import unittest
from game.team import Team


class TeamTests(unittest.TestCase):

    def test_str(self):
        team = Team("Test", None, None, None)
        self.assertEqual(str(team), "Test")

    def test_less_than(self):
        team_a = Team("Test A", None, None, None)
        team_b = Team("Test B", None, None, None)
        team_c = Team("Test C", None, None, None)
        team_d = Team("Test D", None, None, None)

        ordered_list = [team_a, team_b, team_c, team_d]
        team_list = [team_c, team_b, team_d, team_a]
        team_list.sort()

        for x in range(0, len(team_list)):
            self.assertEqual(ordered_list[x], team_list[x])


if __name__ == '__main__':
    unittest.main()
