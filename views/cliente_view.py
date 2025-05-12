from controllers.cliente_controller import *

class ClienteView():

    @staticmethod
    def cadastrar_cliente():
        # Solicita o input ao usuário
        nome = input("\nDigite o nome do cliente: ").strip().lower()

        cpf = input("\nDigite o CPF do cliente: ").strip().replace(".", "").replace("-", "")

        telefone = input("\nDigite o telefone do cliente (DDD + Número):  ").strip().replace("(", "").replace(")", "").replace("-","").replace(" ","")

        endereco = input("\nDigite o endereço do cliente (Logradouro + n° + compl): ").strip().lower()

        # Chama a função de cadastrar o cliente do controller
        sucesso, mensagem = ClienteController.cadastrar_cliente(nome, cpf, telefone, endereco)

        print(mensagem)





    @staticmethod
    def detalhar_clientes():
        # Chama a função de detalhar cliente do controller
        sucesso, mensagem = ClienteController.detalhar_clientes()
        # Exibe a lista caso haja
        print(mensagem)