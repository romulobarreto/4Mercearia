from views.produto_view import *
from daos.venda_dao import *
from datetime import date
from utils.formatacao import formatar_preco
from utils.buscas import criar_dict
from decimal import Decimal
from utils.gerador import gerador_id
from models.venda import *


class VendaController():
    @staticmethod
    def detalhar_itens(itens, produto_id=None):
        # Carrega a lista de produtos
        produtos = ProdutoDao.carregar_produto()

        # Cria o dicionário de acesso rápido
        produtos_dict = criar_dict(produtos)

        if produto_id:
            lista_formatada = "\n🛒 Lista de produtos no carrinho:\n"
            for item in itens:
                produto_nome = produtos_dict[item["produto_id"]]
                if item["produto_id"] == produto_id:
                    lista_formatada += (
                        f"ID: {item["produto_id"]}; Nome: {produto_nome.title()};\n"
                        f"Preço: {formatar_preco(Decimal(item["preco"]))}; Quantidade: {item["quantidade"]}"
                    )
                    break
        else:
            lista_formatada = "\n🛒 Lista de produtos no carrinho:\n"
            for item in sorted(itens, key=lambda c: c["produto_id"]):
                produto_nome = produtos_dict[item["produto_id"]]
                lista_formatada += (
                    f"ID: {item["produto_id"]}; Nome: {produto_nome.title()};\n"
                    f"Preço: {formatar_preco(Decimal(item["preco"]))}; Quantidade: {item["quantidade"]}"
                )
        
        return True, lista_formatada
    






    @staticmethod
    def cadastrar_venda(funcionario_id, cliente_id, itens):
        # Carrega a lista de vendas e produtos
        vendas = VendaDao.carregar_vendas()
        produtos = ProdutoDao.carregar_produto()

        # Gera o ID da venda 
        id = gerador_id(vendas)

        # Pega a data da venda
        data = date.today()

        # Gera o total da venda
        lista_precos = []
        for item in itens:
            lista_precos.append(item["quantidade"] * Decimal(item["preco"]))
        total = sum(lista_precos)

        # Cria a venda
        venda = Venda(id, funcionario_id, data, itens, total, cliente_id)

        # Adiciona a venda na lista de vendas e salva em JSON
        vendas.append(venda.salvar_dict(venda))
        sucesso, mensagem = VendaDao.salvar_vendas(vendas)

        if sucesso:
            for item in itens:
                for produto in produtos:
                    if item["produto_id"] == produto["id"]:
                        produto["quantidade"] -= item["quantidade"]
            ProdutoDao.salvar_produto(produtos)
            return True, mensagem
        else:
            return False, mensagem