from app import app

@app.route("/index")
@app.route("/") #decorator, é uma caracteristica do python que coloca antes e uma função. Para aplicar uma função em cima de outra
def index():    #FUnção route em cima da função index '/' é a rota da página
    return "<h1> Hello, World! <h1>"


@app.route("/test", defaults={'name' : None})
@app.route("/test/<name>")#Chamando uma variavel
def test(name): #2 contrutores? 
    if name:
        return "Olar, %s!" % name #imprimindo com a variavel
    else:
        return "Olar, usuário"