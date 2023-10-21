'''
This python script starts a Flask web application and
displays a text on the screen.

function:
    hello(): Displays a text on the screen
        return - Text

    hbnb(): Displays a text on the screen
        return - Text

    c(text): Displays a text on the screen
        return - Text

    python_(text=none): Displays a text on the screen
        return - Text

    numb(n): Chexks if n is integer
        return - Text
'''

# Import the class Flask from flask module
from flask import Flask, render_template
from markupsafe import escape

# Create an instance of Flask class
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''
    A function that returns a text

    return: a text
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    A function that returns a text

    return: a text
    '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''
    A function that returns a text

    return: a text
    '''
    text = text.replace('_', " ")
    return "C {}".format(escape(text))


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_(text=None):
    '''
    A function that returns a text

    return: a text
    '''
    if text:
        text = text.replace('_', " ")
        return "Python {}".format(text)
    else:
        return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''
    Checks if n is integer

    param:
        n: value to be checked
    return:
        a text
    '''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_html(n):
    '''
    Checks if n is integer

    param:
        n: value to be checked
    return:
        an html resource
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_odd(n):
    '''
    Checks if n is integer, even or odd

    param:
        n: value to be checked
    return:
        an html resource
    '''
    if n % 2 == 0:
        status = 'is even'
    elif n % 2 != 0:
        status = 'is odd'
    return render_template('6-number_odd_or_even.html', n=n, status=status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
