from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9!</h1>' \
           '<h3>Type a "/" after the address in your search bar, followed by your guess.</h3>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return '<h1 style="color: red">Too high, guess again!</h1>' \
               '<img src="https://media.giphy.com/media/5noddpPJQxDNDaPWaP/giphy.gif">'
    elif guess < random_number:
        return '<h1 style="color: blue">Too low, guess again!</h1>' \
               '<img src="https://media.giphy.com/media/B0AXfj1DdyoBAT6Ehn/giphy.gif">'

    else:
        return '<h1 style="color: green">You guessed correctly!!</h1>' \
               '<img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif">'


if __name__ == "__main__":
    app.run()
