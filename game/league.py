class League:

    def __init__(self, name, name_sponsor_format, league_rank, demotes_number, total_teams, sponsor):
        self.name = name
        self.name_sponsor_format = name_sponsor_format
        self.league_rank = league_rank
        self.demotes_number = demotes_number
        self.total_teams = total_teams
        self.sponsor = sponsor
        self.teams = []
