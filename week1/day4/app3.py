from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def route():
    return render_template("index.html")

@app.route("/form",methods=["POST"])
def form():
    name=request.form.get("name")
    return f"{name}"

if __name__ == "__main__":
    app.run(debug=True)