class Fornecedor:
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone

    def salvar_dict(self):
        return {"id": self.id, "nome": self.nome, "telefone": self.telefone}