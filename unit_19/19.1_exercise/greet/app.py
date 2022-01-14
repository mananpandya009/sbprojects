from flask import Flask,request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"



@app.route('/welcome/home')
def w_home():
    return "welcome home"



@app.route('/welcome/back')
def w_back():
    return "welcome back"