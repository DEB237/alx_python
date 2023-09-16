"""
This script starts a Flask web application:
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Handler function for the '/' route.
    Returns a greeting message.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handler function for the '/hbnb' route.
    Returns 'HBNB'.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Handler function for the '/c/<text>' route.
    Displays 'C ' followed by the value of the 'text' variable.
    Replace underscore (_) symbols with a space.
    """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Handler function for the '/python/<text>' route.
    Displays 'Python ' followed by the value of the 'text' variable.
    Replace underscore (_) symbols with a space.
    The default value of 'text' is 'is cool'.
    """
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Handler function for the '/number/<n>' route.
    Displays '<n> is a number' only if n is an integer.
    """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Handler function for the '/number_template/<n>' route.
    Renders an HTML page with '<n> is a number' inside an H1 tag.
    """
    return render_template('5-number.html', num=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Handler function for the '/number_odd_or_even/<n>' route.
    Renders an HTML page displaying '<n> is even' or '<n> is odd' based on
    the value of n being even or odd.
    """
    return render_template('6-number_odd_or_even.html', num=n)

if __name__ == '__main__':
    """
    Main entry point of the application.
    Starts the Flask web server.
    """
    app.run(host='0.0.0.0', port=5000)