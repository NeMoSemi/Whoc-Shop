from flask import Flask, request, url_for, render_template
from jinja2 import FileSystemLoader, Environment


app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='WHOC Shop',
                           username=user)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')