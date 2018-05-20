import random
import numpy as np


class Game(object):

    def __init__(self):
        self.size = 19
        self.winNumber = 5
        self.board = np.array([[0 for _ in range(self.size)] for _ in range(self.size)], dtype=int)

    def start(self):
        counter = 0
        sign = random.randint(1, 2)
        self.reset_file_board()
        while True:
            self.draw_board()
            place = input()
            place = place.split(' ')
            if 1 <= int(place[0]) <= self.size and 1 <= int(place[1]) <= self.size and 0 == \
                    self.board[int(place[0]) - 1][int(place[1]) - 1]:
                self.make_move(int(place[0]), int(place[1]), sign)
                counter = counter + 1
                if self.check_win(int(place[0]) - 1, int(place[1]) - 1, sign):
                    print(str(sign) + " wins")
                    self.draw_board()
                    break
                if counter == self.size * self.size:
                    print("Tie")
                    break
            else:
                print("Error!")

    def draw_board(self):
        for x in range(self.size):
            for y in range(self.size):
                print(self.board[x][y], end=" ")
            print()

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

    def save_board(self):
        np.savetxt("board.txt", self.board, fmt='%i')

    def load_board(self):
        self.board = np.loadtxt("board.txt", dtype=int)

    def reset_file_board(self):
        self.board = np.array([[0 for _ in range(self.size)] for _ in range(self.size)], dtype=int)
        self.save_board()

    def make_move(self, x, y, sign):
        self.load_board()
        self.board[x - 1][y - 1] = sign
        x_enemy = random.randint(0, self.size - 1)
        y_enemy = random.randint(0, self.size - 1)
        while self.board[x_enemy][y_enemy] != 0:
            x_enemy = random.randint(0, self.size - 1)
            y_enemy = random.randint(0, self.size - 1)
        self.board[x_enemy][y_enemy] = self.change_sign(sign)
        self.save_board()
        return 'x={}y={}win={}'.format(x_enemy, y_enemy, self.check_win(x_enemy, y_enemy, 2))

    def change_sign(self, sign):
        if sign == 1:
            return 2
        else:
            return 1


if __name__ == "__main__":
    game = Game()
    game.start()
