from app import db, UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'tab_usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    active = db.Column(db.String(10), nullable=False)
    permiss = db.Column(db.String(10), nullable=False)

    tab_chamados_id = db.relationship('Chamados', backref='tab_chamados', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    