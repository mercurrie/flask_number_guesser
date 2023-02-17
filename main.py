from flask import Flask
import random
import json

app = Flask(__name__)
random_number = random.randint(0, 9)
data_file = open('data.json')
DATA = json.load(data_file)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9!</h1>' \
           '<h3>Type a "/" after the address in your search bar, followed by your guess.</h3>' \
           f'<img src={DATA["HOME_IMG"]}>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return f'<h1 style={DATA["HIGH_COLOR"]}>Too high, guess again!</h1>' \
               f'<img src={DATA["HIGH_IMG"]}>'
    elif guess < random_number:
        return f'<h1 style={DATA["LOW_COLOR"]}>Too low, guess again!</h1>' \
               f'<img src={DATA["LOW_IMG"]}>'

    else:
        return f'<h1 style={DATA["CORRECT_COLOR"]}>You guessed correctly!!</h1>' \
               f'<img src={DATA["CORRECT_IMG"]}>'


if __name__ == "__main__":
    app.run()
