from flask import Flask, render_template, request, session, redirect, url_for
import utils

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query_string = request.form["question"]
        result = utils.look_up(query_string)
        return render_template("result.html", result=result)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.debug = True
    app.secret_key = utils.secret_key
    app.run('0.0.0.0', port=8000)
