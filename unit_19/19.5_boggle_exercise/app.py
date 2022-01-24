from flask import Flask, request, render_template, redirect, session, jsonify
from boggle import Boggle

boggle_obj = Boggle()
backend_board = boggle_obj.make_board()
print(backend_board)
words = [word.lower() for word in boggle_obj.words]
app = Flask(__name__)
app.config['TESTING'] = True
app.config['SECRET_KEY'] = "yoyo"
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


@app.route('/')
def index():
    """Show homepage."""

    return render_template("startpage.html")


@app.route('/init', methods=["POST"])
def initiate_session():
    session['board'] = backend_board
    username = request.form.get("username", "User1")
    session['username'] = username
    session['score'] = 0
    session['guesses'] = []

    return redirect('/board')


@app.route('/board')
def show_board():
    """Show homepage."""
    board = session['board']
    username = session['username']
    score = session['score']
    return render_template("board.html", board=board, username=username, score=score)


@app.route('/boggleapi', methods=['GET'])
def process_guess():
    result_data = dict()
    result_data['username'] = session['username']
    guess = request.args.get("guess")
    is_valid_guess = False
    is_duplicate = False
    if guess in session['guesses']:
        is_duplicate = True

    validity_result = ""
    result_data['score'] = session['score']
    result_data['guesses'] = []
    result_data['guesses'].append(guess)
    result_data['is_duplicate'] = is_duplicate
    session['guesses'] = result_data['guesses']

    if guess.lower() in words:
        is_valid_guess = True
        validity_result = boggle_obj.check_valid_word(backend_board, guess.lower())
        result_data['result'] = validity_result
        result_data['is_valid_guess'] = is_valid_guess
    else:
        result_data['result'] = 'not-a-word'
        result_data['is_valid_guess'] = is_valid_guess

    if validity_result == 'ok':
        if not is_duplicate:
            current_score = session['score']
            current_score += 1
            session['score'] = current_score
            result_data['score'] = session['score']
        else:
            result_data['score'] = session['score']

    return jsonify(result_data)


if __name__ == '__main__':
    app.run()
