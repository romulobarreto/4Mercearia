class Pessoa:
    def __init__(self, id, nome, cpf, telefone):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def salvar_dict(self):
        return {"id": self.id, "nome": self.nome, "cpf": self.cpf, "telefone": self.telefone}