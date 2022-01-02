import unittest
from game.league import League
from game.sponsor import Sponsor


class LeagueTests(unittest.TestCase):

    def test_str(self):
        sponsor = Sponsor("Hello")
        league = League("World", "Scotland", "{} World", 0, 2, 18, sponsor)
        self.assertEqual(str(league), "Hello World")


if __name__ == '__main__':
    unittest.main()
