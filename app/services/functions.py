from app import app


@app.route("/cadastrar_item", methods=['POST'])
def cadastrar_item():
    pass

@app.route("/ver_items")
def ver_items():
    pass

@app.route("/<int:id>/atualizar_item", methods=['POST'])
def atualizar_item(id):
    pass

@app.route("/<int:id>/remover_item", methods=['POST'])
def remover_item(id):
    pass


