from flask import Flask
from flask import url_for


app = Flask(__name__)


@app.route('/')
@app.route('/index')
# @app.route('/hello')
def index():
    return 'Hello, Yandex!'


@app.route('/countdown')
def countdown():
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append('Пуск!')
    return '</br>'.join(countdown_list)


@app.route('/image_sample')
def image_sample():
    return '''<img src= "{}" alt="Здесь была сова">'''.format(
        url_for("static", filename='img/owl.jpeg'))
#     return '''<img src="/static/img/riana.jpg" alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel ="stylesheet" type="text/css" href="{
                    url_for('static', filename="css/style.css")}" />
                    <title>Привет, Яндекс!</title>    
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>   
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')