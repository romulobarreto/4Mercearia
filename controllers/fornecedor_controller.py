from daos.fornecedor_dao import *
from models.fornecedor import *
import re

class FornecedorController:
    @staticmethod
    def formatar_telefone(telefone):
        # Formata o número do telefone de acordo com o padrão brasileiro
        ddd = telefone[0:2]
        if len(telefone) == 11:
            corpo = telefone[2:7]
            final = telefone[7:]
        else:
            corpo = telefone[2:6]
            final = telefone[6:]
        return f"({ddd}) {corpo}-{final}"

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
            lista_formatada += f"{index}°: {fornecedor["nome"].title()} - Telefone: {FornecedorController.formatar_telefone(fornecedor["telefone"])}\n"
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
            return False, f"\n⚠️ O fornecedor {nome.title()} não está cadastrado."
        
        # Verifica se o fornecedor está em uso com algum produto, se estiver, não pode ser excluído
        #TODO Criar a tabela e as funções de produtos para conseguir implementar essa regra de negócio
        
        # Remove o dicionário da categoria da base
        fornecedores.remove(dicionario_fornecedor)

        # Salva a lista atualizada na base
        FornecedorDao.salvar_fornecedor(fornecedores)
        return True, f"✅ O fornecedor {nome.title()} foi deletado com sucesso."
        


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