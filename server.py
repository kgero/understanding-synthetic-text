import json

from flask import Flask, Response, render_template, request

from src.openai_util import get_gpt_response


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', results=['a', 'b'])

@app.route('/get_gpt_response', methods=['POST'])
def get_words_thes():
    data = get_gpt_response(request.form['prompt'])
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run(debug=True)
