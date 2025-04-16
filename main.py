from views.categoria_view import *

def menu():
    # Exibe o menu no terminal
    while True:
        print("\n🖥️ Sistema de gestão de mercearia")
        print("\n📄 Menu:")
        print("1️⃣ - Categoria")
        print("2️⃣ - Sair")

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
            #elif opcao_categoria == "3":
                #TODO Fazer a view e controller que edita a categoria
            elif opcao_categoria == "4":
                CategoriaView.detalhar_categorias()
                CategoriaView.excluir_categoria()
            elif opcao_categoria == "5":
                continue
            else:
                print("⚠️ Opção inválida! Tente novamente.\n")

        elif opcao == "2":
            print("🚪 Saindo do programa...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")




if __name__ == "__main__":
    menu()