from flask import Flask, render_template, escape, url_for, redirect, request, jsonify
from DraBrIW.App.Storage import RDS_UserService, DrinkService, RoundService

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return render_template("index.html")


@flask_app.route('/app')
def app():
    return redirect(url_for('people'))


@flask_app.route('/app/people')
def people():
    return render_template("app/people.html", people=RDS_UserService().get_all())


@flask_app.route('/app/drinks')
def drinks():
    return render_template("app/drinks.html", drinks=DrinkService().get_all())


@flask_app.route('/app/rounds', methods=["GET", "POST"])
def rounds():
    if request.method == "GET":
        return render_template("app/rounds.html", rounds=RoundService().get_all(), people=RDS_UserService().get_all())
    elif request.method == "POST":
        initiator_id = int(request.json["id"])
        RoundService().new_round(RDS_UserService().get_with_uid(initiator_id))
        return jsonify({"status": "ok"})


@flask_app.route('/app/rounds/<int:id>')
def round_id(id: int):
    return render_template("app/round_details.html", round=RoundService().get_with_id(id))


@flask_app.route('/user/<id>')
def get_user(id: int):
    return f"User {escape(id)}"


if flask_app.env == "development":
    @flask_app.after_request
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
