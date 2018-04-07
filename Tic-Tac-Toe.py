from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def get_index():
    return send_from_directory('static', 'index.html')


if __name__ == '__main__':
    app.run(debug=True)