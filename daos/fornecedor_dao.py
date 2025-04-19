import json
import os

class FornecedorDao:
    caminho_arquivo = os.path.join("database", "fornecedor.json")
    
    @classmethod
    def carregar_fornecedor(cls):
        try:
            with open(cls.caminho_arquivo, "r") as arq:
                return json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    @classmethod    
    def salvar_fornecedor(cls, fornecedores):
        try:
            with open(cls.caminho_arquivo, "w") as arq:
                json.dump(fornecedores, arq, indent=4)
                return True, "✅ Dados salvos com sucesso."
        except Exception as e:
            return False, "❌ Dados não salvos por erro, favor, validar."