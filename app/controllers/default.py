from flask import render_template, flash, redirect, url_for, request #Render_Template é uma função do Flask para abrir os arquivos '.html'
from flask_login import login_user, logout_user
from app import app, lm, mongo #chamando as classes do Config.py
from bson.objectid import ObjectId

from app.models.tables import User #importando dados de users
from app.models.forms import LoginForm

@lm.user_loader #Carregar o objeto de usuario no flask_login
def load_user(id):
    return mongo.db.users.find_one({'_id':id})

@app.route("/index")
@app.route("/") #decorator, é uma caracteristica do python que coloca antes e uma função. Para aplicar uma função em cima de outra
def index():    #FUnção route em cima da função index '/' é a rota da página
    online_users = mongo.db.users.find({'online': True})
    return render_template('index.html', online_users = online_users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users
        login_user = user.find_one({'_id' : ObjectId(form.username.data) })
        if login_user:
        #existing_user = users.find_one({'_id' : form.username })
            print(user)
        # if(user) and user.password == form.password.data:
        #     flash("Logged in successfully")
        #     #login_user(user)
        #     return redirect(url_for("index"))
        # else:
        #     flash("Logged in not successfully")
    return render_template('login.html', form=form)


#dar um free no objeto usuario do flask_login
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
    user_collection = mongo.db.users
    user_collection.insert({'username' : 'teste'}, { unique : true })
    return "ok"