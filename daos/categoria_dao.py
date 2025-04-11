import json
import os

class CategoriaDao:
    caminho_arquivo = os.path.join("database", "categoria.json")
    
    @classmethod
    def carregar_categoria(cls):
        try:
            with open(cls.caminho_arquivo, "r") as arq:
                return json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    @classmethod    
    def salvar_categoria(cls, categorias):
        try:
            with open(cls.caminho_arquivo, "w") as arq:
                json.dump(categorias, arq, indent=4)
                return True, "✅ Dados salvos com sucesso."
        except Exception as e:
            return False, "❌ Dados não salvos por erro, favor, validar."