from daos.fornecedor_dao import *
from models.fornecedor import *
import re

class FornecedorController:

    @staticmethod
    def validar_dados(nome, telefone, nome_atual=None):
        # Define o padrão regex para telefone
        padrao_telefone = re.compile("^[1-9][\d][1-9][\d]{3,4}[\d]{4}$")

        # Carrega a lista de fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Valida o valor de nome
        if not nome:
            return False, "⚠️ O nome não pode estar vazio."
        
        if nome != nome_atual and any(Fornecedor["nome"] == nome for fornecedor in fornecedores):
            return False, "🚫 Usuário já cadastrado."
            
        validar_telefone = re.fullmatch(padrao_telefone, telefone)

        if not validar_telefone:
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
    def detalhar_fornecedores():
        # Carregar fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Verifica se existe fornecedor cadastrado
        if not fornecedores:
            return False, "\n⚠️ A lista de fornecedores está vazia!"
        
        # Detalhar Fornecedores
        lista_formatada = "\n📋 Lista de fornecedores cadastrados:\n"
        for index, fornecedor in enumerate(sorted(fornecedores, key=lambda c: c["nome"]), start=1):
            if len(fornecedor["telefone"]) == 11:
                lista_formatada += f"{index}°: {fornecedor["nome"].upper()} - Telefone: ({fornecedor["telefone"][0:2]}) {fornecedor["telefone"][2:7]}-{fornecedor["telefone"][7:]}\n"
            else:
                lista_formatada += f"{index}°: {fornecedor["nome"].upper()} - Telefone: ({fornecedor["telefone"][0:2]}) {fornecedor["telefone"][2:6]}-{fornecedor["telefone"][6:]}\n"
        lista_formatada += "---------------------------"

        return True, lista_formatada
    

    
    @staticmethod
    def excluir_fornecedor(nome):
        # Carrega fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Valida se existe fornecedor cadastrado
        if not fornecedores:
            return False, "⚠️ Não existe nenhum fornecedor para excluir."

        # Valida o nome do fornecedor
        if not nome:
            return False, "⚠️ O nome não pode estar vazio."
        
        # Valida se o nome do fornecedor está cadastrado
        dicionario_fornecedor = None
        for fornecedor in fornecedores:
            if fornecedor["nome"] == nome:
                dicionario_fornecedor = fornecedor
                break

        if not dicionario_fornecedor:
            return False, f"\n⚠️ O fornecedor {nome.upper()} não está cadastrado."
        
        # Verifica se o fornecedor está em uso com algum produto, se estiver, não pode ser excluído
        #TODO Criar a tabela e as funções de produtos para conseguir implementar essa regra de negócio
        
        # Remove o dicionário da categoria da base
        fornecedores.remove(dicionario_fornecedor)

        # Salva a lista atualizada na base
        FornecedorDao.salvar_fornecedor(fornecedores)
        return True, f"✅ O fornecedor {nome.upper()} foi deletado com sucesso."
        


    @staticmethod
    def editar_categoria(nome, novo_nome):
        # Carrega lista de usuários
        categorias = CategoriaDao.carregar_categoria()

        # Valida o nome da categoria
        if not novo_nome:
            return False, f"✅ A categoria {nome.upper()} permanece a mesma."
        
        # Valida se o nome da categoria está cadastrado
        for categoria in categorias:
            if categoria["nome"] == novo_nome:
                return False, f"⚠️ {novo_nome.upper()} já está em uso."
            
        # Encontra a lista que deve ser editado e faz a alteração
        for categoria in categorias:
            if categoria["nome"] == nome:
                categoria["nome"] = novo_nome
                break

        # Salva a lista editada no banco
        sucesso, mensagem = CategoriaDao.salvar_categoria(categorias)

        # Mostra a mensagem de sucesso
        if sucesso:
            return True, f"{mensagem}\nCategoria antiga:{nome.upper()}\nCategoria nova: {novo_nome.upper()}"
        else:
            return False, mensagem