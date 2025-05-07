from views.categoria_view import *
from views.fornecedor_view import *
from views.produto_view import *

def menu():
    # Exibe o menu no terminal
    while True:
        print("\n🖥️ Sistema de gestão de mercearia")
        print("\n📄 Menu:")
        print("1️⃣ - Categoria")
        print("2️⃣ - Fornecedor")
        print("3️⃣ - Produto")
        print("4️⃣ - Funcionário")
        print("5️⃣ - Cliente")
        print("6️⃣ - Caixa/Venda")
        print("7️⃣ - Relatórios")
        print("8️⃣ - Sair")
        

        opcao = input("\nEscolha uma das opções: ").strip()

        if opcao == "1":
            while True:
                print("\n📌Menu de CATEGORIA: ")
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

        elif opcao == "2":
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

        elif opcao == "3":
            while True:
                print("\n📌Menu de PRODUTO: ")
                print("1️⃣ - Cadastrar Produto")
                print("2️⃣ - Detalhar Produtos")
                print("3️⃣ - Editar Produto")
                print("4️⃣ - Excluir Produto")
                print("5️⃣ - Voltar")

                opcao_produto = input("\nEscolha uma das opções: ").strip()

                if opcao_produto == "1":
                    ProdutoView.cadastrar_produto()
                elif opcao_produto == "2":
                    ProdutoView.detalhar_produtos()
                #elif opcao_produto == "3":
                    # Chama a funcao de detalhar produtos 
                    #ProdutoView.detalhar_produtos()
                    # Chama a funcao de editar fornecedor
                    #FornecedorView.editar_fornecedor() #TODO Criar função de editar os produtos
                elif opcao_produto == "4":
                    # Chama a funcao de excluir fornecedor
                    ProdutoView.excluir_produto()
                elif opcao_produto == "5":
                    break
                else:
                    print("⚠️ Opção inválida! Tente novamente.\n")


        elif opcao == "8":
            print("🚪 Saindo do programa...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")




if __name__ == "__main__":
    menu()