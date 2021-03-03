from flask import Flask
app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

if __name__ == '__main__':
    app.run(debug=True)