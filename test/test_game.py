import unittest
from game.game import Game

class GameTest(unittest.TestCase):

    def test_beep(self):
        test_game = Game()
        self.assertEqual(test_game.beep(1), 2)


if __name__ == '__main__':
    unittest.main()
