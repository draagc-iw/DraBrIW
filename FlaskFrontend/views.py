from flask import Flask, render_template, escape, url_for, redirect, request, jsonify
from DraBrIW.App.Storage import UserService, DrinkService, RoundService
from FlaskFrontend import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/app')
def app():
    return redirect(url_for('people'))


@app.route('/app/people')
def people():
    return render_template("app/people.html", people=UserService().get_all())


@app.route('/app/drinks')
def drinks():
    return render_template("app/drinks.html", drinks=DrinkService().get_all())


@app.route('/app/rounds', methods=["GET", "POST"])
def rounds():
    if request.method == "GET":
        return render_template("app/rounds.html", rounds=RoundService().get_all(), people=UserService().get_all())
    elif request.method == "POST":
        initiator_id = int(request.json["id"])
        RoundService().new_round(UserService().get_with_uid(initiator_id))
        return jsonify({"status": "ok"})


@app.route('/app/rounds/<int:round_id>', methods=["GET", "POST"])
def round_details(round_id: int):
    if request.method == "GET":
        return render_template("app/round_details.html", round=RoundService().get_with_id(round_id),
                               people_service=UserService(), drinks_service=DrinkService())
    elif request.method == "POST":
        person_id = int(request.json["personId"])
        drink_id = int(request.json["drinkId"])
        RoundService().add_person(round_id, person_id, drink_id)
        return jsonify({"status": "ok"})


@app.route('/user/<id>')
def get_user(id: int):
    return f"User {escape(id)}"


if app.env == "development":
    @app.after_request
    def add_header(r):
        """
        Add headers to both force latest IE rendering engine or Chrome Frame,
        and also to cache the rendered page for 10 minutes.
        """
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
        return r
