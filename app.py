
from flask_wtf import FlaskForm
from flask import Flask, render_template, jsonify, session
from flask_bootstrap import  Bootstrap
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired
from ai import AiModel

app = Flask(__name__)
app.config['SECRET_KEY'] = "12341234"
Bootstrap(app)


class MyForm(FlaskForm):
    message = StringField(label="Message", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def chat():
    if 'history' not in session:
        session['history'] = []  # Initialize history in the session

    model = AiModel()  # Always create a new model instance

    form = MyForm()
    if form.validate_on_submit():
        user_message = form.message.data
        # Append user message to history
        session['history'].append({"role": "user", "text": user_message})

        # Generate a response
        response = model.generate(user_message)
        bot_response = "AI: '" + response + "'"

        # Append bot response to history
        session['history'].append({"role": "bot", "text": response})

        return jsonify(user_message=user_message, bot_response=bot_response)

    return render_template("chat.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)
