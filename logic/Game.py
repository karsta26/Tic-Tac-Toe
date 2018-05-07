import random
import numpy as np


class Game(object):

    def __init__(self):
        self.size = 19
        self.winNumber = 5
        self.board = np.array([['-' for x in range(self.size)] for y in range(self.size)])

    def start(self):
        sign = random.choice(['X', 'O'])
        counter = 0
        while True:
            self.draw_board()
            place = input()
            place = place.split(' ')
            if 1 <= int(place[0]) <= self.size and 1 <= int(place[1]) <= self.size and '-' == \
                    self.board[int(place[0]) - 1][int(place[1]) - 1]:
                self.board[int(place[0]) - 1][int(place[1]) - 1] = sign
                counter = counter + 1
                if self.check_win(int(place[0]) - 1, int(place[1]) - 1, sign):
                    print(sign + " wins")
                    self.draw_board()
                    break
                if counter == self.size * self.size:
                    print("Tie")
                    break
                if sign == 'O':
                    sign = 'X'
                else:
                    sign = 'O'
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
        while self.board[i][y] == sign:
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
        while self.board[x][j] == sign:
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
        while j < self.size and self.board[i][j] == sign:
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
        while i < self.size and self.board[i][j] == sign:
            right_up_counter = right_up_counter + 1
            j = j - 1
            i = i + 1

        i = x - 1
        j = y + 1
        while j < self.size and self.board[i][j] == sign:
            left_down_counter = left_down_counter + 1
            j = j + 1
            i = i - 1

        counter = left_down_counter + right_up_counter + 1
        if counter == self.winNumber:
            return True

        return False


if __name__ == "__main__":
    game = Game()
    game.start()
