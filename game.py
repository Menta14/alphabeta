import os
from solvers import *
from board import Board

class Game:
    def __init__(self, human='MIN', cpu=minmax, difficulty=3, **kwargs):
        print(**kwargs)
        self.board = Board(**kwargs)
        self.human = human
        self.cpu = cpu
        self.difficulty = difficulty

    def play(self):
        player = self.board.nextplayer
        winner = self.board.winner()
        if winner != None:
            print(('WINNER IS ' + winner) if winner != 'DRAW' else winner)
            return
        if player != self.human:
            self.board = self.cpu(self.board, self.difficulty)[1][1]
        else:
            placed = False
            while not placed:
                self.refresh()
                answer = input('Your turn: ').split()
                if answer[0] == 'quit':
                    print('GAME OVER')
                    return
                try:
                    placed = self.board.place(int(answer[0]), int(answer[1]), player)
                except:
                    continue
        self.refresh()
        self.play()

    def refresh(self):
        os.system('cls')
        print(self.board)