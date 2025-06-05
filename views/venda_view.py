from daos.venda_dao import *
from views.funcionario_view import *
from views.cliente_view import *
from views.produto_view import *
from controllers.venda_controller import *
from utils.buscas import buscar_nome


class VendaView():
    @staticmethod
    def adicionar_itens():
        # Carrega a lista de produtos
        produtos = ProdutoDao.carregar_produto()

        # Adiciona produtos a lista de itens vendidos
        itens = []
        while True:
            # Exibe a lista de produtos
            ProdutoView.detalhar_produtos()

            # Pede o ID do produto que está sendo vendido e valida
            try:
                produto_id = int(input("\nDigite o ID do produto que será vendido: "))
            except ValueError:
                print("\n⚠️ O valor não está na formatação correta.")
                continue

            # Valida se id_produto faz parte da lista de produtos
            dicionario_produto = None
            for produto in produtos:
                if produto["id"] == produto_id:
                    dicionario_produto = produto
                    break
            
            if not dicionario_produto:
                print(f"\n⚠️ O ID: {produto_id}, não está na base produtos.")
                continue

            # Exibe os detalhes do produto escolhido
            ProdutoView.detalhar_produtos(produto_id)

            # Pede a quantidade que será vendida
            try:
                quantidade = int(input("\nDigite a quantidade que será vendida: "))
                if (quantidade - dicionario_produto["quantidade"]) < 0:
                    print(f"\n⚠️ Não temos a quantidade de: {quantidade} em estoque para vender.")
                    continue
            except ValueError:
                print("\n⚠️ O valor não está na formatação correta.")
                continue

            itens.append({"produto_id": dicionario_produto["id"], "quantidade": quantidade, "preco": dicionario_produto["preco"]})

            while True:
                decisao = input("\n📠 Registrar mais itens ao pedido (S/N)? ").strip().lower()
                if decisao == "s":
                    break
                elif decisao == "n":
                    return itens
            





    @staticmethod
    def editar_itens(itens):
        # Carrega a lista de produtos
        produtos = ProdutoDao.carregar_produto()

        # Exibe a lista de itens no carrinho
        sucesso, mensagem = VendaController.detalhar_itens(itens)
        print(mensagem)

        while True:
            # Pede o ID do produto que será editado
            try:
                produto_id = int(input("\nDigite o ID do produto que deseja alterar: "))
            except ValueError:
                print("\n⚠️ O valor não está na formatação correta.")
                continue

            # Valida se id_produto faz parte da lista de produtos
            dicionario_produto = None
            for item in itens:
                if item["produto_id"] == produto_id:
                    dicionario_produto = item
                    break
            
            if not dicionario_produto:
                print(f"\n⚠️ O ID: {produto_id}, não está no carrinho.")
                continue

            # Exibe os dados do item escolhido do carrinho
            sucesso, mensagem = VendaController.detalhar_itens(itens, produto_id)
            print(mensagem)

            # Exibe a quantidade disponível em estoque do produto escolhido
            quantidade_estoque = None
            print(f"\n🛒 Quantidade disponível em estoque do: {buscar_nome(produto_id, produtos).title()}")
            for produto in produtos:
                if produto["id"] == produto_id:
                    quantidade_estoque = produto["quantidade"]
                    print(f"Quantidade: {produto["quantidade"]}")
                    break
            
            while True:
                # Solicita a nova quantidade do produto
                try:
                    quantidade = int(input(f"\nDigite a nova quantidade que deseja vender (Digite 0 para excluir o produto da lista): "))
                except ValueError:
                    print("\n⚠️ O valor não está na formatação correta.")
                    continue

                if quantidade <= 0:
                    itens.remove(dicionario_produto)
                    break
                elif quantidade > quantidade_estoque:
                    print(f"\n⚠️ Temos apenas {quantidade_estoque} em estoque, ajuste o seu pedido.")
                    continue
                else:
                    dicionario_produto["quantidade"] = quantidade
                    print("\n✅ Quantidade atualizada com sucesso.")
                    break
                
            # Verifica se o usuário quer editar mais alguma coisa ou encerrar
            while True:
                decisao = input("\n📠 Editar mais itens no pedido (S/N)? ").strip().lower()
                if decisao == "s":
                    break
                elif decisao == "n":
                    return itens
            


        





    @staticmethod
    def registrar_produtos():
        # Carrega a lista de funcionários, clientes e produtos
        funcionarios = FuncionarioDao.carregar_funcionario()
        clientes = ClienteDao.carregar_cliente()
        produtos = ProdutoDao.carregar_produto()

        if not funcionarios:
            print("\n⚠️ Não existem funcionários cadastrados para realizar a venda.")
            return
        
        if not produtos:
            print("\n⚠️ Não existem produtos cadastrados para realizar a venda.")
            return
        
        # Exibe a lista de funcionários
        FuncionarioView.detalhar_funcionarios()

        # Solicita o ID do funcionário que realizará a venda
        try:
            funcionario_id = int(input("\nDigite o ID do funcionário que realizará a venda: ").strip())
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return  
        
        # Verifica se o ID está na base de dados
        if not any(funcionario["id"] == funcionario_id for funcionario in funcionarios):
            print(f"\n⚠️ O ID: {funcionario_id}, não está na base funcionários.")
            return
        
        # Exibe a lista de clientes
        ClienteView.detalhar_clientes()

        # Solicita o ID do cliente que está comprando
        cliente_id = input("\nDigite o ID do cliente que está comprando (Pressione Enter para registrar sem cliente): ").strip()

        # Verifica se o ID é None, se não for, valida na base de dados
        if cliente_id:
            try:
                cliente_id = int(cliente_id)
                if not any(cliente["id"] == cliente_id for cliente in clientes):
                    print(f"\n⚠️ O ID: {cliente_id}, não está na base clientes.")
                    return
            except ValueError:
                print("\n⚠️ O valor não está na formatação correta.")
                return
        else:
            cliente_id = None
        

