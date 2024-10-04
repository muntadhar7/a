from tkinter import Label

from flask import Flask, render_template, FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

class MyForm(FlaskForm):
    prompt = StringField(label="Prompt", validators=[DataRequired()])
    submit = SubmitField()

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
