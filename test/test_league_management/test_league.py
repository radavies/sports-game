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

    def test_is_in_promo_zone_no_above_league_not_first(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        self.assertEqual(False, league.is_in_promo_zone(3))

    def test_is_in_promo_zone_no_above_league_is_first(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        self.assertEqual(True, league.is_in_promo_zone(1))

    def test_is_in_promo_zone_has_above_league_is_first(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        league.set_league_above(league)
        self.assertEqual(True, league.is_in_promo_zone(1))

    def test_is_in_promo_zone_has_above_league_is_last_promo_spot(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        league.set_league_above(league)
        self.assertEqual(True, league.is_in_promo_zone(2))

    def test_is_in_promo_zone_has_above_league_is_not_in_promo_spot(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        league.set_league_above(league)
        self.assertEqual(False, league.is_in_promo_zone(3))

    def test_is_in_relegation_zone_no_demotion_is_last(self):
        league = League("World", "Scotland", "{} World", 0, 0, 18, None)
        self.assertEqual(True, league.is_in_relegation_zone(18))

    def test_is_in_relegation_zone_no_demotion_is_not_last(self):
        league = League("World", "Scotland", "{} World", 0, 0, 18, None)
        self.assertEqual(False, league.is_in_relegation_zone(17))

    def test_is_in_relegation_zone_has_demotion_is_last(self):
        league = League("World", "Scotland", "{} World", 0, 3, 18, None)
        self.assertEqual(True, league.is_in_relegation_zone(18))

    def test_is_in_relegation_zone_has_demotion_in_last_demotion_spot(self):
        league = League("World", "Scotland", "{} World", 0, 3, 18, None)
        self.assertEqual(True, league.is_in_relegation_zone(16))

    def test_is_in_relegation_zone_has_demotion_not_in_demotion_zone(self):
        league = League("World", "Scotland", "{} World", 0, 3, 18, None)
        self.assertEqual(False, league.is_in_relegation_zone(15))


if __name__ == '__main__':
    unittest.main()
