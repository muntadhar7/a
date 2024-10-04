from flask import  Flask
from ai import output

app = Flask(__name__)

@app.route("/")
def home():
    return output

if __name__ == "__main__":
    app.run(debug=True)
