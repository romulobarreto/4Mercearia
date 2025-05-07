class Produto:
    def __init__(self, id, nome, preco, quantidade, categoria_id, fornecedor_id):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria_id = categoria_id
        self.fornecedor_id = fornecedor_id

    def salvar_dict(self):
        return {"id": self.id, "nome": self.nome, "preco": str(self.preco), "quantidade": self.quantidade, "categoria_id": self.categoria_id, "fornecedor_id": self.fornecedor_id}