from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

@app.route("/index")
@app.route("/") #decorator, é uma caracteristica do python que coloca antes e uma função. Para aplicar uma função em cima de outra
def index():    #FUnção route em cima da função index '/' é a rota da página
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = User("Vitoria", "1234", "Vitoria Fernandes", "vitfCastro@jona.com")
    db.session.add(i)
    db.session.commit()
    return "OK"