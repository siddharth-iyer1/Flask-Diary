from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calendar.html')

@app.route('/journal/<date>')
def journal(date):
    return render_template('journal.html', date=date)

if __name__ == '__main__':
    app.run(debug=True)
