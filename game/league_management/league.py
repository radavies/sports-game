from game.league_management.league_table_row import LeagueTableRow


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
        self.table = []
        self.league_above = None
        self.league_below = None

    def __str__(self):
        return self.name if self.sponsor is None else self.name_sponsor_format.format(self.sponsor.name)

    def add_team_to_league(self, team):
        self.teams.append(team)
        self.table.append(LeagueTableRow(team, 0, 0, 0, 0, 0, 0))

    def get_sorted_league_table(self):
        self.table.sort()
        return self.table

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
