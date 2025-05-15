from validate_docbr import CPF
import re
# Funções de validação

# Função para validar telefone com regex
def validar_telefone(telefone):
    # Padrão regex
    if len(telefone) == 10:
        padrao_telefone = re.compile(r"^([1-9][0-9])([0-9]{8})$")
    elif len(telefone) == 11:
        padrao_telefone = re.compile(r"^([1-9][0-9])[9]([0-9]{8})$")
    else:
        padrao_telefone = re.compile(r"^([1-9][0-9])[1-9]([0-9]{7,8})$")

    validar_telefone = re.fullmatch(padrao_telefone, telefone)

    return validar_telefone




# Função para validar CPF com Validate_docbr
# Cria a instância do validador
validador_cpf = CPF()
def validar_cpf(cpf):
    # Chama a função que valida o CPF e retorna True ou False
    return validador_cpf.validate(cpf)




# Função para validar o endereço (Garantir que tenha letras e números)
def validar_endereco(endereco):
    # Padrão regex
    padrao_endereco = re.compile(r"^[a-zA-Z]+(?: [A-Za-zÀ-ÿ]+)* \d+[A-Za-z0-9\-]*$")

    validar_endereco = re.fullmatch(padrao_endereco, endereco)

    return validar_endereco