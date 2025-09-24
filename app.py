from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start_screen():
    return render_template('start_screen.html')