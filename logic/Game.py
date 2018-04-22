import random

class Game(object):

    def __init__(self):
        self.size = 10
        self.winNumber = 5
        self.board = [['-' for x in range(self.size)] for y in range(self.size)]

    def start(self):
        sign = random.choice(['X', 'O'])
        while True:
            self.draw_board()
            place = input()
            place = place.split(' ')
            if 1 <= int(place[0]) <= self.size and 1 <= int(place[1]) <= self.size and self.board[int(place[0])-1][int(place[1])-1] == '-':
                self.board[int(place[0])-1][int(place[1])-1] = sign
                if sign == 'O':
                    sign = 'X'
                else:
                    sign = 'O'
            else:
                print("Error!")
            if self.check_board():
                print("End")
                self.draw_board()
                break

    def draw_board(self):
        for x in range(self.size):
            for y in range(self.size):
                print(self.board[x][y], end=" ")
            print()

    def check_board(self):

        for i in range(self.size):
            for j in range(0, self.size - self.winNumber):
                counter = 0
                for k in range(self.winNumber):
                    if self.board[i][j] != '-' and self.board[i][j] == self.board[i][j+k]:
                        counter = counter + 1
                if counter >= self.winNumber:
                    return True

        for i in range(self.size):
            for j in range(0, self.size - self.winNumber):
                counter = 0
                for k in range(self.winNumber):
                    if self.board[j][i] != '-' and self.board[j][i] == self.board[j+k][i]:
                        counter = counter + 1
                    if counter >= self.winNumber:
                        return True

        for i in range(self.size - self.winNumber + 1):
            for j in range(self.size - self.winNumber + 1):
                counter = 0
                for k in range(self.winNumber):
                    if self.board[i][j] != '-' and self.board[i][j] == self.board[i + k][j + k]:
                        counter = counter + 1
                    if counter >= self.winNumber:
                        return True

        for i in range(self.size - self.winNumber):
            for j in range(self.winNumber - 1, self.size):
                counter = 0
                for k in range(self.winNumber):
                    if self.board[i][j] != '-' and self.board[i][j] == self.board[i + k][j - k]:
                        counter = counter + 1
                    if counter >= self.winNumber:
                        return True
        return False


if __name__ == "__main__":
    game = Game()
    game.start()