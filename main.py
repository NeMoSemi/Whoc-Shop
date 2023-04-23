from flask import Flask, request, url_for, render_template
# from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from jinja2 import FileSystemLoader, Environment
from data.products import Products

from data import db_session

app = Flask(__name__, template_folder="templates")
# login_manager = LoginManager()
# login_manager.init_app(app)
file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

template = env.get_template("header_and_footer.html")
out = template.render()


@app.route("/")
@app.route("/index")
@app.route("/templates/index.html")
def index():
    previews = []
    with open("templates/preview_of_item.html", mode="r", encoding="utf-8") as form:
        form = form.readlines()
        print(form)
    for i in range(len(items_url)):
        newform = str()
        product = db_sess.query(Products).filter(Products.id == i + 1).first()
        for j in range(len(form)):
            if(j == 3):
                l = '            <img src="'
                r = '" alt="Превью-фото" width="430" height="430">'
                x = l + f"../static/img/{product.id}/1.jpg" + r
                newform += x
                continue
            if(j == 8):
                l = '        <h2>'
                r = '</h2>'
                x = l + f"{product.title}" + r
                newform += x
                continue
            if(j == 9):
                l = '          <a class="contacts-address">'
                r = '</a>'
                x = l + f"{product.about}" + r
                newform += x
                continue
            if(j == 10):
                l = '        <a class="button contacts-button-map" href="'
                r = '">Перейти к товару</a>'
                x = l + f"/templates/item{product.id}.html" + r
                newform += x
                continue
            newform += form[j]
        previews.append(newform)
    return template.render(previews=previews, title="Название товара", about="Описание")


@app.route("/templates/creators.html")
def creators():
    return render_template("creators.html", title="Creators")


@app.route("/templates/about_us.html")
def about_us():
    return render_template("about_us.html", title="About us")


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


if __name__ == "__main__":
    db_session.global_init("db/whoc.db")
    db_sess = db_session.create_session()
    items_url = [f"/templates/item{i[0]}.html" for i in db_sess.query(Products.id).distinct()]
    # print(items_url)
    for url in items_url:
        app.add_url_rule(url, view_func=item)
    app.run(port=8080, host="127.0.0.1")
