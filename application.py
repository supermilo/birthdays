import os
import sqlite3
#from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
#db = SQL("sqlite:///birthdays.db")
conn = sqlite3.connect('birthdays.db', check_same_thread=False)
cursor = conn.cursor()


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        messag = ""
        userDetails = request.form
        name = userDetails['name']
        month = userDetails['month']
        day = userDetails['day']
        if not name:
            messag = "Missing name :("
        elif not month:
            messag = "Missing month :("
        elif not day:
            messag = "Missing day :("
        else:
            cursor.execute(
                "INSERT INTO birthdays (name, month, day) VALUES(?,?,?)", (name,
                month,
                day))

            conn.commit()
            #cursor.close()
        birthdays = cursor.execute("SELECT * FROM birthdays")

        return render_template("index.html", message=messag, birthdays=birthdays)
    else:
        birthdays = cursor.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)

#cursor.close()