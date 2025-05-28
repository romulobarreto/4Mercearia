from decimal import Decimal
from models.funcionario import *
from daos.cargo_dao import *
from daos.funcionario_dao import *
from utils.validacao import validar_cpf, validar_telefone
from utils.formatacao import formatar_preco, formatar_telefone, formatar_cpf
from utils.gerador import gerador_id

class FuncionarioController():

    @staticmethod
    def validar_dados(nome, cpf, telefone, cargo_id, salario, cpf_atual=None):
        # Carrega a lista de funcionários e de cargos
        funcionarios = FuncionarioDao.carregar_funcionario()
        cargos = CargoDao.carregar_cargos()

        # Valida o nome
        if not nome:
            return False, "\n⚠️ O nome precisa ser preenchido."
        
        # Valida o cpf (Verificar retorno da funcao)
        validador_cpf = validar_cpf(cpf)

        if not validador_cpf:
            return False, "\n⚠️ CPF inválido."
        
        if cpf != cpf_atual and any(funcionario["cpf"] == cpf for funcionario in funcionarios):
            return False, f"\n❌ CPF já cadastrado."
        
        # Valida o telefone
        verificar_telefone = validar_telefone(telefone)

        if not verificar_telefone:
            return False, f"\n⚠️ O telefone: {telefone} não está no padrão. Use o formato DDD + número (Ex: 11987654321)."
        
        # Valida o cargo
        if not any(cargo["id"] == cargo_id for cargo in cargos):
            return False, f"\n ⚠️ Não existe cargo cadastrado para o ID: {cargo_id}."
        
        # Valida o salário
        if salario <= Decimal("0"):
            return False, "\n⚠️ O funcionário não pode trabalhar de graça."
        
        # Retorna sucesso
        return True, "\n✅ Dados validados."
    




    @staticmethod
    def cadastrar_funcionario(nome, cpf, telefone, cargo_id, salario):
        # Valida os dados recebidos
        sucesso, mensagem = FuncionarioController.validar_dados(nome, cpf, telefone, cargo_id, salario)

        if not sucesso:
            return False, mensagem
        
        # Carrega a lista de funcionários
        funcionarios = FuncionarioDao.carregar_funcionario()

        # Cria o ID do funcionário
        id = gerador_id(funcionarios)

        # Cria o funcionário
        funcionario = Funcionario(id, nome, cpf, telefone, cargo_id, salario)

        # Adiciona o funcionário a lista de cadastro
        funcionarios.append(funcionario.salvar_dict())

        # Salva o funcionário no banco (JSON)
        sucesso, mensagem = FuncionarioDao.salvar_funcionario(funcionarios)

        # Mensagem de sucesso
        if sucesso:
            return True, mensagem
        else:
            return False, mensagem
