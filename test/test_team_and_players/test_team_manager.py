import unittest
from game.teams_and_players.team_manager import TeamManager
from game.teams_and_players.team import Team
from game.generators.player_generator import PlayerGenerator
from game.enums.positions import Positions


class TeamManagerTests(unittest.TestCase):

    def setUp(self):
        # Generate a team for the tests with specific numbers of players
        player_generator = PlayerGenerator()
        players = []
        # Generate Forwards
        for counter in range(0, 2):
            players.append(player_generator._generate_player(Positions.Forward, 0))
        # Generate Mid
        for counter in range(0, 4):
            players.append(player_generator._generate_player(Positions.Midfielder, 0))
        # Generate Def
        for counter in range(0, 4):
            players.append(player_generator._generate_player(Positions.Defender, 0))
        # Generate GKs
        for counter in range(0, 1):
            players.append(player_generator._generate_player(Positions.GK, 0))

        self.team = Team(
            "Test Team",
            None,
            players,
            "Test League"
        )
        self.team_manager = TeamManager(self.team)

    def test_viable_positions_full_match_is_correct_for_squad(self):
        for formation_key in self.team_manager.viable_formations["full_match"]:
            for position_key in self.team_manager.formations.formations[formation_key]:
                self.assertLessEqual(
                    self.team_manager.formations.formations[formation_key][position_key],
                    len(self.team_manager.positions[position_key])
                )

    def test_viable_positions_part_match_is_correct_for_squad(self):
        for formation_key in self.team_manager.viable_formations["part_match"]:
            matches = 0
            for position_key in self.team_manager.formations.formations[formation_key]:
                if self.team_manager.formations.formations[formation_key][position_key] <= len(self.team_manager.positions[position_key]):
                    matches += 1
            self.assertGreater(matches, 0)


if __name__ == '__main__':
    unittest.main()