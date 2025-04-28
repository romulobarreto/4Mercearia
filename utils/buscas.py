# Buscas de categoria
def criar_dict_categorias(categorias):
    return {categoria["id"]: categoria["nome"] for categoria in categorias}


def buscar_id_categoria(categoria_nome, categorias):
    # Busca o ID da categoria a partir do nome
    categoria_id = next((categoria["id"] for categoria in categorias if categoria["nome"] == categoria_nome), None)
    return categoria_id



# Buscas de fornecedor
def criar_dict_fornecedores(fornecedores):
    return {fornecedor["id"]: fornecedor["nome"] for fornecedor in fornecedores}


def buscar_id_fornecedor(fornecedor_nome, fornecedores):
    # Busca o ID do fornecedor a partir do nome
    fornecedor_id = next((fornecedor["id"] for fornecedor in fornecedores if fornecedor["nome"] == fornecedor_nome), None)

    return fornecedor_id