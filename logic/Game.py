import numpy as np


class Game(object):

    def __init__(self):
        self.size = 19
        self.winNumber = 5
        self.board = np.array([[0 for _ in range(self.size)] for _ in range(self.size)], dtype=int)

    def check_win(self, x, y, sign):

        counter = self.check_one_way(x, y, -1, 0, sign) + self.check_one_way(x, y, 1, 0, sign) + 1
        if counter == self.winNumber:
            return True

        counter = self.check_one_way(x, y, 0, -1, sign) + self.check_one_way(x, y, 0, 1, sign) + 1
        if counter == self.winNumber:
            return True

        counter = self.check_one_way(x, y, 1, 1, sign) + self.check_one_way(x, y, -1, -1, sign) + 1
        if counter == self.winNumber:
            return True

        counter = self.check_one_way(x, y, 1, -1, sign) + self.check_one_way(x, y, -1, 1, sign) + 1
        if counter == self.winNumber:
            return True

        return False

    def check_one_way(self, x, y, x_direction, y_direction, sign):
        counter = 0
        i = x + x_direction
        j = y + y_direction
        while i >= 0 and j >= 0 and i < self.size and j < self.size and self.board[i][j] == sign:
            counter = counter + 1
            j = j + x_direction
            i = i + y_direction
        return counter

    def change_sign(self, sign):
        if sign == 1:
            return 2
        else:
            return 1

    def reset(self):
        self.board = np.array([[0 for _ in range(self.size)] for _ in range(self.size)], dtype=int)

    def available_moves(self):
        return np.where(self.board.ravel() == 0)[0]

    def tie(self):
        if 0 not in self.board:
            return True
        return False
