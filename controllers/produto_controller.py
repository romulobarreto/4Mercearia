from decimal import Decimal
from models.produto import *
from daos.produto_dao import *
from daos.categoria_dao import *
from daos.fornecedor_dao import *
from utils.formatacao import formatar_preco
from utils.buscas import criar_dict_categorias, criar_dict_fornecedores

class ProdutoController():
    @staticmethod
    def validar_dados(nome, preco, quantidade, categoria_id, fornecedor_id, nome_atual=None):
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
        if preco <= Decimal('0'):
            return False, "\n⚠️ O produto não pode ser gratuíto."
        
        # Valida se a quantidade em estoque é igual ou superior a zero
        if quantidade < 0:
            return False, "\n⚠️ Não é possível ter estoque negativo de um produto."
        
        # Valida se a categoria é valida
        if not any(categoria["id"] == categoria_id for categoria in categorias):
            return False, f"\n⚠️ O ID: {categoria_id} não está na lista de categorias."
    
        # Valida se o fornecedor é válido
        if not any(fornecedor["id"] == fornecedor_id for fornecedor in fornecedores):
            return False, f"\n⚠️ O ID: {fornecedor_id} não está na lista de fornecedores."
        
        # Mensagem de sucesso
        return True, "\n✅ Dados aprovados."
    




    @staticmethod
    def cadastrar_produto(nome, preco, quantidade, categoria_id, fornecedor_id):
        # Chama a função e valida os dados inputados
        sucesso, mensagem = ProdutoController.validar_dados(nome, preco, quantidade, categoria_id, fornecedor_id)
        if not sucesso:
            return False, mensagem
        
        # Carregar lista de produtos, categorias e fornecedores
        produtos = ProdutoDao.carregar_produto()
        categorias = CategoriaDao.carregar_categoria()
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Define o valor do ID para produto
        id = max([produto["id"] for produto in produtos], default=0) + 1

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
        for produto in sorted(produtos, key=lambda c: c["nome"]):
            categoria_nome = categorias_dict[produto["categoria_id"]]
            fornecedor_nome = fornecedores_dict[produto["fornecedor_id"]]

            lista_formatada += (
                f"ID {produto["id"]}: {produto["nome"].title()}\n"
                f"Preço: {formatar_preco(Decimal(produto["preco"]))}\n"
                f"Quantidade em estoque: {produto["quantidade"]}\n"
                f"Categoria: {categoria_nome.title()}\n"
                f"Fornecedor: {fornecedor_nome.title()}\n"
                f"---------------------------\n"
            )

        return True, lista_formatada
    




    @staticmethod
    def excluir_produto(id_produto):
        # Carrega a lista de produtos
        produtos = ProdutoDao.carregar_produto()

        # Verifica se o ID informado está na base de produtos
        dicionario_produto = None
        for produto in produtos:
            if produto["id"] == id_produto:
                dicionario_produto = produto
                break
        
        if not dicionario_produto:
            return False, f"\n⚠️ {id_produto} não está na lista de produtos."            
            
        # Verifica se o produto escolhido faz parte de uma venda, se fizer, não permite a exclusão do produto
        #TODO Criar a parte do caixa da mercearia e implementar a regra de negócio
            
        # Pega o dicionário do produto escolhido e remove da lista da produtos
        produtos.remove(dicionario_produto)

        # Salva a lista atualizada
        sucesso, mensagem = ProdutoDao.salvar_produto(produtos)

        return True, f"\n✅ {dicionario_produto["nome"].title()} foi removido com sucesso."
    



    @staticmethod
    def editar_produto(nome, preco, quantidade, categoria_id, fornecedor_id, lista_produto):
        # Chama a validação de dados
        sucesso, mensagem = ProdutoController.validar_dados(nome, preco, quantidade, categoria_id, fornecedor_id, lista_produto["nome"])

        if not sucesso:
            return False, mensagem
        
        # Carrega a lista de produtos
        produtos = ProdutoDao.carregar_produto()

        # Atualiza os dados novos na lista
        for produto in produtos:
            if produto["id"] == lista_produto["id"]:
                produto["nome"] = nome
                produto["preco"] = str(preco)
                produto["quantidade"] = quantidade
                produto["categoria_id"] = categoria_id
                produto["fornecedor_id"] = fornecedor_id
                break

        # Salva as alterações no banco
        sucesso, mensagem = ProdutoDao.salvar_produto(produtos)
        
        if sucesso:
            return True, "✅ Produto editado com sucesso."
        else:
            return False, "⚠️ Erro ao salvar a alteração no banco de dados."