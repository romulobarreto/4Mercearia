from validate_docbr import CPF
import re
# Funções de validação

# Função para validar telefone com regex
def validar_telefone(telefone):
    # Padrão regex
    padrao_telefone = re.compile("^[1-9][\d][1-9][\d]{3,4}[\d]{4}$")

    validar_telefone = re.fullmatch(padrao_telefone, telefone)

    return validar_telefone




# Função para validar CPF com Validate_docbr
# Cria a instância do validador
validador_cpf = CPF()
def validar_cpf(cpf):
    # Chama a função que valida o CPF e retorna True ou False
    return validador_cpf.validate(cpf)