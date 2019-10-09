from flask import render_template, escape, url_for, redirect, request, jsonify
from App.Storage import UserService, DrinkService, RoundService
from App.User import User
from FlaskFrontend import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/app')
def base_app():
    return redirect(url_for('people'))


@app.route('/app/people', methods=["GET", "POST"])
def people():
    print(request.endpoint)
    if request.method == "GET":
        return render_template("app/people.html", people=UserService().get_all(), drinks=DrinkService().get_all())
    elif request.method == "POST":
        first_name = request.json["personFirstName"]
        last_name = request.json["personLastName"]
        new_user = User(first_name, last_name)
        UserService().add(new_user)
        return jsonify({"status": "ok"})


@app.route('/app/people/<int:person_id>', methods=["POST"])
def person_edit(person_id: int):
    if request.method == "POST":
        drink_id = request.json["drinkId"]
        UserService().change_drink(person_id, drink_id)
        return jsonify({"status": "ok"})


@app.route('/app/drinks', methods=["GET", "POST"])
def drinks():
    if request.method == "GET":
        return render_template("app/drinks.html", drinks=DrinkService().get_all())
    elif request.method == "POST":
        drink_name = request.json["drinkName"]
        DrinkService().add(drink_name)
        return jsonify({"status": "ok"})


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
        rnd = RoundService().get_with_id(round_id)
        return render_template("app/round_details.html", round=rnd,
                               people=UserService().get_all(), drinks=DrinkService().get_all())
    elif request.method == "POST":
        if request.json["action"] == "close":
            RoundService().close_round(round_id)
        else:
            person_id = int(request.json["personId"])
            drink_id = request.json["drinkId"] if "drinkId" in request.json else None
            RoundService().add_person(round_id, person_id, drink_id)
        return jsonify({"status": "ok"})


@app.route('/user/<id>')
def get_user(id: int):
    return f"User {escape(id)}"


@app.template_test("not in")
def not_in(item, iterable):
    return item not in iterable


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
