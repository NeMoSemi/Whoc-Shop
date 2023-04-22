from flask import Flask, request, url_for, render_template
from jinja2 import FileSystemLoader, Environment

from data import db_session

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='WHOC Shop',
                           username=user)


if __name__ == '__main__':
    db_session.global_init("db/whoc.db")
    app.run(port=8080, host='127.0.0.1')