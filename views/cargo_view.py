from controllers.cargo_controller import *

class CargoView:

    @staticmethod
    def cadastrar_cargo():
        # Pede os inputs ao usuário de ID e Nome do cargo
        nome = input("\nDigite o nome do cargo: ").strip().lower()

        # Cria o cargo e retorna a mensagem
        sucesso, mensagem = CargoController.cadastrar_cargo(nome)
        print(mensagem)





    
    @staticmethod
    def detalhar_cargos(id=None):
        # Chama a função do controller para detalhar os cargos
        sucesso, mensagem = CargoController.detalhar_cargos(id)
        # Exibe resultado
        print(mensagem)







    @staticmethod
    def excluir_cargo():
        # Carrega a lista de cargos
        cargos = CargoDao.carregar_cargos()

        # Valida se existe cargo cadastrado
        if not cargos:
            print("⚠️ Não existe nenhum cargo para excluir.")
            return 
        
        # Exibe lista de cargos cadastrados
        CargoView.detalhar_cargos()

        # Solicita o ID do cargo que será excluído
        id_cargo = input("\nDigite o ID do CARGO que deseja excluir (Caso queira cancelar, deixe em branco): ").strip()

        if not id_cargo:
            print("✅ Nenhum cargo foi excluído.")
            return
        
        try:
            id_cargo = int(id_cargo)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        # Chama a função que exclui o cargo
        sucesso, mensagem = CargoController.excluir_cargo(id_cargo)

        # Exibe o resultado da função
        print(mensagem)







    @staticmethod
    def editar_cargo():
        # Carrega a lista de cargos
        cargos = CargoDao.carregar_cargos()

        # Valida se existe cargos cadastrado
        if not cargos:
            print("⚠️ Não existe nenhum cargo para editar.")
            return 
        
        # Exibe lista de cargos cadastrados
        CargoView.detalhar_cargos()

        # Pega o input do usuário
        id_cargo = input("\nDigite o ID do CARGO que deseja editar (Caso queira cancelar, deixe em branco): ").strip()

        if not id_cargo:
            print("✅ Nenhum cargo foi alterado.")
            return
        
        try:
            id_cargo = int(id_cargo)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        # Valida se o ID do CARGO está cadastrado
        dicionario_cargo = None
        for cargo in cargos:
            if cargo["id"] == id_cargo:
                dicionario_cargo = cargo
                break
        
        if not dicionario_cargo:
            print(f"\n⚠️ O ID: {id_cargo}, não está na lista de cadastro.")
            return
                
        
        # Mostra os detalhes do cargo selecionado
        CargoView.detalhar_cargos(id_cargo)

        # Input com o nome atualizado
        novo_nome = input('\nDigite o novo nome do cargo (ou pressione Enter para manter o mesmo): ').strip().lower()

        # Chama a função de editar o cargo
        sucesso, mensagem = CargoController.editar_cargo(id_cargo, novo_nome, dicionario_cargo)

        # Mostra a mensagem de sucesso
        print(mensagem)