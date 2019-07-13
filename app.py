from flask import Flask

app = Flask(__name__) #instância da classe Flask

@app.route("/") #decorator, é uma caracteristica do python que coloca antes e uma função. Para aplicar uma função em cima de outra
def index():    #FUnção route em cima da função index '/' é a rota da página
    return "<h1> Hello, World! <h1>"

if __name__ == "__main__":
    app.run()
