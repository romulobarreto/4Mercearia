from views.categoria_view import *
from views.fornecedor_view import *
from views.produto_view import *
from views.cliente_view import *
from views.cargo_view import *
from views.funcionario_view import *
from views.venda_view import *
from views.relatorio_view import *


def menu():
    # Exibe o menu no terminal
    while True:
        print("\n🖥️ Sistema de gestão de mercearia")
        print("\n📄 Menu:")
        print("1️⃣ - Fornecedor")
        print("2️⃣ - Produto")
        print("3️⃣ - Funcionário")
        print("4️⃣ - Cliente")
        print("5️⃣ - Caixa/Venda")
        print("6️⃣ - Relatórios")
        print("7️⃣ - Sair")
        

        opcao = input("\nEscolha uma das opções: ").strip()            

        if opcao == "1":
            while True:
                print("\n📌Menu de FORNECEDOR: ")
                print("1️⃣ - Cadastrar Fornecedor")
                print("2️⃣ - Detalhar Fornecedores")
                print("3️⃣ - Editar Fornecedor")
                print("4️⃣ - Excluir Fornecedor")
                print("5️⃣ - Voltar")

                opcao_fornecedor = input("\nEscolha uma das opções: ").strip()

                if opcao_fornecedor == "1":
                    FornecedorView.cadastrar_fornecedor()
                elif opcao_fornecedor == "2":
                    FornecedorView.detalhar_fornecedores()
                elif opcao_fornecedor == "3":
                    FornecedorView.editar_fornecedor()
                elif opcao_fornecedor == "4":
                    FornecedorView.excluir_fornecedor()
                elif opcao_fornecedor == "5":
                    break
                else:
                    print("⚠️ Opção inválida! Tente novamente.\n")





        elif opcao == "2":
            while True:
                print("\n📌Menu de PRODUTO: ")
                print("1️⃣ - Cadastrar Produto")
                print("2️⃣ - Detalhar Produtos")
                print("3️⃣ - Editar Produto")
                print("4️⃣ - Excluir Produto")
                print("5️⃣ - 🗂️ CATEGORIA")
                print("6️⃣ - Voltar")

                opcao_produto = input("\nEscolha uma das opções: ").strip()

                if opcao_produto == "1":
                    ProdutoView.cadastrar_produto()
                elif opcao_produto == "2":
                    ProdutoView.detalhar_produtos()
                elif opcao_produto == "3":
                    ProdutoView.editar_produto()
                elif opcao_produto == "4":
                    ProdutoView.excluir_produto()
                elif opcao_produto == "5":
                    while True:
                        print("\n📌 Menu de CATEGORIA: ")
                        print("1️⃣ - Cadastrar Categoria")
                        print("2️⃣ - Detalhar Categorias")
                        print("3️⃣ - Editar Categoria")
                        print("4️⃣ - Excluir Categoria")
                        print("5️⃣ - Voltar")

                        opcao_categoria = input("\nEscolha uma das opções: ").strip()

                        if opcao_categoria == "1":
                            CategoriaView.cadastrar_categoria()
                        elif opcao_categoria == "2":
                            CategoriaView.detalhar_categorias()
                        elif opcao_categoria == "3":
                            CategoriaView.editar_categoria()
                        elif opcao_categoria == "4":
                            CategoriaView.excluir_categoria()
                        elif opcao_categoria == "5":
                            break
                        else:
                            print("⚠️ Opção inválida! Tente novamente.\n")

                elif opcao_produto == "6":
                    break
                else:
                    print("⚠️ Opção inválida! Tente novamente.\n")






        elif opcao == "3":
            while True:
                print("\n📌 Menu de FUNCIONÁRIO: ")
                print("1️⃣ - Cadastrar Funcionário")
                print("2️⃣ - Detalhar Funcionários")
                print("3️⃣ - Editar Funcionário")
                print("4️⃣ - Excluir Funcionário")
                print("5️⃣ - 🖥️ CARGO")
                print("6️⃣ - Voltar")

                opcao_funcionario = input("\nEscolha uma das opções: ").strip()

                if opcao_funcionario == "1":
                    FuncionarioView.cadastrar_funcionario()
                elif opcao_funcionario == "2":
                    FuncionarioView.detalhar_funcionarios()
                elif opcao_funcionario == "3":
                    FuncionarioView.editar_funcionario()
                elif opcao_funcionario == "4":
                    FuncionarioView.excluir_funcionario()
                    
                elif opcao_funcionario == "5":
                    while True:
                        print("\n📌 Menu de CARGO: ")
                        print("1️⃣ - Cadastrar Cargo")
                        print("2️⃣ - Detalhar Cargos")
                        print("3️⃣ - Editar Cargo")
                        print("4️⃣ - Excluir Cargo")
                        print("5️⃣ - Voltar")

                        opcao_cargo = input("\nEscolha uma das opções: ").strip()

                        if opcao_cargo == "1":
                            CargoView.cadastrar_cargo()
                        elif opcao_cargo == "2":
                            CargoView.detalhar_cargos()
                        elif opcao_cargo == "3":
                            CargoView.editar_cargo()
                        elif opcao_cargo == "4":
                            CargoView.excluir_cargo()
                        elif opcao_cargo == "5":
                            break
                        else:
                            print("\n⚠️ Opção inválida! Tente novamente.")

                elif opcao_funcionario == "6":
                    break
                else:
                    print("⚠️ Opção inválida! Tente novamente.\n")






        elif opcao == "4":
            while True:
                print("\n📌 Menu de CLIENTE: ")
                print("1️⃣ - Cadastrar Cliente")
                print("2️⃣ - Detalhar Clientes")
                print("3️⃣ - Editar Cliente")
                print("4️⃣ - Excluir Cliente")
                print("5️⃣ - Voltar")

                opcao_cliente = input("\nEscolha uma das opções: ").strip()

                if opcao_cliente == "1":
                    ClienteView.cadastrar_cliente()
                elif opcao_cliente == "2":
                    ClienteView.detalhar_clientes()
                elif opcao_cliente == "3":
                    ClienteView.editar_cliente()
                elif opcao_cliente == "4":
                    ClienteView.excluir_cliente()    
                elif opcao_cliente == "5":
                    break
                else:
                    print("⚠️ Opção inválida! Tente novamente.\n")




        


        elif opcao == "5":
            while True:
                print("\n🛒 Menu de CARRINHO: ")
                print("1️⃣ - Cadastrar Pedido")
                print("2️⃣ - Voltar")

                opcao_venda = input("\nEscolha uma das opções: ").strip()

                if opcao_venda == "1":
                    VendaView.registrar_produtos()
                elif opcao_venda == "2":
                    break
                else:
                    print("⚠️ Opção inválida! Tente novamente.\n")






        elif opcao == "6":
            while True:
                print(f"\n📑 Menu de RELATÓRIOS:")
                print("1️⃣ - Exportar Cargos")
                print("2️⃣ - Exportar Categorias")
                print("3️⃣ - Exportar Clientes")
                print("4️⃣ - Exportar Fornecedores")
                print("5️⃣ - Exportar Funcionários")
                print("6️⃣ - Exportar Produtos")
                print("7️⃣ - Exportar Vendas")
                print("8️⃣ - Exportar Vendas Por Período")
                print("9️⃣ - Exportar Produtos Mais Vendidos")
                print("🔟 - Exportar Clientes Que Mais Compram")
                print("1️⃣ 1️⃣ - Voltar")

                opcao_exportacao = input("\nEscolha uma das opções: ").strip()

                if opcao_exportacao == "1":
                    RelatorioView.exportar_cargo()
                elif opcao_exportacao == "2":
                    RelatorioView.exportar_categoria()
                elif opcao_exportacao == "3":
                    RelatorioView.exportar_cliente()
                elif opcao_exportacao == "4":
                    RelatorioView.exportar_fornecedor()
                elif opcao_exportacao == "5":
                    RelatorioView.exportar_funcionario()
                elif opcao_exportacao == "6":
                    RelatorioView.exportar_produto()
                elif opcao_exportacao == "7":
                    RelatorioView.exportar_venda()
                elif opcao_exportacao == "8":
                    RelatorioView.exportar_venda_por_data()
                elif opcao_exportacao == "9":
                    RelatorioView.exportar_produto_mais_vendido()
                elif opcao_exportacao == "10":
                    RelatorioView.exportar_clientes_com_mais_compras()
                elif opcao_exportacao == "11":
                    break
                else:
                    print("⚠️ Opção inválida! Tente novamente.\n")





        elif opcao == "7":
            print("🚪 Saindo do programa...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")




if __name__ == "__main__":
    menu()