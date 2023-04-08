from app import db


class Estoque(db.Model):
    __tablename__ = 'tab_estoque'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(255), nullable=False)
    data_add = db.Column(db.String(50), nullable=False)
    qtd = db.Column(db.String(50), nullable=False)

    chamados_id = db.Column(db.Integer, db.ForeignKey('tab_chamados.id'))