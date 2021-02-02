import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")



@app.route("/get_terms")
def get_terms():
    terms = list(mongo.db.terms.find())
    return render_template("terms.html", terms=terms)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks whether someone else has already taken this username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Someone else already has this username.")
            return redirect(url_for("register"))

        # Takes info from form and stores it in the database
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # new user goes into session cookie
        session["user"] = request.form.get("username").lower()
        flash("All systems go! You have registered successfully!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username":request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("The password and/or username is incorrect.")
                return redirect(url_for("login"))

        else:
            flash("The password and/or username is incorrect.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # gets username of current session user from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # delete user from session cookies
    flash("You have logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_term")
def add_term():
    return render_template("add_term.html")


# SET 'DEBUG' TO 'FALSE' BEFORE DEPLOYMENT!
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)
