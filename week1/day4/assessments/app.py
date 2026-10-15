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
    session["userName"]=userName
    session["password"]=password

    return redirect(url_for('home'))

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

if __name__=="__main__":
    dbConnection()
    app.run(debug=True)