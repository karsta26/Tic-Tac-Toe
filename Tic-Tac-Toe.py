from flask import Flask, render_template, request
from machine_learning.Agent import Agent

app = Flask(__name__)
agent = Agent()


@app.route('/', methods=['GET', 'POST'])
def get_index():
    if request.args.get('x') and request.args.get('y'):
        x = request.args.get('x')
        y = request.args.get('y')
        enemy_move = agent.make_move(int(x), int(y), 1)
        return enemy_move
    elif request.args.get('reset'):
        agent.reset()
        return 'OK'
    else:
        agent.reset()
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
