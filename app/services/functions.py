from app import app, request, redirect, render_template
from ..models.tab_estoque import Estoque
from app import db
from datetime import datetime


@app.route("/cadastrar_item", methods=['POST'])
def cadastrar_item():
    if request.method  =='POST':
        ES = Estoque()
        ES.item = request.form['nome_item']
        ES.qtd = request.form['qnt_item']
        ES.data_add = datetime.today()
        db.session.add(ES)
        db.session.commit()

@app.route("/ver_items")
def ver_items():
    todosItems = Estoque.query.all()
    return todosItems


@app.route("/<int:id>/atualizar_item", methods=['POST'])
def atualizar_item(id):
    item = Estoque.query.filter_by(id=id).first()
    if request.method == 'POST':
        ES = Estoque()
        ES.item = request.form['nome_item']
        ES.qtd = request.form['qnt_item']
        #data de atualização do item
        ES.data_add = datetime.today()
        db.session.add(ES)
        db.session.commit()

    return render_template("atualizar_item.html", item=item)

@app.route("/<int:id>/remover_item", methods=['POST'])
def remover_item(id):
    ES = Estoque()
    ES.query.filter_by(id=id).first()
    db.session.delete(ES)
    db.session.commit()
    

