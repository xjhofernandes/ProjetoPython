from flask import render_template, flash, redirect, url_for, request #Render_Template é uma função do Flask para abrir os arquivos '.html'
from flask_login import login_user, logout_user
from app import app, lm, mongo #chamando as classes do Config.py
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.tables import User #importando dados de users
from app.models.forms import LoginForm, SearchForm #chamando o forms

@lm.user_loader #Carregar o objeto de usuario no flask_login
def load_user(username):
    u = mongo.db.users.find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])

@app.route("/index",methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST']) #decorator, é uma caracteristica do python que coloca antes e uma função. Para aplicar uma função em cima de outra
def index():    #FUnção route em cima da função index '/' é a rota da página
    online_users = mongo.db.users.find({'online': True})
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', online_users = online_users, form = search)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = mongo.db.users.find_one({"_id": form.username.data})
        print(user)
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully")
            return redirect(url_for("index"))
        flash("Wrong username or password")
    return render_template('login.html', title='login', form=form)



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
    hashed_value = generate_password_hash('1234')
    store_password = hashed_value
    user_collection = mongo.db.users
    user_collection.insert({'username' : 'senha','password' : store_password})
    return hashed_value

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    print(search.data['search'])
    #user = mongo.db.users.find_one({"username": search_string})
    user = mongo.db.users.find_one({"username": search.data['search']})
    print(user)
    if user:
        return "O usuario " + search.data['search'] + " Existe no banco"

    return "não achou"