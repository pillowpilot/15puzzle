#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from puzzle import Puzzle

class Searcher(object):
    def __init__(self):
        pass
    
    def greedy(self, origin, target, max_iterations=500):
        moves = []
        iterations = 1
        while origin != target and iterations <= max_iterations:
            iterations += 1

            possible_moves = []
            moveUp = origin
            moveUp.up()
            moveDown = origin
            moveDown.down()
            

def main():
    solved_state = Puzzle()
    puzzle = Puzzle()
    searcher = Searcher()

    puzzle.up()
    puzzle.up()
    puzzle.up()

    print( solved_state )
    print( puzzle )

    solved, moves = searcher.greedy(solved_state, puzzle)

    print( solved )
    print( moves  )
    
    

if __name__ == '__main__':
    main()
