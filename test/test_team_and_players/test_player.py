import unittest
from game.teams_and_players.player import Player


class PlayerTests(unittest.TestCase):

    def test_str(self):
        player = Player("Hello", "World", None, None)
        self.assertEqual("Hello World", str(player))


if __name__ == '__main__':
    unittest.main()
