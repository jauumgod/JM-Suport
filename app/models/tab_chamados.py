from app import db
from ..models import tab_estoque


class Chamados(db.Model):
    __tablename__ = 'tab_chamados'
    id = db.Column(db.Integer, primary_key=True)
    data_add = db.Column(db.String(255), nullable=False)
    data_fim = db.Column(db.String(255), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    tipo_ch = db.Column(db.String(255), nullable=False)
    situacao = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(100))

    tab_usuarios_id = db.Column(db.Integer, db.ForeignKey('tab_usuarios.id'))
    
    tab_estoque_id = db.relationship('Estoque', backref='tab_chamados', lazy='dynamic')
    
    def __repr__(self):
        return '<Chamados {}>'.format(self.descricao)
