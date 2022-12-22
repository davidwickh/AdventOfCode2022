from dataclasses import dataclass


def read_input():
    """Reads the input file and returns a list of ints"""
    with open('input.txt') as f:
        return [[int(char) for char in line.strip()] for line in f]


def get_row(grid, y, x):
    """Returns the row at the given y coordinate, excluding the tree at the given x coordinate"""
    return grid[y]


def get_column(grid, x, y):
    """Returns the column at the given x coordinate, excluding the tree at the given y coordinate"""
    return [row[x] for row in grid]


def count_visible_trees(grid):
    """Counts the number of visible trees in the grid"""
    visible_trees = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # if the tree is on the edge of the grid, it is visible
            if x == 0 or x == len(grid[0]) - 1 or y == 0 or y == len(grid) - 1:
                visible_trees += 1
                continue
            else:
                current_tree = grid[y][x]
                row = get_row(grid, y, x)
                row_up, row_down = row[:x], row[x + 1:]
                column = get_column(grid, x, y)
                column_left, column_right = column[:y], column[y + 1:]
                if all([tree < current_tree for tree in row_up]) or all(
                        [tree < current_tree for tree in row_down]) or all(
                    [tree < current_tree for tree in column_left]) or all(
                    [tree < current_tree for tree in column_right]):
                    visible_trees += 1

    return visible_trees


@dataclass
class TreeGrid:
    """A class to represent the tree grid"""
    grid: list[list[int]]

    def look_up(self, x, y):
        """Looks up from the given coordinates and returns the first tree it finds"""
        for row in self.grid[:y]:
            if row[x] > 0:
                return row[x]
        return None

    def look_down(self, x, y):
        """Looks down from the given coordinates and returns the first tree it finds"""
        for row in self.grid[y + 1:]:
            if row[x] > 0:
                return row[x]
        return None

    def look_left(self, x, y):
        """Looks left from the given coordinates and returns the first tree it finds"""
        for tree in self.grid[y][:x]:
            if tree > 0:
                return tree
        return None

    def look_right(self, x, y):
        """Looks right from the given coordinates and returns the first tree it finds"""
        for tree in self.grid[y][x + 1:]:
            if tree > 0:
                return tree
        return None

    def return_tree_height(self, x, y):
        """Returns the given coordinates and returns the height of the tree"""
        return self.grid[y][x]



def score_trees(grid):
    highest_score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            score = {"up": 0, "down": 0, "left": 0, "right": 0}
            current_tree_height = grid[y][x]
            column = get_row(grid, y, x)
            column_left, column_right = if column[:x] not None col.reverse(), column[x + 1:]
            row = get_column(grid, x, y)
            row_up, row_down = row[:y].reverse(), row[y + 1:]

            for tree in row_up:
                if tree < current_tree_height:
                    score["up"] += 1
                elif tree >= current_tree_height:
                    score["up"] += 1
                    break
            for tree in row_down:
                if tree < current_tree_height:
                    score["down"] += 1
                elif tree >= current_tree_height:
                    score["down"] += 1
                    break
            for tree in column_left:
                if tree < current_tree_height:
                    score["left"] += 1
                elif tree >= current_tree_height:
                    score["left"] += 1
                    break
            for tree in column_right:
                if tree < current_tree_height:
                    score["right"] += 1
                elif tree >= current_tree_height:
                    score["right"] += 1
                    break

            # multiply the scores together to get the total score
            total_score = score["up"] * score["down"] * score["left"] * score["right"]
            if total_score > highest_score:
                highest_score = total_score

    return highest_score


if __name__ == "__main__":
    raw_data = read_input()

    TreeGrid

    visible_trees = count_visible_trees(tree_grid)
    print(f'Part 1: {visible_trees}')

    highest_score = score_trees(tree_grid)
    print(f'Part 2: {highest_score}')
