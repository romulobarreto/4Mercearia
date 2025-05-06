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
        CategoriaView.detalhar_categorias()
        categoria_nome = input("\nDigite o nome da categoria (ou deixe vazio para interromper o cadastro): ").strip().lower()

        # Mostra os fornecedores disponíveis para o usuário escolher um
        FornecedorView.detalhar_fornecedores()
        fornecedor_nome = input("\nDigite o nome do fornecedor (ou deixe vazio para interromper o cadastro): ").strip().lower()

        # Chama a função de cadastrar um produto
        sucesso, mensagem = ProdutoController.cadastrar_produto(nome, preco, quantidade, categoria_nome, fornecedor_nome)
        print(mensagem)


    @staticmethod
    def detalhar_produtos():
        # Chama a função de detalhar 
        sucesso, mensagem = ProdutoController.detalhar_produtos()
        # Exibe o resultado
        print(mensagem)