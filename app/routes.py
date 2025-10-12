from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    name_user = "Carlos"
    dados = {"status": "Solteiro", "idade": 18}

    return render_template('index.html', nome_user=name_user, dados=dados)
