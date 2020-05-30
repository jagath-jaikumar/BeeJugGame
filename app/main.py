from flask import Flask, render_template, request, session
import random


app = Flask(__name__)
app.secret_key = 'some secret key'

@app.route("/")
def home():
    session["name"] = '0'
    session["score"] = 0
    session["checkpoint"] = '/agreement'
    return render_template('game/index.html')



@app.route("/character_select")
def character_select():
    return render_template('game/character_select.html')



@app.route("/agreement", methods=["GET","POST"])
def agreement():

    try:
        session["name"] = request.form["firstname"]
        if session["name"] == "":
            session["name"] = 'Wandering Traveler'
    except:
        pass

    return render_template('game/agreement.html', name=session["name"])


@app.route("/lose")
def lose():
    global score

    lose_options = ['You Lose!', 'Better Luck Next Time', "Gave it your best shot...", "Oh well"]
    index = random.randint(0,len(lose_options)-1)
    lose_line = lose_options[index]

    return render_template('game/lose.html', lose_line = lose_line, score=session["score"], checkpoint=session["checkpoint"])


@app.route("/about")
def about():
    return render_template('extra/about.html')

@app.route("/round1")
def round1():
    return render_template('game/rounds/round1.html')


@app.route("/round2")
def round2():
    return "prep round2"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
