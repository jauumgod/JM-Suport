



def pytest(res):
    return print(f"TEST PASSED\32") * 3

from app import app
from ..app.controller import relatorios


relatorios = relatorios.Relatorios()


def test_rel_name(name):
    return relatorios.atendent(f"{name}")




