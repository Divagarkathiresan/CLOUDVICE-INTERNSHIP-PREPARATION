from flask import Flask,render_template,request,session,redirect,url_for
import sqlite3

app=Flask(__name__)
app.secret_key="mySecretKey"

def dbConnection():
    connection=sqlite3.connect("users.db")
    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            password TEXT
        )
    """)
    connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                status TEXT
            )
        """)
    connection.close()


@app.route("/")
def home():
    if 'userName' in session:
        return render_template("homePage.html",userName=session["userName"],password=session["password"])
    return render_template("loginPage.html")


@app.route("/login",methods=["POST"])
def login():

    userName=request.form.get("name")
    password=request.form.get("password")
    connection = sqlite3.connect("users.db")
    user = connection.execute("SELECT name, password FROM users WHERE name = ? AND password = ?",(userName, password)).fetchone()
    connection.close()

    if user:
        session["userName"] = user[0]
        session["password"]=user[1]
        return redirect(url_for("home"))

    return f"Invalid user, register first"


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        userName=request.form.get("name")
        password=request.form.get("password")
        Connection=sqlite3.connect("users.db")
        Connection.execute("insert into users (name,password) values (?,?)",(userName,password))
        Connection.commit()
        Connection.close()

        return redirect(url_for('home'))

    return render_template("registerPage.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route("/add-task",methods=["POST"])
def addTask():
    task=request.form.get("task")
    Connection=sqlite3.connect("users.db")
    Connection.execute("insert into tasks (title,status) values (?,?)",(task,"PENDING"))
    Connection.commit()
    Connection.close()
    return redirect(url_for('getTasks'))

@app.route("/get-task")
def getTasks():
    Connection=sqlite3.connect("users.db")
    tasks=Connection.execute("select * from tasks").fetchall()
    return render_template('Tasks.html',tasks=tasks)


if __name__=="__main__":
    dbConnection()
    app.run(debug=True)