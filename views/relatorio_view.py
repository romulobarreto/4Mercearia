from daos.cargo_dao import *
from daos.categoria_dao import *
from daos.fornecedor_dao import *
from daos.cliente_dao import *
from daos.funcionario_dao import *
from daos.produto_dao import *
from daos.venda_dao import *
from utils.exportacao import *
from utils.buscas import *
from utils.formatacao import *
from decimal import Decimal
from datetime import datetime

class RelatorioView():
    @staticmethod
    def exportar_cargo():
        # Carrega a lista de cargos
        cargos = CargoDao.carregar_cargos()

        # Valida se existe cargo cadastrado
        if not cargos:
            print("⚠️ Não existe nenhum cargo cadastrado.")
            return 

        # Chama a função de exportar relatórios
        sucesso, mensagem = exportar_relatorio(cargos, "cargos")  

        if sucesso:
            print(mensagem)
            return 
        





    
    @staticmethod
    def exportar_categoria():
        # Carrega a lista de categorias
        categorias = CategoriaDao.carregar_categoria()

        # Valida se existe categorias cadastrada
        if not categorias:
            print("⚠️ Não existe nenhuma categoria cadastrada.")
            return 

        # Chama a função de exportar relatórios
        sucesso, mensagem = exportar_relatorio(categorias, "categorias")  

        if sucesso:
            print(mensagem)
            return   
        






    @staticmethod
    def exportar_cliente():
        # Carrega a lista de clientes
        clientes = ClienteDao.carregar_cliente()

        # Valida se existe cliente cadastrado
        if not clientes:
            print("⚠️ Não existe nenhum cliente cadastrado.")
            return 

        # Chama a função de exportar relatórios
        sucesso, mensagem = exportar_relatorio(clientes, "clientes")  

        if sucesso:
            print(mensagem)
            return
        
    





    @staticmethod
    def exportar_fornecedor():
        # Carrega a lista de fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Valida se existe fornecedor cadastrado
        if not fornecedores:
            print("⚠️ Não existe nenhum fornecedor cadastrado.")
            return 

        # Chama a função de exportar relatórios
        sucesso, mensagem = exportar_relatorio(fornecedores, "fornecedores")  

        if sucesso:
            print(mensagem)
            return
        



    


    @staticmethod
    def exportar_funcionario():
        # Carrega a lista de funcionarios e cargos
        funcionarios = FuncionarioDao.carregar_funcionario()
        cargos = CargoDao.carregar_cargos()

        # Valida se existe funcionários cadastrados
        if not funcionarios:
            print("⚠️ Não existe nenhum funcionário cadastrado.")
            return 

        # Ajusta o salario do funcionario para exportar em Real-BR
        for funcionario in funcionarios:
            funcionario["cargo_id"] = buscar_nome(funcionario["cargo_id"], cargos)
            funcionario["salario"] = formatar_preco_dados(Decimal(funcionario["salario"]))

        # Chama a função de exportar relatórios
        sucesso, mensagem = exportar_relatorio(funcionarios, "funcionarios")  

        if sucesso:
            print(mensagem)
            return
        
    






    @staticmethod
    def exportar_produto():
        # Carrega a lista de fornecedores, categorias e produtos
        produtos = ProdutoDao.carregar_produto()
        categorias = CategoriaDao.carregar_categoria()
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Valida se existe produto cadastrado
        if not produtos:
            print("⚠️ Não existe nenhum produto cadastrado.")
            return 

        # Ajusta o preço do produto para exportar em Real-BR
        categoria_dict = criar_dict(categorias)
        fornecedor_dict = criar_dict(fornecedores)

        for produto in produtos:
            categoria_nome = categoria_dict[produto["categoria_id"]]
            fornecedor_nome = fornecedor_dict[produto["fornecedor_id"]]
            produto["preco"] = formatar_preco_dados(Decimal(produto["preco"]))
            produto["categoria_id"] = categoria_nome
            produto["fornecedor_id"] = fornecedor_nome

        # Chama a função de exportar relatórios
        sucesso, mensagem = exportar_relatorio(produtos, "produtos")  

        if sucesso:
            print(mensagem)
            return
        





    @staticmethod
    def exportar_venda():
        # Carrega a lista de vendas, produtos, cliente e funcionários
        vendas = VendaDao.carregar_vendas()
        produtos = ProdutoDao.carregar_produto()
        clientes = ClienteDao.carregar_cliente()
        funcionarios = FuncionarioDao.carregar_funcionario()

        # Valida se existe venda cadastrada
        if not vendas:
            print("⚠️ Não existe nenhuma venda cadastrada.")
            return 
        
        # Ajusta a lista de vendas para ser exportada
        clientes_dict = criar_dict(clientes)
        funcionarios_dict = criar_dict(funcionarios)
        produtos_dict = criar_dict(produtos)

        lista_vendas = []
        for venda in vendas:
            funcionario_nome = funcionarios_dict.get(venda["funcionario_id"], "Desconhecido")
            cliente_nome = clientes_dict.get(venda["cliente_id"], "Não identificado") if venda.get("cliente_id") else "Não identificado"

            for item in venda["itens"]:
                produto_nome = produtos_dict.get(item["produto_id"], "Desconhecido")
                linha = {
                    "ID Venda": venda["id"],
                    "Data": formatar_data_br(venda["data"]),
                    "Funcionário": funcionario_nome,
                    "Cliente": cliente_nome,
                    "Produto": produto_nome,
                    "Quantidade": item["quantidade"],
                    "Preço Unitário": formatar_preco_dados(Decimal(item["preco"]))
                }
                lista_vendas.append(linha)
        
        # Chama a função de exportar relatórios
        sucesso, mensagem = exportar_relatorio(lista_vendas, "vendas")  

        if sucesso:
            print(mensagem)
            return
        






    @staticmethod
    def exportar_venda_por_data():
        # Carrega a lista de vendas, produtos, cliente e funcionários
        vendas = VendaDao.carregar_vendas()
        produtos = ProdutoDao.carregar_produto()
        clientes = ClienteDao.carregar_cliente()
        funcionarios = FuncionarioDao.carregar_funcionario()

        # Valida se existe venda cadastrada
        if not vendas:
            print("⚠️ Não existe nenhuma venda cadastrada.")
            return 
        
        # Solicita a data inicial e final ao usuário
        print("\n🗓️ Data Inicial:")
        while True:
            try:
                dia_inicio = int(input("Digite o dia inicial: "))
                mes_inicio = int(input("Digite o mês inicial: "))
                ano_inicio = int(input("Digite o ano inicial: "))
                break
            except ValueError:
                print("\n⚠️ O valor não está na formatação correta.")
                continue
        
        print("\n🗓️ Data Final:")
        while True:
            try:
                dia_fim = int(input("Digite o dia final: "))
                mes_fim = int(input("Digite o mês final: "))
                ano_fim = int(input("Digite o ano final: "))
                break
            except ValueError:
                print("\n⚠️ O valor não está na formatação correta.")
                continue

        # Ajusta a data inicial e final
        data_inicial = datetime.strptime(f"{ano_inicio}-{mes_inicio:02}-{dia_inicio:02}", "%Y-%m-%d")
        data_final = datetime.strptime(f"{ano_fim}-{mes_fim:02}-{dia_fim:02}", "%Y-%m-%d")

        # Ajusta a lista de vendas para ser exportada
        clientes_dict = criar_dict(clientes)
        funcionarios_dict = criar_dict(funcionarios)
        produtos_dict = criar_dict(produtos)

        lista_vendas = []

        for venda in vendas:
            funcionario_nome = funcionarios_dict.get(venda["funcionario_id"], "Desconhecido")
            cliente_nome = clientes_dict.get(venda["cliente_id"], "Não identificado") if venda.get("cliente_id") else "Não identificado"
            data_venda = datetime.strptime(venda["data"], "%Y-%m-%d")
            if data_inicial <= data_venda <= data_final:
                for item in venda["itens"]:
                    produto_nome = produtos_dict.get(item["produto_id"], "Desconhecido")
                    linha = {
                        "ID Venda": venda["id"],
                        "Data": formatar_data_br(venda["data"]),
                        "Funcionário": funcionario_nome,
                        "Cliente": cliente_nome,
                        "Produto": produto_nome,
                        "Quantidade": item["quantidade"],
                        "Preço Unitário": formatar_preco_dados(Decimal(item["preco"]))
                    }
                    lista_vendas.append(linha)
        
        if not lista_vendas:
            print(f"\n⚠️ Nenhuma venda registrada no período entre: \nData Inicial: {formatar_data_br(data_inicial)}\nData Final: {formatar_data_br(data_final)}")
            return
        
        # Chama a função de exportar relatórios
        sucesso, mensagem = exportar_relatorio(lista_vendas, "vendas")  

        if sucesso:
            print(mensagem)
            return
        






    @staticmethod
    def exportar_produto_mais_vendido():
        # Carrega a lista de vendas e produtos
        vendas = VendaDao.carregar_vendas()
        produtos = ProdutoDao.carregar_produto()

        # Valida se existe venda cadastrada
        if not vendas:
            print("⚠️ Não existe nenhuma venda cadastrada.")
            return
        
        # Cria um dicionário com os nomes dos produtos a partir do ID
        produtos_dict = criar_dict(produtos)

        # Dicionário para agrupar as quantidades vendidas por produto_id
        resumo_vendas = {}

        for venda in vendas:
            for item in venda["itens"]:
                produto_id = item["produto_id"]
                quantidade = item["quantidade"]
                nome_produto = produtos_dict.get(produto_id, "Desconhecido")

                if produto_id not in resumo_vendas:
                    resumo_vendas[produto_id] = {
                        "Produto": nome_produto,
                        "Quantidade Vendida": quantidade
                    }
                else:
                    resumo_vendas[produto_id]["Quantidade Vendida"] += quantidade
        
        # Converte o dicionário em lista e ordena do mais vendido para o menos vendido
        lista_mais_vendidos = sorted(resumo_vendas.values(), key=lambda x: x["Quantidade Vendida"], reverse=True)

        # Exporta o relatório
        sucesso, mensagem = exportar_relatorio(lista_mais_vendidos, "produtos_mais_vendidos")  

        if sucesso:
            print(mensagem)
            return
        








    @staticmethod
    def exportar_clientes_com_mais_compras():
        # Carrega a lista de vendas e clientes
        vendas = VendaDao.carregar_vendas()
        clientes = ClienteDao.carregar_cliente()

        # Valida se existe venda cadastrada
        if not vendas:
            print("⚠️ Não existe nenhuma venda cadastrada.")
            return
        
        # Cria um dicionário com os nomes dos clientes a partir do ID
        clientes_dict = criar_dict(clientes)

        # Cria um dicioário de cliente e quntidade comprada
        resumo_compras = {}

        for venda in vendas:
            cliente_id = venda.get("cliente_id")
            if cliente_id:
                cliente_nome = clientes_dict[venda["cliente_id"]]
                if cliente_id not in resumo_compras:
                    resumo_compras[cliente_id] = {
                        "Cliente": cliente_nome,
                        "Compras": 1
                    }
                else:
                    resumo_compras[cliente_id]["Compras"] += 1
            else:
                cliente_id = 0
                cliente_nome = "Desconhecido"
                if cliente_id not in resumo_compras:
                    resumo_compras[cliente_id] = {
                        "Cliente": cliente_nome,
                        "Compras": 1
                    }
                else:
                    resumo_compras[cliente_id]["Compras"] += 1
        

        # Converte o dicionário em lista e ordena do mais vendido para o menos vendido
        lista_mais_compras = sorted(resumo_compras.values(), key=lambda c: c["Compras"], reverse=True)

        # Exporta o relatório
        sucesso, mensagem = exportar_relatorio(lista_mais_compras, "clientes_mais_compras")  

        if sucesso:
            print(mensagem)
            return