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



    @staticmethod
    def editar_categoria():
        # Carrega a lista de categorias
        categorias = CategoriaDao.carregar_categoria()

        # Pega o input do usuário
        nome = input("\nDigite a categoria que deseja editar: ").strip().lower()

        # Valida se existe categoria cadastrada
        if not categorias:
            print("⚠️ Não existe nenhuma categoria para editar.")
            return

        # Valida o nome da categoria
        if not nome:
            print("⚠️ A categoria não pode estar vazia.")
            return
        
        # Valida se o nome da categoria está cadastrado
        dicionario_categoria = None
        for categoria in categorias:
            if categoria["nome"] == nome:
                dicionario_categoria = categoria
                break

        if not dicionario_categoria:
            print(f"\n⚠️ A categoria {nome} não está cadastrada.")
            return
        
        # Mostra os detalhes da categoria selecionada
        print(f"\nDetalhes da categoria:\nID: {dicionario_categoria["id"]}\nNome: {dicionario_categoria["nome"].upper()}")

        # Input com o nome atualizado
        novo_nome = input('\nDigite o novo nome da categoria (ou pressione Enter para manter o mesmo): ').strip().lower()

        # Chama a função de editar a categoria
        sucesso, mensagem = CategoriaController.editar_categoria(nome, novo_nome)

        # Mostra a mensagem de sucesso
        print(mensagem)