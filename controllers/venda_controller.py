from views.produto_view import *
from datetime import date
from utils.formatacao import formatar_preco
from utils.buscas import criar_dict
from decimal import Decimal


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