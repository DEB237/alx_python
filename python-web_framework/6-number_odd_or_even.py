#!/usr/bin/python3

"""
    Copy the previous task to a new script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”

        /hbnb: display “HBNB”
        
        /c/<text>: display “C ” followed by the value of the text
        variable (replace underscore _ symbols with a space )

        /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        
        The default value of text is “is cool”
        
        /number/<n>: display “n is a number” only if n is an integer
        
        /number_template/<n>: display a HTML page only if n is an integer:
        
            H1 tag: “Number: n” inside the tag BODY
        
            
        /number_odd_or_even/<n>: display a HTML page only if n is an integer:
            
            H1 tag: “Number: n is even|odd” inside the tag BODY
    
    You must use the option strict_slashes=False in your route definition
"""


from flask import Flask, render_template


"""create a web application instance"""
app = Flask(__name__)

"""Define a route for the root URL ("/") and set strict_slashes to False"""
@app.route('/', strict_slashes=False)
def hello():
    """Return the 'Hello HBNB!' message as the response"""
    return 'Hello HBNB!'

"""Define a route for the '/hbnb' URL and set strict_slashes to False"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return the "HBNB" message as the response"""
    return 'HBNB'

"""Define a route for the "/c/<text>" URL and set strict_slashes to False"""
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """replace underscores (_) with spaces in the text variable"""
    text = text.replace("_", " ")
    """Return "C " followed by the value of the text variable"""
    return 'C {}'.format(text)

"""Define a route for the "/python/<text>" URL and set strict_slashes to False"""
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text='is cool'):
    """replace underscores (_) with spaces in the text variable"""
    text = text.replace("_", " ")
    """Return "Python " followed by the value of the text variable"""
    return 'Python {}'.format(text)

"""Define a route for the "/number/<n>" URL and set strict_slashes to False"""
@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """check if n is an integer"""
    if isinstance(n, int):
        """Return "n is a number" only if n is an integer"""
        return '{} is a number'.format(n)
    else:
        """Return a 404 error if n is not an integer"""
        return '{} is a number'.format(n), 404
    
"""define a route for the /number_template/<n> URL and set strict_slashes to False"""
@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """check if n is an integer"""
    if isinstance(n, int):
        """Return "n is a number" only if n is an integer"""
        return render_template('5-number.html', n=n)
    else:
        """Return a 404 error if n is not an integer"""
        return render_template('5-number.html', n=n), 404
    
"""define a route for the /number_odd_or_even/<n> URL and set strict_slashes to False"""
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """check if n is an integer"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, result='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, result='odd')
        """render the 'number_odd_or_even.html' template and pass the value of n and the result to the template"""

if __name__ == '__main__':
    """Start the application and make it listen on IP address 0.0.0.0 and port 5000"""
    app.run(host='0.0.0.0', port=5000)
