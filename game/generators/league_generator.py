from game.league_management.league import League
from game.generators.team_generator import TeamGenerator


class LeagueGenerator:

    def create_leagues(self, places):

        leagues = {
            "Scotland": [],
            "England & Wales": []
        }

        scot_prem = League(
            "Scottish Premier League", "Scotland",
            "{} Scottish Premier League", 0, 2, 18, None
        )
        scot_champ = League(
            "Scottish Championship",
            "Scotland", "{} Scottish Championship", 1, 2, 18, None
        )

        scot_prem.set_league_below(scot_champ)
        scot_champ.set_league_above(scot_prem)

        leagues["Scotland"].append(scot_prem)
        leagues["Scotland"].append(scot_champ)

        eng_prem = League(
            "England & Wales Premier League",
            "England & Wales", "England & Wales {} Premier League", 0, 3, 22, None
        )
        eng_champ = League(
            "England & Wales Championship",
            "England & Wales", "England & Wales {} Championship", 1, 2, 18, None
        )
        eng_league_one = League(
            "England & Wales Junior League",
            "England & Wales", "England & Wales {} Junior League", 2, 3, 12, None
        )

        eng_prem.set_league_below(eng_champ)
        eng_champ.set_league_above(eng_prem)
        eng_champ.set_league_below(eng_league_one)
        eng_league_one.set_league_above(eng_champ)

        leagues["England & Wales"].append(eng_prem)
        leagues["England & Wales"].append(eng_champ)
        leagues["England & Wales"].append(eng_league_one)

        self._create_starting_teams(leagues, places)

        return leagues

    @staticmethod
    def _create_starting_teams(leagues, places):
        team_gen = TeamGenerator(places)

        for league in leagues["Scotland"]:
            team_gen.generate_teams_for_league(league)

        for league in leagues["England & Wales"]:
            team_gen.generate_teams_for_league(league)
