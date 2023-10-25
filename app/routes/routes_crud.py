from app import app, render_template, url_for, request, redirect, flash, db, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.tab_usuarios import User
from ..models.tab_chamados import Chamados
from ..models.tab_estoque import Estoque
from flask_login import login_manager, login_required, logout_user
import time



@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method=='POST':
        user = User()
        user.username = request.form['username']
        user.password = generate_password_hash(request.form['password'])
        user.email = request.form['email']
        user.permiss = request.form['perm']
        user.active = 'S'
        query = User.query.filter_by(username=user.username).first()

        if query:
            flash("Usuario Já existe")
            time.sleep(2)
            return redirect("login")
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    


@app.route("/usuarios_desativados")
def usuarios_desativados():
    usuarios_desativados = User.query.filter_by(active="nao")
    return render_template("login.html", usuarios=usuarios_desativados)

@app.route('/disable_user/<int:user_id>', methods=['POST'])
def disable_user(user_id):
    user = User.query.get_or_404(user_id)
    user.active = 'N'
    db.session.update(user)
    db.session.commit()
    return 'User disabled'


@app.route("/atualizar_dados/<int:id>", methods=['GET', 'POST'])
def atualizar_dados(id):
    usuario = User.query.filter_by(id=id)
    if request.method == 'post':
        senha = request.form['senha']

        
@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = Chamados.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return 'Chamado excluido'


def tratar_lista(lista):
    variavel = ''
    if lista:
        for i in lista:
            variavel = i
    lista = variavel
    return lista

# @app.route("<int:id>/disable_usuario", methods=['GET', 'POST'])
# def disable_usuario(id):
#     query = Usuarios.query.filter_by(id=id)
#     if query:
#         is_active= 'nao'
#         db.update(is_active)
#         db.commit()

@app.route("/buscar", methods=['GET', 'POST'])
def buscar_chamado():

    chamados = Chamados.query.all()

    if request.method == 'POST':
        valor = request.form['busca']
        flash("campo de busca vazio!")
        return render_template("erros/not_found.html")
    

    busca = valor
    for i, j in chamados.items():
        if busca == i:
            return render_template("search_page.html", result = i, name = valor)

        
    else:
        flash("O link desejado não foi encontrado")
        return render_template("erros/not_found.html")
    
