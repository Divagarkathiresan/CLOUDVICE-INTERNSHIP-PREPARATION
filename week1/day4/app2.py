from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def route():
    return "App is running"

@app.route("/name")
def dispName():
    return render_template("index.html",name="Divagar",age=21)

if __name__ == "__main__":
    app.run(debug=True)