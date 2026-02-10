class BoggleSolver:
    """
    Boggle game class that stores the grid, dictionary,
    and computes all valid solutions.
    """
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

        # Convert dictionary to lowercase for easy comparison
        self.dictionary_set = set(word.lower() for word in dictionary)

        # Precompute all prefixes to prune the search
        self.prefixes = set()
        for word in self.dictionary_set:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])

        self.rows = len(grid)
        self.cols = len(grid[0])

    def getSolution(self):
        """
        Finds and returns all valid words in the grid.
        """
        self.solutions = []
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                self._dfs(r, c, "", visited)

        # Return sorted list for consistent autograder output
        return sorted(self.solutions)

    def _dfs(self, r, c, current_word, visited):
        """
        Depth-first search to explore all valid paths starting at (r, c).
        """
        # Mark this cell as visited
        visited[r][c] = True

        # Add the current cell's letters (handle Qu, St, Ie)
        cell_value = self.grid[r][c].lower()
        new_word = current_word + cell_value

        # Prune search if no dictionary word starts with this prefix
        if new_word not in self.prefixes:
            visited[r][c] = False
            return

        # Check if the word is valid
        if len(new_word) >= 3 and new_word in self.dictionary_set:
            if new_word not in self.solutions:
                self.solutions.append(new_word)

        # Explore all 8 possible directions
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr = r + dr
                nc = c + dc
                if self._is_valid(nr, nc, visited):
                    self._dfs(nr, nc, new_word, visited)

        # Backtrack
        visited[r][c] = False

    def _is_valid(self, r, c, visited):
        """
        Checks whether a cell is inside the grid and not yet visited.
        """
        if r < 0 or r >= self.rows:
            return False
        if c < 0 or c >= self.cols:
            return False
        if visited[r][c]:
            return False
        return True


def main():
    """
    Main function to run the Boggle solver.
    """
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "quartz", "rat",
        "tar", "tarp", "ten", "went", "wet", "arty",
        "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()

