from flask import Flask, request, url_for, render_template
from jinja2 import FileSystemLoader, Environment

from data import db_session

app = Flask(__name__, template_folder='templates')
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('header_and_footer.html')
out = template.render()

@app.route('/')
@app.route('/index')
def index():
    # user = "Ученик Яндекс.Лицея"
    return template.render()


if __name__ == '__main__':
    db_session.global_init("db/whoc.db")
    app.run(port=8080, host='127.0.0.1')