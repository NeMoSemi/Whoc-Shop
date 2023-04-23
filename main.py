from flask import Flask, request, url_for, render_template
# from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from jinja2 import FileSystemLoader, Environment
from data.products import Products

from data import db_session

app = Flask(__name__, template_folder='templates')
# login_manager = LoginManager()
# login_manager.init_app(app)
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('header_and_footer.html')
out = template.render()

@app.route('/')
@app.route('/index')
@app.route('/templates/index.html')
def index():
    return template.render()


@app.route('/templates/creators.html')
def creators():
    return render_template('creators.html', title='Creators')


@app.route('/templates/about_us.html')
def about_us():
     return render_template('about_us.html', title='About us')


@app.route('/templates/item.html')
def item():
    db_sess = db_session.create_session()
    product = db_sess.query(Products).filter(Products.id == 1).first()
    imgAdress = f"../static/img/{product.id}/"
    print(imgAdress)
    return render_template('item.html', title='About us',
                           productTitle=product.title, about=product.about,
                           cost=product.cost, type=product.instrument_type,
                           image1=imgAdress+"1.jpg", image2=imgAdress+"2.jpg",
                           image3=imgAdress+"3.jpg", image4=imgAdress+"4.jpg")


if __name__ == '__main__':
    db_session.global_init("db/whoc.db")
    app.run(port=8080, host='127.0.0.1')
