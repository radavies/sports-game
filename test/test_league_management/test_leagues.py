import unittest
from game.league_management.leagues import Leagues
from game.league_management.league import League
from game.team import Team


class LeaguesTests(unittest.TestCase):

    def setUp(self):

        league_one = League("League One", "Scotland", "{} League One", 0, 2, 18, None)
        team_one = Team("Team 1", None, None, "Test")
        team_two = Team("Team 2", None, None, "Test")
        team_three = Team("Team 3", None, None, "Test")
        league_one.add_team_to_league(team_one)
        league_one.add_team_to_league(team_two)
        league_one.add_team_to_league(team_three)

        league_two = League("League Two", "Scotland", "{} League Two", 0, 2, 18, None)
        team_four = Team("Team 4", None, None, "Test")
        team_five = Team("Team 5", None, None, "Test")
        team_six = Team("Team 6", None, None, "Test")
        league_two.add_team_to_league(team_four)
        league_two.add_team_to_league(team_five)
        league_two.add_team_to_league(team_six)

        league_three = League("League Three", "England & Wales", "{} League Three", 0, 2, 18, None)
        team_seven = Team("Team 7", None, None, "Test")
        team_eight = Team("Team 8", None, None, "Test")
        team_nine = Team("Team 9", None, None, "Test")
        league_three.add_team_to_league(team_seven)
        league_two.add_team_to_league(team_eight)
        league_two.add_team_to_league(team_nine)

        leagues_obj = {
            "Scotland": [league_one, league_two],
            "England & Wales": [league_three]
        }

        self.leagues = Leagues(leagues_obj)

    def test_two_leagues_in_country_first_league(self):
        returned = self.leagues.find_team_and_league("Team 2")
        self.assertEqual("Team 2", returned["team"].name)
        self.assertEqual("League One", returned["league"].name)

    def test_two_leagues_in_country_second_league(self):
        returned = self.leagues.find_team_and_league("Team 6")
        self.assertEqual("Team 6", returned["team"].name)
        self.assertEqual("League Two", returned["league"].name)

    def test_one_leagues_in_country(self):
        returned = self.leagues.find_team_and_league("Team 7")
        self.assertEqual("Team 7", returned["team"].name)
        self.assertEqual("League Three", returned["league"].name)


if __name__ == '__main__':
    unittest.main()
