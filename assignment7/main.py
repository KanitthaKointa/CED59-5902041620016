from flask import Flask,render_template , request
from wtforms import StringField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

class RegisterForm(FlaskForm):
    Firstname = StringField("FirstName", validators=[InputRequired()])
    Lastname = StringField("Lastname", validators=[InputRequired()])
    Email = StringField("Email",  validators=[InputRequired("Please enter your email address."), Email("Please enter your email again.")])
    Username = StringField("Username", validators=[InputRequired()])
    Password = PasswordField("Password", validators=[InputRequired(), Length(min=8, message="Please enter your password 8 character.")])

@app.route('/')
def student():
    form = RegisterForm()
    return render_template('meaw.html', form=form)


@app.route('/regis', methods=["GET", "POST"])
def regis():
    form = RegisterForm()
    if form.validate_on_submit():
        return "Register OK"
    return render_template('meaw.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)