from daos.categoria_dao import *
from models.categoria import *

class CategoriaController:
    
    @staticmethod
    def cadastrar_categoria(nome):
        # Carrega a lista de categorias
        categorias = CategoriaDao.carregar_categoria()

        # Valida o valor de nome
        if not nome:
            return False, "⚠️ O nome não pode estar vazio."
        
        for categoria in categorias:
            if categoria["nome"] == nome:
                return False, f"\n⚠️ A categoria {nome} já está cadastrada."
        
        # Define o valor do maior_id
        id = max([categoria["id"] for categoria in categorias], default=0) + 1

        # Cria a categoria
        categoria = Categoria(id, nome)

        # Transforma a categoria em dicionário e adiciona na lista
        categorias.append(categoria.salvar_dict())

        # Salva a lista de categoria no banco e exibe a mensagem
        sucesso, mensagem = CategoriaDao.salvar_categoria(categorias)

        if sucesso:
            return True, mensagem
        else:
            return False, mensagem
        


    @staticmethod
    def detalhar_categorias():
        # Carregar categorias
        categorias = CategoriaDao.carregar_categoria()

        # Verifica se existe categoria cadastrada
        if not categorias:
            return False, "\n⚠️ A lista de categorias está vazia!"
        
        # Detalhar categorias
        lista_formatada = "\n📋 Lista de usuários cadastrados:\n"
        for index, categoria in enumerate(sorted(categorias, key=lambda c: c["nome"]), start=1):
            lista_formatada += f"{index}°: {categoria["nome"].upper()}\n"
        lista_formatada += "---------------------------"

        return True, lista_formatada
    

    
    @staticmethod
    def excluir_categoria(nome):
        # Carrega categorias
        categorias = CategoriaDao.carregar_categoria()

        # Valida se existe categoria cadastrada
        if not categorias:
            return False, "⚠️ Não existe nenhuma categoria para excluir."

        # Valida o nome da categoria
        if not nome:
            return False, "⚠️ A categoria não pode estar vazia."
        
        # Valida se o nome da categoria está cadastrado
        dicionario_categoria = None
        for categoria in categorias:
            if categoria["nome"] == nome:
                dicionario_categoria = categoria
                break

        if not dicionario_categoria:
            return False, f"\n⚠️ A categoria {nome} não está cadastrada."
        
        # Verifica se a categoria está em uso com algum produto, se estiver, não pode ser excluída
        #TODO Criar a tabela e as funções de produtos para conseguir implementar essa regra de negócio
        
        # Remove o dicionário da categoria da base
        categorias.remove(dicionario_categoria)

        # Salva a lista atualizada na base
        CategoriaDao.salvar_categoria(categorias)
        return True, f"✅ A categoria {nome} foi deletada com sucesso."
        
