
from nis import cat
from pdb import post_mortem
from flask import Flask,request,render_template, redirect, flash, session
from random import choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey



app = Flask(__name__)
retake_survey = False
app.config['SECRET_KEY'] = "yoyo"
responses = []
question_number = 0
#debug = DebugToolbarExtension(app)


satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])



@app.route('/initiate', methods=["POST"])
def initiate_session():
    session['responses'] = []
    return redirect('/questions/0')



@app.route('/')
def load_survey_home():
    """Return homepage."""
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("survey_form.html",title=title, instructions=instructions)


@app.route('/questions/<random_str>')
def show_question_again(random_str):
    flash(f"Hello little user!! You can't escape this question!!")
    id = len(session['responses'])
    return redirect(f'/questions/{id}')


@app.route('/questions/<int:question_id>')
def show_question(question_id):

    if question_id == len(session['responses']):
        question_obj = satisfaction_survey.questions[question_id]
        question = question_obj.question
        choices = question_obj.choices
        user_text_input = question_obj.allow_text
        return render_template("questions.html", question=question, choices=choices, user_text_input = user_text_input)
    else:
        flash(f"Hello little user!! You can't escape this question!!")
        id = len(session['responses'])
        return redirect(f'/questions/{id}')


@app.route('/answers', methods=["POST"])
def process_answers():
    print(request.method)
    if request.method == 'POST': 
        user_input = request.form["choice"]
        responses = session['responses']
        responses.append(user_input)
        session['responses'] = responses
        question_number = len(session['responses'])
        if question_number < len(satisfaction_survey.questions):
            return redirect(f"/questions/{question_number}")
        else:
            return redirect('/endpage')
    elif request.method == 'GET': 
        question_number = len(session['responses'])
        return redirect(f"/questions/{question_number}")



@app.route('/endpage')
def show_endpage():

    return render_template("endpage.html")    


if __name__ == '__main__':
    app.run()


