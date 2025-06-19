from flask import Flask, render_template, request , redirect ,url_for , flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key'  


class login_page(FlaskForm):
    user = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(),Email()])
    passwords = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("login")


@app.route('/', methods = ["GET" , "POST"])
def homepage():
     return render_template("home_page.html")

@app.route('/login', methods = ["POST" , "GET"])
def login():
     form = login_page()
     if form.validate_on_submit():
          user = form.user.data
          email = form.email.data
          passwords = form.passwords.data
          return redirect(url_for("homapage"))
     return render_template("login.html", form = form)

@app.route('/about')
def about():
     return render_template("about.html")

if __name__ == "__main__":
     app.run( debug = True , port = 15000)