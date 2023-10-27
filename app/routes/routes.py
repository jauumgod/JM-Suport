from app import app, check_password_hash, generate_password_hash, render_template, url_for, request, redirect, flash, db, time, datetime, date,login_manager, login_required, logout_user, login_user, LoginManager, current_user
from ..models.tab_usuarios import User
from ..models.tab_chamados import Chamados
from ..models.tab_estoque import Estoque
import datetime


ROWS_PER_PAGE = 7

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route("/")
def pagina_inicial():
    return render_template("routes/pagina_inicial.html")


@app.route('/profile')
def profile():
    if current_user.is_authenticated:
        user = current_user.username
        return render_template('config/profile.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        usuario = request.form['usuario']
        senha = request.form['senha']

        user = User.query.filter_by(username=usuario).first()

        if not user or not check_password_hash(user.password, senha):
            flash("Usuario ou senha incorretos")
            return redirect(url_for("login"))
        
        login_user(user, duration=datetime.timedelta(days=1))

        if user.permiss == 'A':
            return redirect(url_for("chamados_suporte_admin"))
        elif user.permiss == 'T':
            return redirect(url_for("chamados_suporte"))
        else:
            return redirect(url_for("chamados_usuario"))
    
    return render_template("auth/login_.html")


@app.route("/chamados_suporte")
@login_required
def chamados_suporte():
    page = request.args.get('page',1,type=int)
    ch = Chamados.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("routes/chamados_suporte.html", chamados = ch)

@app.route("/chamados_suporte_admin")
@login_required
def chamados_suporte_admin():
    page = request.args.get('page',1,type=int)
    ch = Chamados.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("routes/chamados_suporte_admin.html", chamados = ch )

@app.route("/chamados_usuario")
@login_required
def chamados_usuario():
    user = current_user.username
    page = request.args.get('page',1,type=int)
    meus_chamados = Chamados.query.filter_by(tab_usuarios_id=current_user.username).paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("routes/chamados_usuario.html", chamados = meus_chamados, user=user)


@app.route("/abrir_chamados/", methods=['GET','POST'])
@login_required
def abrir_chamado():
    if request.method == 'POST':
        ch = Chamados()
        ch.titulo = request.form['title']
        ch.descricao = request.form['descricao']
        ch.data_add = date.today()
        ch.tipo_ch = request.form['select_type']
        ch.data_fim = "algum dia"
        ch.situacao = "Aberto"
        ch.telefone = request.form['telefone']
        user = current_user.username
        ch.tab_usuarios_id = user
        db.session.add(ch)
        db.session.commit()
        return redirect(url_for("chamados_usuario"))
        
    return render_template("routes/abrir_chamados.html")

@login_required
@app.route("/<int:id>/visualizar_chamados", methods=['GET', 'POST'])
def visualizar_chamados(id):
    items = Estoque.query.all()
    chamado = Chamados.query.filter_by(id=id).all()
    chamado_id = Chamados.query.filter_by(id=id).first()
    if request.method=='POST':
        ass_por = current_user.username
        chamado_id.query.filter_by(id=id).update({"ass_por": ass_por})
        db.session.commit()
        return redirect(url_for("chamados_suporte"))

    return render_template("routes/visualizar_chamados.html", chamado=chamado, items= items)

@login_required
@app.route("/<int:id>/visualizar_chamados_usuario", methods=['GET', 'POST'])
def visualizar_chamados_usuario(id):
    query = Chamados.query.filter_by(id=id).all()
    return render_template("routes/visualizar_chamados_usuario.html", chamado=query)

@login_required
@app.route("/<int:id>/visualizar_contas", methods=['GET','POST'])
def visualizar_contas(id):
    conta = User.query.filter_by(id=id).all()
    if request.method=='POST':
        US = User()
        alterar_senha = request.form (generate_password_hash['nova_senha'])
        US.password = alterar_senha
        conta.password(US)
        db.session.add(conta)
        db.session.commit()

    return render_template("routes/visualizar_contas.html", conta = conta)



@app.route("/<int:id>/fechar_chamado", methods=['GET', 'POST'])
@login_required
def fechar_chamados(id):
    chamado = Chamados.query.filter_by(id=id).all()
    chamado_id = Chamados.query.filter_by(id=id).first()
    return render_template("routes/fechar_chamados.html", chamado = chamado, chamado_id=chamado_id)


@app.route("/espera")
@login_required
def chamados_espera():
    chamados = Chamados.query.filter_by(situacao='processamento')
    if chamados:
        return render_template("routes/chamados_espera.html", ch_espera = chamados)

@app.route("/chamados_assumidos")
def chamados_assumidos():
    chamados = "Nenhum Chamado Assumido"
    return render_template("routes/chamados_assumidos.html", chamados=chamados)


@app.route("/gerenciar_contas")
#@login_required
def gerenciar_contas():

    page = request.args.get('page',1,type=int)
    users = User.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("config/gerenciar_contas.html", users=users)


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/assinatura", methods=['GET', 'POST'])
def assinatura():    
    return render_template("auth/assinatura.html")


@app.route("/meus_chamados")
def meus_chamados():
    return render_template("routes/meus_chamados.html")



@app.route("/relatorios")
def relatorios():

    return render_template("relatorios/relatorios.html")