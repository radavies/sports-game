from game.league_management.league_table_row import LeagueTableRow


class League:

    def __init__(self, name, country, name_sponsor_format, league_rank, demotes_number, total_teams, sponsor):
        self.name = name
        self.country = country
        self.name_sponsor_format = name_sponsor_format
        self.league_rank = league_rank
        self.demotes_number = demotes_number
        self.total_teams = total_teams
        self.sponsor = sponsor
        self.teams = []
        self.table = []

    def __str__(self):
        return self.name if self.sponsor is None else self.name_sponsor_format.format(self.sponsor.name)

    def add_team_to_league(self, team):
        self.teams.append(team)
        self.table.append(LeagueTableRow(team, 0, 0, 0, 0, 0, 0))

    def get_sorted_league_table(self):
        self.table.sort()
        return self.table
