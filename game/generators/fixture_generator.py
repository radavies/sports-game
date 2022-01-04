

class FixtureGenerator:

    def __init__(self):
        # Notes - this generator works best for the team the first position as they get the best H/A distro
        # Currently doesn't work for odd numbers of teams (could add a "day off" flag to fix?)
        # The algo does give the correct home / away fixtures (1x vs each team home and away)
        # However the order isn't always great (number of H/A in a row, the order in which teams face each other)
        self.normal_matches = {}
        self.return_matches = {}

    def generate_fixtures_for_league(self, league):
        teams = league.teams
        middle_index = len(teams) // 2

        rotation = list(teams)
        for round_counter in range(0, len(teams)-1):
            rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]
            home_half = rotation[:middle_index]
            away_half = rotation[middle_index:]

            self._create_fixtures_for_round(home_half, away_half, round_counter)

        return self._generate_full_fixture_list()

    def _create_fixtures_for_round(self, home_half, away_half, round_counter):
        counter = 0
        for team in home_half:
            fixture = [team, away_half[counter]]
            if round_counter in self.normal_matches:
                self.normal_matches[round_counter].append(fixture)
                self.return_matches[round_counter].append(list(reversed(fixture)))
            else:
                self.normal_matches[round_counter] = [fixture]
                self.return_matches[round_counter] = [list(reversed(fixture))]

            counter += 1

    def _generate_full_fixture_list(self):
        match_days = {}
        normal_counter = 1
        plus_one_counter = 2

        for key in self.normal_matches:
            match_days[normal_counter] = [self.normal_matches[key]]
            match_days[normal_counter + 1] = self.return_matches[plus_one_counter]

            normal_counter += 2
            plus_one_counter += 1
            if plus_one_counter >= len(self.return_matches):
                plus_one_counter = 0

        return match_days
