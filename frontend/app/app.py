from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    string = None
    if request.method == 'POST':
        uppercase = True if request.form.get('uppercase') else False
        digits = True if request.form.get('digits') else False
        symbols = True if request.form.get('symbols') else False
        length = request.form.get('length')

        string = requests.get('http://localhost:5000/generate/&length={0}&digits={1}&symbols={2}&uppercase={3}'.format(
                                                                            length,
                                                                            digits,
                                                                            symbols,
                                                                            uppercase)).text
    return render_template('index.html', string=string)


@app.route('/generate/<query>')
def generate(query):
    backend = 'pwdgen_backend:7777'
    return requests.get('http://{0}/{1}'.format(backend,query)).text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
