from flask import Flask
import random
app = Flask(__name__)


random_number = random.randint(1, 10)


@app.route("/")
def home():
    image_path = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
    return "<body>" \
           "<p>Guess the number between 1 to 10 and enter it in the url \"numbers/(your guessed number)\"</p>" \
           f"<img src={image_path}>" \
           "</body>"


@app.route("/numbers/<int:guessed_number>")
def guess_number(guessed_number):
    higher_img_path = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    lower_img_path = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    correct_img_path = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
    out_of_the_img_path = "https://media.giphy.com/media/FOL5mK0tXUmXe/giphy.gif"
    # random_number = random.randint(1, 10)
    if 11 > guessed_number > random_number:
        return "<body>" \
               "<p>Your guess is higher than the actual number</p>" \
               f"<img src={higher_img_path}>" \
               "</body>"
    elif 0 < guessed_number < random_number:
        return "<body>" \
               "<p>Your guess is lower than the actual number</p>" \
               f"<img src={lower_img_path}>" \
               "</body>"
    elif guessed_number == random_number:
        return "<body>" \
               "<p>You guessed the right number!!</p>" \
               f"<img src={correct_img_path}>" \
               "</body>"
    else:
        return "<body>" \
               "<p>Why are you guessing out of the range number?</p>" \
               f"<img src={out_of_the_img_path}>" \
               "</body>"


if __name__ == "__main__":
    app.run(debug=True)
