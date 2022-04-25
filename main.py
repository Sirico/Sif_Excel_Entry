from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



# Lists
brand = ['Addidas', 'Nike', 'Puma']
colour = ['Red', 'Black', 'Blue']
gender = ['Men','Women','Kids']

# flask instant
app = Flask(__name__)


# Route_Decorator
@app.route('/')
def index():
    first_name = "Darren"
    return render_template('index.html', first_name=first_name,brand = brand)


#Variables



# localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#Error pages

#
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500





