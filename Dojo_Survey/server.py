from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"


@app.route('/')
def index():
    option_list = ['San Jose', 'New York', 'Seattle', 'Burbank', 'Bellevue']
    language_list = ['Python', 'PHP', 'Javascript', 'C#', 'CSS']
    return render_template('index.html', cities=option_list, languages=language_list)

@app.route('/process', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')
 
@app.route('/result')
def show_user():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)