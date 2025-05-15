from daos.fornecedor_dao import *
from daos.produto_dao import *
from models.fornecedor import *
from utils.formatacao import *
from utils.buscas import buscar_nome_fornecedor
from utils.validacao import validar_telefone

class FornecedorController:
    @staticmethod
    def validar_dados(nome, telefone, nome_atual=None):

        # Carrega a lista de fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Valida o valor de nome
        if not nome:
            return False, "⚠️ O nome não pode estar vazio."
        
        if nome != nome_atual and any(fornecedor["nome"] == nome for fornecedor in fornecedores):
            return False, "🚫 Fornecedor já cadastrado."
            
        verficar_telefone = validar_telefone(telefone)

        if not verficar_telefone:
            return False, f"⚠️ O telefone: {telefone} não está no padrão. Use o formato DDD + número (Ex: 11987654321)"
        
        return True, "✅ Dados aprovados."
        





    
    @staticmethod
    def cadastrar_fornecedor(nome, telefone):
        # Chama a validação de dados
        sucesso, mensagem = FornecedorController.validar_dados(nome,telefone)

        if not sucesso:
            return False, mensagem
        
        # Carrega a lista de fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()
        
        # Define o valor do maior_id
        id = max([fornecedor["id"] for fornecedor in fornecedores], default=0) + 1

        # Cria o fornecedor
        fornecedor = Fornecedor(id, nome, telefone)

        # Transforma o fornecedor em dicionário e adiciona na lista
        fornecedores.append(fornecedor.salvar_dict())

        # Salva a lista de fornecedores no banco e exibe a mensagem
        sucesso, mensagem = FornecedorDao.salvar_fornecedor(fornecedores)

        if sucesso:
            return True, mensagem
        else:
            return False, mensagem
        






    @staticmethod
    def detalhar_fornecedores(id=None):
        # Carregar fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Verifica se existe fornecedor cadastrado
        if not fornecedores:
            return False, "\n⚠️ A lista de fornecedores está vazia!"
        
        # Detalhar Fornecedores
        if id:
            lista_formatada = "\n📋 Detalhes do fornecedor:\n"
            for fornecedor in fornecedores:
                if fornecedor["id"] == id:
                    lista_formatada += f"ID {fornecedor["id"]}: {fornecedor["nome"].title()} - Telefone: {formatar_telefone(fornecedor["telefone"])}\n---------------------------"
                    break
        else:    
            lista_formatada = "\n📋 Lista de fornecedores cadastrados:\n"
            for fornecedor in sorted(fornecedores, key=lambda c: c["nome"]):
                lista_formatada += f"ID {fornecedor["id"]}: {fornecedor["nome"].title()} - Telefone: {formatar_telefone(fornecedor["telefone"])}\n"
            lista_formatada += "---------------------------"

        return True, lista_formatada
    






    
    @staticmethod
    def excluir_fornecedor(id_fornecedor):
        # Carrega lista de fornecedores e produtos
        fornecedores = FornecedorDao.carregar_fornecedor()
        produtos = ProdutoDao.carregar_produto()
        
        # Valida se o ID do fornecedor está cadastrado
        dicionario_fornecedor = None
        for fornecedor in fornecedores:
            if fornecedor["id"] == id_fornecedor:
                dicionario_fornecedor = fornecedor
                break

        if not dicionario_fornecedor:
            return False, f"\n⚠️ O ID: {id_fornecedor} não está na lista de fornecedores."
        
        # Verifica se o fornecedor está em uso com algum produto, se estiver, não pode ser excluído
        nome_fornecedor = buscar_nome_fornecedor(id_fornecedor, fornecedores)
        for produto in produtos:
            if produto["fornecedor_id"] == id_fornecedor:
                return False, f"\n⚠️ {nome_fornecedor.title()} não pode ser excluído pois está sendo usado por um produto."
        
        # Remove o dicionário da categoria da base
        fornecedores.remove(dicionario_fornecedor)

        # Salva a lista atualizada na base
        FornecedorDao.salvar_fornecedor(fornecedores)
        return True, f"✅ O fornecedor {nome_fornecedor.title()} foi excluído com sucesso."
        






    @staticmethod
    def editar_fornecedor(nome, telefone, lista_fornecedor):
        # Valida os dados
        sucesso, mensagem = FornecedorController.validar_dados(nome, telefone, lista_fornecedor["nome"])
        if not sucesso:
            return False, mensagem

        # Carrega lista de fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Encontra o fornecedor na lista e edita a informação diretamente
        for fornecedor in fornecedores:
            if fornecedor["nome"] == lista_fornecedor["nome"]:
                fornecedor["nome"] = nome
                fornecedor["telefone"] = telefone
                break
        
        # Salva a lista editada no banco
        sucesso, mensagem = FornecedorDao.salvar_fornecedor(fornecedores)

        if sucesso:
            return True, "✅ Fornecedor editado com sucesso."
        else:
            return False, "⚠️ Erro ao salvar a alteração no banco de dados."