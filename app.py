from flask import Flask, render_template

app = Flask(__name__)

# Dummy leaderboard data
leaderboard_data = [
    {'username': 'player1', 'score': 100},
    {'username': 'player2', 'score': 90},
    {'username': 'player3', 'score': 80},
    {'username': 'player4', 'score': 70},
    {'username': 'player5', 'score': 60},
]

@app.route('/')
def leaderboard():
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
