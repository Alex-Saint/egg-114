import unittest
from io import StringIO
from contextlib import redirect_stdout
import part5_testable as p5

from unittest.mock import patch


class TestGreet(unittest.TestCase):

    def test_canFight_fightable(self):
        output = StringIO()

        with redirect_stdout(output):
            p5.canFight(20, 10)

        self.assertEqual(output.getvalue(), "you can fight the monster\n\n")

    def test_canFight_not_fightable(self):
        output = StringIO()

        with redirect_stdout(output):
            p5.canFight(9, 10)

        self.assertEqual(output.getvalue(), "you aren’t high enough level\n\n")

    def test_getHealths(self):
        monster_health, player_health = p5.getHealths()

        self.assertGreaterEqual(monster_health, 0)
        self.assertGreaterEqual(player_health, 0)

    @patch("builtins.input", side_effect=['k', 'k', 'k', 'k'])
    def test_fight(self, mock_input):
        monster_health, player_health = p5.fight(10, 10)

        self.assertEqual(monster_health, -2)
        self.assertEqual(player_health, 2)

    def test_determineWinner_monster_wins(self):
        output = StringIO()

        with redirect_stdout(output):
            p5.determineWinner(10, 0)

        self.assertEqual(output.getvalue(), "the monster killed you\n")

    def test_determineWinner_player_wins(self):
        output = StringIO()

        with redirect_stdout(output):
            p5.determineWinner(0, 10)

        self.assertEqual(output.getvalue(), "you killed the monster\n")

    def test_determineWinner_both_die(self):
        output = StringIO()

        with redirect_stdout(output):
            p5.determineWinner(0, 0)

        self.assertEqual(output.getvalue(),
                         "you killed the monster\nthe monster killed you\n")

    def test_writeHealths(self):
        p5.writeHealths(10, 10)
        self.test_getHealths()


if __name__ == "__main__":
    unittest.main()
