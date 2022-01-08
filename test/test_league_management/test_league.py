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
        self.assertEqual(test_number, len(league.league_table_rows))

    def test_is_in_promo_zone_no_above_league_not_first(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        self.assertFalse(league.is_in_promo_zone(3))

    def test_is_in_promo_zone_no_above_league_is_first(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        self.assertTrue(league.is_in_promo_zone(1))

    def test_is_in_promo_zone_has_above_league_is_first(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        league.set_league_above(league)
        self.assertTrue(league.is_in_promo_zone(1))

    def test_is_in_promo_zone_has_above_league_is_last_promo_spot(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        league.set_league_above(league)
        self.assertTrue(league.is_in_promo_zone(2))

    def test_is_in_promo_zone_has_above_league_is_not_in_promo_spot(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        league.set_league_above(league)
        self.assertFalse(league.is_in_promo_zone(3))

    def test_is_in_relegation_zone_no_demotion_is_last(self):
        league = League("World", "Scotland", "{} World", 0, 0, 18, None)
        self.assertTrue(league.is_in_relegation_zone(18))

    def test_is_in_relegation_zone_no_demotion_is_not_last(self):
        league = League("World", "Scotland", "{} World", 0, 0, 18, None)
        self.assertFalse(league.is_in_relegation_zone(17))

    def test_is_in_relegation_zone_has_demotion_is_last(self):
        league = League("World", "Scotland", "{} World", 0, 3, 18, None)
        self.assertTrue(league.is_in_relegation_zone(18))

    def test_is_in_relegation_zone_has_demotion_in_last_demotion_spot(self):
        league = League("World", "Scotland", "{} World", 0, 3, 18, None)
        self.assertTrue(league.is_in_relegation_zone(16))

    def test_is_in_relegation_zone_has_demotion_not_in_demotion_zone(self):
        league = League("World", "Scotland", "{} World", 0, 3, 18, None)
        self.assertFalse(league.is_in_relegation_zone(15))

    def test_get_next_fixture_for_team_no_fixtures(self):
        league = League("World", "Scotland", "{} World", 0, 3, 18, None)
        self.assertIsNone(league.get_next_fixture_for_team(Team("Test", None, None, league.name)))

    def test_get_next_fixture_for_team_not_in_next_match_day(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        test_number = 18
        for x in range(0, test_number):
            league.add_team_to_league(Team(str(x), None, None, league.name))
        league.generate_fixtures()
        self.assertIsNone(league.get_next_fixture_for_team(Team("Test", None, None, league.name)))

    def test_get_next_fixture_for_team_home(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        test_number = 18
        the_team = None
        for x in range(0, test_number):
            new_team = Team(str(x), None, None, league.name)
            if the_team is None:
                the_team = new_team
            league.add_team_to_league(new_team)

        league.generate_fixtures_with_chosen_team(the_team)

        fixture = league.get_next_fixture_for_team(the_team)
        self.assertIsNotNone(fixture)
        self.assertEqual(the_team, fixture[0])

    def test_get_next_fixture_for_team_away(self):
        league = League("World", "Scotland", "{} World", 0, 2, 18, None)
        test_number = 18
        the_team = None
        for x in range(0, test_number):
            new_team = Team(str(x), None, None, league.name)
            if the_team is None:
                the_team = new_team
            league.add_team_to_league(new_team)

        league.generate_fixtures_with_chosen_team(the_team)
        # Pop off the first fixture because in the 2nd one the chosen team will be away
        league.fixtures.pop(0)

        fixture = league.get_next_fixture_for_team(the_team)
        self.assertIsNotNone(fixture)
        self.assertEqual(the_team, fixture[1])


if __name__ == '__main__':
    unittest.main()
