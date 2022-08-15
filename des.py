from crypt import methods
from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from flask import url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://testeuser:Analog21@localhost:3306/desapegando3d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column('usu_id', db.Integer, primary_key=True)
    nome = db.Column('usu_nome', db.String(256))
    email = db.Column('usu_email', db.String(256))
    senha = db.Column('usu_senha', db.String(256))
    rua = db.Column('usu_rua', db.String(256))
    cidade = db.Column('usu_cidade', db.String(256))
    estado = db.Column('usu_estado', db.String(256))
    cep = db.Column('usu_cep', db.String(256))

    def __init__(self, nome, email, senha, rua, cidade, estado,cep):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cad/usuario")
def usuario():
    return render_template('usuario.html', titulo="Cadastro de Usuario")


@app.route("/login/caduser", methods=['post'])
def caduser():
    usuario = Usuario(request.form.get('nome'), request.form.get('email'), request.form.get('senha'), request.form.get('rua'), request.form.get('cidade'), request.form.get('estado'), request.form.get('cep')) #parâmetros para passar para tabelas do banco de dados
    db.session.add(usuario) #adiciona os parametros listados acima na tabela do banco de dados
    db.session.commit()
    return redirect(url_for(usuario))




@app.route("/cad/anuncio")
def anuncio():
    return render_template('anuncio.html')

@app.route("/anuncios/pergunta")
def pergunta():
    return render_template('pergunta.html')

@app.route("/anuncios/compra")
def compra():
    print("anuncio comprado")
    return ""

@app.route("/anuncio/favoritos")
def favoritos():
    print("favorito inserido")
    return f"<h4>Comprado</h4>"

@app.route("/config/categoria")
def categoria():
    return render_template('categoria.html')

@app.route("/relatorios/vendas")
def relVendas():
    return render_template('relVendas.html')

@app.route("/relatorios/compras")
def relCompras():
    return render_template('relCompras.html')


if __name__ == 'des':
    print("des")
    db.create_all()
    

