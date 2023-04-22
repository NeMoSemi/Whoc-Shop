import uuid


class Product:
    def __init__(self, name, description, foto, us_who_post):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.foto = foto
        self.us_who_post = us_who_post.info()
        self.us_post_id = self.us_who_post[0]
        self.is_not_bought = True

    def info(self):
        return [self.id, self.us_who_post, self.name, self.description, self.foto]

    def buy_status(self):
        return self.is_not_bought

    def change_buy_status(self):
        self.is_not_bought = False