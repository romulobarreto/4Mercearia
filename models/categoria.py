class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def salvar_dict(self):
        return {"id": self.id, "nome": self.nome}