from ..models.tab_usuarios import User


def buscar_usuario(id):
    id = id
    select = User.query.filter_by(id=id).first()
    id = select
    return id