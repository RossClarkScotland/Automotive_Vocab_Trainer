import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
import random


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
# Opens the home page
def home():
    return render_template("index.html")


@app.route("/get_terms")
# Opens terms template, lists all course terms alphabetically
def get_terms():
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        return render_template("terms.html", terms=terms)


@app.route("/definitions_first")
# Shows terms page terms by definition first
def definitions_first():
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        return render_template("definitions_first.html", terms=terms)


@app.route("/topics_definitions_first/<topic_id>")
# Shows terms in topic pages by definition first
def topics_definitions_first(topic_id):
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        topic = mongo.db.topics.find_one({"_id": ObjectId(topic_id)})
        return render_template("topics_definitions_first.html", terms=terms, topic=topic)


@app.route("/shuffle_deck")
# Shuffles the order of terms on terms page
def shuffle_deck():
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        random.shuffle(terms)
    return render_template("terms.html", terms=terms)


@app.route("/shuffle_definitions_first")
# Shuffles terms page items when definitions display first
def shuffle_definitions_first():
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        random.shuffle(terms)
    return render_template("definitions_first.html", terms=terms)


@app.route("/shuffle_topics_definitions_first/<topic_id>")
# Shuffles topics pages' items when definitions display first
def shuffle_topics_definitions_first(topic_id):
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        topic = mongo.db.topics.find_one({"_id": ObjectId(topic_id)})
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        random.shuffle(terms)
    return render_template("topics_definitions_first.html", terms=terms, topic=topic)


@app.route("/search", methods=["GET", "POST"])
# Searches terms within terms page
def search():
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        query = request.form.get("query")
        terms = list(mongo.db.terms.find({"$text": {"$search": query}}))
        return render_template("terms.html", terms=terms)


@app.route("/register", methods=["GET", "POST"])
# Enables user registration
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
# Enables users to log in
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
# Renders user profile page
def profile(username):
    if 'user' not in session:
        return render_template("login.html")
    else:
        # gets username of current session user from the database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        terms = list(mongo.db.terms.find().sort("term_name", 1))

        if session["user"]:
            return render_template("profile.html", username=username, terms=terms)

        return redirect(url_for("login"))


@app.route("/logout")
# Logs user out
def logout():
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        # delete user from session cookies
        flash("You have logged out.")
        session.pop("user")
        return redirect(url_for("login"))


@app.route("/add_term", methods=["GET", "POST"])
# Allows user to add to the terms list
def add_term():
    if 'user' not in session:
        return redirect(url_for("login"))
    elif request.method == "POST":
        term = {
            "topic_name": request.form.get("topic_name"),
            "term_name": request.form.get("term_name"),
            "definition": request.form.get("definition"),
            "definition_source": request.form.get("definition_source"),
            "created_by": session["user"]

        }
        mongo.db.terms.insert_one(term)
        flash("You have added a term!")
        return redirect(url_for("get_terms"))

    topics = mongo.db.topics.find()
    return render_template("add_term.html", topics=topics)


@app.route("/edit_term/<term_id>", methods=["GET", "POST"])
# Allows users to edit items in the terms list
def edit_term(term_id):
    if 'user' not in session:
        return redirect(url_for("login"))
    elif request.method == "POST":
        submit = {
            "topic_name": request.form.get("topic_name"),
            "term_name": request.form.get("term_name"),
            "definition": request.form.get("definition"),
            "definition_source": request.form.get("definition_source"),
            "created_by": session["user"]
        }
        mongo.db.terms.update({"_id": ObjectId(term_id)}, submit)
        flash("You have edited the term!")
        return redirect(url_for("get_terms"))

    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    topics = mongo.db.topics.find().sort("topic_name", 1)
    return render_template("edit_term.html", term=term, topics=topics)


@app.route("/delete_term/<term_id>")
# Allows user to delete from the terms list
def delete_term(term_id):
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        mongo.db.terms.remove({"_id": ObjectId(term_id)})
        flash("You have removed a term from the glossary.")
        return redirect(url_for("get_terms"))


@app.route("/get_topics")
# renders topics page
def get_topics():
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        topics = list(mongo.db.topics.find())
        return render_template("topics.html", topics=topics)


@app.route("/add_topic", methods=["GET", "POST"])
# Enables user to add a new topic
def add_topic():
    if 'user' not in session:
        return redirect(url_for("login"))
    elif request.method == "POST":
        topic = {
            "topic_name": request.form.get("topic_name"),
            "img_url": request.form.get("img_url")
        }
        mongo.db.topics.insert_one(topic)
        flash("You added a new topic!")
        return redirect(url_for("get_topics"))

    return render_template("add_topic.html")


@app.route("/edit_topic/<topic_id>", methods=["GET", "POST"])
# Enables user to edit a topic
def edit_topic(topic_id):
    if 'user' not in session:
        return redirect(url_for("login"))
    elif request.method == "POST":
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
# Enables user to delete a topic
def delete_topic(topic_id):
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        mongo.db.topics.remove({"_id": ObjectId(topic_id)})
        flash("You removed a topic!")
        return redirect(url_for("get_topics"))


@app.route("/get_topic/<topic_id>")
# Renders get_topic page
def get_topic(topic_id):
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        topic = mongo.db.topics.find_one({"_id": ObjectId(topic_id)})
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        return render_template("get_topic.html", topic=topic, terms=terms)


@app.route("/shuffle_topic/<topic_id>")
# Shuffles terms within individual topic pages
def shuffle_topic(topic_id):
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        topic = mongo.db.topics.find_one({"_id": ObjectId(topic_id)})
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        random.shuffle(terms)
        return render_template("get_topic.html", topic=topic, terms=terms)


@app.route("/delete")
# Renders delete account page
def delete():
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template("delete.html", username=username)


@app.route("/delete_user")
# Deletes user from the database
def delete_user():
    if 'user' not in session:
        return redirect(url_for("login"))
    else:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        print(username)
        mongo.db.users.delete_one({"username": username})
        flash("You have deleted your account!")
        session.pop("user")
        return render_template("register.html", username=username)


@app.route("/how_to_use")
# Opens the How to use this site page
def how_to_use():
    return render_template("how_to_use.html")



# SET 'DEBUG' TO 'FALSE' BEFORE DEPLOYMENT!
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)