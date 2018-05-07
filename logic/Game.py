import random
import numpy as np

class Game(object):

    def __init__(self):
        self.size = 19
        self.winNumber = 5
        self.board = np.array([['-' for x in range(self.size)] for y in range(self.size)])

    def start(self):
        sign = random.choice(['X', 'O'])
        while True:
            self.draw_board()
            place = input()
            place = place.split(' ')
            if 1 <= int(place[0]) <= self.size and 1 <= int(place[1]) <= self.size and self.board[int(place[0])-1][int(place[1])-1] == '-':
                self.board[int(place[0])-1][int(place[1])-1] = sign
                if self.check_win(int(place[0])-1, int(place[1])-1, sign):
                    print(sign + " wins")
                    self.draw_board()
                    break
                if self.is_board_full():
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
        lcounter = 0
        rcounter = 0
        while self.board[i][y] == sign:
            lcounter = lcounter + 1
            i = i - 1

        i = x + 1
        while i < self.size and self.board[i][y] == sign:
            rcounter = rcounter + 1
            i = i + 1

        counter = lcounter + rcounter + 1
        if counter == self.winNumber:
            return True

        j = y - 1
        upcounter = 0
        downcounter = 0
        while self.board[x][j] == sign:
            downcounter = downcounter + 1
            j = j - 1

        j = y + 1
        while j < self.size and self.board[x][j] == sign:
            upcounter = upcounter + 1
            j = j + 1

        counter = upcounter + downcounter + 1
        if counter == self.winNumber:
            return True

        i = x + 1
        j = y + 1
        rdowncounter = 0
        lupcounter = 0
        while i < self.size and j < self.size and self.board[i][j] == sign:
            rdowncounter = rdowncounter + 1
            j = j + 1
            i = i + 1

        i = x - 1
        j = y - 1
        while j < self.size and self.board[i][j] == sign:
            lupcounter = lupcounter + 1
            j = j - 1
            i = i - 1

        counter = lupcounter + rdowncounter + 1
        if counter == self.winNumber:
            return True

        i = x + 1
        j = y - 1
        rupcounter = 0
        ldowncounter = 0
        while i < self.size and self.board[i][j] == sign:
            rupcounter = rupcounter + 1
            j = j - 1
            i = i + 1

        i = x - 1
        j = y + 1
        while j < self.size and self.board[i][j] == sign:
            ldowncounter = ldowncounter + 1
            j = j + 1
            i = i - 1

        counter = ldowncounter + rupcounter + 1
        if counter == self.winNumber:
            return True

        return False

    def is_board_full(self):
        answer = True
        for sublist in self.board:
            if '-' in sublist:
                answer = False
        return answer


if __name__ == "__main__":
    game = Game()
    game.start()