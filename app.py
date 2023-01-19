from flask import Flask
from flask import render_template, request
from labirint_game import Labirint_game
from forms import GameForm
from Config import Config

app =Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    Labirint_game(width=3, height=3)
    return render_template("index.html")

@app.route("/game/", methods=['POST', 'GET'])
def game():
    #form = GameForm()
    game_now = Labirint_game(width=3, height=3)
    form = GameForm()
    if request.method == 'POST':
        way = request.form.get('way')
        steps = request.form.get('number_steps')

    if game_now.win != True:
        print(id(game_now))
        print(game_now.start, game_now.exit, game_now.win)
        return render_template("game.html", game_now=game_now, form=form)
    else:
        return render_template("win_congrats.html")

if __name__ =='__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)