import numpy as np
from itertools import groupby

class Board:
    def __init__(self, custom_board=None, boardsize = (3, 3), m = None):
        if custom_board is None:
            self.boardsize = boardsize
            self.board = np.zeros(self.boardsize, dtype=int)
        else:
            self.board = custom_board
            self.boardsize = custom_board.shape
        if m is not None and m > min(self.boardsize):
            raise Exception('M arg not valid')
        self.m = m
        self.nextplayer = self.getNextPlayer()
        self.playernames = {'MAX': 1, 'MIN': -1, 'DRAW': 0, None: 0}
        self.displaynames = {1: 'X', 0: ' ', -1: 'O'}

    def __str__(self):
        grid = ''
        for line in self.board:
            add = ' | '.join([self.displaynames[elem] for elem in line])
            grid += add
            grid += '\n' + '-'*len(add) + '\n'
        return grid

    def __repr__(self):
        return str(self)

    def getLines(self):
        lines = []
        for config in [self.board, self.board.T]:
            for line in config:
                lines.append(line)
        for config in [self.board, np.fliplr(self.board)]:
            for k in range(self.boardsize[1] - 2):
                lines.append(np.diag(config, k))
            for k in range(self.boardsize[0] - 2):
                lines.append(np.diag(config, -k))
        return lines

    def winner(self):
        if self.m is not None:
            return self.winnerM()
        cnt = 0
        for line in self.getLines():
            localScore = sum(line)
            if localScore == self.playernames['MAX']*len(line):
                return 'MAX'
            if localScore == self.playernames['MIN']*len(line):
                return 'MIN'
            for elem in line:
                cnt += 1 if elem == 0 else 0
        return 'DRAW' if cnt == 0 else None

    def winnerM(self):
        cnt = 0
        for line in self.getLines():
            for elem in line:
                cnt += 1 if elem == 0 else 0
            subseqs = [list(group) for _, group in groupby(line)]
            winningseqs = [seq for seq in subseqs if len(seq) >= self.m]
            if len(winningseqs) == 0:
                continue
            if winningseqs[0][0] == self.playernames['MAX']:
                return 'MAX'
            if winningseqs[0][0] == self.playernames['MIN']:
                return 'MIN'
        return 'DRAW' if cnt == 0 else None 

    def estimate(self):
        #if self.m is not None:
         #   return self.estimateM()
        score = 0
        for line in self.getLines():
            score += sum(line)
        return score
    
    def estimateM(self):
        pass

    def nextStates(self):
        suc = []
        for i, line in enumerate(self.board):
            for j, elem in enumerate(line):
                if elem == 0:
                    curr = self.board.copy()
                    curr[i][j] = self.playernames[self.nextplayer]
                    suc.append((Board(curr, m=self.m), (i, j)))
        return suc

    def place(self, x, y, player):
        if self.board[x][y] != 0:
            return False
        self.board[x][y] = self.playernames[player]
        self.nextplayer = self.getNextPlayer()
        return True
    
    def getNextPlayer(self):
        cnt = {1: 0, 0: 0, -1: 0}
        decode = {-1: 'MIN', 1: 'MAX'}
        for lines in self.board:
            for elem in lines:
                cnt[elem] += 1
        del cnt[0]
        return decode[min(cnt.keys(), key=lambda x: cnt[x])]