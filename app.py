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
    terms = list(mongo.db.terms.find().sort("term_name", 1))
    return render_template("terms.html", terms=terms)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    terms = list(mongo.db.terms.find({"$text": {"$search": query}}))
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

        # Credit to my fellow student Helen Goatly for helping me work out,
        # via Slack, that the two following lines of code were necessary
        password = request.form.get("password")
        passwordcheck = request.form.get("passwordcheck")

        # Ensures the user has entered their password as intended
        if password != passwordcheck:
            flash("Passwords do not match! Please try again.")
            return redirect(url_for("register"))

        if password == passwordcheck:
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


@app.route("/add_term", methods=["GET", "POST"])
def add_term():
    if request.method == "POST":
        term = {
            "topic_name": request.form.get("topic_name"),
            "term_name": request.form.get("term_name"),
            "definition": request.form.get("definition"),
            "definition_source": request.form.get("definition_source"),
            "created_by": session["user"]

        }
        mongo.db.terms.insert_one(term)
        flash("You have added a term to the glossary!")
        return redirect(url_for("get_terms"))

    topics = mongo.db.topics.find()
    return render_template("add_term.html", topics=topics)


@app.route("/edit_term/<term_id>", methods=["GET", "POST"])
def edit_term(term_id):
    if request.method == "POST":
        submit = {
            "topic_name": request.form.get("topic_name"),
            "term_name": request.form.get("term_name"),
            "definition": request.form.get("definition"),
            "definition_source": request.form.get("definition_source"),
            "created_by": session["user"]
        }
        mongo.db.terms.update({"_id": ObjectId(term_id)}, submit)
        flash("You have edited the term!")

    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    topics = mongo.db.topics.find().sort("topic_name", 1)
    return render_template("edit_term.html", term=term, topics=topics)


@app.route("/delete_term/<term_id>")
@app.route("/delete_term/<term_id>")
def delete_term(term_id):
    mongo.db.terms.remove({"_id": ObjectId(term_id)})
    flash("You have removed a term from the glossary.")
    return redirect(url_for("get_terms"))


@app.route("/get_topics")
def get_topics():
    topics = list(mongo.db.topics.find())
    return render_template("topics.html", topics=topics)


@app.route("/add_topic", methods=["GET", "POST"])
def add_topic():
    if request.method == "POST":
        topic = {
            "topic_name": request.form.get("topic_name"),
            "img_url": request.form.get("img_url")
        }
        mongo.db.topics.insert_one(topic)
        flash("You added a new topic!")
        return redirect(url_for("get_topics"))

    return render_template("add_topic.html")


@app.route("/edit_topic/<topic_id>", methods=["GET", "POST"])
def edit_topic(topic_id):
    if request.method == "POST":
        submit = {
            "topic_name": request.form.get("topic_name"),
            "img_url": request.form.get("img_url")
        }
        mongo.db.topics.update({"_id": ObjectId(topic_id)}, submit)
        flash("You edited the topic!")
        return redirect(url_for("get_topics"))

    topic = mongo.db.topics.find_one({"_id": ObjectId(topic_id)})
    return render_template("edit_topic.html", topic=topic)


@app.route("/delete_topic/<topic_id>")
def delete_topic(topic_id):
    mongo.db.topics.remove({"_id": ObjectId(topic_id)})
    flash("You removed a topic!")
    return redirect(url_for("get_topics"))


# SET 'DEBUG' TO 'FALSE' BEFORE DEPLOYMENT!
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)
