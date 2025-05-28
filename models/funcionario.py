from models.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, id, nome, cpf, telefone, id_cargo, salario):
        super().__init__(id, nome, cpf, telefone)
        self.id_cargo = id_cargo
        self.salario = salario

    def salvar_dict(self):
        return {"id": self.id, "nome": self.nome, "cpf": self.cpf, "telefone": self.telefone, "cargo": self.id_cargo, "salario": self.salario}