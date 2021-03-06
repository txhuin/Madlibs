from random import sample
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# # route to handle the landing page of a website.
# @app.route('/')
# def start_here():
#     return "Hi! This is the home page."

# # route to display a simple web page
@app.route('/')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html", person=player, compliment=compliment)


@app.route('/game')
def show_game_form():
    response = request.args.get("response")

    print response
    if response == "yes":
        return render_template("game.html")
    else:

        return render_template("goodbye.html")

@app.route('/madlib', methods=["GET","POST"])
def show_madlib():

    person = request.args.get("person")
    noun= request.args.get("noun")
    adjective= request.args.get("adjective")
    color = request.args.get("color")
    animals = request.args.getlist("animals")

    random_template= choice(["madlib.html","madlib2.html","madlib3.html", "madlib4.html"])
    print random_template


    return render_template(random_template, person=person, noun=noun, adjective=adjective, 
        color=color, animals=animals)
    

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
