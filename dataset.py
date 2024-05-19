import pandas as pd
import numpy as np
from board import Board
from solvers import alphabeta

class GamesDataset(pd.DataFrame):
    def __init__(self, lines=3, columns=3, solver=alphabeta, difficulty=1):
        super().__init__(columns=['states', 'best_move'])
        self.boardsize = lines, columns
        self.solver = solver
        self.difficulty = difficulty
    
    def __weight_function(self, x, a, n):
        return 1 - (x/a)**n

    def generateState(self, a=10, n=4):
        total_cells = self.boardsize[0]*self.boardsize[1]
        half_cells = total_cells // 2
        integers = np.arange(1, half_cells + 1)
        probs = self.__weight_function(integers, a, n)
        probs /= np.sum(probs)
        rng = np.random.default_rng()
        maxcells = rng.choice(integers, p=probs)
        mincells = maxcells - 1
        board = np.zeros(self.boardsize, dtype=int)
        indices = rng.permutation(total_cells)
        board.flat[indices[:maxcells]] = 1
        board.flat[indices[maxcells:maxcells+mincells]] = -1
        board = Board(board)
        try:
            solution = self.solver(board, self.difficulty)[1][1]
        except:
            solution = board.winner()
        return board, solution