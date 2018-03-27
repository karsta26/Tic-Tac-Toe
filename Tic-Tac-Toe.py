from flask import Flask, send_from_directory
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def get_index():
    return send_from_directory('static', 'index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5123)
