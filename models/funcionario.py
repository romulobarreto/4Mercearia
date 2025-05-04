from models.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, id, nome, cpf, telefone, cargo, salario):
        super().__init__(id, nome, cpf, telefone)
        self.cargo = cargo
        self.salario = salario

    def salvar_dict(self):
        return {"id": self.id, "nome": self.nome, "cpf": self.cpf, "telefone": self.telefone, "cargo": self.cliente, "salario": self.salario}