class Leagues:

    def __init__(self, leagues):
        self.leagues = leagues

    def find_team(self, team_name):
        found_team = None
        for league in self.leagues["Scotland"]:
            for team in league.teams:
                if team.name == team_name:
                    found_team = team
                    break

        if found_team is None:
            for league in self.leagues["England & Wales"]:
                for team in league.teams:
                    if team.name == team_name:
                        found_team = team
                        break

        return found_team
