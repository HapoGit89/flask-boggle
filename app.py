from boggle import Boggle

from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)

app.config["SECRET_KEY"] = "sehrgeheim"


boggle_game = Boggle()
game_board = []




@app.route('/')
def show_start():
        return render_template('start.html')


@app.route('/game')
def start_game():
    game_board = boggle_game.make_board()
    session['board'] = game_board
    print (session['board'])
    return render_template('game.html', board=game_board)



@app.route('/guess', methods= ['POST'])
def validate_guess():
    guess =  request.get_json()['guess']
    print(guess)
    if boggle_game.check_valid_word(game_board, guess['guess']) == True:
        print("Valid")
    else:
        print("not Valid")    
    return f"{guess}"

