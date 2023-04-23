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
@app.route('/templates/index.html')
def index():
    # user = "Ученик Яндекс.Лицея"
    return template.render()


@app.route('/templates/creators.html')
def creators():
    return render_template('creators.html', title='Creators')


@app.route('/templates/about_us.html')
def about_us():
    return render_template('about_us.html', title='About us')


if __name__ == '__main__':
    db_session.global_init("db/whoc.db")
    app.run(port=8080, host='127.0.0.1')