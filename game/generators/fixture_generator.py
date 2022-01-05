class FixtureGenerator:

    def __init__(self):
        # Notes - this generator works best for the team the first position as they get the best H/A distro
        # Currently doesn't work for odd numbers of teams (could add a "day off" flag to fix?)
        # The algo does give the correct home / away fixtures (1x vs each team home and away)
        # However the order isn't always great (number of H/A in a row, the order in which teams face each other)
        self.normal_matches = []
        self.return_matches = []

    def generate_fixtures_for_league(self, teams):
        middle_index = len(teams) // 2

        rotation = list(teams)
        for round_counter in range(0, len(teams)-1):
            rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]
            home_half = rotation[:middle_index]
            away_half = rotation[middle_index:]

            self._create_fixtures_for_round(home_half, away_half)

        return self._generate_full_fixture_list()

    def _create_fixtures_for_round(self, home_half, away_half):
        counter = 0
        home_round = []
        away_round = []
        for team in home_half:
            home_round.append([team, away_half[counter]])
            away_round.append([away_half[counter], team])
            counter += 1

        self.normal_matches.append(home_round)
        self.return_matches.append(away_round)

    def _generate_full_fixture_list(self):
        match_days = []
        plus_one_counter = 2

        for fixture in self.normal_matches:
            match_days.append(fixture)
            match_days.append(self.return_matches[plus_one_counter])

            plus_one_counter += 1
            if plus_one_counter >= len(self.return_matches):
                plus_one_counter = 0

        return match_days
