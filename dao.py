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
        
# -------------------------------------------------------------------------------

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
    def salvar_fornecedor(cls, categorias):
        try:
            with open(cls.caminho_arquivo, "w") as arq:
                json.dump(categorias, arq, indent=4)
                return True, "✅ Dados salvos com sucesso."
        except Exception as e:
            return False, "❌ Dados não salvos por erro, favor, validar."
        
# -------------------------------------------------------------------------------

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
    def salvar_produto(cls, categorias):
        try:
            with open(cls.caminho_arquivo, "w") as arq:
                json.dump(categorias, arq, indent=4)
                return True, "✅ Dados salvos com sucesso."
        except Exception as e:
            return False, "❌ Dados não salvos por erro, favor, validar."

# -------------------------------------------------------------------------------