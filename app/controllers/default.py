from flask import render_template, flash, redirect, url_for #Render_Template é uma função do Flask para abrir os arquivos '.html'
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm

#load_user é uma função que faz o carregamento dos usuários
@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/") #decorator, é uma caracteristica do python que coloca antes e uma função. Para aplicar uma função em cima de outra
def index():    #FUnção route em cima da função index '/' é a rota da página
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
            flash("Logged in")
        else:  
            flash("Invalid Login")
    return render_template('login.html', form=form)

#dar um free no usuario
@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))

#User.query.filter_by(password="1234").all()  é o Linq/Lambad do Flask
#r.name, é possível alterar o dado do bando de dados (update)

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    r = User.query.filter_by(password="1234").first() 
    print(r.name, r.email)
    
    return "OK"