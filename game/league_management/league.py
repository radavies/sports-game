from game.league_management.league_table_row import LeagueTableRow
from game.generators.fixture_generator import FixtureGenerator


class League:

    def __init__(self, name, country, name_sponsor_format, league_rank,
                 demotes_number, total_teams, sponsor):
        self.name = name
        self.country = country
        self.name_sponsor_format = name_sponsor_format
        self.league_rank = league_rank
        self.demotes_number = demotes_number
        self.total_teams = total_teams
        self.sponsor = sponsor
        self.teams = []
        self.league_table_rows = {}
        self.fixtures = []
        self.league_above = None
        self.league_below = None
        self.current_match_day = 1
        self.results = {}

    def __str__(self):
        return self.name if self.sponsor is None else self.name_sponsor_format.format(self.sponsor.name)

    def add_team_to_league(self, team):
        self.teams.append(team)
        self.league_table_rows[team.name] = LeagueTableRow(team, 0, 0, 0, 0, 0, 0)

    def get_sorted_league_table(self):
        table = list(self.league_table_rows.values())
        table.sort()
        return table

    def set_league_above(self, league):
        self.league_above = league

    def set_league_below(self, league):
        self.league_below = league

    def is_in_promo_zone(self, position):
        if self.league_above is not None:
            # demotes number + 1 to get the range to include the last promo spot
            if position in range(1, self.league_above.demotes_number + 1):
                return True
            else:
                return False
        return position == 1

    def is_in_relegation_zone(self, position):
        if self.demotes_number != 0:
            # demotes number - 1 to account for the last place being included in the demotes number
            # total teams + 1 to include the last place in the range
            if position in reversed(range(self.total_teams - (self.demotes_number - 1), self.total_teams + 1)):
                return True
            else:
                return False
        return position == self.total_teams

    def generate_fixtures_with_chosen_team(self, team):
        self.teams.insert(0, self.teams.pop(self.teams.index(team)))
        self.generate_fixtures()

    def generate_fixtures(self):
        generator = FixtureGenerator()
        self.fixtures = generator.generate_fixtures_for_league(self.teams)

    def get_next_fixture_for_team(self, team):
        if len(self.fixtures) > 0:
            next_match_day = self.fixtures[0]
            for fixture in next_match_day:
                if team in fixture:
                    return fixture
        return None

    def get_next_match_day(self):
        if len(self.fixtures) > 0:
            return self.fixtures[0]
        return None

    def advance_to_next_match_day(self):
        if len(self.fixtures) > 0:
            self.fixtures.pop(0)
            self.current_match_day += 1

    def save_match_result_and_update_table(self, result):
        if self.current_match_day in self.results:
            self.results[self.current_match_day].append(result)
        else:
            self.results[self.current_match_day] = [result]

        home_team_won = result.home_scored > result.away_scored
        draw = result.home_scored == result.away_scored

        # Update home team's record
        home_league_table_row = self.league_table_rows[result.home_team.name]
        home_league_table_row.played += 1
        if home_team_won:
            home_league_table_row.won += 1
        elif draw:
            home_league_table_row.drawn += 1
        else:
            home_league_table_row.lost += 1

        home_league_table_row.goals_for += result.home_scored
        home_league_table_row.goals_against += result.away_scored

        # Update away team's record
        away_league_table_row = self.league_table_rows[result.away_team.name]
        away_league_table_row.played += 1
        if home_team_won:
            away_league_table_row.lost += 1
        elif draw:
            away_league_table_row.drawn += 1
        else:
            away_league_table_row.won += 1

        away_league_table_row.goals_for += result.away_scored
        away_league_table_row.goals_against += result.home_scored
