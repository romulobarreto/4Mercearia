from models.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, id, nome, cpf, telefone, cargo_id, salario):
        super().__init__(id, nome, cpf, telefone)
        self.cargo_id = cargo_id
        self.salario = salario

    def salvar_dict(self):
        return {"id": self.id, "nome": self.nome, "cpf": self.cpf, "telefone": self.telefone, "cargo": self.cargo_id, "salario": str(self.salario)}