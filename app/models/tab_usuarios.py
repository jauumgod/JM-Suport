from app import db, UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'tab_usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome_usr = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.String(10), nullable=False)
    permiss = db.Column(db.String(100), nullable=False)


    def __str__(self):
        return self.name
