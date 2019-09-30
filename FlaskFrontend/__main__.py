from flask import Flask, render_template, escape, url_for, redirect
from DraBrIW.App.Storage import RDS_UserService, DrinkService

flask_app = Flask(__name__)


# flask_app.config(extra_files=['./static/css/app.css'])

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
    print(DrinkService().get_all())
    return render_template("app/drinks.html", drinks=DrinkService().get_all())


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
