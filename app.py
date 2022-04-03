
from flask import Flask, redirect,render_template, url_for
app = Flask(__name__)

# rota da pagina principal
@app.route("/")
@app.route("/home")
def home():
    return render_template("pilha.html",)

@app.route("/fila")
def fila():
    return render_template("fila.html",)

@app.route("/fila_circular")
def fila_circular():
    return render_template("fila-circular.html",)

if __name__ == '__main__':
   app.run(debug=True) 
