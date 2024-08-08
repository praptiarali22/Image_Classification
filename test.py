import os
os.environ['FLASK_APP'] = 'test.py'
os.environ['FLASK_ENV'] = 'development'

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running!"

if __name__ == '__main__':
    app.run(debug=True)
