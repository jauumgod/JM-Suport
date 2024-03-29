from flask import Flask, render_template, redirect, request, url_for, jsonify, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_manager, login_required, logout_user, login_user, LoginManager, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask_migrate import Migrate
import time
import psycopg2
from datetime import date, datetime, timedelta





app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy()
mi = Migrate(app, db)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.init_app(app)



from .models import tab_chamados, tab_estoque, tab_usuarios
from .routes import routes, routes_crud, routes_estoque


 