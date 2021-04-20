from flask import Flask
import random
import string


app = Flask(__name__)


def random_str(string, length):
    return ''.join(random.choice(string) for i in range(length))


def generate_string(length=8,
                    uppercase=False,
                    symbols=False,
                    digits=False):

    lc = random_str(string.ascii_lowercase, length*11)
    uc = ''
    sls = ''
    dg = ''

    if uppercase:
        uc = random_str(string.ascii_uppercase, length*11)
    if symbols:
        sls = random_str(string.punctuation, length*11)
    if digits:
        dg = random_str(string.digits, length*11)

    full = uc+sls+lc+dg

    shuffle = ''.join(random.sample(full, len(full)))

    return(shuffle[:length])





@app.route('/<query>', methods=['GET'])
def get_query(query):
    symbols = False
    uppercase = False
    digits = False
    length = 8

    if 'symbols' in query and 'length' in query and 'uppercase' in query and 'digits' in query:
        args = query.split('&')
        for i in args:
            if i == ''or i == ' ':
                continue
            type = i.split('=')[0].lower()
            state = i.split('=')[1].lower()
            if type == 'symbols' and state == 'true':
                symbols = True
                print('symbols true')
            if type == 'uppercase' and state == 'true':
                uppercase = True
                print('uppercase true')
            if type == 'digits' and state == 'true':
                digits = True
                print('digits true')
            if type == 'length':
                length = int(state)

        passwd = generate_string(length, uppercase, symbols, digits)
        print(passwd)
        return str(passwd)
    else:
        args = ['error']
    return 'hello world {}'.format(args)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
