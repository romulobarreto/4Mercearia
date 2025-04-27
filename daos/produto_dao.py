import json
import os

class ProdutoDao:
    caminho_arquivo = os.path.join("database", "produto.json")
    
    @classmethod
    def carregar_produto(cls):
        try:
            with open(cls.caminho_arquivo, "r") as arq:
                return json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    @classmethod    
    def salvar_produto(cls, produtos):
        try:
            with open(cls.caminho_arquivo, "w") as arq:
                json.dump(produtos, arq, indent=4)
                return True, "✅ Dados salvos com sucesso."
        except Exception as e:
            return False, "❌ Dados não salvos por erro, favor, validar."