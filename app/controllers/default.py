from flask import render_template, flash
from flask_login import login_user
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
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.data.password:
            login_user(user)
            flash("Logged in")
        else:
            flash("Invalid Login")
    else:
        print(form.errors)
    return render_template('login.html', form=form)

#User.query.filter_by(password="1234").all()  é o Linq/Lambad do Flask
#r.name, é possível alterar o dado do bando de dados (update)

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    r = User.query.filter_by(password="1234").first() 
    print(r.name, r.email)
    return "OK"