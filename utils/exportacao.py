import pandas as pd
from datetime import date

def exportar_relatorio(lista, nome_base):
    # Transforma a lista em um dataframe
    df = pd.DataFrame(lista)

    # Gera o nome do arquivo com data
    data_hoje = date.today().strftime("%Y-%m-%d")
    nome_arquivo = f"relatorio_{nome_base}_{data_hoje}.xlsx"

    # Salva em excel
    df.to_excel(nome_arquivo, index=False)

    # Retorno da função
    return True, f"✅ Relatório {nome_arquivo} exportado com sucesso."