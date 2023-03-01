from boggle import Boggle

from flask import Flask, redirect, jsonify, request, render_template, session, redirect

app = Flask(__name__)

app.config["SECRET_KEY"] = "sehrgeheim"


boggle_game = Boggle()
game_board = []





@app.route('/')
def show_start():
    """ Shows Start Page"""
    return render_template('start.html')


@app.route('/game')
def start_game():
    """ Builds Gameboard, initializes session and render Game Page"""
    game_board = boggle_game.make_board()
    session['board'] = game_board
    session['words'] = []
    session ['num_of_game'] = 0
    session ['high_score'] = 0
    return render_template('game.html', board=game_board, num_games = session ['num_of_game'], high_score = session ['high_score'])

@app.route('/newgame')
def new_game():
    """ Builds Gameboard and GAme Page but with realtime session values"""
    game_board = boggle_game.make_board()
    session['board'] = game_board
    high_score = session ['high_score']
    num_of_game = session['num_of_game']
    print("new game")
    return render_template('game.html', board=game_board, num_games = session ['num_of_game'], high_score = session ['high_score'])


@app.route('/guess', methods= ['POST'])
def validate_guess():
    """ gets players guess and returns validation status"""
    guess =  request.get_json()['guess'].lower()
    if guess in session['words']:
        return "Already scored that one!"
    if boggle_game.check_valid_word(session['board'], guess) == "ok":
        words = session['words']
        words.append(guess)
        session['words'] = words
    return boggle_game.check_valid_word(session['board'], guess)
    

@app.route('/gameend', methods= ['POST'])
def end_game():
    """ Receives Score at the end of game from backend and increases num of game var"""
    score =  request.get_json()['score']
    session["num_of_game"] += 1
    if score > session["high_score"]:
        session["high_score"] = score
    return redirect('/newgame')
    
    
