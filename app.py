from flask import Flask, render_template

import os

app = Flask(__name__)

@app.route('/')
def index():
    #return ' 1 Pranks<br><a href="/play">Horn</a>'
    return render_template('index.html')

@app.route('/play')
def play():
    os.system("mpg321 /home/pi/pipranksound/sounds/horn.mp3&")
    return 'You played a prank sound!<br><a href="/">Back to Menu</a>'  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
