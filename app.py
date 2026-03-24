from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return f'<h1> Bosh sahifa </h1>'

@app.route('/about')
def haqida():
    return f'Bu About sahifasi'

@app.route('/data')
def datalar():
    my_list = list(range(1, 11))
    return f'List qiymatlari: {my_list}'


if __name__ == '__main__':
    app.run(debug=True)
