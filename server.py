import json

from flask import Flask, Response, render_template, request

from src.openai_util import get_gpt_response


app = Flask(__name__)

@app.route('/view-five-simple')
def view_five_simple():
    return render_template('view_five_simple.html')

@app.route('/view-five-complex')
def view_five_complex():
    return render_template('view_five_complex.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_gpt_response', methods=['POST'])
def do_get_gpt_response():
    data = get_gpt_response(request.form['prompt'], int(request.form['max_tokens']))
    resp = Response(json.dumps(data).encode('utf8'), status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run(debug=True)
