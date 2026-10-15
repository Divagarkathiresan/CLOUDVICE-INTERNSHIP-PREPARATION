from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "This is an about page"

@app.route("/contact")
def contact():
    return "This is a contact page"

@app.route("/user/<name>")
def getName(name):
    return f"Hello , {name}"

if __name__ == "__main__":
    app.run(debug=True)