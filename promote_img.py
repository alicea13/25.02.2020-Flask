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


@app.route("/promotion_image")
def promo_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                        <body>
                        <h1>Жди нас, Марс!</h1>   
                        <img src= "{url_for("static", filename='img/MARS.png')}">
                        <div class="alert alert-dark" role="alert">
                            <div class="font-weight-bold">
                                Человечество вырастает из детства.
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="font-weight-bold">
                                Человечеству мала одна планета.
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="font-weight-bold">
                                Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="font-weight-bold">
                                И начнем с Марса!
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="font-weight-bold">
                                Присоединяйся!
                            </div>
                        </div>
                      </head>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
