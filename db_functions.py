from data import db_session
from data.products import Products


def add_product(arg_item):
    product = Products()
    product.title = arg_item[4]
    product.about = arg_item[5]
    product.cost = arg_item[6]
    db_sess = db_session.create_session()
    db_sess.add(product)
    db_sess.commit()
    id = db_sess.query(Products).filter(Products.title == arg_item[4]).first().id
    src = f"../static/img/{id}/"
    for i in range(4):
        with open(f"{src}{i + 1}.jpg", "wb") as img:
            img.write(arg_item[i])