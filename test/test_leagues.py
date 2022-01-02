import unittest
from game.leagues import Leagues
from game.league import League
from game.team import Team


class LeaguesTests(unittest.TestCase):

    def setUp(self):

        league_one = League("League One", "Scotland", "{} League One", 0, 2, 18, None)
        team_one = Team("Team 1", None, None, "Test")
        team_two = Team("Team 2", None, None, "Test")
        team_three = Team("Team 3", None, None, "Test")
        league_one.teams.append(team_one)
        league_one.teams.append(team_two)
        league_one.teams.append(team_three)

        league_two = League("League Two", "Scotland", "{} League Two", 0, 2, 18, None)
        team_four = Team("Team 4", None, None, "Test")
        team_five = Team("Team 5", None, None, "Test")
        team_six = Team("Team 6", None, None, "Test")
        league_two.teams.append(team_four)
        league_two.teams.append(team_five)
        league_two.teams.append(team_six)

        league_three = League("League Three", "England & Wales", "{} League Three", 0, 2, 18, None)
        team_seven = Team("Team 7", None, None, "Test")
        team_eight = Team("Team 8", None, None, "Test")
        team_nine = Team("Team 9", None, None, "Test")
        league_three.teams.append(team_seven)
        league_two.teams.append(team_eight)
        league_two.teams.append(team_nine)

        leagues_obj = {
            "Scotland": [league_one, league_two],
            "England & Wales": [league_three]
        }

        self.leagues = Leagues(leagues_obj)

    def test_two_leagues_in_country_first_league(self):
        returned = self.leagues.find_team_and_league("Team 2")
        self.assertEqual(returned["team"].name, "Team 2")
        self.assertEqual(returned["league"].name, "League One")

    def test_two_leagues_in_country_second_league(self):
        returned = self.leagues.find_team_and_league("Team 6")
        self.assertEqual(returned["team"].name, "Team 6")
        self.assertEqual(returned["league"].name, "League Two")

    def test_one_leagues_in_country(self):
        returned = self.leagues.find_team_and_league("Team 7")
        self.assertEqual(returned["team"].name, "Team 7")
        self.assertEqual(returned["league"].name, "League Three")


if __name__ == '__main__':
    unittest.main()
