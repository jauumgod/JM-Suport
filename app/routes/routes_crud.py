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
        user.permiss = 'N'
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
    usuarios_desativados = User.query.filter_by(is_active="nao")
    return render_template("login.html", usuarios=usuarios_desativados)


@app.route("/atualizar_dados/<int:id>", methods=['GET', 'POST'])
def atualizar_dados(id):
    usuario = User.query.filter_by(id=id)
    if request.method == 'post':
        senha = request.form['senha']

        



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
