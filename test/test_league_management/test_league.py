import unittest
from game.league_management.league import League
from game.team import Team
from game.sponsor import Sponsor


class LeagueTests(unittest.TestCase):

    def test_str(self):
        sponsor = Sponsor("Hello")
        league = League("World", "Scotland", "{} World", 0, 2, 18, sponsor)
        self.assertEqual(str(league), "Hello World")

    def test_add_team_to_league(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        test_number = 18
        for x in range(0, test_number):
            league.add_team_to_league(Team(str(x), None, None, league.name))

        self.assertEqual(test_number, len(league.teams))
        self.assertEqual(test_number, len(league.table))


if __name__ == '__main__':
    unittest.main()
