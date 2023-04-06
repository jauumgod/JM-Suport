from app import app, render_template, url_for, request, redirect, flash, db
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.tab_usuarios import User
from ..models.tab_chamados import Chamados
from ..models.tab_estoque import Estoque
from flask_login import login_manager, login_required, logout_user, login_user, LoginManager
from datetime import date
import time


login_manager = LoginManager(app)

@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def pagina_inicial():
    return render_template("pagina_inicial.html")




@app.route("/login", methods=['GET', 'POST'])
def login():
    databases = ['kurujao', 'lenovo']
    if request.method == "POST":
        usuario = request.form['user']
        senha = request.form['pass']

        user = User.query.filter_by(username=usuario).first()

        if not user or not check_password_hash(user.password, senha):
            flash("Usuario ou senha incorretos")
            return redirect(url_for("login"))
        
        login_user(user, duration=datetime.timedelta(days=2))

        return redirect(url_for("chamados_usuario"))
    
    return render_template("login.html", databases=databases)

ROWS_PER_PAGE = 5
@app.route("/chamados_suporte")
@login_required
def chamados_suporte():
    page = request.args.get('page',1,type=int)
    ch = Chamados.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("chamados_suporte.html", ch = ch)

@app.route("/fechar_chamado", methods=['GET', 'POST'])
@login_required
def fechar_chamado():
    situacao = 'fechado'
    db.update(situacao)
    db.commit()

@app.route("/processamento", methods=['GET','POST'])
@login_required
def processamento():
    chamado = Chamados.query.filter_by(id=id)
    chamado.situacao = 'processamento'
    db.update(chamado.situacao)
    db.commit()

ROWS_PER_PAGE = 10

@app.route("/chamados_usuario")
@login_required
def chamados_usuario():
    page = request.args.get('page',1,type=int)
    meus_chamados = Chamados.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("chamados_usuario.html", chamados = meus_chamados)


@app.route("/abrir_chamados/", methods=['GET','POST'])
@login_required
def abrir_chamado():
    if request.method == 'POST':
        ch = Chamados()
        ch.titulo = request.form['title']
        ch.descricao = request.form['descricao']
        ch.nome_usr =  current_user    
        ch.data_add = date.today()
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
@login_required
def chamados_espera():
    chamados = Chamados.query.filter_by(situacao='processamento')
    if chamados:
        return render_template("chamados_espera.html", ch_espera = chamados)


ROWS_PER_PAGE = 10
@app.route("/gerenciar_contas")
@login_required
def gerenciar_contas():
    page = request.args.get('page',1,type=int)
    users = User.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("gerenciar_contas.html", users=users)


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))