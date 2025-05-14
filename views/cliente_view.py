from controllers.cliente_controller import *
from utils.formatacao import formatar_cpf

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




    @staticmethod
    def excluir_cliente():
        # Carregar clientes
        clientes = ClienteDao.carregar_cliente()

        # Verifica se existe clientes cadastrados
        if not clientes:
            print("⚠️ Não existe nenhum cliente para excluir.")
            return

        # Exibe lista de clientes ao usuário
        ClienteView.detalhar_clientes()

        # Pede o ID do cliente que o usuário deseja excluir
        id_excluir = input("\nDigite o ID do cliente que deseja excluir (Caso queira cancelar, deixe em branco):")

        if not id_excluir:
            print(f"\n✅ Nenhum cliente foi excluído.")
            return
        
        try:
            id_excluir = int(id_excluir)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        # Chama a função de exclusão do controller
        sucesso, mensagem = ClienteController.excluir_cliente(id_excluir)
        print(mensagem)