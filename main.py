from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')

if __name__ == '__main__':
    app.run(debug=True)
