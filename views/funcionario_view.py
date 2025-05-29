from controllers.funcionario_controller import *
from views.cargo_view import *
from utils.formatacao import formatar_cpf, formatar_telefone, formatar_preco
from decimal import Decimal, InvalidOperation
from utils.buscas import buscar_nome, buscar_nome

class FuncionarioView():

    @staticmethod
    def cadastrar_funcionario():
        # Carrega as listas de cargos e verifica se está vazia
        cargos = CargoDao.carregar_cargos()
        
        if not cargos:
            print("\n🚫 Não existe nenhum cargo cadastrado, não é possível cadastrar um funcionário.")
            return
        
        # Solicita os inputs ao usuário
        nome = input("\nDigite o nome do funcionário: ").strip().lower()

        cpf = input("\nDigite o CPF do funcionário: ").strip().replace(".", "").replace("-", "")

        telefone = input("\nDigite o telefone do funcionário (DDD + Número):  ").strip().replace("(", "").replace(")", "").replace("-","").replace(" ","")

        # Exibe os cargos disponíveis para cadastro
        CargoView.detalhar_cargos()

        try:
            cargo_id = int(input("\nDigite o ID do cargo que será atribuído ao funcionário: ").strip())
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        try:
            salario = Decimal(input("\nDigite o salário do funcionário: R$").strip().replace(".", "").replace(",", "."))
        except InvalidOperation:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        # Chama a função de cadastrar funcionário
        sucesso, mensagem = FuncionarioController.cadastrar_funcionario(nome, cpf, telefone, cargo_id, salario)
        print(mensagem)






    @staticmethod
    def detalhar_funcionarios(id=None):
        # Chama a função de detalhar
        sucesso, mensagem = FuncionarioController.detalhar_funcionarios(id)
        # Exibe o resultado
        print(mensagem)