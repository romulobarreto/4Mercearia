from views.categoria_view import *
from views.fornecedor_view import *
from views.produto_view import *
from views.cliente_view import *
from views.cargo_view import *

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
                print("2️⃣ - Detalhar Funcionário")
                print("3️⃣ - Editar Funcionário")
                print("4️⃣ - Excluir Funcionário")
                print("5️⃣ - 🖥️ CARGO")
                print("6️⃣ - Voltar")

                opcao_funcionario = input("\nEscolha uma das opções: ").strip()

                #if opcao_funcionario == "1":
                    #ClienteView.cadastrar_cliente()
                #elif opcao_funcionario == "2":
                    #ClienteView.detalhar_clientes()
                #elif opcao_funcionario == "3":
                    #ClienteView.editar_cliente()
                #elif opcao_funcionario == "4":
                    #ClienteView.excluir_cliente()
                if opcao_funcionario == "5":
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
                            print("⚠️ Opção inválida! Tente novamente.\n")

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







        elif opcao == "7":
            print("🚪 Saindo do programa...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")




if __name__ == "__main__":
    menu()