from daos.cargo_dao import *
from daos.funcionario_dao import *
from models.cargo import *
from utils.buscas import buscar_nome
from utils.gerador import gerador_id

class CargoController:

    @staticmethod
    def validar_dados(nome, nome_atual=None):
        # Carrega a lista de cargos
        cargos = CargoDao.carregar_cargos()

        # Valida o valor de nome
        if not nome:
            return False, "⚠️ O nome não pode estar vazio."
        
        if nome != nome_atual and any(cargo["nome"] == nome for cargo in cargos):
            return False, "🚫 Cargo já cadastrado."
        
        return True, "✅ Dados aprovados."




    
    @staticmethod
    def cadastrar_cargo(nome):
        # Carrega a lista de cargos
        cargos = CargoDao.carregar_cargos()

        # Valida o valor de nome
        sucesso, mensagem = CargoController.validar_dados(nome)
        if not sucesso:
            return False, mensagem
        
        # Define o valor do maior_id
        id = gerador_id(cargos)

        # Cria o cargo
        cargo = Cargo(id, nome)

        # Transforma o cargo em dicionário e adiciona na lista
        cargos.append(cargo.salvar_dict())

        # Salva a lista de cargos no banco e exibe a mensagem
        sucesso, mensagem = CargoDao.salvar_cargo(cargos)

        if sucesso:
            return True, mensagem
        else:
            return False, mensagem
        





    @staticmethod
    def detalhar_cargos(id=None):
        # Carregar cargos
        cargos = CargoDao.carregar_cargos()

        # Verifica se existe cargo cadastrado
        if not cargos:
            return False, "\n⚠️ A lista de cargos está vazia!"
        
        # Detalhar cargos
        if id:
            lista_formatada = "\n📋 Detalhes do cargo:\n"
            for cargo in cargos:
                if cargo["id"] == id:
                    lista_formatada += f"ID {cargo["id"]}: {cargo["nome"].title()}\n---------------------------"
                    break
        else:
            lista_formatada = "\n📋 Lista de cargos cadastrados:\n"
            for cargo in sorted(cargos, key=lambda c: c["nome"]):
                lista_formatada += f"ID {cargo["id"]}: {cargo["nome"].title()}\n"
            lista_formatada += "---------------------------"

        return True, lista_formatada
    




    
    @staticmethod
    def excluir_cargo(id_cargo):
        # Carrega lista de cargos e funcionarios
        cargos = CargoDao.carregar_cargos()
        funcionarios = FuncionarioDao.carregar_funcionario()

        # Valida se o id do cargo está cadastrado
        dicionario_cargo = None
        for cargo in cargos:
            if cargo["id"] == id_cargo:
                dicionario_cargo = cargo
                break
        
        if not dicionario_cargo:
            return False, f"⚠️ O ID: {id_cargo}, não está na lista de cadastro."
                
        
        # Verifica se o cargo está em uso com algum funcionario, se estiver, não pode ser excluído
        cargo_nome = buscar_nome(id_cargo, cargos)
        for funcionario in funcionarios:
            if funcionario["cargo_id"] == id_cargo:
                return False, f"\n⚠️ {cargo_nome.title()} não pode ser excluído pois está sendo usado por um funcionário."
        
        # Remove o dicionário do cargo da base
        cargos.remove(dicionario_cargo)

        # Salva a lista atualizada na base
        CargoDao.salvar_cargo(cargos)
        return True, f"✅ O cargo {cargo_nome.title()} foi deletado com sucesso."
        






    @staticmethod
    def editar_cargo(id_cargo, novo_nome, dicionario_cargo):
        # Carrega lista de cargos
        cargos = CargoDao.carregar_cargos()

        cargo_nome = buscar_nome(id_cargo, cargos)

        # Valida o nome do cargo
        if not novo_nome:
            return False, f"✅ O cargo {cargo_nome.title()} permanece a mesmo."
        
        # Valida se o nome do cargo está cadastrado
        sucesso, mensagem = CargoController.validar_dados(novo_nome, dicionario_cargo["nome"])
        if not sucesso:
            return False, mensagem
            
        # Encontra a lista que deve ser editado e faz a alteração
        for cargo in cargos:
            if cargo["id"] == id_cargo:
                cargo["nome"] = novo_nome
                break

        # Salva a lista editada no banco
        sucesso, mensagem = CargoDao.salvar_cargo(cargos)

        # Mostra a mensagem de sucesso
        if sucesso:
            return True, f"{mensagem}\nCargo antigo: {cargo_nome.title()}\nCargo novo: {novo_nome.title()}"
        else:
            return False, mensagem