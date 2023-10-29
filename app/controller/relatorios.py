from app import app, datetime, timedelta
from models import tab_chamados

chamados = tab_chamados.Chamados()

class Relatorios:
    def __init__(self):
        return self.name
    
    def day(begin, end):
        result = chamados.query.filter(chamados.data_add.between(begin, end)).all()
        return result
    
    def week():
        today = datetime.today()
        end_of_last_week = today - timedelta(days=today.weekday() + 1)
        start_of_last_week = end_of_last_week - timedelta(days=6)
        result = chamados.query.filter(chamados.data_add.between(start_of_last_week, end_of_last_week)).all()
        return result
    
    def months(begin):
        result = chamados.query.filter_by(data_add = begin).all() 
        return result
    
    def atendent(atendent):
        result = chamados.query.filter_by(ass_por = atendent).all()
        return
    
    def client(client):
        result = chamados.query.filter_by(tab_usuarios_id=client).all()
        return result
    
    def categoria(categoria):
        result = chamados.query.filter_by(tipo_ch = categoria).all()
        
        return result
    



