from models.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, id, nome, cpf, telefone, endereco):
        super().__init__(id, nome, cpf, telefone)
        self.endereco = endereco

    def salvar_dict(self):
        return {"id": self.id, "nome": self.nome, "cpf": self.cpf, "telefone": self.telefone, "endereco": self.endereco}