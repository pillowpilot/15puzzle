#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Simple module to model the 15 Puzzle game.
With a simple mahattan-based distance between instances
to test a greedy aproach.

Probably, this module is going to be extended to
support other metrics. In the mean while, I need to learn
a little bit more of Python. ^_^.

I am trying to produce a code following the Google Python Style
and maximize the Pylint score of this module.
"""

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
            self.empty = list(puzzle.empty) # Use list() to copy

    def _is_possible(self, move):
        """Private method. Centralize checks.

        Args:
            move (int): Identifies the move to check.
                0: move up, 1: move down, 2: move right, 3: move left.

        Returns:
            If the especified move is possible, returns true.
            False otherwise.
        """
        x_coordinate, y_coordinate = self.empty
        if move == 0: # Up
            return x_coordinate > 0
        elif move == 1: # Down
            return x_coordinate < 3
        elif move == 2: # Right
            return y_coordinate < 3
        elif move == 3: # Left
            return y_coordinate > 0
        else: # ?
            return False

    def _move(self, move):
        """Private method. Returns a copy of the puzzle over
        which the especified move has been performed.

        Args:
            move (int): Identifies the move to be performed.
                0: moves up, 1: moves down, 2: moves right, 3: moves left.

        Returns:
            A copy of the puzzle over which the move has been realized.
            If the move is not possible, then a copy of the current puzzle.
        """
        if self._is_possible(move) is True:
            new_copy = Puzzle(self)
            x_coord, y_coord = new_copy.empty
            if move == 0: # Up
                x_offset = -1
                y_offset = 0
            elif move == 1: # Down
                x_offset = 1
                y_offset = 0
            elif move == 2: # Right
                x_offset = 0
                y_offset = 1
            elif move == 3: # Left
                x_offset = 0
                y_offset = -1
            else: # ?
                x_offset = 0
                y_offset = 0
            new_copy.state[x_coord][y_coord] = \
                new_copy.state[x_coord + x_offset][y_coord + y_offset]
            new_copy.state[x_coord + x_offset][y_coord + y_offset] = None
            new_copy.empty = [x_coord + x_offset, y_coord + y_offset]
            return new_copy
        else:
            return Puzzle(self)

    def is_possible_up(self):
        """Check if the 'up' move is possible."""
        return self._is_possible(0)

    def up(self):
        """Return a copy after making the 'up' move.

        Returns:
            A copy of the puzzle after making the 'up' move.
            If it is not possible, then return a copy of the current state.
        """
        return self._move(0)

    def is_possible_down(self):
        """Check if the 'down' move is possible."""
        return self._is_possible(1)

    def down(self):
        """Return a copy after making the 'down' move.

        Returns:
            A copy of the puzzle after making the 'down' move.
            If it is not possible, then return a copy of the current state.
        """
        return self._move(1)

    def is_possible_right(self):
        """Check if the 'right' move is possible."""
        return self._is_possible(2)

    def right(self):
        """Return a copy after making the 'right' move.

        Returns:
            A copy of the puzzle after making the 'right' move.
            If it is not possible, then return a copy of the current state.
        """
        return self._move(2)

    def is_possible_left(self):
        """Check if the 'left' move is possible."""
        return self._is_possible(3)

    def left(self):
        """Return a copy after making the 'left' move.

        Returns:
            A copy of the puzzle after making the 'left' move.
            If it is not possible, then return a copy of the current state.
        """
        return self._move(3)

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

        return distance

    def __eq__(self, p):
        return self.state == p.state

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

    tst1 = Puzzle()
    print('Original:\n{}'.format(tst1))
    # Check moves
    tst1 = tst1.up()
    print('Moving up:\n{}'.format(tst1))
    tst1 = tst1.down()
    print('Moving down:\n{}'.format(tst1))
    tst1 = tst1.left()
    print('Moving left:\n{}'.format(tst1))
    tst1 = tst1.right()
    print('Moving right:\n{}'.format(tst1))
    # Check constraints
    tst1 = tst1.right()
    print('Trying to move right:\n{}'.format(tst1))
    tst1 = tst1.down()
    print('Trying to move right:\n{}'.format(tst1))
    # Check distances
    tst1 = Puzzle()
    tst2 = Puzzle()
    tst2 = tst2.up()
    tst2 = tst2.up()
    tst2 = tst2.left()
    tst2 = tst2.left()
    print('Distance(\n{}, \n{}) = {}\n'\
          .format(tst1, tst1, tst1.distance(tst1)))
    print('Distance(\n{}, \n{}) = {}\n'\
          .format(tst2, tst2, tst2.distance(tst2)))
    print('Distance(\n{}, \n{}) = {}\n'\
          .format(tst1, tst2, tst1.distance(tst2)))
    # Check equality
    print('Check if \n{} equals \n{}. {}\n'.format(tst1, tst1, tst1 == tst1))
    print('Check if \n{} equals \n{}. {}\n'.format(tst2, tst2, tst2 == tst2))
    print('Check if \n{} equals \n{}. {}\n'.format(tst1, tst2, tst1 == tst2))

if __name__ == '__main__':
    main()
