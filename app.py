"""Example of flask main file."""
from flask import Flask
app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


@app.route('/api/readiness')
def readiness():
    """Returns readiness-ok message."""
    return 'readiness-ok'


@app.route('/api/liveness')
def liveness():
    """Returns liveness-ok message."""
    return 'liveness-ok'


if __name__ == '__main__':
    app.run()
