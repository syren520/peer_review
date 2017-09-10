from flask import Flask
from flask import render_template
from service.Scheme import get_scheme
from flask import request

app = Flask(__name__)


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/scheme', methods=['POST', 'GET'])
def scheme():
    fellow_amount = int(request.form['fellow_amount'])
    amount_of_video_to_watch = int(request.form['amount_of_video_to_watch'])
    if fellow_amount <= amount_of_video_to_watch:
        return render_template('error.html')
    else:
        scheme_data = get_scheme(int(request.form['fellow_amount']), int(request.form['amount_of_video_to_watch']))

        return render_template('scheme.html', scheme=enumerate(scheme_data))
