from controllers.cliente_controller import *
from utils.formatacao import formatar_cpf, formatar_telefone

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
    def detalhar_clientes(id=None):
        # Chama a função de detalhar cliente do controller
        sucesso, mensagem = ClienteController.detalhar_clientes(id)
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






    @staticmethod
    def editar_cliente():
        # Carrega a base de clientes
        clientes = ClienteDao.carregar_cliente()

        if not clientes:
            print("⚠️ Não existe nenhum cliente para editar.")
            return
        
        # Exibe lista de clientes ao usuário
        ClienteView.detalhar_clientes()

        # Pede o ID do cliente que será editado
        id_editar = input("\nDigite o ID do cliente que deseja editar (Caso queira cancelar, deixe em branco):")

        if not id_editar:
            print(f"\n✅ Nenhum cliente foi editado.")
            return
        
        try:
            id_editar = int(id_editar)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        # Valida se o ID da categoria está cadastrado
        dicionario_cliente = None
        for cliente in clientes:
            if cliente["id"] == id_editar:
                dicionario_cliente = cliente
                break
        
        if not dicionario_cliente:
            print(f"\n⚠️ O ID: {id_editar}, não está na lista de cadastro.")
            return

        # Exibe o cliente selecionado para edição
        ClienteView.detalhar_clientes(id_editar)

        # Solicita a chave ao usuário
        chave = input("\nEscolha a opção que deseja editar:\nNome\nCPF\nTelefone\nEndereço\n").strip().lower().replace("ç","c")

        # Valida se a chave existe
        if chave not in dicionario_cliente:
            print(f'\n⚠️ A opção: {chave} é inválida.')
            return 
        
        # Solicita o input com o novo valor e ajusta os dados para poder chamar a funcao de editar do controller
        if chave == "nome":
            nome = input('\nDigite o novo nome do cliente (ou pressione Enter para manter o mesmo): ').strip().lower()
            if not nome:
                print(f"\n✅ O nome do cliente {dicionario_cliente["nome"].title()} foi mantido.")
                return
            cpf = dicionario_cliente["cpf"]
            telefone = dicionario_cliente["telefone"]
            endereco = dicionario_cliente["endereco"]

        elif chave == "cpf":
            cpf = input('\nDigite o novo CPF do cliente (ou pressione Enter para manter o mesmo): ').strip().lower()
            if not cpf:
                print(f"\n✅ O CPF do cliente {dicionario_cliente["nome"].title()} foi mantido.")
                return
            nome = dicionario_cliente["nome"]
            telefone = dicionario_cliente["telefone"]
            endereco = dicionario_cliente["endereco"]

        elif chave == "telefone":
            telefone = input('\nDigite o novo telefone do cliente (ou pressione Enter para manter o mesmo): ').strip().lower()
            if not telefone:
                print(f"\n✅ O teledone do cliente {dicionario_cliente["nome"].title()} foi mantido.")
                return
            nome = dicionario_cliente["nome"]
            cpf = dicionario_cliente["cpf"]
            endereco = dicionario_cliente["endereco"]

        elif chave == "endereco":
            endereco = input('\nDigite o novo endereço do cliente (ou pressione Enter para manter o mesmo): ').strip().lower()
            if not endereco:
                print(f"\n✅ O endereço do cliente {dicionario_cliente["nome"].title()} foi mantido.")
                return
            nome = dicionario_cliente["nome"]
            cpf = dicionario_cliente["cpf"]
            telefone = dicionario_cliente["telefone"]

        # Chama a controller para editar os dados
        sucesso, mensagem = ClienteController.editar_cliente(nome, cpf, telefone, endereco, dicionario_cliente)

        # Mostra a mensagem de sucesso no terminal
        if sucesso:
            if chave == "nome":
                print(mensagem)
                print(f"O cliente teve o nome atualizado:\nDe: {dicionario_cliente["nome"].title()}\nPara: {nome.title()}")
                return
            elif chave == "cpf":
                print(mensagem)
                print(f"{nome.title()} teve o CPF atualizado:\nDe: {formatar_cpf(dicionario_cliente["cpf"])}\nPara: {formatar_cpf(cpf)}")
                return
            elif chave == "telefone":
                print(mensagem)
                print(f"{nome.title()} teve o telefone atualizado:\nDe: {formatar_telefone(dicionario_cliente["telefone"])}\nPara: {formatar_telefone(telefone)}")
                return
            elif chave == "endereco":
                print(mensagem)
                print(f"{nome.title()} teve o endereço atualizado:\nDe: {dicionario_cliente["endereco"].title()}\nPara: {endereco.title()}")
                return
        else:
            print(mensagem)