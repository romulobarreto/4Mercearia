from decimal import Decimal
from models.funcionario import *
from daos.cargo_dao import *
from daos.venda_dao import *
from daos.funcionario_dao import *
from utils.validacao import validar_cpf, validar_telefone
from utils.formatacao import formatar_preco, formatar_telefone, formatar_cpf
from utils.gerador import gerador_id
from utils.buscas import criar_dict

class FuncionarioController():

    @staticmethod
    def validar_dados(nome, cpf, telefone, cargo_id, salario, cpf_atual=None):
        # Carrega a lista de funcionários e de cargos
        funcionarios = FuncionarioDao.carregar_funcionario()
        cargos = CargoDao.carregar_cargos()

        # Valida o nome
        if not nome:
            return False, "\n⚠️ O nome precisa ser preenchido."
        
        # Valida o cpf (Verificar retorno da funcao)
        validador_cpf = validar_cpf(cpf)

        if not validador_cpf:
            return False, "\n⚠️ CPF inválido."
        
        if cpf != cpf_atual and any(funcionario["cpf"] == cpf for funcionario in funcionarios):
            return False, f"\n❌ CPF já cadastrado."
        
        # Valida o telefone
        verificar_telefone = validar_telefone(telefone)

        if not verificar_telefone:
            return False, f"\n⚠️ O telefone: {telefone} não está no padrão. Use o formato DDD + número (Ex: 11987654321)."
        
        # Valida o cargo
        if not any(cargo["id"] == cargo_id for cargo in cargos):
            return False, f"\n⚠️ Não existe cargo cadastrado para o ID: {cargo_id}."
        
        # Valida o salário
        if salario <= Decimal("0"):
            return False, "\n⚠️ O funcionário não pode trabalhar de graça."
        
        # Retorna sucesso
        return True, "\n✅ Dados validados."
    




    @staticmethod
    def cadastrar_funcionario(nome, cpf, telefone, cargo_id, salario):
        # Valida os dados recebidos
        sucesso, mensagem = FuncionarioController.validar_dados(nome, cpf, telefone, cargo_id, salario)

        if not sucesso:
            return False, mensagem
        
        # Carrega a lista de funcionários
        funcionarios = FuncionarioDao.carregar_funcionario()

        # Cria o ID do funcionário
        id = gerador_id(funcionarios)

        # Cria o funcionário
        funcionario = Funcionario(id, nome, cpf, telefone, cargo_id, salario)

        # Adiciona o funcionário a lista de cadastro
        funcionarios.append(funcionario.salvar_dict())

        # Salva o funcionário no banco (JSON)
        sucesso, mensagem = FuncionarioDao.salvar_funcionario(funcionarios)

        # Mensagem de sucesso
        if sucesso:
            return True, mensagem
        else:
            return False, mensagem
        






    @staticmethod
    def detalhar_funcionarios(id=None):
        # Carrega a lista de funcionários e de cargos
        cargos = CargoDao.carregar_cargos()
        funcionarios = FuncionarioDao.carregar_funcionario()

        # Verifica se possui funcionário cadastrado
        if not funcionarios:
            return False, "\n⚠️ A lista de funcionários está vazia."
        
        # Cria o dicionário de acesso rápido de ID - Cargo
        cargos_dict = criar_dict(cargos)

        # Formata e exibe a lista de um único ID
        if id:
            lista_formatada = "\n📋 Detalhes do funcionário:\n"
            for funcionario in funcionarios:
                cargo_nome = cargos_dict[funcionario["cargo_id"]]
                if funcionario["id"] == id:
                    lista_formatada += (
                        f"ID {funcionario["id"]}: {funcionario["nome"].title()}\n"
                        f"CPF: {formatar_cpf(funcionario["cpf"])}\n"
                        f"Telefone: {formatar_telefone(funcionario["telefone"])}\n"
                        f"Cargo: {cargo_nome.title()}\n"
                        f"Salário: {formatar_preco(Decimal(funcionario["salario"]))}\n"
                        f"---------------------------\n"
                    )
                    break
        # Formata e exibe a lista completa
        else:
            lista_formatada = "\n📋 Lista de funcionários cadastrados:\n"
            for funcionario in sorted(funcionarios, key=lambda c: c["nome"]):
                cargo_nome = cargos_dict[funcionario["cargo_id"]]
                
                lista_formatada += (
                    f"ID {funcionario["id"]}: {funcionario["nome"].title()}\n"
                    f"CPF: {formatar_cpf(funcionario["cpf"])}\n"
                    f"Telefone: {formatar_telefone(funcionario["telefone"])}\n"
                    f"Cargo: {cargo_nome.title()}\n"
                    f"Salário: {formatar_preco(Decimal(funcionario["salario"]))}\n"
                    f"---------------------------\n"
                )
        
        return True, lista_formatada
    





    @staticmethod
    def excluir_funcionário(id_funcionario):
        # Carrega a lista de funcionários e vendas
        funcionarios = FuncionarioDao.carregar_funcionario()
        vendas = VendaDao.carregar_vendas()

        # Verifica se o ID informado está na base de cadastro
        dicionario_funcionario = None
        for funcionario in funcionarios:
            if funcionario["id"] == id_funcionario:
                dicionario_funcionario = funcionario
                break

        # Caso nenhum funcionário encontrado, finaliza a função
        if not dicionario_funcionario:
            return False, f"\n⚠️ O ID: {id_funcionario}, não está na lista de funcionários."
        
        # Verificar se o funcionário realizou alguma venda, se sim, não permitir exclusão do mesmo.
        for venda in vendas:
            if venda["cliente_id"] == id_funcionario:
                return False, f"\n⚠️ O ID: {id_funcionario} faz parte de uma venda, não pode ser excluído."

        # Remove o funcionário escolhido da lista
        funcionarios.remove(dicionario_funcionario)

        # Salva a lista sem o funcionário
        sucesso, mensagem = FuncionarioDao.salvar_funcionario(funcionarios)

        return True, f"\n✅ {dicionario_funcionario["nome"].title()} foi removido com sucesso."
    








    @staticmethod
    def editar_funcionario(nome, cpf, telefone, cargo_id, salario, lista_funcionario):
        # Chama a validação de dados
        sucesso, mensagem = FuncionarioController.validar_dados(nome, cpf, telefone, cargo_id, salario, lista_funcionario["cpf"])

        if not sucesso:
            return False, mensagem
        
        # Carrega a lista de funcionários
        funcionarios = FuncionarioDao.carregar_funcionario()

        # Atualiza a lista de funcionários
        for funcionario in funcionarios:
            if funcionario["id"] == lista_funcionario["id"]:
                funcionario["nome"] = nome
                funcionario["cpf"] = cpf
                funcionario["telefone"] = telefone
                funcionario["cargo_id"] = cargo_id
                funcionario["salario"] = str(salario)
                break
        
        # Salva as alterações no banco
        sucesso, mensagem = FuncionarioDao.salvar_funcionario(funcionarios)

        if sucesso:
            return True, "✅ Funcionário editado com sucesso."
        else:
            return False, "⚠️ Erro ao salvar a alteração no banco de dados."