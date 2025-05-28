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
    def detalhar_categorias(id=None):
        # Chama a função do controller para detalhar as categorias
        sucesso, mensagem = CategoriaController.detalhar_categorias(id)
        # Exibe resultado
        print(mensagem)







    @staticmethod
    def excluir_categoria():
        # Carrega a lista de categorias
        categorias = CategoriaDao.carregar_categoria()

        # Valida se existe categoria cadastrada
        if not categorias:
            print("⚠️ Não existe nenhuma categoria para excluir.")
            return 
        
        # Exibe lista de categorias cadastradas
        CategoriaView.detalhar_categorias()

        # Solicita o ID da categoria que será excluída
        id_categoria = input("\nDigite o ID categoria que deseja excluir (Caso não queira excluir nenhuma, deixe em branco): ").strip()

        if not id_categoria:
            print("✅ Nenhuma categoria foi excluída.")
            return
        
        try:
            id_categoria = int(id_categoria)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        # Chama a função que exclui a categoria
        sucesso, mensagem = CategoriaController.excluir_categoria(id_categoria)

        # Exibe o resultado da função
        print(mensagem)







    @staticmethod
    def editar_categoria():
        # Carrega a lista de categorias
        categorias = CategoriaDao.carregar_categoria()

        # Valida se existe categoria cadastrada
        if not categorias:
            print("⚠️ Não existe nenhuma categoria para editar.")
            return 
        
        # Exibe lista de categorias cadastradas
        CategoriaView.detalhar_categorias()

        # Pega o input do usuário
        id_categoria = input("\nDigite o ID da categoria que deseja editar (Caso não queira editar nenhuma, deixe em branco): ").strip()

        if not id_categoria:
            print("✅ Nenhuma categoria foi alterada.")
            return
        
        try:
            id_categoria = int(id_categoria)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        # Valida se o ID da categoria está cadastrado
        dicionario_categoria = None
        for categoria in categorias:
            if categoria["id"] == id_categoria:
                dicionario_categoria = categoria
                break
        
        if not dicionario_categoria:
            print(f"\n⚠️ O ID: {id_categoria}, não está na lista de cadastro.")
            return
                
        
        # Mostra os detalhes da categoria selecionada
        CategoriaView.detalhar_categorias(id_categoria)

        # Input com o nome atualizado
        novo_nome = input('\nDigite o novo nome da categoria (ou pressione Enter para manter o mesmo): ').strip().lower()

        # Chama a função de editar a categoria
        sucesso, mensagem = CategoriaController.editar_categoria(id_categoria, novo_nome, dicionario_categoria)

        # Mostra a mensagem de sucesso
        print(mensagem)