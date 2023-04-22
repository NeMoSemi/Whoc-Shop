from flask import Flask, request, url_for, render_template
from jinja2 import FileSystemLoader, Environment


app = Flask(__name__, template_folder='templates')
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

#template = env.get_template('header_and_footer.html')
#out = template.render()
#print(out)

@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    #return template.render()
    return render_template('catalog-item.html', title='WHOC Shop',
                           username=user)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')