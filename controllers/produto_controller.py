from models.produto import *
from daos.produto_dao import *
from daos.categoria_dao import *
from daos.fornecedor_dao import *
from utils.formatacao import formatar_preco
from utils.buscas import criar_dict_categorias, criar_dict_fornecedores, buscar_id_categoria, buscar_id_fornecedor

class ProdutoController():
    @staticmethod
    def validar_dados(nome, preco, quantidade, categoria_nome, fornecedor_nome, nome_atual=None):
        # Carregar lista de produtos, categorias e fornecedores
        produtos = ProdutoDao.carregar_produto()
        categorias = CategoriaDao.carregar_categoria()
        fornecedores = FornecedorDao.carregar_fornecedor()


        # Valida se nome está vazio e se é um nome diferente dos já cadastrados
        if not nome:
            return False, "\n⚠️ O nome não pode estar vazio."

        if nome != nome_atual and any(produto["nome"] == nome for produto in produtos):
            return False, "\n🚫 Produto já cadastrado." 
        
        # Valida se o preço é maior que zero
        if preco <= 0:
            return False, "\n⚠️ O produto não pode ser gratuíto."
        
        # Valida se a quantidade em estoque é igual ou superior a zero
        if quantidade < 0:
            return False, "\n⚠️ Não é possível ter estoque negativo de um produto."
        
        # Se categoria estiver vazia, cancela a validação
        if not categoria_nome:
            return False, f"⚠️ Cadastro interrompido."
        
        # Valida se a categoria é valida
        if not any(categoria["nome"] == categoria_nome for categoria in categorias):
            return False, f"\n⚠️ {categoria_nome.title()} não está na lista de categorias."
        
        # Se fornecedor estiver vazio, cancela a validação
        if not fornecedor_nome:
            return False, f"⚠️ Cadastro interrompido."

        # Valida se o fornecedor é válido
        if not any(fornecedor["nome"] == fornecedor_nome for fornecedor in fornecedores):
            return False, f"\n⚠️ {fornecedor_nome.title()} não está na lista de fornecedores."
        
        # Mensagem de sucesso
        return True, "\n✅ Dados aprovados."
    

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
        id = max([produto["id"] for produto in produtos], default=0) + 1

        # Chama o ID da categoria
        categoria_id = buscar_id_categoria(categoria_nome, categorias)

        # Chama o ID do fornecedor
        fornecedor_id = buscar_id_fornecedor(fornecedor_nome, fornecedores)

        # Cria o produto
        produto = Produto(id, nome, preco, quantidade, categoria_id, fornecedor_id)

        # Adiciona o produto na lista de produtos e salva exibindo a mensagem de sucesso
        produtos.append(produto.salvar_dict())
        sucesso, mensagem = ProdutoDao.salvar_produto(produtos)

        if sucesso:
            return True, mensagem
        else:
            return False, mensagem
        

    @staticmethod
    def detalhar_produtos():
        # Carrega a lista de produtos, categorias e fornecedores
        produtos = ProdutoDao.carregar_produto()
        categorias = CategoriaDao.carregar_categoria()
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Verifica se existe produtos, caso não haja, exibe erro
        if not produtos:
            return False, "\n⚠️ A lista de produtos está vazia!"
        
        # Cria os dicionários de acesso rápido de categoria e fornecedor
        categorias_dict = criar_dict_categorias(categorias)
        fornecedores_dict = criar_dict_fornecedores(fornecedores)
        
        # Formata a lista de produtos e exibe
        lista_formatada = "\n📋 Lista de produtos cadastrados:\n"
        for index, produto in enumerate(sorted(produtos, key=lambda c: c["nome"]), start=1):
            categoria_nome = categorias_dict[produto["categoria_id"]]
            fornecedor_nome = fornecedores_dict[produto["fornecedor_id"]]

            lista_formatada += (
                f"{index}°: {produto["nome"].title()}\n"
                f"Preço: {formatar_preco(produto["preco"])}\n"
                f"Quantidade em estoque: {produto["quantidade"]}\n"
                f"Categoria: {categoria_nome.title()}\n"
                f"Fornecedor: {fornecedor_nome.title()}\n"
                f"---------------------------"
            )

        return True, lista_formatada