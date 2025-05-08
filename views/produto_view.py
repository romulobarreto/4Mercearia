from decimal import Decimal, InvalidOperation
from controllers.produto_controller import *
from views.fornecedor_view import *
from views.categoria_view import *

class ProdutoView():
    @staticmethod
    def cadastrar_produto():
        # Carrega as listas de categoria e fornecedores e verifica se estão vazias, se estiverem, cancela o cadastro
        categorias = CategoriaDao.carregar_categoria()
        fornecedores = FornecedorDao.carregar_fornecedor()

        if not categorias:
            print("\n🚫 Não existe nenhuma categoria cadastrada, não é possível cadastrar um produto.")
            return
        
        if not fornecedores:
            print("\n🚫 Não existe nenhum fornecedor cadastrado, não é possível cadastrar um produto.")
            return

        # Solicita os inputs ao usuário
        nome = input("\nDigite o nome do produto: ").strip().lower()
        try:
            preco = Decimal(input("\nDigite o preço do produto: ").strip())
        except InvalidOperation:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        try:
            quantidade = int(input("\nDigite a quantidade em estoque do produto: ").strip())
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        # Mostra as categorias disponíveis para o usuário escolher uma
        print("\n📋 Lista de categorias:")
        for categoria in sorted(categorias, key=lambda c: c["nome"]):
            print(f"{categoria["id"]}: {categoria["nome"].title()}")

        categoria_id = input("\nDigite o ID da categoria (ou deixe vazio para interromper o cadastro): ").strip()

        if not categoria_id:
            print("✅ Nenhuma categoria foi alterada.")
            return
        
        try:
            categoria_id = int(categoria_id)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        # Mostra os fornecedores disponíveis para o usuário escolher um
        print("\n📋 Lista de fornecedores:")
        for fornecedor in sorted(fornecedores, key=lambda c: c["nome"]):
            print(f"{fornecedor["id"]}: {fornecedor["nome"].title()}")

        fornecedor_id = input("\nDigite o ID do fornecedor (ou deixe vazio para interromper o cadastro): ").strip()

        if not fornecedor_id:
            print("✅ Nenhum fornecedor foi editado.")
            return
        
        try:
            fornecedor_id = int(fornecedor_id)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        # Chama a função de cadastrar um produto
        sucesso, mensagem = ProdutoController.cadastrar_produto(nome, preco, quantidade, categoria_id, fornecedor_id)
        print(mensagem)


    @staticmethod
    def detalhar_produtos():
        # Chama a função de detalhar 
        sucesso, mensagem = ProdutoController.detalhar_produtos()
        # Exibe o resultado
        print(mensagem)


    @staticmethod
    def excluir_produto():
        # Chama a lista de produto
        produtos = ProdutoDao.carregar_produto()

        # Se a lista estiver vazia, encerra a função
        if not produtos:
            return False, "\n⚠️ Não existem produtos para serem excluídos."
        
        # Chama e exibe a lista de produtos para o usuário ver as opções e escolher uma
        print("\n📋 Lista de produtos:")
        for produto in sorted(produtos, key=lambda c: c["nome"]):
            print(f"{produto["id"]}: {produto["nome"].title()}")

        # Solicita ao usuário o ID do produto que ele deseja excluir
        id_produto = input("\nDigite o ID do produto que deseja excluir (Caso não queira excluir nenhum, deixe em branco): ")

        if not id_produto:
            print("✅ Nenhum produto foi excluído.")
            return

        # Converte o ID para INT
        try:
            id_produto = int(id_produto)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return       

        # Chama a função de excluir o produto
        sucesso, mensagem = ProdutoController.excluir_produto(id_produto)

        print(mensagem)