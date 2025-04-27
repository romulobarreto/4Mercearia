from models.produto import *
from daos.produto_dao import *
from daos.categoria_dao import *
from daos.fornecedor_dao import *

class ProdutoController():
    @staticmethod
    def validar_dados(nome, preco, quantidade, categoria_nome, fornecedor_nome, nome_atual=None):
        # Carregar lista de produtos, categorias e fornecedores
        produtos = ProdutoDao.carregar_produto()
        categorias = CategoriaDao.carregar_categoria()
        fornecedores = FornecedorDao.carregar_fornecedor()


        # Valida se nome está vazio e se é um nome diferente dos já cadastrados
        if not nome:
            return False, "⚠️ O nome não pode estar vazio."

        if nome != nome_atual and any(produto["nome"] == nome for produto in produtos):
            return False, "🚫 Produto já cadastrado." 
        
        # Valida se o preço é maior que zero
        if preco <= 0:
            return False, "⚠️ O produto não pode ser gratuíto."
        
        # Valida se a quantidade em estoque é igual ou superior a zero
        if quantidade < 0:
            return False, "⚠️ Não é possível ter estoque negativo de um produto."
        
        # Valida se a categoria é valida
        if not any(categoria["nome"] == categoria_nome for categoria in categorias):
            return False, f"⚠️ {categoria_nome.title()} não está na lista de categorias."

        # Valida se o fornecedor é válido
        if not any(fornecedor["nome"] == fornecedor_nome for fornecedor in fornecedores):
            return False, f"⚠️ {fornecedor_nome.title()} não está na lista de fornecedores."
        
        # Mensagem de sucesso
        return True, "✅ Dados aprovados."
    

    @staticmethod
    def cadastrar_produto(nome, preco, quantidade, categoria_nome, fornecedor_nome):
        # Chama a função e valida os dados inputados
        sucesso, mensagem = ProdutoController.validar_dados(nome, preco, quantidade, categoria_nome, fornecedor_nome)
        if not sucesso:
            return False, mensagem
        
        # Carregar lista de produtos, categorias e fornecedores
        produtos = ProdutoDao.carregar_produto()
        categorias = CategoriaDao.carregar_categoria()
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Define o valor do ID para produto
        id = max([produto[nome] for produto in produtos], default=0) + 1

        # Chama o ID da categoria
        categoria_id = next((categoria["id"] for categoria in categorias if categoria["nome"] == categoria_nome), None)

        # Chama o ID do fornecedor
        fornecedor_id = next((fornecedor["id"] for fornecedor in fornecedores if fornecedor["nome"] == fornecedor_nome), None)

        # Cria o produto
        produto = Produto(id, nome, preco, quantidade, categoria_id, fornecedor_id)

        # Adiciona o produto na lista de produtos e salva exibindo a mensagem de sucesso
        produtos.append(produto.salvar_dict())
        sucesso, mensagem = ProdutoDao.salvar_produto(produtos)

        if sucesso:
            return True, mensagem
        else:
            return False, mensagem