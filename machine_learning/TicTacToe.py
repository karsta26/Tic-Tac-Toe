import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from logic.Game import Game


class TicTacToe(gym.Env):

    def __init__(self):
        self.game = Game()
        self.size = self.game.size

        low = np.array([[0 for _ in range(self.size)] for _ in range(self.size)])
        low = np.array([low, low])

        high = np.array([[1 for _ in range(self.size)] for _ in range(self.size)])
        high = np.array([high, high])

        self.action_space = spaces.Discrete(self.size * self.size)
        self.observation_space = spaces.Box(low, high)

        self.seed()
        self.state = low

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def get_action_for_opponent(self, random=True):
        moves = self.game.available_moves()
        if random:
            move = np.random.choice(moves)
            return move
        else:
            raise NotImplemented

    def make_move(self, action, sign):
        x = action // self.size
        y = action % self.size

        if sign == 1:
            self.state[0][x][y] = 1
            self.game.board[x][y] = 1
        elif sign == 2:
            self.state[1][x][y] = 1
            self.game.board[x][y] = 2

        return x, y

    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))

        reward = 0.0
        done = False

        x_1, y_1 = self.make_move(action, 1)

        if self.game.check_win(x_1, y_1, 1):
            reward = 1.0
            done = True
        else:
            opponent_action = self.get_action_for_opponent(random=True)
            x_2, y_2 = self.make_move(opponent_action, 2)

            if self.game.check_win(x_2, y_2, 2):
                reward = -1.0
                done = True
            elif self.game.tie():
                reward = 0.0
                done = True

        return self.state, reward, done, {}

    def reset(self):
        self.game.reset()

        low = np.array([[0 for _ in range(self.size)] for _ in range(self.size)])
        low = np.array([low, low])

        self.state = low

        return self.state

    def render(self, mode='human'):
        if not (mode == 'human'):
            print(self.game.board)
        return None

    def close(self):
        pass
