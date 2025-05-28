# Funções de busca
def criar_dict(lista):
    # Cria lista simplificada de ID na chave com Nome 
    return {item["id"]: item["nome"] for item in lista}


def buscar_id(nome, lista):
    # Busca o ID a partir do nome
    item_id = next((item["id"] for item in lista if item["nome"] == nome), None)
    return item_id

def buscar_nome(id, lista):
    # Busca o nome a partir do ID
    item_nome = next((item["nome"] for item in lista if item["id"] == id))
    return item_nome