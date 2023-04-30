import flask_login
from flask import Flask, request, render_template, make_response, session, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from jinja2 import FileSystemLoader, Environment
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired

from data import db_session
from data.products import Products
from data.users import Users

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = 'never-gonna-give-you-up'
login_manager = LoginManager()
login_manager.init_app(app)
file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

# template = env.get_template("index.html")
# out = template.render()


@app.route("/")
@app.route("/index")
@app.route("/templates/index.html")
def index():
    previews = []
    for i in range(len(items_url)):
        newform = str()
        product = db_sess.query(Products).filter(Products.id == i + 1).first()

    return render_template("index.html", previews=previews, title="Название товара",
                           about="Описание")


@app.route('/edit_user_profile.html', methods=['post', 'get'])
def edit_user_profile():
    if current_user.is_authenticated:
        if request.method == 'POST':
            about_me1 = request.form.get('aboutme')
            db_ses = db_session.create_session()
            user = db_ses.query(Users).filter(Users.id == current_user.get_id()).first()
            user.about = about_me1
            db_ses.commit()
            if about_me1:
                return redirect("/templates/user.html")
            else:
                return redirect("/templates/user.html")
        return render_template('edit_user.html')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(Users).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/templates/creators.html")
def creators():
    return render_template("creators.html", title="Creators")


@app.route("/templates/catalog.html")
def catalog():
    return render_template("catalog.html", title="Catalog", products=db_sess.query(Products).all())


@app.route("/templates/news.html")
def news():
    return render_template("news.html", title="News")  # , products=db_sess.query(Products).all())


# items_url = ["/templates/item/1.html", "/templates/item/2.html", "/templates/item/3.html"]


@app.route("/templates/item.html")
def item():
    l = 0
    pid = request.base_url
    for i in range(4, len(pid)):
        if(pid[i:-5].isdigit()):
            l = i
            break
    pid = int(request.base_url[l:-5])
    product = db_sess.query(Products).filter(Products.id == pid).first()
    imgAdress = f"../static/img/{product.id}/"
    # print(imgAdress)
    return render_template("item.html", title="About us",
                           productTitle=product.title, about=product.about,
                           cost=product.cost, type=product.instrument_type,
                           image1=imgAdress + "1.jpg", image2=imgAdress + "2.jpg",
                           image3=imgAdress + "3.jpg", image4=imgAdress + "4.jpg")


@app.route("/templates/user.html")
def user():
    if current_user.is_authenticated:
        cur_user = db_sess.query(Users).filter(Users.name == current_user.name).first()
        userId = cur_user.id
        userAbout = "Здесь пока ничего нет"
        if(cur_user.about):
            userAbout = cur_user.about
        print(userId)
        return render_template("user.html", title="User", userAbout=userAbout, userId=userId)


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Users).filter(Users.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)

    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(Users).filter(Users.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = Users(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == "__main__":
    db_session.global_init("db/whoc.db")
    db_sess = db_session.create_session()
    items_url = [f"/templates/item{i[0]}.html" for i in db_sess.query(Products.id).distinct()]
    # print(items_url)
    for url in items_url:
        app.add_url_rule(url, view_func=item)

    app.run(port=8080, host="127.0.0.1")
