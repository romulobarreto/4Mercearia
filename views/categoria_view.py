from controllers.categoria_controller import *

class CategoriaView:

    @staticmethod
    def cadastrar_categoria():
        # Pede os inputs ao usuário de ID e Nome da categoria
        nome = input("\nDigite o nome da categoria: ").strip().lower()

        # Cria o usuário e retorna a mensagem
        sucesso, mensagem = CategoriaController.cadastrar_categoria(nome)
        print(mensagem)

    
    @staticmethod
    def detalhar_categorias():
        # Chama a função do controller para detalhar as categorias
        sucesso, mensagem = CategoriaController.detalhar_categorias()
        # Exibe resultado
        print(mensagem)


    @staticmethod
    def excluir_categoria():
        # Pega o input do usuário
        nome = input("\nDigite a categoria que deseja excluir: ").strip().lower()

        # Chama a função que exclui a categoria
        sucesso, mensagem = CategoriaController.excluir_categoria(nome)

        # Exibe o resultado da função
        print(mensagem)