from flask import Flask, jsonify, request
from flask_cors import CORS

from server.search import search

app = Flask(__name__)
CORS(app)

import sys

sys.path.append('')


@app.route('/', methods=['GET'])
def index():
    return jsonify('hahah')


@app.route('/search', methods=['GET', 'POST'])
def movies():
    text = request.args.get('q', '')
    if text != '':
        result = search(text)
        return jsonify(result['hits']['hits'])
    else:
        return jsonify('none')


if __name__ == "__main__":
    app.run(debug=True)
