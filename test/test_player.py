import unittest
from game.player import Player


class PlayerTests(unittest.TestCase):

    def test_str(self):
        player = Player("Hello", "World", None, None)
        self.assertEqual(str(player), "Hello World")


if __name__ == '__main__':
    unittest.main()
