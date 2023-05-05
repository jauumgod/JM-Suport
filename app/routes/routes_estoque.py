from app import app, render_template, url_for, request, redirect, flash, db, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.tab_estoque import Estoque
from ..models import tab_usuarios
from flask_login import login_manager, login_required, logout_user
import time



@app.route("/estoque")
def listar_estoque():
    lst_estoque = Estoque.query.all()

    return render_template("gerenciar_estoque.html", lst_estoque=lst_estoque)







