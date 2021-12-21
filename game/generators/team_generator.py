class TeamGenerator:

    def __init__(self, places):
        self.generated_teams = []
        self.place_data = places.places.copy()

    def generate_teams_for_league(self, league):

        city_chance = 75
        if league.league_rank == 1:
            city_chance = 50
        elif league.league_rank > 1:
            city_chance = 25

        town_or_sub_chance = 90
        if league.league_rank == 1:
            town_or_sub_chance = 75
        elif league.league_rank > 1:
            town_or_sub_chance = 50

        village_chance = 100
        if league.league_rank == 1:
            town_or_sub_chance = 90
        elif league.league_rank > 1:
            town_or_sub_chance = 85


        for counter in range(0, league.total_teams):



