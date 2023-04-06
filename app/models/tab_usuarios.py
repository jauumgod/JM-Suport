from app import db, UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'tab_usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    active = db.Column(db.String(10), nullable=False)
    permiss = db.Column(db.String(10), nullable=False)
    
    chamados_id = db.relationship('User', backref='tab_usuarios', lazy='dynamic')

    
    def __str__(self):
        return self.name

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)