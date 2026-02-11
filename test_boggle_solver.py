# test_boggle_solver.py

import unittest
from boggle_solver import Boggle

class TestBoggle(unittest.TestCase):

    #  Single word in small grid
    def test_single_word(self):
        grid = [["C","A","T"]]
        dictionary = ["cat"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), ["cat"])

    #  Multiple words in 3x3 grid
    def test_multiple_words(self):
        grid = [
            ["C","A","T"],
            ["D","O","G"],
            ["R","A","T"]
        ]
        dictionary = ["cat", "dog", "rat"]
        game = Boggle(grid, dictionary)
        self.assertEqual(sorted(game.getSolution()), sorted(["cat","dog","rat"]))

    #  Word not present
    def test_word_not_present(self):
        grid = [["A","B"],["C","D"]]
        dictionary = ["hello"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    #  Empty dictionary
    def test_empty_dictionary(self):
        grid = [["A","B"],["C","D"]]
        dictionary = []
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    # 5️⃣ 1x1 grid edge case
    def test_1x1_grid(self):
        grid = [["A"]]
        dictionary = ["a","b"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    #  Empty grid
    def test_empty_grid(self):
        grid = [[]]
        dictionary = ["a","b"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    #  Diagonal word usage
    def test_diagonal_word(self):
        grid = [
            ["C","X","X"],
            ["X","A","X"],
            ["X","X","T"]
        ]
        dictionary = ["cat"]
        game = Boggle(grid, dictionary)
        self.assertIn("cat", game.getSolution())

    #  Repeated letters usage
    def test_repeated_letters(self):
        grid = [
            ["A","A"],
            ["A","A"]
        ]
        dictionary = ["aaa"]
        game = Boggle(grid, dictionary)
        self.assertIn("aaa", game.getSolution())

    #  "Qu" handling
    def test_qu_word(self):
        grid = [
            ["Qu","A"],
            ["T","S"]
        ]
        dictionary = ["quat"]
        game = Boggle(grid, dictionary)
        self.assertIn("quat", game.getSolution())

    #  4x4 grid scalability
    def test_4x4_grid(self):
        grid = [
            ["T","W","Y","R"],
            ["E","N","P","H"],
            ["G","Z","Qu","R"],
            ["O","N","T","A"]
        ]
        dictionary = ["ten","went","quart","net"]
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        self.assertTrue(len(result) > 0)

if __name__ == "__main__":
    unittest.main()

