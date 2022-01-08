import random
from utils import get_name_data_from_file
from game.generators.player_generator import PlayerGenerator
from game.team import Team
from game.names import Names


class TeamGenerator:

    def __init__(self, places):
        self.generated_teams = []
        self.places = places
        self.names = Names(get_name_data_from_file())
        self.player_generator = PlayerGenerator()

    def generate_teams_for_league(self, league):
        probabilities = {
            "Cities": 0,
            "Towns or Suburban Areas": 0,
            "Villages": 0,
            "Education": 0
        }

        if league.league_rank == 0:
            probabilities["Cities"] = 90
            probabilities["Towns or Suburban Areas"] = 99
            probabilities["Villages"] = 100
            probabilities["Education"] = 101

        elif league.league_rank == 1:
            probabilities["Cities"] = 70
            probabilities["Towns or Suburban Areas"] = 95
            probabilities["Villages"] = 100
            probabilities["Education"] = 101

        elif league.league_rank > 1:
            probabilities["Cities"] = 30
            probabilities["Towns or Suburban Areas"] = 75
            probabilities["Villages"] = 85
            probabilities["Education"] = 100

        for counter in range(0, league.total_teams):
            type_choice = random.randint(1, 100)
            if type_choice <= probabilities["Cities"]:
                league.add_team_to_league(self._generate_team(
                    self._select_place(league.country, "Cities", True),
                    league.league_rank,
                    league.name
                ))
            elif type_choice <= probabilities["Towns or Suburban Areas"]:
                league.add_team_to_league(self._generate_team(
                    self._select_place(league.country, "Towns or Suburban Areas", True),
                    league.league_rank,
                    league.name
                ))
            elif type_choice <= probabilities["Villages"]:
                league.add_team_to_league(self._generate_team(
                    self._select_place(league.country, "Villages", True),
                    league.league_rank,
                    league.name
                ))
            else:
                league.add_team_to_league(self._generate_team(
                    self._select_place(league.country, "Education", False),
                    league.league_rank,
                    league.name
                ))

    def _select_place(self, country, place_type, search_down):
        open_options = []
        if place_type != "Towns or Suburban Areas":
            open_options.extend(
                [option for option in self.places.places[country][place_type] if not option["Has Team"]]
            )
        else:
            open_options.extend(
                [option for option in self.places.places[country]["Towns"] if not option["Has Team"]]
            )
            open_options.extend(
                [option for option in self.places.places[country]["Suburban Areas"] if not option["Has Team"]]
            )

        if len(open_options) == 0:
            if search_down:
                if place_type == "Cities":
                    return self._select_place(country, "Towns or Suburban Areas", search_down)
                elif place_type == "Towns or Suburban Areas":
                    return self._select_place(country, "Villages", search_down)
                elif place_type == "Villages":
                    return self._select_place(country, "Education", search_down)
                else:
                    return self._select_place(country, "Cities", not search_down)
            else:
                if place_type == "Cities":
                    return self._select_place(country, "Education", not search_down)
                elif place_type == "Towns or Suburban Areas":
                    return self._select_place(country, "Cities", search_down)
                elif place_type == "Villages":
                    return self._select_place(country, "Towns or Suburban Areas", search_down)
                else:
                    return self._select_place(country, "Villages", search_down)

        choice = random.randint(0, len(open_options) - 1)
        place_to_use = open_options[choice]
        place_to_use["Has Team"] = True
        return place_to_use

    def _generate_team(self, place, league_rank, league_name):
        return Team(
            self._generate_team_name(place),
            place,
            self.player_generator.generate_initial_squad_for_team(league_rank),
            league_name
        )

    def _generate_team_name(self, place):
        return self.names.generate_name(place["Name"], True)
