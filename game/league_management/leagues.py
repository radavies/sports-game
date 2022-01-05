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

    def generate_fixtures_for_leagues(self, chosen_team):
        for country in self.leagues:
            for league in self.leagues[country]:
                if league.name == chosen_team.current_league_name:
                    league.generate_fixtures_with_chosen_team(chosen_team)
                else:
                    league.generate_fixtures()
