from flask import Flask, render_template, request

from logic.Game import Game

app = Flask(__name__)

game = Game()


@app.route('/', methods=['GET', 'POST'])
def get_index():
    if request.args.get('x') and request.args.get('y'):
        x = request.args.get('x')
        y = request.args.get('y')
        enemy_move = game.make_move(int(x) + 1, int(y) + 1, 1)
        return enemy_move
    else:
        game.reset_file_board()
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
