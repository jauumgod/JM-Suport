from app import app, time, generate_password_hash, check_password_hash,render_template, url_for, request, redirect, flash, db, session, login_manager, login_required, logout_user
from ..models.tab_estoque import Estoque
from ..models import tab_usuarios




@app.route("/estoque")
def listar_estoque():
    lst_estoque = Estoque.query.all()

    return render_template("gerenciar_estoque.html", lst_estoque=lst_estoque)







