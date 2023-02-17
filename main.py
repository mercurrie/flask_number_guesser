from flask import Flask
import random
import json

app = Flask(__name__)
random_number = random.randint(0, 9)
data_file = open('data.json')
DATA = json.load(data_file)


@app.route('/')
def home():
    return f'<h1>{DATA["HOME_H1"]}</h1>' \
           f'<h3>{DATA["HOME_H3"]}</h3>' \
           f'<img src={DATA["HOME_IMG"]}>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return f'<h1 style={DATA["HIGH_COLOR"]}>{DATA["HIGH_MESSAGE"]}</h1>' \
               f'<img src={DATA["HIGH_IMG"]}>'
    elif guess < random_number:
        return f'<h1 style={DATA["LOW_COLOR"]}>{DATA["LOW_MESSAGE"]}</h1>' \
               f'<img src={DATA["LOW_IMG"]}>'

    else:
        return f'<h1 style={DATA["CORRECT_COLOR"]}>{DATA["CORRECT_MESSAGE"]}</h1>' \
               f'<img src={DATA["CORRECT_IMG"]}>'


if __name__ == "__main__":
    app.run()
