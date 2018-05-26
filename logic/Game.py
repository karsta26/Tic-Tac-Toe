import numpy as np


class Game(object):

    def __init__(self):
        self.size = 19
        self.winNumber = 5
        self.board = np.array([[0 for _ in range(self.size)] for _ in range(self.size)], dtype=int)

    def check_win(self, x, y, sign):

        i = x - 1
        left_counter = 0
        right_counter = 0
        while i >= 0 and self.board[i][y] == sign:
            left_counter = left_counter + 1
            i = i - 1

        i = x + 1
        while i < self.size and self.board[i][y] == sign:
            right_counter = right_counter + 1
            i = i + 1

        counter = left_counter + right_counter + 1
        if counter == self.winNumber:
            return True

        j = y - 1
        up_counter = 0
        down_counter = 0
        while j >= 0 and self.board[x][j] == sign:
            down_counter = down_counter + 1
            j = j - 1

        j = y + 1
        while j < self.size and self.board[x][j] == sign:
            up_counter = up_counter + 1
            j = j + 1

        counter = up_counter + down_counter + 1
        if counter == self.winNumber:
            return True

        i = x + 1
        j = y + 1
        right_down_counter = 0
        left_up_counter = 0
        while i < self.size and j < self.size and self.board[i][j] == sign:
            right_down_counter = right_down_counter + 1
            j = j + 1
            i = i + 1

        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0 and self.board[i][j] == sign:
            left_up_counter = left_up_counter + 1
            j = j - 1
            i = i - 1

        counter = left_up_counter + right_down_counter + 1
        if counter == self.winNumber:
            return True

        i = x + 1
        j = y - 1
        right_up_counter = 0
        left_down_counter = 0
        while j >= 0 and i < self.size and self.board[i][j] == sign:
            right_up_counter = right_up_counter + 1
            j = j - 1
            i = i + 1

        i = x - 1
        j = y + 1
        while i >= 0 and j < self.size and self.board[i][j] == sign:
            left_down_counter = left_down_counter + 1
            j = j + 1
            i = i - 1

        counter = left_down_counter + right_up_counter + 1
        if counter == self.winNumber:
            return True

        return False

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
