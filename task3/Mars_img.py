from flask import Flask
from flask import url_for


app = Flask(__name__)


@app.route('/')
def text():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    promo_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                  'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                  'Присоединяйся!']
    return '</br>'.join(promo_list)


@app.route('/image_mars')
def mars_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                        <body>
                        <h1>Жди нас, Марс!</h1>   
                        <img src= "{url_for("static", filename='img/MARS.png')}">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_1.css')}" />
                        <h2>Вот она какая, красная планета.</h2>
                      </head>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
