from flask import Flask, render_template, request
app = Flask(__name__)

name = '0'
score = 0

@app.route("/")
def hello():
    return render_template('game/index.html')



@app.route("/character_select")
def character_select():
    return render_template('game/character_select.html')



@app.route("/agreement", methods=["GET","POST"])
def agreement():
    global name

    name = request.form["firstname"]
    if name == "":
        name = 'Wandering Traveler'

    return render_template('game/agreement.html', name=name)


@app.route("/lose")
def lose():

    return "you lose"


@app.route("/round1")
def round1():
    return "prep round1"


@app.route("/round2")
def round2():
    return "prep round2"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
