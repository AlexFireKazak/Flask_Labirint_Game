from flask import Flask
from flask import render_template, request
from lab_game import Pole, Player
from forms import GameForm
from Config import Config

app =Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    return render_template("index.html", gamenow=Player())

@app.route("/game/<game_now>", methods=['POST', 'GET'])
@app.route("/game/", methods=['POST', 'GET'])
def game(game_now=None):
    if not game_now:
        game_now = Player()
    print(game_now.__dict__)
    print('1start:', game_now.start, 'exit', game_now.exit, game_now.win)
    form = GameForm()
    if request.method == 'POST':
        way = request.form.get('way')
        steps = int(request.form.get('number_steps'))
        game_now.go_to(way, steps)
        if game_now.win != True:
            print('win?', game_now.win)
            print(id(game_now))
            print('start:', game_now.start, 'exit', game_now.exit, game_now.win)
            return render_template("game.html", game_now=game_now, form=form)
        else:
            return render_template("win_congrats.html", game_now=Player())
    return render_template('game.html', game_now=game_now, form=form)

if __name__ =='__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)