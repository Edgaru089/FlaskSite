from flask import Flask, abort, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/show_entries')
def show_entries():
    return render_template('show_entries.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
