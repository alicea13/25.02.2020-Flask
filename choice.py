from flask import Flask


app = Flask(__name__)


@app.route('/choice/<planet_name>')
def planet(planet_name):
    if planet_name.lower() == "меркурий":
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                            <body>
                        <h1 class="font-weight-normal">
                            <h1 class="display-3">
                                Мое предложение: {"меркурий".capitalize()}
                            </h1>
                        </h1>
                        <div class="alert alert-light" role="alert">
                            <div class="h1">
                                    {planets_fact["меркурий"][0]}
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="h1">
                                    {planets_fact["меркурий"][1]}
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="h1">
                                    {planets_fact["меркурий"][2]}
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="h1">
                                    {planets_fact["меркурий"][3]}
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="h1">
                                    {planets_fact["меркурий"][4]}
                            </div>
                        </div>
                            
                      </body>
                    </html>"""
    if planet_name.lower() == "венера":
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                            <body>
                        <h1 class="font-weight-normal">
                            <h1 class="display-3">
                                Мое предложение: {"венера".capitalize()}
                            </h1>
                        </h1>
                        <div class="alert alert-light" role="alert">
                            <div class="h1">
                                    {planets_fact["венера"][0]}
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="h1">
                                    {planets_fact["венера"][1]}
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="h1">
                                    {planets_fact["венера"][2]}
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="h1">
                                    {planets_fact["венера"][3]}
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="h1">
                                    {planets_fact["венера"][4]}
                            </div>
                        </div>

                      </body>
                    </html>"""
    if planet_name.lower() == "земля":
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                            <body>
                        <h1 class="font-weight-normal">
                            <h1 class="display-3">
                                Мое предложение: {"земля".capitalize()}
                            </h1>
                        </h1>
                        <div class="alert alert-light" role="alert">
                            <div class="h1">
                                    {planets_fact["земля"][0]}
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="h1">
                                    {planets_fact["земля"][1]}
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="h1">
                                    {planets_fact["земля"][2]}
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="h1">
                                    {planets_fact["земля"][3]}
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="h1">
                                    {planets_fact["земля"][4]}
                            </div>
                        </div>

                      </body>
                    </html>"""
    if planet_name.lower() == "марс":
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                            <body>
                        <h1 class="font-weight-normal">
                            <h1 class="display-3">
                                Мое предложение: {"марс".capitalize()}
                            </h1>
                        </h1>
                        <div class="alert alert-light" role="alert">
                            <div class="h1">
                                    {planets_fact["марс"][0]}
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="h1">
                                    {planets_fact["марс"][1]}
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="h1">
                                    {planets_fact["марс"][2]}
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="h1">
                                    {planets_fact["марс"][3]}
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="h1">
                                    {planets_fact["марс"][4]}
                            </div>
                        </div>

                      </body>
                    </html>"""
    if planet_name.lower() == "юпитер":
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                            <body>
                        <h1 class="font-weight-normal">
                            <h1 class="display-3">
                                Мое предложение: {"юпитер".capitalize()}
                            </h1>
                        </h1>
                        <div class="alert alert-light" role="alert">
                            <div class="h1">
                                    {planets_fact["юпитер"][0]}
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="h1">
                                    {planets_fact["юпитер"][1]}
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="h1">
                                    {planets_fact["юпитер"][2]}
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="h1">
                                    {planets_fact["юпитер"][3]}
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="h1">
                                    {planets_fact["юпитер"][4]}
                            </div>
                        </div>

                      </body>
                    </html>"""
    if planet_name.lower() == "сатурн":
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                            <body>
                        <h1 class="font-weight-normal">
                            <h1 class="display-3">
                                Мое предложение: {"сатурн".capitalize()}
                            </h1>
                        </h1>
                        <div class="alert alert-light" role="alert">
                            <div class="h1">
                                    {planets_fact["сатурн"][0]}
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="h1">
                                    {planets_fact["сатурн"][1]}
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="h1">
                                    {planets_fact["сатурн"][2]}
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="h1">
                                    {planets_fact["сатурн"][3]}
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="h1">
                                    {planets_fact["сатурн"][4]}
                            </div>
                        </div>

                      </body>
                    </html>"""
    if planet_name.lower() == "уран":
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                            <body>
                        <h1 class="font-weight-normal">
                            <h1 class="display-3">
                                Мое предложение: {"уран".capitalize()}
                            </h1>
                        </h1>
                        <div class="alert alert-light" role="alert">
                            <div class="h1">
                                    {planets_fact["уран"][0]}
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="h1">
                                    {planets_fact["уран"][1]}
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="h1">
                                    {planets_fact["уран"][2]}
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="h1">
                                    {planets_fact["уран"][3]}
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="h1">
                                    {planets_fact["уран"][4]}
                            </div>
                        </div>

                      </body>
                    </html>"""
    if planet_name.lower() == "нептун":
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                            <body>
                        <h1 class="font-weight-normal">
                            <h1 class="display-3">
                                Мое предложение: {"нептун".capitalize()}
                            </h1>
                        </h1>
                        <div class="alert alert-light" role="alert">
                            <div class="h1">
                                    {planets_fact["нептун"][0]}
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="h1">
                                    {planets_fact["нептун"][1]}
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="h1">
                                    {planets_fact["нептун"][2]}
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="h1">
                                    {planets_fact["нептун"][3]}
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="h1">
                                    {planets_fact["нептун"][4]}
                            </div>
                        </div>"""
    if planet_name.lower() == "плутон":
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                           crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                            <body>
                        <h1 class="font-weight-normal">
                            <h1 class="display-3">
                                Мое предложение: {"плутон".capitalize()}
                            </h1>
                        </h1>
                        <div class="alert alert-light" role="alert">
                            <div class="h1">
                                    {planets_fact["плутон"][0]}
                            </div>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <div class="h1">
                                    {planets_fact["плутон"][1]}
                            </div>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <div class="h1">
                                    {planets_fact["плутон"][2]}
                            </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <div class="h1">
                                    {planets_fact["плутон"][3]}
                            </div>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <div class="h1">
                                    {planets_fact["плутон"][4]}
                            </div>
                        </div>"""


planets_fact = {"меркурий": ["Самая медлительная планета;",
                             "Один ее день растягивается почти на полгода земных;",
                             "Достаточно быстрое движение вокруг Солнца;",
                             "Облетает его всего за 88 дней;",
                             "Наконец, она просто красива!"],
                "венера": ["По праву считается самой яркой планетой Солнечной системы;",
                           "Более интенсивно, чем другие, способна отражать солнечный свет.;",
                           "«Возвращая» 76% из 100%;",
                           "Причина – в атмосферном окружении планеты, а конкретно, в ее облаках;",
                           "Наконец, она просто красива!"],
                "земля": ["Единственная из планет, которая не названа в честь божества;",
                          "Вместе с Меркурием, Венерой и Марсом образует группу планет так называемой земной группы;",
                          "Лидирует среди них по массе и размерам,",
                          "А также по степени гравитации и по силе магнитных полей;",
                          "Наконец, она просто красива!"],
                "марс": ["Единственная планета нашей системы, имеющая красноватый оттенок",
                         "Диаметр Марса равен 6800 км. Он меньше Венеры и Земли, но больше Меркурия;",
                         "Является рекордсменом среди прочих как обладательница самой высокой горы;",
                         "Местный вулкан Олимп поднимается в высоту на 27 километров;",
                         "Наконец, она просто красива!"],
                "юпитер": ["Самая быстрая по скорости оборота вокруг собственной оси;",
                           "Делает полное вращение всего за 12 часов;",
                           "Делает оборот вокруг Солнца за целых 12 лет;",
                           "Потоки атмосферы на нем приходят в движение за счет круговорота воды;",
                           "Наконец, она просто красива!"],
                "сатурн": ["На втором месте по количеству спутников;",
                           "У него их 60. Больше только у Юпитера – 63;",
                           "Самая далекая планета Солнечной системы, видимая невооруженным глазом;",
                         "Чтобы совершить один оборот вокруг Солнца, ему требуется 29,5 лет;",
                           "Наконец, она просто красива!"],
                "уран": ["Расположение наиболее точно соответствует условной вертикальной оси:",
                         "Он находится к ней под углом 98 градусов;",
                         "Уран является одной из наиболее холодной планетой в Солнечной системе;",
                         "Лето длится 42 года;",
                         "Наконец, она просто красива!"],
                "нептун": ["Плутон и Нептун находятся между собою в орбитальном резонансе «два к трем»;",
                           "Нептун производит три оборота вокруг звезды;",
                           "Часто разгуливаются ветры;",
                           "Их скорость может достигать 320 км в час;",
                           "Наконец, она просто красива!"],
                "плутон": ["Плутон и Нептун находятся между собою в орбитальном резонансе «два к трем»;",
                           "Плутон производит два оборота вокруг звезды;",
                           "Еще не так давно астрономия считала, что в Солнечной системе 9 планет;",
                           "В 2006 году решением Астрономического союза Плутон был исключен из общего списка;",
                           "Причиной стали небольшие размеры, не позволяющие причислять его к планетам;",
                           ]
                }

if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
