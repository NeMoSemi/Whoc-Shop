import uuid
import urllib


class User:
    def __init__(self, f_n, s_n, age, prof_foto, password):
        self.id = uuid.uuid4()
        self.first_name = f_n
        self.second_name = s_n
        self.age = age
        self.prof_foto = prof_foto
        self.password = password

    def change_prof_foto(self, new_foto):
        self.prof_foto = new_foto

    def info(self):
        return [self.id, self.first_name, self.second_name, self.age, self.prof_foto, self.password]

