# Setup:
# $ pip install Flask
# $ python hello.py
# * Running on http://localhost:5000/

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

