from models.cliente import *
from daos.cliente_dao import *
from utils.validacao import validar_cpf, validar_telefone, validar_endereco
from utils.formatacao import formatar_telefone, formatar_cpf

class ClienteController():

    @staticmethod
    def validar_dados(nome, cpf, telefone, endereco, cpf_atual=None):
        # Carrega a lista de clientes
        clientes = ClienteDao.carregar_cliente()

        # Valida o nome
        if not nome:
            return False, "\n⚠️ O nome precisa ser preenchido."
        
        # Valida o cpf (Verificar retorno da funcao)
        validador_cpf = validar_cpf(cpf)

        if not validador_cpf:
            return False, "\n⚠️ CPF inválido."

        if cpf != cpf_atual and any(cliente["cpf"] == cpf for cliente in clientes):
            return False, f"\n❌ CPF já cadastrado."

        # Valida o telefone
        verificar_telefone = validar_telefone(telefone)

        if not verificar_telefone:
            return False, f"\n⚠️ O telefone: {telefone} não está no padrão. Use o formato DDD + número (Ex: 11987654321)."
        
        # Valida o endereço
        verificar_endereco = validar_endereco(endereco)

        if not verificar_endereco:
            return False, f"\n⚠️ O endereço precisa conter Logradouro + N° + Complemento (Opcional)."
        
        # Retorna sucesso
        return True, "\n✅ Dados validados."
    




    @staticmethod
    def cadastrar_cliente(nome, cpf, telefone, endereco):
        # Valida os dados recebidos
        sucesso, mensagem = ClienteController.validar_dados(nome, cpf, telefone, endereco)

        if not sucesso:
            return False, mensagem
        
        # Carrega a lista de clientes
        clientes = ClienteDao.carregar_cliente()

        # Cria o ID do cliente
        id = max([cliente["id"] for cliente in clientes], default=0) + 1

        # Cria o cliente
        cliente = Cliente(id, nome, cpf, telefone, endereco)

        # Adiciona o cliente a lista de clientes
        clientes.append(cliente.salvar_dict())

        # Salva o cliente no banco (JSON)
        sucesso, mensagem = ClienteDao.salvar_cliente(clientes)

        if sucesso:
            return True, mensagem
        else:
            return False, mensagem
        
    

    @staticmethod
    def detalhar_clientes():
        # Carrega lista de clientes
        clientes = ClienteDao.carregar_cliente()

        if not clientes:
            return False, "\n⚠️ Nenhum cliente cadastrado para exibir, faça um cadastro."
        
        lista_formatada = "\n📋 Lista de clientes cadastrados:\n"
        for index, cliente in enumerate(sorted(clientes, key=lambda c: c["nome"]), start=1):
            lista_formatada += f"{index}°: {cliente["nome"].title()}\nCPF: {formatar_cpf(cliente["cpf"])}\nTelefone: {formatar_telefone(cliente["telefone"])}\nEndereço: {cliente["endereco"].title()}\n_______________________________\n"

        return True, lista_formatada