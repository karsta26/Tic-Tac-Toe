import requests
import time


class ModelSource(object):

    def __init__(self):
        self.URL = "http://gomokuonline.com/gomoku"
        params = {'reset': 'true', 'play': 'false', 'random': self.get_random()}
        r = requests.get(url=self.URL, params=params)
        self.cookies = dict(JSESSIONID=r.cookies['JSESSIONID'])

    @staticmethod
    def get_random():
        return int(round(time.time() * 1000))

    def get_ai_move(self, x_user, y_user):
        params = {'x': x_user, 'y': y_user, 'random': self.get_random()}

        r = requests.get(url=self.URL, params=params, cookies=self.cookies)
        data = r.json()

        x_ai = data[1]
        y_ai = data[2]

        return x_ai, y_ai

    def reset(self):
        params = {'reset': 'true', 'play': 'false', 'random': self.get_random()}
        r = requests.get(url=self.URL, params=params)
        self.cookies = dict(JSESSIONID=r.cookies['JSESSIONID'])
