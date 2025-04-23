from views.categoria_view import *
from views.fornecedor_view import *

def menu():
    # Exibe o menu no terminal
    while True:
        print("\n🖥️ Sistema de gestão de mercearia")
        print("\n📄 Menu:")
        print("1️⃣ - Categoria")
        print("2️⃣ - Fornecedor")
        print("3️⃣ - Sair")

        opcao = input("\nEscolha uma das opções: ").strip()

        if opcao == "1":
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
                CategoriaView.detalhar_categorias()
                CategoriaView.editar_categoria()
            elif opcao_categoria == "4":
                CategoriaView.detalhar_categorias()
                CategoriaView.excluir_categoria()
            elif opcao_categoria == "5":
                continue
            else:
                print("⚠️ Opção inválida! Tente novamente.\n")

        elif opcao == "2":
            print("\n📌Menu de FORNECEDOR: ")
            print("1️⃣ - Cadastrar Fornecedor")
            print("2️⃣ - Detalhar Fornecedores")
            print("3️⃣ - Editar Fornecedor")
            print("4️⃣ - Excluir Fornecedor")
            print("5️⃣ - Voltar")

            opcao_fornecedor = input("\nEscolha uma das opções: ").strip()

            if opcao_fornecedor == "1":
                FornecedorView.cadastrar_fornecedor()
            #elif opcao_fornecedor == "2":
                #CategoriaView.detalhar_categorias() #TODO Ajustar para chamar a funcao de detalhar fornecedores
            #elif opcao_fornecedor == "3":
                #CategoriaView.detalhar_categorias() #TODO Ajustar para chamar a funcao de detalhar fornecedores
                #CategoriaView.editar_categoria() #TODO Ajustar para chamar a funcao de editar fornecedor
            #elif opcao_fornecedor == "4":
                #CategoriaView.detalhar_categorias() #TODO Ajustar para chamar a funcao de detalhar fornecedores
                #CategoriaView.excluir_categoria() #TODO Ajustar para chamar a funcao de excluir fornecedor
            elif opcao_fornecedor == "5":
                continue
            else:
                print("⚠️ Opção inválida! Tente novamente.\n")


        elif opcao == "3":
            print("🚪 Saindo do programa...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")




if __name__ == "__main__":
    menu()