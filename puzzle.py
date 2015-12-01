#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Puzzle(object):
    """Class to model the 15puzzle game.

    Args:
        puzzle (Puzzle): Copy constructor.

    Attributes:
        state (list of list): The current state of the puzzle. The empty spot is None.
        empty (list of int): The x and y coordinates of the empty spot.
            Use python notation, so the upper left corner is [0][0].

    """
    def __init__(self, puzzle=None):
        if puzzle is None:
            # Allocate structure, probably no pythonic.
            self.state = []
            for row in range(4):
                self.state.append([[], [], [], []])
            counter = 1
            # Initializate to solved state
            for row in range(4):
                for col in range(4):
                    self.state[row][col] = counter
                    counter += 1
            # Place empty spot
            self.state[3][3] = None
            self.empty = [3, 3]
        else:
            self.state = list(puzzle.state) # Use list() to copy

    def up(self):
        """Move the empty spot one position up, if possible."""

        x_coordinate, y_coordinate = self.empty
        if x_coordinate > 0:
            self.state[x_coordinate][y_coordinate] = self.state[x_coordinate-1][y_coordinate]
            self.state[x_coordinate-1][y_coordinate] = None
            self.empty = [x_coordinate-1, y_coordinate]

    def down(self):
        """Move the empty spot one position down, if possible."""

        x_coordinate, y_coordinate = self.empty
        if x_coordinate < 3:
            self.state[x_coordinate][y_coordinate] = self.state[x_coordinate+1][y_coordinate]
            self.state[x_coordinate+1][y_coordinate] = None
            self.empty = [x_coordinate+1, y_coordinate]

    def left(self):
        """Move the empty spot one position to the left, if possible."""

        x_coordinate, y_coordinate = self.empty
        if y_coordinate > 0:
            self.state[x_coordinate][y_coordinate] = self.state[x_coordinate][y_coordinate-1]
            self.state[x_coordinate][y_coordinate-1] = None
            self.empty = [x_coordinate, y_coordinate-1]

    def right(self):
        """Move the empty spot one possition to the right, if possible."""

        x_coordinate, y_coordinate = self.empty
        if y_coordinate < 3:
            self.state[x_coordinate][y_coordinate] = self.state[x_coordinate][y_coordinate+1]
            self.state[x_coordinate][y_coordinate+1] = None
            self.empty = [x_coordinate, y_coordinate+1]

    def distance(self, puzzle):
        """Define the distance (moves) between two instances.

        Args:
            puzzle (Puzzle): The other instance to measure with.

        """
        def locate(item, matrix):
            """A helper to locate an item in a state.

            Note:
                Assumption: The item is in the matrix.

            Rerturn:
                positions (int, int): A tuple of two int.

            """
            index = 0
            while item not in matrix[index]:
                index += 1

            return (index, matrix[index].index(item))

        def manhattan(point_a, point_b):
            """A helper to calculate the Manhattan Distance.

            Args:
                point_a, point_b (list of two int): Points to measure.

            Return:
                A positive int.

            """
            return abs(point_a[0]-point_b[0]) + abs(point_a[1]-point_b[1])

        distance = 0
        for row in self.state:
            for item in row:
                point_a = locate(item, self.state)
                point_b = locate(item, puzzle.state)
                distance += manhattan(point_a, point_b)

        return distance // 2

    def __str__(self):
        """Pretty print of the current state of the puzzle."""

        string = ""
        for row in self.state:
            string += '[{0:02d}'.format(row[0])
            for item in row[1:]:
                if item is not None:
                    string += ', {0:02d}'.format(item)
                else:
                    string += ', __'
            string += ']\n'
        return string

def main():
    """Just to check the class"""

    p = Puzzle()
    print(p)
    # Check moves
    p.up()
    print(p)
    p.down()
    print(p)
    p.left()
    print(p)
    p.right()
    print(p)
    # Check constraints
    p.right()
    print(p)
    p.down()
    print(p)
    # Check distances
    p = Puzzle()
    q = Puzzle()
    q.up()
    q.up()
    print(p.distance(p))
    print(q.distance(q))
    print(p.distance(q))

if __name__ == '__main__':
    main()
