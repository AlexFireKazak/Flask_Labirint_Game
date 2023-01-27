from flask import Flask
from flask import render_template, request
from labirint_game import Labirint_Game
from forms import GameForm, UserNameForm
from Config import Config
import random

app =Flask(__name__)
app.config.from_object(Config)

with open("Phrases.txt", 'r', encoding="utf-8") as phrases:
    text_steps = phrases.readlines()


@app.route("/", methods=['POST', 'GET'])
def index():
#    form = UserNameForm()
 #   if request.method == 'POST':
 #       user_name = request.form.get('user_name')
    return render_template("index.html", game_now=Labirint_Game())


@app.route("/game/", methods=['POST', 'GET'])
def game(game_now=Labirint_Game()):
    print('1start:', game_now.start, 'exit', game_now.exit, game_now.win)
    form = GameForm()
    if request.method == 'POST':
        way = request.form.get('way')
        steps = int(request.form.get('number_steps'))
        game_now.go_to(way, steps)
        if game_now.win != True:
            print('start:', game_now.start, 'exit', game_now.exit, game_now.win)
            return render_template("game.html", game_now=game_now, form=form, steps=random.choice(text_steps))
        else:
            return render_template("win_congrats.html", game_now=game_now.new_start_exit())
    return render_template('game.html', game_now=game_now, form=form)

if __name__ =='__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)