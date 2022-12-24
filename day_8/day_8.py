from dataclasses import dataclass


def read_input():
    """Reads the input file and returns a list of ints"""
    with open('input.txt') as f:
        return [[int(char) for char in line.strip()] for line in f]


@dataclass
class TreeGrid:
    """A class to represent the tree grid"""
    grid: list[list[int]]

    def look_up(self, x, y):
        """Looks up from the given coordinates and returns the first tree it finds
        123
        234
        345
        -> look_up(1, 2)
        [3, 2]
        """
        trees_up = []
        for row in self.grid[:y][::-1]:
            if row[x]:
                trees_up.append(row[x])
        if trees_up:
            return trees_up
        return None

    def look_down(self, x, y):
        """Looks down from the given coordinates and returns the first tree it finds
        123
        234
        345
        -> look_down(1, 0)
        [3, 4]
        """
        trees_down = []
        for row in self.grid[y + 1:]:
            if row[x]:
                trees_down.append(row[x])
        if trees_down:
            return trees_down
        return None

    def look_left(self, x, y):
        """Looks left from the given coordinates and returns the first tree it finds
        123
        234
        345
        -> look_left(3, 2)
        [4, 3]
        """
        trees_left = []
        for tree in self.grid[y][:x][::-1]:
            trees_left.append(tree)
        if trees_left:
            return trees_left
        return None

    def look_right(self, x, y):
        """Looks right from the given coordinates and returns the first tree it finds
        123
        234
        345
        -> look_right(0, 1)
        [3, 4]
        """
        trees_right = []
        for tree in self.grid[y][x + 1:]:
            trees_right.append(tree)
        if trees_right:
            return trees_right
        return None

    def return_tree_height(self, x, y):
        """Returns the given coordinates and returns the height of the tree"""
        return self.grid[y][x]


def count_visible_trees(grid: TreeGrid):
    """Counts the number of visible trees in the grid"""
    visible_trees = 0
    for y in range(len(grid.grid)):
        for x in range(len(grid.grid[y])):
            # if the tree is on the edge of the grid, it is visible
            current_tree = grid.return_tree_height(x, y)
            row_up = grid.look_up(x, y)
            row_down = grid.look_down(x, y)
            column_left = grid.look_left(x, y)
            column_right = grid.look_right(x, y)

            if row_up is None or row_down is None or column_left is None or column_right is None:
                visible_trees += 1
                continue
            else:
                if all([tree < current_tree for tree in row_up]) or \
                        all([tree < current_tree for tree in row_down]) or \
                        all([tree < current_tree for tree in column_left]) or \
                        all([tree < current_tree for tree in column_right]):
                    visible_trees += 1

    return visible_trees


def score_trees(grid: TreeGrid):
    """Function handles the scoring of the trees by looping through the grid and calling the look methods on each tree.
    The score is calculated by counting the number of trees that can be seen from the given tree, which can be calculated
    by see if the height of the tree is greater than the height of the trees that can be seen from it. The total score is
    just the multiplication of the number of trees that can be seen in each direction."""

    highest_score = 0
    width = len(grid.grid[0])
    height = len(grid.grid)
    for x in range(len(grid.grid[0])):
        for y in range(len(grid.grid)):
            if grid.return_tree_height(x, y) == 0:
                continue
            else:
                score = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
                up = grid.look_up(x, y)
                trees_direct = {'up': grid.look_up(x, y), 'down': grid.look_down(x, y), 'left': grid.look_left(x, y),
                                'right': grid.look_right(x, y)}
                for direction, trees in trees_direct.items():
                    if trees is None:
                        score[direction] = 0
                        continue
                    for tree in trees:
                        if tree is not None and tree < grid.return_tree_height(x, y):
                            score[direction] += 1
                        else:
                            score[direction] += 1
                            break
                total_score = score['up'] * score['down'] * score['left'] * score['right']
                if total_score > highest_score:
                    highest_score = total_score
    return highest_score


if __name__ == "__main__":
    raw_data = read_input()

    tree_grid = TreeGrid(raw_data)

    visible_trees = count_visible_trees(tree_grid)
    print(f'Part 1: {visible_trees}')

    highest_score = score_trees(tree_grid)
    print(f'Part 2: {highest_score}')
