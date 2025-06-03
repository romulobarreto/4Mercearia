import json
import os

class VendaDao:
    # Define o caminha padrão do banco de categoria
    caminho_arquivo = os.path.join("database", "venda.json")
    
    # Carrega a lista de vendas, caso não haja lista, traz uma lista vazia
    @classmethod
    def carregar_vendas(cls):
        try:
            with open(cls.caminho_arquivo, "r") as arq:
                return json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    # Salva as alterações no arquivo, reescrevendo a base e retornando mensagem    
    @classmethod    
    def salvar_vendas(cls, vendas):
        try:
            with open(cls.caminho_arquivo, "w") as arq:
                json.dump(vendas, arq, indent=4)
                return True, "\n✅ Dados salvos com sucesso."
        except Exception as e:
            return False, "❌ Dados não salvos por erro, favor, validar."