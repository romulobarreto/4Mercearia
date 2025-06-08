class Venda():
    def __init__(self, id, funcionario_id, data, itens, total, cliente_id=None):
        self.id = id
        self.funcionario_id = funcionario_id
        self.cliente_id = cliente_id
        self.data = data
        self.itens = itens
        self.total = total

    # Salvar em forma de dicionário
    def salvar_dict(self):
        return {"id": self.id, "funcionario_id": self.funcionario_id, "cliente_id": self.cliente_id, "data": self.data.strftime('%Y-%m-%d'), "itens": self.itens, "total": str(self.total)}