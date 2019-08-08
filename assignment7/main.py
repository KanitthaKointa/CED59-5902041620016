from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


app = Flask(__name__)

@app.route('/')
def member():
    return render_template('meaw.html')

@app.route('/',methods=['post'])
def Register():
    return 'Register Ok Hahahaha';

if __name__ == "__main__":
    app.run(debug=True)