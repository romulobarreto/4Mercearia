from controllers.categoria_controller import *

class CategoriaView:

    @staticmethod
    def cadastrar_categoria():
        # Pede os inputs ao usuário de ID e Nome da categoria
        nome = input("\nDigite o nome da categoria: ").strip().lower()

        # Cria o usuário e retorna a mensagem
        sucesso, mensagem = CategoriaController.cadastrar_categoria(nome)
        print(mensagem)