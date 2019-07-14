from flask import render_template
from app import app

@app.route("/index")
@app.route("/") #decorator, é uma caracteristica do python que coloca antes e uma função. Para aplicar uma função em cima de outra
def index():    #FUnção route em cima da função index '/' é a rota da página
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('base.html')


# @app.route("/test", defaults={'name' : None})
# @app.route("/test/<name>")#Chamando uma variavel
# def test(name): #2 contrutores? 
#     if name:
#         return "Olar, <b> %s</b> t!" % name #imprimindo com a variavel
#     else:
#         return "Olar, usuário"