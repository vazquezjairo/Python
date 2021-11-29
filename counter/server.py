from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'
app.count = 0

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:    
        session["count"] += 1
    return render_template("index.html")    



@app.route("/count", methods=["POST"])
def addCount():
    if request.form["click"]=="add2":
        session["count"] += 1
    elif request.form["click"]=="reset":
        session["count"] = 0
    return redirect("/")



@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)