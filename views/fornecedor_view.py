from controllers.fornecedor_controller import *

class FornecedorView:

    @staticmethod
    def cadastrar_fornecedor():
        # Pede os inputs ao usuário de Nome e Telefone do fornecedor
        nome = input("\nDigite o nome do fornecedor: ").strip().lower()
        telefone = input("\nDigite o telefone (DDD + Número): ").strip().replace("(", "").replace(")", "").replace("-","").replace(" ","")

        # Cria o usuário e retorna a mensagem
        sucesso, mensagem = FornecedorController.cadastrar_fornecedor(nome, telefone)
        print(mensagem)

    
    @staticmethod
    def detalhar_fornecedores():
        # Chama a função do controller para detalhar os fornecedores
        sucesso, mensagem = FornecedorController.detalhar_fornecedores()
        # Exibe resultado
        print(mensagem)


    @staticmethod
    def excluir_fornecedor():
        # Carrega a lista de fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Verifica se existe fornecedor cadastrado
        if not fornecedores:
            print("⚠️ Não existe nenhum fornecedor para excluir.")
            return 
        
        # Mostra a lista de fornecedores ao usuário
        print("\n📋 Lista de fornecedores:")
        for fornecedor in sorted(fornecedores, key=lambda c: c["nome"]):
            print(f"ID: {fornecedor["id"]} - {fornecedor["nome"].title()}")

        # Pega o input do usuário do ID do fornecedor e valida
        id_fornecedor = input("\nDigite o ID do fornecedor que deseja excluir (Caso não queira excluir nenhum, deixe em branco): ").strip()

        if not id_fornecedor:
            print("✅ Nenhum fornecedor foi excluído.")
            return
        
        try:
            id_fornecedor = int(id_fornecedor)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        # Chama a função que exclui o fornecedor
        sucesso, mensagem = FornecedorController.excluir_fornecedor(id_fornecedor)

        # Exibe o resultado da função
        print(mensagem)



    @staticmethod
    def editar_fornecedor():
        # Carrega a lista de fornecedores
        fornecedores = FornecedorDao.carregar_fornecedor()

        # Valida se existe categoria cadastrada
        if not fornecedores:
            print("⚠️ Não existe nenhum fornecedor para editar.")
            return

        # Exibe a lista de fornecedores cadastrados
        print("\n📋 Lista de fornecedores:")
        for fornecedor in sorted(fornecedores, key=lambda c: c["nome"]):
            print(f"ID: {fornecedor["id"]} - {fornecedor["nome"].title()}")
            

        # Pega o input do usuário do ID do usuário que deseja editar
        id_fornecedor = input("\nDigite o ID do fornecedor que deseja editar (Caso não queira excluir nenhum, deixe em branco): ").strip()

        # Valida se o nome_fornecedor está na lista de fornecedores e se não está vazio
        if not id_fornecedor:
            print("✅ Nenhum fornecedor foi editado.")
            return
        
        try:
            id_fornecedor = int(id_fornecedor)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        lista_fornecedor = None
        for fornecedor in fornecedores:
            if fornecedor["id"] == id_fornecedor:
                lista_fornecedor = fornecedor
                break
        
        if not lista_fornecedor:
            print(f"❌ O ID: {id_fornecedor}, não é um fornecedor cadastrado.")
            return
        
        # Mostra os detalhes do fornecedor selecionado
        print(f"\n📋 Detalhes do fornecedor:\nID: {lista_fornecedor["id"]}\nNome: {lista_fornecedor["nome"].title()}\nTelefone: {formatar_telefone(lista_fornecedor["telefone"])}")
        
        # Solicita a chave ao usuário
        chave = input("\nEscolha a opção que deseja editar:\nNome\nTelefone\n").strip().lower()

        # Valida se a chave existe
        if chave not in lista_fornecedor:
            print(f'\n⚠️ A chave: {chave} é inválida.')
            return
        
        # Solicita o input com o novo valor e ajusta nome e telefone para poder chamar a funcao de editar do controller
        if chave == "nome":
            nome = input('\nDigite o novo nome do fornecedor (ou pressione Enter para manter o mesmo): ').strip().lower()
            if not nome:
                print(f"\n✅ O nome do fornecedor {lista_fornecedor["nome"].title()} foi mantido.")
                return
            else:
                telefone = lista_fornecedor["telefone"]

        elif chave == "telefone":
            telefone = input('\nDigite o novo telefone do fornecedor Ex:(DDD + Número) (ou pressione Enter para manter o mesmo): ').strip().replace("(", "").replace(")", "").replace("-","").replace(" ","")
            if not telefone:
                print(f"\n✅ O telefone do fornecedor {lista_fornecedor["nome"].title()} foi mantido.")
                return
            else:
                nome = lista_fornecedor["nome"]

        # Chama a função de editar do controller
        sucesso, mensagem = FornecedorController.editar_fornecedor(nome, telefone, lista_fornecedor)

        # Mostra a mensagem de sucesso no terminal
        if sucesso:
            if chave == "nome":
                print(mensagem)
                print(f"O fornecedor teve o nome atualizado:\nDe: {lista_fornecedor["nome"].title()}\nPara: {nome.title()}")
                return
            elif chave == "telefone":
                print(mensagem)
                print(f"{lista_fornecedor["nome"].title()} teve o telefone atualizado:\nDe: {formatar_telefone(lista_fornecedor["telefone"])}\nPara: {formatar_telefone(telefone)}")
                return
        else:
            print(mensagem)