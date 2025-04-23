from controllers.fornecedor_controller import *

class FornecedorView:

    @staticmethod
    def cadastrar_fornecedor():
        # Pede os inputs ao usuário de Nome e Telefone do fornecedor
        nome = input("\nDigite o nome do fornecedor: ").strip().lower()
        telefone = input("\nDigite o telefone (DDD + Número): ").strip().replace("(", "").replace(")", "").replace("-","").replace(" ","")

        # Cria o usuário e retorna a mensagem
        sucesso, mensagem = FornecedorController.cadastrar_fornecedor(nome, telefone)
        print(mensagem)

    
    @staticmethod
    def detalhar_fornecedores():
        # Chama a função do controller para detalhar os fornecedores
        sucesso, mensagem = FornecedorController.detalhar_fornecedores()
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