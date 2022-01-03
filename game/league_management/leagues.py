class Leagues:

    def __init__(self, leagues):
        self.leagues = leagues

    def find_team_and_league(self, team_name):
        found_team = None
        found_league = None
        for league in self.leagues["Scotland"]:
            for team in league.teams:
                if team.name == team_name:
                    found_team = team
                    found_league = league
                    break

        if found_team is None:
            for league in self.leagues["England & Wales"]:
                for team in league.teams:
                    if team.name == team_name:
                        found_team = team
                        found_league = league
                        break

        return {
            "team": found_team,
            "league": found_league
        }
