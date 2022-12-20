from dataclasses import dataclass


def read_input():
    """Reads the input file and returns a list of ints"""
    with open('input.txt') as f:
        return [line.strip() for line in f.readlines()]


@dataclass
class TreeGrid:
    """A class to represent the tree grid"""
    grid: list[list]

    def __post_init__(self):
        self.grid = [[int(char) for char in line] for line in self.grid]

    def check_visibility(self, x, y):
        """Checks if the tree at the given coordinates is visible. A tree is visible if all of the other trees between
        it and an edge of the grid are shorter than it, or if the tree is on the edge of the grid."""

        if x == 0 or x == len(self.grid[0]) - 1 or y == 0 or y == len(self.grid) - 1:
            return True

        # Check if there are any trees in the same row
        if any([tree > self.grid[y][x] for tree in self.grid[y]]):
            return False

        # Check if there are any trees in the same column
        if any([tree > self.grid[y][x] for tree in [row[x] for row in self.grid]]):
            return False

        return True


if __name__ == "__main__":
    tree_grid = read_input()
    tree_grid = TreeGrid(tree_grid)
    visible_trees = 0
    for y in range(len(tree_grid.grid)):
        for x in range(len(tree_grid.grid[y])):
            if tree_grid.check_visibility(x, y):
                visible_trees += 1

    print(visible_trees)
