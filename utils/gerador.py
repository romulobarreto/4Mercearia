def gerador_id(lista):
    # Puxa o ID máximo que possui na lista
    id = max([item["id"] for item in lista], default=0) + 1
    # Retorna o ID
    return id