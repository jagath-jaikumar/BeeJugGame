from flask import Flask, render_template, request, session
import random




app = Flask(__name__)

app.secret_key = 'some secret key'


@app.route("/")
def home():
    session["name"] = '0'
    session["score"] = 0
    session["checkpoint"] = '/agreement'
    session["round1complete"] = False
    session["round1vars"] = []
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

    lose_options = ['You Lose!', 'Better Luck Next Time', "Gave it your best shot...", "Oh well"]
    index = random.randint(0,len(lose_options)-1)
    lose_line = lose_options[index]

    return render_template('game/lose.html', lose_line = lose_line, score=session["score"], checkpoint=session["checkpoint"])


@app.route("/about")
def about():
    return render_template('extra/about.html')

@app.route("/round1", defaults={'option': None})
@app.route("/round1/<option>")
def round1(option):



    print(option)
    if option == 'option1':
        session["round1vars"].append(1)
    if option == 'option2':
        session["round1vars"].append(2)
    if option == 'option3':
        session["round1vars"].append(3)
    session.modified = True
    print(session["round1vars"])

    if 1 in session["round1vars"] and 2 in session["round1vars"] and 3 in session["round1vars"]:
        session["round1complete"] = True


    return render_template('game/rounds/round1.html', round1complete = session["round1complete"], option = option)


@app.route("/round2")
def round2():
    return "prep round2"

if __name__ == "__main__":
    # Only for debugging while developing

    app.run(host='0.0.0.0', debug=True, port=80)
