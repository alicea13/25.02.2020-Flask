from flask import Flask, url_for


i = 0
app = Flask(__name__)


@app.route('/i')
def show_i():
    global i
    i += 1
    return str(i)


@app.route('/greeting/<username>')
def greeting(username):
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                   integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                   crossorigin="anonymous">
                    <title>Привет, {}</title>
                  </head>
                  <body>
                    <h1>Привет, {}!</h1>
                  </body>
                </html>'''.format(username, username)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')