from flask import Flask,request,render_template
from random import choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story


app = Flask(__name__)
app.config['SECRET_KEY'] = "yoyo"

@app.route('/')
def load_madlibs():
    """Return homepage."""

    return render_template("madlibs_form.html")

@app.route('/story')
def make_story():
    if request.args.get("place") and request.args.get("noun") and request.args.get("verb") and request.args.get("adjective") and request.args.get("plural_noun"):
        ans = dict()
        ans["place"] = request.args.get("place")
        ans["noun"] = request.args.get("noun")
        ans["verb"] = request.args.get("verb")
        ans["adjective"] = request.args.get("adjective")
        ans["plural_noun"] = request.args.get("plural_noun")
        
        story = Story(
            [request.args.get("place"), request.args.get("noun"), request.args.get("verb"), request.args.get("adjective"), request.args.get("plural_noun")],
            """Once upon a time in a long-ago {place}, there lived a
            large {adjective} {noun}. It loved to {verb} {plural_noun}."""
        )
        story_text = story.generate(ans)
    else:
        story_text = "Sorry one of the fields were missing input!!"

    #return story_text + str(ans) + str(request.args)
    return render_template("story.html", story_text = story_text)
