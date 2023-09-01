"""
This script starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Handler function for the '/' route.
    Returns a greeting message.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    """
    Main entry point of the application.
    Starts the Flask web server.
    """
    app.run(host='0.0.0.0', port=5000)