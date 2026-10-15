from flask import Flask,request,render_template
import sqlite3

app=Flask(__name__)

def dbCreation():
    connection = sqlite3.connect("users.db")
    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)
    connection.close()

@app.route("/")
def route():
    return render_template("home.html")

@app.route("/form",methods=["POST"])
def addUser():
    connection = sqlite3.connect("users.db")
    name=request.form.get("name")
    connection.execute("insert into users (name) values (?)",(name,))
    connection.commit()
    connection.close()
    return "user added"

@app.route("/getUsers")
def allUsers():
    connection = sqlite3.connect("users.db")
    ListOfUsers=connection.execute("select * from users").fetchall()
    return render_template("listOfUsers.html",users=ListOfUsers)

if __name__=="__main__":
    dbCreation()
    app.run(debug=True)