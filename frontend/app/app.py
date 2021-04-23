from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    string = None
    backend = 'pwdgen_backend:7777'

    if request.method == 'POST':
        uppercase = True if request.form.get('uppercase') else False
        digits = True if request.form.get('digits') else False
        symbols = True if request.form.get('symbols') else False
        length = request.form.get('length')
        string = requests.get('http://{0}/&length={1}&digits={2}&symbols={3}&uppercase={4}'.format(
                                                                            backend,
                                                                            length,
                                                                            digits,
                                                                            symbols,
                                                                            uppercase)).text
    return render_template('index.html', string=string)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
