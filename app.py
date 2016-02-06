from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Pranks<br><a href="/play">Horn</a>'

@app.route('/play')
def play():
    os.system("omxplayer -o local /home/pi/pipranksound/sounds/horn.mp3")
    return 'You played a prank sound!<br><a href="/">Back to Menu</a>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
