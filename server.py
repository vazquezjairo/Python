from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def check4():
    return render_template("index4.html")

@app.route('/<int:x>/<int:y>')
def xyindex(x,y):
    return render_template("xyindex.html",id_num1=x,id_num2=y)

if __name__ == "__main__":
    app.run(debug=True, port=8000)