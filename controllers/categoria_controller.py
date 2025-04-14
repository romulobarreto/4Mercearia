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
                return False, "⚠️ A categoria já está cadastrada."
        
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



