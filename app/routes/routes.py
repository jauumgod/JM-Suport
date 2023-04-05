from app import app, render_template, url_for, request, redirect, flash, db, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.tab_usuarios import Usuarios
from ..models.tab_chamados import Chamados
from ..models.tab_estoque import Estoque
from flask_login import login_manager, login_required, logout_user, login_user, current_user
import datetime
import time




@app.route("/")
def pagina_inicial():
    return render_template("pagina_inicial.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    databases = ['kurujao', 'lenovo']
    if request.method == "POST":
        usuario = request.form['user']
        senha = request.form['pass']

        consulta = Usuarios.query.filter_by(username=usuario).first()

        if not consulta or not check_password_hash(consulta.password, senha):
            flash("Usuario ou senha incorretos")
            return redirect(url_for("login"))
        
        login_user(consulta,True)        
        return redirect(url_for("chamados_usuario"))
    
    return render_template("login.html", databases=databases)

@login_manager.user_loader
def load_user(id):
    return Usuarios.query.get(int(id))

ROWS_PER_PAGE = 5
@app.route("/chamados_suporte")
def chamados_suporte():
    page = request.args.get('page',1,type=int)
    ch = Chamados.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("chamados_suporte.html", ch = ch)

@app.route("/fechar_chamado", methods=['GET', 'POST'])
def fechar_chamado():
    situacao = 'fechado'
    db.update(situacao)
    db.commit()

@app.route("/processamento", methods=['GET','POST'])
def processamento():
    chamado = Chamados.query.filter_by(id=id)
    chamado.situacao = 'processamento'
    db.update(chamado.situacao)
    db.commit()

ROWS_PER_PAGE = 10
@app.route("/chamados_usuario")
def chamados_usuario():
    page = request.args.get('page',1,type=int)
    meus_chamados = Chamados.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("chamados_usuario.html", chamados = meus_chamados)

@app.route("/abrir_chamados", methods=['GET','POST'])
def abrir_chamado():
    if request.method == 'POST':
        ch = Chamados()
        ch.titulo = request.form['title']
        ch.descricao = request.form['descricao']
        ch.nome_usr =  current_user()    
        ch.data_add = datetime.today()
        ch.tipo_ch = request.form['select_type']
        ch.data_fim = "algum dia"
        ch.situacao = "Aberto"
        
        db.session.add(ch)
        db.session.commit()
        return redirect(url_for("chamados_usuario"))
    else:
        flash("não foi possivel abrir o chamado")
        
    return render_template("abrir_chamados.html")

@app.route("/espera")
def chamados_espera():
    chamados = Chamados.query.filter_by(situacao='processamento')
    if chamados:
        return render_template("chamados_espera.html", ch_espera = chamados)


ROWS_PER_PAGE = 10
@app.route("/gerenciar_contas")
def gerenciar_contas():
    page = request.args.get('page',1,type=int)
    users = Usuarios.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("gerenciar_contas.html", users=users)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))