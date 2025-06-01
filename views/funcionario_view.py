from controllers.funcionario_controller import *
from views.cargo_view import *
from utils.formatacao import formatar_cpf, formatar_telefone, formatar_preco
from decimal import Decimal, InvalidOperation
from utils.buscas import buscar_nome, buscar_nome

class FuncionarioView():

    @staticmethod
    def cadastrar_funcionario():
        # Carrega as listas de cargos e verifica se está vazia
        cargos = CargoDao.carregar_cargos()
        
        if not cargos:
            print("\n🚫 Não existe nenhum cargo cadastrado, não é possível cadastrar um funcionário.")
            return
        
        # Solicita os inputs ao usuário
        nome = input("\nDigite o nome do funcionário: ").strip().lower()

        cpf = input("\nDigite o CPF do funcionário: ").strip().replace(".", "").replace("-", "")

        telefone = input("\nDigite o telefone do funcionário (DDD + Número):  ").strip().replace("(", "").replace(")", "").replace("-","").replace(" ","")

        # Exibe os cargos disponíveis para cadastro
        CargoView.detalhar_cargos()

        try:
            cargo_id = int(input("\nDigite o ID do cargo que será atribuído ao funcionário: ").strip())
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        try:
            salario = Decimal(input("\nDigite o salário do funcionário: R$").strip().replace(".", "").replace(",", "."))
        except InvalidOperation:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        # Chama a função de cadastrar funcionário
        sucesso, mensagem = FuncionarioController.cadastrar_funcionario(nome, cpf, telefone, cargo_id, salario)
        print(mensagem)






    @staticmethod
    def detalhar_funcionarios(id=None):
        # Chama a função de detalhar
        sucesso, mensagem = FuncionarioController.detalhar_funcionarios(id)
        # Exibe o resultado
        print(mensagem)






    @staticmethod
    def excluir_funcionario():
        # Carrega a lista de funcionários
        funcionarios = FuncionarioDao.carregar_funcionario()

        if not funcionarios:
            print("\n⚠️ Não existem funcionários para serem excluídos.")
            return
        
        # Exibe a lista de funcionários cadastrados
        FuncionarioView.detalhar_funcionarios()

        # Solicita o ID do funcionário que será excluído
        id_funcionario = input("\nDigite o ID do funcionário que deseja excluir (Caso queira cancelar, deixe em branco): ")

        if not id_funcionario:
            print("✅ Nenhum funcionário foi excluído.")
            return

        # Converte o ID para INT
        try:
            id_funcionario = int(id_funcionario)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return 
        
        # Chama a função para excluir o funcionário
        sucesso, mensagem = FuncionarioController.excluir_funcionário(id_funcionario)
        print(mensagem)







    
    @staticmethod
    def editar_funcionario():
        # Carrega a lista de funcionarios e de cargos e verifica se estão vazias
        funcionarios = FuncionarioDao.carregar_funcionario()
        cargos = CargoDao.carregar_cargos()

        if not cargos:
            print("\n🚫 Não existe nenhum cargo cadastrado, não é possível editar um funcionário.")
            return

        if not funcionarios:
            print("\n🚫 Não existe nenhum funcionário cadastrado, não é possível editar.")
            return
        
        # Chama a lista de funcionários
        FuncionarioView.detalhar_funcionarios()

        # Solicita o ID do funcionário que será editado e valida
        id_funcionario = input("\nDigite o ID do funcionario que deseja editar (Caso queira cancelar, deixe em branco): ")

        if not id_funcionario:
            print("✅ Nenhum funcionario foi editado.")
            return

        # Converte o ID para INT
        try:
            id_funcionario = int(id_funcionario)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        # Verifica se o ID corresponde a um funcionario cadastrado
        lista_funcionario = None
        for funcionario in funcionarios:
            if funcionario["id"] == id_funcionario:
                lista_funcionario = funcionario
                break
        
        if not lista_funcionario:
            print(f"❌ O ID: {id_funcionario}, não é um funcionario cadastrado.")
            return

        # Exibe o funcionario escolhido de forma detalhada
        FuncionarioView.detalhar_funcionarios(id_funcionario)

        # Solicita a chave ao usuário
        chave = input("\nDigite a chave que deseja alterar (Nome, CPF, Telefone, Cargo, Salário): ").strip().lower().replace("á", "a").replace("cargo", "cargo_id")

        if chave not in lista_funcionario:
            print(f'\n⚠️ A chave: {chave} é inválida.')
            return
        
        # Pede o input para atualizar a chave que o usuário escolheu

        # Caso queira mudar o nome
        if chave == "nome":
            nome = input("\nDigite o novo nome do funcionário (ou pressione Enter para manter o mesmo): ")

            if not nome:
                print(f"\nO nome do funcionário: {lista_funcionario["nome"].title()} foi mantido.")
                return
            else:
                cpf = lista_funcionario["cpf"]
                telefone = lista_funcionario["telefone"]
                cargo_id = lista_funcionario["cargo_id"]
                salario = Decimal(lista_funcionario["salario"])

        # Caso queira mudar o CPF
        elif chave == "cpf":
            cpf = input("\nDigite o novo CPF do funcionário (ou pressione Enter para manter o mesmo): ").strip().replace(".","").replace("-","")

            if not cpf:
                print(f"\nO CPF do funcionário: {lista_funcionario["nome"].title()} foi mantido.")
                return
            else:
                nome = lista_funcionario["nome"]
                telefone = lista_funcionario["telefone"]
                cargo_id = lista_funcionario["cargo_id"]
                salario = Decimal(lista_funcionario["salario"])

        # Caso queira mudar o Telefone
        elif chave == "telefone": 
            telefone = input('\nDigite o novo telefone do funcionário (ou pressione Enter para manter o mesmo): ').strip().replace("(", "").replace(")", "").replace("-","").replace(" ","")

            if not telefone:
                print(f"\n✅ O teledone do funcionário {lista_funcionario["nome"].title()} foi mantido.")
                return
            else:
                nome = lista_funcionario["nome"]
                cpf = lista_funcionario["cpf"]
                cargo_id = lista_funcionario["cargo_id"]
                salario = Decimal(lista_funcionario["salario"])

        # Caso queira mudar o cargo
        elif chave == "cargo_id":
            # Exibe a lista de cargos
            CargoView.detalhar_cargos()

            # Solicita o input do ID do novo cargo
            cargo_id = input(f"\nDigite o ID do novo cargo do funcionário (ou pressione Enter para manter o mesmo): ").strip()

            if not cargo_id:
                print(f"\n✅ O cargo do funcionário {lista_funcionario["nome"].title()} foi mantido.")
                return
            else:
                nome = lista_funcionario["nome"]
                cpf = lista_funcionario["cpf"]
                telefone = lista_funcionario["telefone"]
                salario = Decimal(lista_funcionario["salario"])

        # Caso queira mudar o salário
        elif chave == "salario":
            salario = input('\nDigite o novo salário do funcionário (ou pressione Enter para manter o mesmo): R$').strip().replace(".", "").replace(",", ".")

            if not salario:
                print(f"\n✅ O salário do funcionário {lista_funcionario["nome"].title()} foi mantido.")
                return
            try:
                salario = Decimal(salario)
            except InvalidOperation:
                print("\n⚠️ O valor não está na formatação correta.")
                return
            nome = lista_funcionario["nome"]
            cpf = lista_funcionario["cpf"]
            telefone = lista_funcionario["telefone"]
            cargo_id = lista_funcionario["cargo_id"]

        # Chama a função de editar do controller
        sucesso, mensagem = FuncionarioController.editar_funcionario(nome, cpf, telefone, cargo_id, salario, lista_funcionario)

        # Mostra a mensagem de sucesso no terminal
        if sucesso:
            if chave == "nome":
                print(mensagem)
                print(f"O funcionário teve o nome atualizado:\nDe: {lista_funcionario["nome"].title()}\nPara: {nome.title()}")
                return
            elif chave == "cpf":
                print(mensagem)
                print(f"{lista_funcionario["nome"].title()} teve o CPF atualizado:\nDe: {formatar_cpf(lista_funcionario["cpf"])}\nPara: {formatar_cpf(cpf)}")
                return
            elif chave == "telefone":
                print(mensagem)
                print(f"{lista_funcionario["nome"].title()} teve o telefone atualizado:\nDe: {formatar_telefone(lista_funcionario["telefone"])}\nPara: {formatar_telefone(telefone)}")
                return
            elif chave == "cargo_id":
                print(mensagem)
                print(f"{lista_funcionario["nome"].title()} teve o cargo atualizado:\nDe: {buscar_nome(lista_funcionario["cargo_id"], cargos).title()}\nPara: {buscar_nome(cargo_id, cargos).title()}")
                return
            elif chave == "salario":
                print(mensagem)
                print(f"{lista_funcionario["nome"].title()} teve o salário atualizado:\nDe: {formatar_preco(float(lista_funcionario["salário"]))}\nPara: {formatar_preco(salario)}")
                return
        else:
            print(mensagem)