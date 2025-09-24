from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start_screen():
    return render_template('start_screen.html')

@app.route('/play')
def play_game():
    # initialize gamestate here

    return render_template('game.html')

if __name__ == "__main__":
    app.run()