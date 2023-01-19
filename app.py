from flask import Flask
from flask import render_template
from labirint_game import Labirint_game
from forms import GameForm
import Config

app =Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/game/")
def game():
    form = GameForm()
    game_now = Labirint_game()
    if game_now.win != True:
        return render_template("game.html", game_now=game_now, form=form)
    else:
        return render_template("win_congrats.html")

if __name__ =='__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)