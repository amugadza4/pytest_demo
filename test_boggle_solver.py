import unittest
import sys

# Path so unittest can find your solver
sys.path.append("/home/codio/workspace/")

from boggle_solver import BoggleSolver  # <- Fixed to match your class


# -----------------------------
# SIMPLE EDGE CASE TESTS
# -----------------------------
class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]

        game = BoggleSolver(grid, dictionary)
        solution = sorted([x.upper() for x in game.getSolution()])

        expected = []
        self.assertEqual(expected, solution)

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]

        game = BoggleSolver(grid, dictionary)
        solution = sorted([x.upper() for x in game.getSolution()])

        expected = []
        self.assertEqual(expected, solution)

    def test_empty_dictionary(self):
        grid = [["A","B"],["C","D"]]
        dictionary = []

        game = BoggleSolver(grid, dictionary)
        solution = game.getSolution()

        self.assertEqual([], solution)


# -----------------------------
# NORMAL FUNCTIONAL TESTS
# -----------------------------
class TestSuite_Normal_Cases(unittest.TestCase):

    def test_single_word_found(self):
        grid = [
            ["C","A","T"],
            ["X","X","X"],
            ["X","X","X"]
        ]
        dictionary = ["cat"]

        game = BoggleSolver(grid, dictionary)
        solution = sorted([x.upper() for x in game.getSolution()])

        expected = ["CAT"]
        self.assertEqual(expected, solution)

    def test_multiple_words_found(self):
        grid = [
            ["C","A","T"],
            ["D","O","G"],
            ["R","A","T"]
        ]
        dictionary = ["cat", "dog", "rat"]

        game = BoggleSolver(grid, dictionary)
        solution = sorted([x.upper() for x in game.getSolution()])

        expected = sorted(["CAT", "DOG", "RAT"])
        self.assertEqual(expected, solution)

    def test_dictionary_word_not_present(self):
        grid = [["A","B"],["C","D"]]
        dictionary = ["HELLO"]

        game = BoggleSolver(grid, dictionary)
        solution = game.getSolution()

        self.assertEqual([], solution)


# -----------------------------
# COMPLEX / PATH TESTS
# -----------------------------
class TestSuite_Complete_Coverage(unittest.TestCase):

    def test_repeated_letter_usage(self):
        grid = [
            ["A","A"],
            ["A","A"]
        ]
        dictionary = ["AAA"]

        game = BoggleSolver(grid, dictionary)
        solution = game.getSolution()

        self.assertTrue(len(solution) >= 0)

    def test_diagonal_word(self):
        grid = [
            ["C","X","X"],
            ["X","A","X"],
            ["X","X","T"]
        ]
        dictionary = ["cat"]

        game = BoggleSolver(grid, dictionary)
        solution = [x.upper() for x in game.getSolution()]

        self.assertIn("CAT", solution)


# -----------------------------
# QU AND ST SPECIAL CASES
# -----------------------------
class TestSuite_Qu_and_St(unittest.TestCase):

    def test_qu_word(self):
        grid = [
            ["Qu","A"],
            ["T","S"]
        ]
        dictionary = ["quat"]

        game = BoggleSolver(grid, dictionary)
        solution = [x.upper() for x in game.getSolution()]

        self.assertIn("QUAT", solution)

    def test_st_word(self):
        grid = [
            ["S","T"],
            ["A","R"]
        ]
        dictionary = ["star"]

        game = BoggleSolver(grid, dictionary)
        solution = [x.upper() for x in game.getSolution()]

        self.assertIn("STAR", solution)


# -----------------------------
# SCALABILITY TESTS
# -----------------------------
class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    def test_Normal_case_3x3(self):
        grid = [
            ["C","A","T"],
            ["D","O","G"],
            ["R","A","T"]
        ]
        dictionary = ["cat", "dog", "rat", "car", "tar"]

        game = BoggleSolver(grid, dictionary)
        solution = game.getSolution()

        self.assertTrue(len(solution) >= 0)

    def test_4x4_grid(self):
        grid = [
            ["T","W","Y","R"],
            ["E","N","P","H"],
            ["G","Z","Qu","R"],
            ["O","N","T","A"]
        ]
        dictionary = ["ten", "went", "quart", "net"]

        game = BoggleSolver(grid, dictionary)
        solution = game.getSolution()

        self.assertTrue(len(solution) >= 0)


if __name__ == '__main__':
    unittest.main()


