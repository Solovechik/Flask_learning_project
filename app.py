from flask import Flask, render_template, request
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.form:
        x = int(request.form['width'])
        y = int(request.form['height'])
        GameOfLife(x, y)
    else:
        GameOfLife(25, 25)
    return render_template('index.html', title='Welcome!')


@app.route('/live')
def live():
    cnt = GameOfLife()
    cnt = cnt.counter
    if cnt > 0:
        new_generation = GameOfLife()
        new_generation.form_new_generation()
        new_generation = new_generation.world
    else:
        new_generation = GameOfLife()
        new_generation.generate_universe()
        new_generation = new_generation.world
    old_generation = GameOfLife()
    old_generation = old_generation.old_world
    alive_cells = GameOfLife()
    alive_cells = alive_cells.alive_cells
    if cnt > 1 and old_generation == new_generation or alive_cells == 0:
        return render_template('game_over.html', title='Game Over!')
    return render_template('live.html', new_generation=new_generation, counter=cnt, old_generation=old_generation, title='Game "LIFE"')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


