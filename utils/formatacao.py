def formatar_telefone(telefone):
        # Formata o número do telefone de acordo com o padrão brasileiro
        ddd = telefone[0:2]
        if len(telefone) == 11:
            corpo = telefone[2:7]
            final = telefone[7:]
        else:
            corpo = telefone[2:6]
            final = telefone[6:]
        return f"({ddd}) {corpo}-{final}"