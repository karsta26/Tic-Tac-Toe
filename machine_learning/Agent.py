from machine_learning.Learning import Learning


class Agent(object):

    def __init__(self):
        self.learning = Learning()
        self.learning.load_model_from_file()
        self.size = self.learning.env.size

    def make_move(self, x_user, y_user, sign):
        self.learning.env.make_move(x_user * self.size + y_user, sign)

        ai_sign = self.learning.env.game.change_sign(sign)
        ai_action = self.learning.choose_action(ai_sign)

        x_ai = ai_action // self.size
        y_ai = ai_action % self.size

        self.learning.env.make_move(ai_action, ai_sign)

        return 'x={}y={}win={}'.format(x_ai, y_ai, self.learning.env.game.check_win(x_ai, y_ai, ai_sign))

    def reset(self):
        self.learning.env.reset()
