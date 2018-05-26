import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.models import load_model
from machine_learning.TicTacToe import TicTacToe


class Learning(object):

    def __init__(self):
        self.env = TicTacToe()
        self.model = None
        self.file_name = 'model_{}_{}.h5'.format(self.env.game.size, self.env.game.winNumber)
        self.y = 0.95
        self.eps = 0.5
        self.decay_factor = 0.999

    def load_model_from_file(self, path_to_file=""):
        try:
            self.model = load_model(path_to_file + self.file_name)
            # without this line model does not work correctly
            self.model.predict(np.expand_dims(self.env.state, axis=0))[0]
            print('model loaded')
        except:
            print('model not found - creating new one')
            self.create_new_model()

    def create_new_model(self):
        self.model = Sequential()
        self.model.add(Flatten(input_shape=self.env.observation_space.shape))
        self.model.add(Dense(100, activation='sigmoid'))
        self.model.add(Dense(self.env.action_space.n, activation='linear'))
        self.model.compile(loss='mse', optimizer='adam', metrics=['mae'])
        self.model.summary()

    def choose_action(self, sign):
        predictions = []
        if sign == 1:
            predictions = self.model.predict(np.expand_dims(self.env.state, axis=0))[0]
        elif sign == 2:
            predictions = self.model.predict(np.expand_dims(self.env.state[::-1], axis=0))[0]

        action = np.argmax(predictions)
        moves = self.env.game.available_moves()
        next_max_value = 1

        if action not in moves:
            sorted_array = np.sort(predictions)[::-1]

            while action not in moves:
                q_value = sorted_array[next_max_value]
                next_max_value += 1
                item_index = np.where(predictions == q_value)
                action = item_index[0][0]

        return action

    def start_learning(self, num_episodes=1000):
        result = {-1: 0, 0: 0, 1: 0}
        for i in range(num_episodes):
            if i % 100 == 0:
                print("Episode {} of {}".format(i + 1, num_episodes))
            state = self.env.reset()
            self.eps *= self.decay_factor
            done = False
            while not done:
                if np.random.random() < self.eps:
                    moves = self.env.game.available_moves()
                    action = np.random.choice(moves)
                else:
                    action = self.choose_action(1)

                new_state, reward, done, _ = self.env.step(action)

                target = reward + self.y * np.max(self.model.predict(np.expand_dims(new_state, axis=0)))
                target_vec = self.model.predict(np.expand_dims(state, axis=0))[0]
                target_vec[action] = target

                self.model.fit(np.expand_dims(state, axis=0),
                               target_vec.reshape(-1, self.env.game.size * self.env.game.size),
                               epochs=1, verbose=0)

                state = new_state

                if done and num_episodes > 200:
                    result[reward] += 1

        self.model.save(self.file_name)

        print('#' * 10)
        print('win: {}'.format(result[1]))
        print('draw: {}'.format(result[0]))
        print('lost: {}'.format(result[-1]))


if __name__ == "__main__":
    learn = Learning()
    learn.load_model_from_file()
    learn.start_learning()
