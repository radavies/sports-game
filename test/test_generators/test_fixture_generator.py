import unittest
from game.generators.fixture_generator import FixtureGenerator
from game.league_management.league import League
from game.team import Team


class FixtureGeneratorTests(unittest.TestCase):

    def setUp(self):
        self.generator = FixtureGenerator()

    def test_generate_fixtures_for_league_four_teams_correct_number_of_matches_etc(self):
        number_of_teams = 4

        league = League("Test", "Scotland", "{} Test", 0, 2, number_of_teams, None)

        for counter in range(0, number_of_teams):
            league.add_team_to_league(Team("{} Team".format(str(counter)), None, None, league.name))

        match_days = self.generator.generate_fixtures_for_league(league.teams)

        self.assertEqual(6, len(match_days))

        for match_day in match_days:
            # Assert there are the right number of fixtures
            self.assertEqual(2, len(match_day))
            for fixture in match_day:
                # Assert there are 2 teams in a fixture
                self.assertEqual(number_of_teams // 2, len(fixture))
                self.assertIsInstance(fixture[0], Team)
                self.assertIsInstance(fixture[1], Team)

    def test_generate_fixtures_for_league_six_teams_correct_number_of_matches_etc(self):
        number_of_teams = 6

        league = League("Test", "Scotland", "{} Test", 0, 2, number_of_teams, None)

        for counter in range(0, number_of_teams):
            league.add_team_to_league(Team("{} Team".format(str(counter)), None, None, league.name))

        match_days = self.generator.generate_fixtures_for_league(league.teams)

        self.assertEqual(10, len(match_days))

        for match_day in match_days:
            # Assert there are the right number of fixtures
            self.assertEqual(number_of_teams // 2, len(match_day))
            for fixture in match_day:
                # Assert there are 2 teams in a fixture
                self.assertEqual(2, len(fixture))
                self.assertIsInstance(fixture[0], Team)
                self.assertIsInstance(fixture[1], Team)

    def test_generate_fixtures_for_league_twelve_teams_correct_number_of_matches_etc(self):
        number_of_teams = 12

        league = League("Test", "Scotland", "{} Test", 0, 2, number_of_teams, None)

        for counter in range(0, number_of_teams):
            league.add_team_to_league(Team("{} Team".format(str(counter)), None, None, league.name))

        match_days = self.generator.generate_fixtures_for_league(league.teams)

        self.assertEqual(22, len(match_days))

        for match_day in match_days:
            # Assert there are the right number of fixtures
            self.assertEqual(number_of_teams // 2, len(match_day))
            for fixture in match_day:
                # Assert there are 2 teams in a fixture
                self.assertEqual(2, len(fixture))
                self.assertIsInstance(fixture[0], Team)
                self.assertIsInstance(fixture[1], Team)

    def test_generate_fixtures_for_league_eighteen_teams_correct_number_of_matches_etc(self):
        number_of_teams = 18

        league = League("Test", "Scotland", "{} Test", 0, 2, number_of_teams, None)

        for counter in range(0, number_of_teams):
            league.add_team_to_league(Team("{} Team".format(str(counter)), None, None, league.name))

        match_days = self.generator.generate_fixtures_for_league(league.teams)

        self.assertEqual(34, len(match_days))

        for match_day in match_days:
            # Assert there are the right number of fixtures
            self.assertEqual(number_of_teams // 2, len(match_day))
            for fixture in match_day:
                # Assert there are 2 teams in a fixture
                self.assertEqual(2, len(fixture))
                self.assertIsInstance(fixture[0], Team)
                self.assertIsInstance(fixture[1], Team)

    def test_generate_fixtures_for_league_correct_matches(self):
        number_of_teams = 18

        league = League("Test", "Scotland", "{} Test", 0, 2, number_of_teams, None)

        for counter in range(0, number_of_teams):
            league.add_team_to_league(Team("{} Team".format(str(counter)), None, None, league.name))

        match_days = self.generator.generate_fixtures_for_league(league.teams)

        first_team = league.teams[0]

        # Assert the selected team is in the right fixture
        # Also assert that they flip home / away
        is_home_team = True
        for match_day in match_days:
            first_fixture = match_day[0]
            self.assertIn(first_team, first_fixture)
            self.assertEqual(is_home_team, first_fixture[0] is first_team)
            is_home_team = not is_home_team

    def test_generate_fixtures_for_league_all_teams_have_a_match(self):
        number_of_teams = 18

        league = League("Test", "Scotland", "{} Test", 0, 2, number_of_teams, None)
        fixture_tracker = {}

        for counter in range(0, number_of_teams):
            team = Team("{} Team".format(str(counter)), None, None, league.name)
            league.add_team_to_league(team)
            fixture_tracker[team.name] = False

        match_days = self.generator.generate_fixtures_for_league(league.teams)

        for match_day in match_days:
            for fixture in match_day:
                fixture_tracker[fixture[0].name] = True
                fixture_tracker[fixture[1].name] = True

        for result in fixture_tracker.values():
            self.assertTrue(result)
