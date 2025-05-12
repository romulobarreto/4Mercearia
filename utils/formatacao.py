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






def formatar_cpf(cpf):
     # Formata o número do CPF com "." e "-"
     return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"






def formatar_preco(preco):
     # Formata o preço para ser exibido no formato Real(R$)
     preco_formatado = f"R${preco:,.2f}".replace(",", "v").replace(".",",").replace("v",".")
     return preco_formatado