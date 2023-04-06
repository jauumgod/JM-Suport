from flask import Flask, render_template, redirect, request, url_for, jsonify, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
import time
import psycopg2




app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager(app)
login_manager.init_app(app)



from .models import tab_chamados, tab_estoque, tab_usuarios
from .routes import routes, routes_crud, routes_estoque


